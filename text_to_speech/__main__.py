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

    -s, --service
        google, watson, itri, baidu

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

import sys
import getopt
from gtts import gTTS
try:
    opts, args = getopt.getopt(sys.argv[1:], "o:s:n:p:hv", ["output", "service", "name", "password", "help", "version"])
except getopt.GetoptError as e:
    print(__doc__)
    sys.exit("invalid option")

name = None
password = None
service_type = 'google'
output_file = 'out.mp3'

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
    elif o in ('-s', '--service'):
        service_type = a
    elif o in ('-o', '--output'):
        output_file = a

text_need_to_speech = ' '.join(args)

if service_type == 'google':
    tts = gTTS(text='Hello 123', lang='en')
    tts.save(output_file)

else:
    sys.exit("invalid service type")


