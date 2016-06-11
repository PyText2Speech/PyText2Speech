""" PyText2Speech

NAME
	text_to_speech -  text to speech

SYNOPSIS
	text_to_speech [OPTION] [TEXT]...

DESCRIPTION
    -n, --name
        user name for service IBM watson/ITRI/Baidu.

    -p, --password
        password

	-h, --help
		show usage

	-v, --version

EXAMPLES
    text_to_speech -n USERNAME -p PASSWORD TEXT TO SPPECH


COPYRIGHT
	MIT Licence

SOURCE
    https://github.com/PyText2Speech/PyText2Speech
"""

import os
import sys
import getopt
try:
    opts, args = getopt.getopt(sys.argv[1:], "n:p:hv", ["name", "password", "help", "version"])
except getopt.GetoptError as e:
    print(__doc__)
    sys.exit("invalid option")

name = None
password = None

for o, a in opts:
    if o in ('-h', '--help'):
        print(__doc__)
        sys.exit(0)
    elif o in ('-v', '--version'):
        print(0.1)
        sys.exit(0)
    elif o in ('-n', '--name'):
        name = a
    elif o in ('-p', '--password'):
        password = a

text_need_to_speech = ' '.join(args)

print('speech: ' + text_need_to_speech)
