#!/usr/bin/env python3
"""Migrate FreeOTP tokens.xml to importable JSON for FreeOTP+."""

import argparse
import json
import xml.etree.ElementTree as ET


parser = argparse.ArgumentParser(description='FOTP migration to FOTPplus')
parser.add_argument(
    '-i', action='store', dest='f_input', default='tokens.xml',
    help='Input filename, if not specified "tokens.xml" used'
)
parser.add_argument(
    '-o', action='store', dest='f_output', default=None,
    help='Output filename, if not specified stdout used'
)
args = parser.parse_args()

export = dict()
export['tokens'] = list()

root = ET.parse(args.f_input).getroot()
for el in root:
    if "tokenOrder" in el.attrib['name']:
        export['tokenOrder'] = json.loads(el.text)
    else:
        export['tokens'].append(json.loads(el.text))

if args.f_output:
    with open(args.f_output, 'w') as fout:
        fout.write(json.dumps(export))
else:
    print(json.dumps(export))
