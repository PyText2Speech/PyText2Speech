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
from text_to_speech.configs import server
from text_to_speech.get_speech import get_speech
from langdetect import detect
from text_to_speech.watson import Watson
from text_to_speech.google import Google
from text_to_speech.itri import Itri
from text_to_speech.baidu import BaiduSpeech
from text_to_speech.cmd_player import play


def main(argv=None):
    if not argv:
        argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "l:o:s:n:p:hv", ["lang", "output", "service", "name", "password", "help", "verbose"])
    except getopt.GetoptError as e:
        print(__doc__)
        sys.exit("invalid option: " + str(e))

    name = None
    password = None
    service_type = None
    output_file = None
    verbose = False
    lang = None

    for o, a in opts:
        if o in ('-h', '--help'):
            print(__doc__)
            sys.exit(0)
        elif o in ('-v', '--verbose'):
            verbose = True
        elif o in ('-n', '--name'):
            lang = a
        elif o in ('-l', '--lang'):
            name = a
        elif o in ('-p', '--password'):
            password = a
        elif o in ('-s', '--service'):
            service_type = a
        elif o in ('-o', '--output'):
            output_file = a


    # TODO: detect languge in follow
    text_need_to_speech = ' '.join(args)

    if not lang:
        lang = detect(text_need_to_speech)

    if not service_type:
        service_type = get_speech(lang).NAME

    if not name and not password:
        try:
            s = server[service_type.upper()]
            name = s['name']
            password = s['pwd']
        except KeyError:
            sys.exit("invalid service type")

    if verbose:
        print('[{}] {} > {}'.format(service_type, text_need_to_speech, output_file))
    if service_type == 'GOOGLE':
        # tts = gTTS(text=text_need_to_speech, lang=lang)
        # tts.save(output_file)
        speaker = Google(name, password, output_file)
    elif service_type == 'WATSON':
        speaker = Watson(name, password, output_file)
    elif server == "ITIR":
        speaker = Itri(name, password, output_file)
    elif server == 'BAIDU':
        speaker = BaiduSpeech(name, password, output_file)
    else:
        sys.exit("invalid service type")

    play(speaker.make_file())

if __name__ == "__main__":
    from text_to_speech.cmd_player import play
    main(sys.argv[1:])
