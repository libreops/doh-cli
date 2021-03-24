import dns.message
import requests
import base64
import json
import sys
import time
import itertools


def answer(domain, rr, endpoint, format_json=None, debug=None, verbose=None,
           response_time=None, request_dnssec=None):
    """
    Sends query to DNS provider and prints the answer.
    """
    message = dns.message.make_query(domain, rr)

    if request_dnssec:
        message.want_dnssec()

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
        answers.append(response.to_text().split("\n"))

    answers = list(itertools.chain.from_iterable(answers))

    if format_json:
        jdns = []
        for answer in answers:
            output_json = answer.split()
            jdns.append(
                {"Query": output_json[0], "TTL": output_json[1],
                 "RR": output_json[3], "Answer": output_json[4:99]})
        if debug:
            jdns.append({"Debug": debug})
        if verbose:
            jdns.append({"Verbose": verbose})
        if response_time:
            jdns.append({"Query Time": response_time})
        return json.dumps(jdns)

    output_plain = ""
    for answer in answers:
        delimeter = "IN " + rr + " "
        if request_dnssec and 'IN RRSIG' in answer:
            delimeter = "IN RRSIG " + rr + " "
        output_plain += "{0}\n".format(answer.split(delimeter)[-1])
    if debug:
        output_plain += "\nDebug: \n{0}\n".format(debug)
    if verbose:
        output_plain += "\nVerbose: \n{0}\n".format(verbose)
    if response_time:
        output_plain += "\nQuery Time: \n{0}\n".format(response_time)

    return output_plain
