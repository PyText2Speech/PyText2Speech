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

	-v, --verbose

EXAMPLES
    text2speech -o output.mp3 -s google  Have a goode day

COPYRIGHT
	MIT Licence

SOURCE
    https://github.com/PyText2Speech/PyText2Speech
"""

import sys
import getopt
from gtts import gTTS


def main(argv=None):
    if not argv:
        argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "o:s:n:p:hv", ["output", "service", "name", "password", "help", "verbose"])
    except getopt.GetoptError as e:
        print(__doc__)
        sys.exit("invalid option: " + str(e))

    name = None
    password = None
    service_type = 'google'
    output_file = 'out.mp3'
    verbose = False

    for o, a in opts:
        if o in ('-h', '--help'):
            print(__doc__)
            sys.exit(0)
        elif o in ('-v', '--verbose'):
            verbose = True
        elif o in ('-n', '--name'):
            name = a
        elif o in ('-p', '--password'):
            password = a
        elif o in ('-s', '--service'):
            service_type = a
        elif o in ('-o', '--output'):
            output_file = a

    text_need_to_speech = ' '.join(args)

    if verbose:
        print('[{}] {} > {}'.format(service_type, text_need_to_speech, output_file))
    if service_type == 'google':
        tts = gTTS(text=text_need_to_speech, lang='en')
        tts.save(output_file)
    else:
        sys.exit("invalid service type")


if __name__ == "__main__":
    main(sys.argv[1:])
