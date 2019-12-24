# doh-cli

a simple **DNS over HTTPS** client

This is a simple DoH python client (RFC 8484, GET), **json** output by default!
In ~55 lines of code (more or less).

## Install

    pip3 install doh-cli

## Requirements

It's based on (tested on Python 3.8.0).

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

## Supported DoH Servers

- https://libredns.gr
- https://dns.google
- https://cloudflare-dns.com
- https://quad9.net
- https://doh.cleanbrowsing.org

## Some Examples

- IPv4

    `doh-cli libredns.gr A`

```json
[{"Query": "libredns.gr.", "TTL": "366", "RR": "A", "Answer": "116.203.115.192"}]
```

you can use [jq](https://stedolan.github.io/jq/) to format, parse output:

    doh-cli libredns.gr A | jq .

```json
[
  {
    "Query": "libredns.gr.",
    "TTL": "54",
    "RR": "A",
    "Answer": "116.203.115.192"
  }
]
```

- IPv6

    `doh-cli libredns.gr AAAA | jq .`

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

- CNAME

    `doh-cli www.libredns.gr CNAME | jq .`

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

- Plain Output

    `doh-cli libredns.gr A --output plain`

```
116.203.115.192
```

- debug

    `doh-cli libredns.gr A --output plain --debug`

```
https://doh.libredns.gr/dns-query?dns=lSIBAAABAAAAAAAACGxpYnJlZG5zAmdyAAABAAE
116.203.115.192
```

- Change DNS server

    `doh-cli libredns.gr A --output plain --dns cloudflare`

```
116.203.115.192
```

or you can use LibreDNS Block Trackers endpoint:

    doh-cli --output plain --dns libredns-ads analytics.google.com A

```
0.0.0.0
```
