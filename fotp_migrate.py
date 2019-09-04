#!/usr/bin/env python3
"""
Get FreeOTP tokens.

Steps to get tokens.xml
1. Android -> Settings -> System -> About -> Buil number (tap,tap,tap)
  to get android developer mode
2. In "Developer options" allow "USB debugging"
3. Connect phone to PC

ADB backup (case for FreeOTP)
1. install 'adb'
2. adb backup -f freeotp-backup.ab -apk org.fedorahosted.freeotp
3. asked for password so entry some <password>

In case encrypted phone
1. download https://github.com/nelenkov/android-backup-extractor/releases
2. java -jar abe-all.jar unpack freeotp-backup.ab freeotp.tar <password>
3. tar xvf freeotp.tar
4. tokens are in apps/org.fedorahosted.freeotp/sp/tokens.xml
5. run this script in same folder as 'tokens.xml'

Do import after export in short time frame as OTP counter can get raised and
your generated tokens won't work.
"""

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
