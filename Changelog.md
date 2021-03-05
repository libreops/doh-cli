# Changelog

This document tracks all notable changes to doh-cli, introduced on each release.

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
