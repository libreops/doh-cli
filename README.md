# doh-cli

A simple **DNS over HTTPS** client for the command line.

This is a simple DoH python client (RFC 8484, GET), which supports **plain** (default) and **json** output.

## Install

```bash
pip3 install doh-cli
```

### Upgrade

or upgrade to latest version by

```bash
pip install --upgrade doh-cli
```

## Requirements

It's based & tested on Python 3.

If you want to contribute, you can clone the repository and install all dependencies locally:

```bash
pip3 install .
```

## Usage

```bash
doh-cli libredns.gr A
```

## Help

```bash
doh-cli --help
```

## Supported Resource Records

- A
- AAAA
- CNAME
- HTTPS
- MX
- NS
- SOA
- SPF
- SRV
- SVCB
- TXT
- CAA
- DNSKEY
- DS

## Supported DoH Providers

- [LibreDNS](https://libredns.gr)
- [Google](https://dns.google)
- [Cloudflare](https://cloudflare-dns.com)
- [Quad9](https://quad9.net)
- [CleanBrowsing](https://doh.cleanbrowsing.org)
- [CIRA](https://www.cira.ca/cybersecurity-services/canadian-shield)
- [SecureDNS](https://securedns.eu/)
- you may also provide your own DoH server URL

### DoH Options

- libredns (**default**)
- libredns-ads (LibreDNS No-Trackers/Ads)
- google
- cloudflare
- quad9
- cleanbrowsing (blocks access to adult, pornographic and explicit sites, also VPNs)
- cleanbrowsing-secure (blocks access to phishing, malware and malicious domains)
- cleanbrowsing-adult (blocks access to all adult, pornographic and explicit sites)
- cira (CIRA's Canadian Shield)
- cira-protect (Malware and phishing protection)
- cira-family (blocking pornographic content plus protected)
- securedns
- securedns-ads (blockign ads, malware and phishing)

## Some Examples

### IPv4

```bash
doh-cli libredns.gr A
```

```bash
116.202.176.26
```

in json

```bash
doh-cli libredns.gr A --json
```

```json
[{"Query": "libredns.gr.", "TTL": "366", "RR": "A", "Answer": "116.202.176.26"}]
```

you can use [jq](https://stedolan.github.io/jq/) to format, parse output:

```bash
doh-cli libredns.gr A --json | jq .
```

```json
[
  {
    "Query": "libredns.gr.",
    "TTL": "54",
    "RR": "A",
    "Answer": "116.202.176.26"
  }
]
```

### IPv6

```bash
doh-cli example.org AAAA

2606:2800:220:1:248:1893:25c8:1946
```

```json
doh-cli example.org AAAA --json | jq .

[
  {
    "Query": "example.org.",
    "TTL": "45832",
    "RR": "AAAA",
    "Answer": [
      "2606:2800:220:1:248:1893:25c8:1946"
    ]
  }
]

```

### CNAME

```bash
doh-cli www.libredns.gr CNAME --json | jq .
```

```json
[
  {
    "Query": "www.libredns.gr.",
    "TTL": "600",
    "RR": "CNAME",
    "Answer": "libredns.gr."
  }
]
```

### MX

```bash
doh-cli libreops.cc MX --json | jq .
```

```json
[
  {
    "Query": "libreops.cc.",
    "TTL": "10794",
    "RR": "MX",
    "Answer": [
      "10",
      "spool.mail.gandi.net.",
      "libreops.cc.",
      "10794",
      "IN",
      "MX",
      "50",
      "fb.mail.gandi.net."
    ]
  }
]
```

### CAA

```bash
doh-cli libredns.gr CAA --json
```

```json
[{"Query": "libredns.gr.", "TTL": "590", "RR": "CAA", "Answer": ["0", "issue", "\"letsencrypt.org\""]}]
```

### DNSKEY

> DNS Key record 	The key record used in DNSSEC. Uses the same format as the KEY record.

```bash
doh-cli DNSKEY nasa.gov

256 3 8 AwEAAd86yGbz2WUp4VqClb1svSW9oyx0 CQqCCGebNIEEqbXsF5PtCz225RKL3cDr mPHIeSETR6iUvfPSDiKquYearoLFmPjU 0q1AJJmrZIzl9rDgMx/c9OPJxBnhp196 ntJEaGySgXSoaXQEdUpm8lZzhkjftTfC X9mwDY2abxa3Vq3t
256 3 8 AwEAAa/Jh5zZ/apbhzIG6CEUT8LL+WNK +HuVLbFf/pxk5Q/Qmng08J1+24B5ObWK +lUNGHN/FYC0TVbbofeHHOLVS88CBmK9 Zu5RWqDicYYKFu8vra+MXEcwLc6E0fTf R9I/OAIWF6GScPHnkq8GoK2qau8gSD96 UsAw6mCsWEqdyqof
257 3 8 AwEAAbo7ImTCXl2KuV8NK+0zEvLC+OrN M0/6rT/kKZncFc0CqIIQwZUJtdurpvi3 mUFY0J6Pv394E2gu/OLOe+EcIRatjxSv KITBM+PJTJq0OtwsGtBQyu4uU8hS2SNE g1hEJVGHE5q5LWIAy01TBnibyGOyVJE4 N3M50ezp4E7DqEYG6WkhZQxLDjn0T4ex KPDqIkP+QUB6OwF2CWKtWtpPIpI1i9h9 OgIWUfXb3uLEgcnJlAYYAf9Jw35hPPDo FP+Zi9fJ4mQ0olm8gj4668QZoCJ57MDr 3p3Rntfw5Ca+AQVNwnaqcB7iUWHYPZP0 KLk7V02NloWXpwNHOA8O1TsOYtc=

```

### DS

>Delegation signer 	The record used to identify the DNSSEC signing key of a delegated zone

```bash
doh-cli nasa.gov DS --output=json | jq .

[
  {
    "Query": "nasa.gov.",
    "TTL": "3588",
    "RR": "DS",
    "Answer": [
      "41452",
      "8",
      "2",
      "7490b7f47af44d4c0bed3a7a2fefeb50cf55e3209e5a82e30a44f9d4aa9ae688"
    ]
  }
]
[
  {
    "Query": "nasa.gov.",
    "TTL": "3588",
    "RR": "DS",
    "Answer": [
      "41452",
      "8",
      "1",
      "83bb6c5ac559bbe1e8b17a98465145265a3cafc4"
    ]
  }
]
```

### DNSSEC

Using `--dnssec` sets the `EDNS DO` flag. The response will then include the DNSSEC signature for the requested record set.

```bash
doh-cli A nasa.gov --dnssec
52.0.14.116
23.22.39.120
8 2 600 20210325164559 20210223160609 6816 nasa.gov. HqVx19SOdF4Mx2+UZl7rhecv99zJdj07 86R7sAAXP2poG5QDa9zpYz7WXz/y2UtV HpMk+0gfb2SrxQ1p93+VWs0S2UxnwZQI 8qtwuB6/9780LVLa8ZHEDVZzdO1NAAx1 AfaaQ0FjoxErPipPBi4edvMSYjnvVhY+ 0baRH2i1syk=
```

### Plain Output

```bash
doh-cli libredns.gr A
```

```bash
116.202.176.26
```

### verbose

```bash
doh-cli libredns.gr A --verbose
```

```bash
116.202.176.26
Verbose: https://doh.libredns.gr/dns-query?dns=lSIBAAABAAAAAAAACGxpYnJlZG5zAmdyAAABAAE
```

### debug

```bash
doh-cli test.libredns.gr A --debug
```

```bash
116.202.176.26
Debug:  id 24169
opcode QUERY
rcode NOERROR
flags QR RD RA
;QUESTION
test.libredns.gr. IN A
;ANSWER
test.libredns.gr. 3600 IN A 116.202.176.26
;AUTHORITY
libredns.gr. 1822 IN SOA ns1.gandi.net. hostmaster.gandi.net. 1582812814 10800 3600 604800 10800
;ADDITIONAL
```

### Query time

```bash
doh-cli test.libredns.gr A --time
```

```bash
116.202.176.26
Query time:  531.764
```

```bash
doh-cli test.libredns.gr --time --json | jq .
```

```json
[
  {
    "Query": "test.libredns.gr.",
    "TTL": "3600",
    "RR": "A",
    "Answer": [
      "116.202.176.26"
    ]
  },
  {
    "Query Time": "476.537"
  }
]
```

**Disclaimer**: This value is related to the client request towards the DoH provider, not the actual dns response.

### Choose another DNS server

```bash
doh-cli libredns.gr A --dns cloudflare
```

```bash
116.202.176.26
```

or you can use LibreDNS Block Trackers endpoint:

```bash
doh-cli --dns libredns-ads analytics.google.com A
```

```bash
0.0.0.0
```

or provide your own DoH url:

```bash
doh-cli --url https://doh.libredns.gr/dns-query www.example.com A
```

```bash
93.184.216.34
```

**Notice**: This option (--url) overrides the --dns option.
