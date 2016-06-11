from text_to_speech.baidu import BaiduSpeech
from text_to_speech.watson import Watson
from text_to_speech.itri import Itri
from text_to_speech.google import Google


def get_speech(lang):

    lang = lang.lower()
    if lang in 'zh':
        speech_class = BaiduSpeech
    elif lang in 'tai':
        speech_class = Itri
    elif lang in ['ja', 'jp', 'it', 'en']:
        speech_class = Watson
    else:
        speech_class = Google

    return speech_class
