# Changelog

This document tracks all notable changes to doh-cli, introduced on each release.

## v0.8 - 2025-01-10

- Added support for RFC9460

## v0.7 - 2022-10-29

- Argument url is overwriting dns argument with it's default value (fix bug)

## v0.6 - 2021-03-25

- Add support to request DNSSEC signatures
- Support handling multiple answer sections in a response
- Use itertools to append multiple dns answers
- Simplify doh-cli plain/json usage
- Enhance code readability
- Make doh-cli module more independent
- Update README accordingly

## v0.5 - 2021-03-05

- Add support for DNSKEY and DS RRs
- Update README with new RR examples
- Fix output bug on multiple answers

## v0.4 - 2021-03-02

- Update Documentation Notes
- Add custom DoH endpoint --url option
- Add version option to doh-cli
- Add cleanbrowsing & securedns DoH Endpoints
- Verbose option returns the rest DoH request
- Show multiple DNS answers when exist
- Use base64url for dns request message
- DNS response should have "application/dns-message" headers
- Using RequestException instead of generic Exception
- Split module for readability and modularity

## v0.3 - 2020-04-12

- Swapping positional arguments (domain, RR) if needed
- Check Response Status in case of a Server Error
- Switched default output to plain
- Debug, Verbose & Query Time values are now part of plain/json output

## v0.2 - 2020-04-08

- Support custom DoH endpoints
- More verbose debug option
- Allow user to use any RR type
- Add CIRA provider
- New time option for query response time
- Expand documentation
- New verbose option for displaying DNS wire

## v0.1 - 2019-12-24

- Initial release
