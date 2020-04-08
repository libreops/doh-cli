# doh-cli

a simple **DNS over HTTPS** client

This is a simple DoH python client (RFC 8484, GET), **json** output by default!
In less than 100 lines of code (more or less).

## Install

    pip3 install doh-cli

## Requirements

It's based & tested on Python 3.

If you want to contribute, you can clone the repository and install all
dependencies locally:

    pip3 install .

## Usage

    doh-cli libredns.gr A

## Help

    doh-cli --help

## Supported Resource Records

- A
- AAAA
- CNAME
- MX
- NS
- SOA
- SPF
- SRV
- TXT
- CAA

## Supported DoH Servers

- https://libredns.gr
- https://dns.google
- https://cloudflare-dns.com
- https://quad9.net
- https://doh.cleanbrowsing.org
- https://www.cira.ca/cybersecurity-services/canadian-shield
- you may also provide your own DoH server URL

### DoH Options

- libredns (**default**)
- libredns-ads (LibreDNS No-Trackers/Ads)
- google
- cloudflare
- quad9
- cleanbrowsing
- cira (CIRA's Canadian Shield)
- cira-protect (Protected adds malware and phishing blocking)
- cira-family (Family blocks malware and phishing plus pornographic content)

## Some Examples

### IPv4

    doh-cli libredns.gr A

```json
[{"Query": "libredns.gr.", "TTL": "366", "RR": "A", "Answer": "116.202.176.26"}]
```

you can use [jq](https://stedolan.github.io/jq/) to format, parse output:

    doh-cli libredns.gr A | jq .

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

    doh-cli libredns.gr AAAA | jq .

```json
[
  {
    "Query": "libredns.gr.",
    "TTL": "207",
    "RR": "AAAA",
    "Answer": "2a01:4f8:c2c:52bf::1"
  }
]
```

### CNAME

    doh-cli www.libredns.gr CNAME | jq .

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

    doh-cli libreops.cc MX | jq .

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

    doh-cli libredns.gr CAA

```json
[{"Query": "libredns.gr.", "TTL": "590", "RR": "CAA", "Answer": ["0", "issue", "\"letsencrypt.org\""]}]
```

### Plain Output

    doh-cli libredns.gr A --output plain

```bash
116.202.176.26
```

### verbose

    doh-cli libredns.gr A --output plain --verbose

```bash
https://doh.libredns.gr/dns-query?dns=lSIBAAABAAAAAAAACGxpYnJlZG5zAmdyAAABAAE
116.202.176.26
```

### debug

    doh-cli test.libredns.gr A --output plain --debug

```bash
id 24169
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

116.202.176.26
```

### Query time

    doh-cli test.libredns.gr A --output plain --time

```bash
Query time: 531.764

116.202.176.26
```

    doh-cli test.libredns.gr --time

```bash
Query time: 540.990

[{"Query": "test.libredns.gr.", "TTL": "3600", "RR": "A", "Answer": ["116.202.176.26"]}]
```

Disclaimer: This value is relative to python request against DoH service, not the actual dns response.

### Choose another DNS server

    doh-cli libredns.gr A --output plain --dns cloudflare

```bash
116.202.176.26
```

or you can use LibreDNS Block Trackers endpoint:

    doh-cli --output plain --dns libredns-ads analytics.google.com A

```bash
0.0.0.0
```

or provide your own DoH url:

    doh-cli --output plain --dns https://doh.libredns.gr/dns-query www.example.com A

```bash
93.184.216.34
```
