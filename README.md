# JZP

[![Build](https://github.com/antoniovazquezblanco/jzp/actions/workflows/build.yml/badge.svg)](https://github.com/antoniovazquezblanco/jzp/actions/workflows/build.yml)
[![PyPI](https://img.shields.io/pypi/v/jzp)](https://pypi.org/project/jzp/)
[![Snyk](https://snyk.io/advisor/python/jzp/badge.svg)](https://snyk.io/advisor/python/jzp)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE.md)

A libary for dealing with the compression and decompression of Agilent JZP files.

I could not find documentation about this propietary format. Researching https://github.com/miek/agltzip I understood that the files consist on various possible versions of a header followed by LZSS compressed files.

## Installing

Install and update using `pip`:

```bash
$ pip install -U jzp
```

## Usage

Once installed, the `jzp` command will be available. An example usge for file extracting can be:

```bash
$ jzp -xf ./sys5462x.jzp
```

## Links

- PyPI Releases: https://pypi.org/project/jzp/
- Source Code: https://github.com/antoniovazquezblanco/jzp
- Issue Tracker: https://github.com/antoniovazquezblanco/jzp/issues
