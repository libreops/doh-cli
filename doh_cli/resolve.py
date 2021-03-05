import dns.message
import requests
import base64
import json
import sys
import time


def answer(domain, rr, endpoint, output, debug=None, verbose=None,
           response_time=None, request_dnssec=False):
    """
    Sends query to DNS provider and prints the answer.
    """
    message = dns.message.make_query(domain, rr)
    if request_dnssec:
        message.use_edns(edns=True)
        message.want_dnssec(request_dnssec)
    dns_req = base64.urlsafe_b64encode(message.to_wire()).decode("UTF8").rstrip("=")

    start_time = time.time() * 1000
    try:
        r = requests.get(endpoint, params={"dns": dns_req},
                         headers={"Content-type": "application/dns-message"})
        r.raise_for_status()
    except requests.RequestException as reqerror:
        sys.stderr.write("{0}\n".format(reqerror))
        sys.exit(1)
    query_time = time.time() * 1000

    if "application/dns-message" not in r.headers["Content-Type"]:
        print("The answer from: {0} is not a DNS response!".format(endpoint))
        sys.exit(1)

    response = dns.message.from_wire(r.content)

    if debug:
        debug = response.to_text()

    if verbose:
        delimeter = "?" if "?" not in endpoint else "&"
        verbose = endpoint + delimeter + "dns=" + dns_req

    if response_time:
        response_time = format(round((query_time - start_time), 3))

    answers = []

    # append all answers from response in a list
    for response in dns.message.from_wire(r.content).answer:
        answers.append(response.to_text().split("\n"))

    if output == "plain":
        for answer in answers:
            for item in answer:
                delimeter = "IN " + rr + " "
                if request_dnssec and 'IN RRSIG' in item:
                    delimeter = "IN RRSIG " + rr + " "
                output_plain = item.split(delimeter)[-1]
                print(output_plain)
        if debug:
            print("Debug:\n{0}".format(debug))
        if verbose:
            print("Verbose: {0}".format(verbose))
        if response_time:
            print("Query Time: {0}".format(response_time))
    else:
        jdns = []
        for answer in answers:
            for item in answer:
                output_json = item.split()
                jdns.append(
                    {"Query": output_json[0], "TTL": output_json[1], "RR":
                        output_json[3], "Answer": output_json[4:99]})
        if debug:
            jdns.append({"Debug": debug})
        if verbose:
            jdns.append({"Verbose": verbose})
        if response_time:
            jdns.append({"Query Time": response_time})
        print(json.dumps(jdns))
