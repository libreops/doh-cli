import dns.message
import requests
import base64
import json
import sys
import time


def answer(domain, rr, endpoint, output, debug=None, verbose=None, response_time=None):
    """
    Sends query to DNS provider and prints the answer.
    """
    message = dns.message.make_query(domain, rr)
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

    for response in dns.message.from_wire(r.content).answer:
        answers = response.to_text().split("\n")

    for answer in answers:
        if output == "plain":
            delimeter = "IN " + rr + " "
            output_plain = answer.split(delimeter)[-1]
            print(output_plain)
            if debug:
                print("Debug: {0}".format(debug))
            if verbose:
                print("Verbose: {0}".format(verbose))
            if response_time:
                print("Query Time: {0}".format(response_time))
        else:
            jdns = []
            output_json = answer.split()
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
