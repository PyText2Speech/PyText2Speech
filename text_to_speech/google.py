from gtts import gTTS
from text_to_speech.base import Speech


class Google(Speech):
    NAME = 'Google'
    # 'af': 'Afrikaans'
    # 'sq': 'Albanian'
    # 'ar': 'Arabic'
    # 'hy': 'Armenian'
    # 'ca': 'Catalan'
    # 'zh': 'Chinese',
    # 'zh-cn': 'Chinese (Mandarin/China)'
    # 'zh-tw': 'Chinese (Mandarin/Taiwan)'
    # 'zh-yue': 'Chinese (Cantonese)'
    # 'hr': 'Croatian'
    # 'cs': 'Czech'
    # 'da': 'Danish'
    # 'nl': 'Dutch'
    # 'en': 'English'
    # 'en-au': 'English (Australia)'
    # 'en-uk': 'English (United Kingdom)'
    # 'en-us': 'English (United States)'
    # 'eo': 'Esperanto'
    # 'fi': 'Finnish'
    # 'fr': 'French'
    # 'de': 'German'
    # 'el': 'Greek'
    # 'ht': 'Haitian Creole'
    # 'hi': 'Hindi'
    # 'hu': 'Hungarian'
    # 'is': 'Icelandic'
    # 'id': 'Indonesian'
    # 'it': 'Italian'
    # 'ja': 'Japanese'
    # 'ko': 'Korean'
    # 'la': 'Latin'
    # 'lv': 'Latvian'
    # 'mk': 'Macedonian'
    # 'no': 'Norwegian'
    # 'pl': 'Polish'
    # 'pt': 'Portuguese'
    # 'pt-br': 'Portuguese (Brazil)'
    # 'ro': 'Romanian'
    # 'ru': 'Russian'
    # 'sr': 'Serbian'
    # 'sk': 'Slovak'
    # 'es': 'Spanish'
    # 'es-es': 'Spanish (Spain)'
    # 'es-us': 'Spanish (United States)'
    # 'sw': 'Swahili'
    # 'sv': 'Swedish'
    # 'ta': 'Tamil'
    # 'th': 'Thai'
    # 'tr': 'Turkish'
    # 'vi': 'Vietnamese'
    # 'cy': 'Welsh'

    LANGUAGES = ('en', 'zh-cn', 'ja')

    ENGLISH_VOICES = (
        u'en', u'en-au', u'en-us', u'en-uk'
    )

    CHINESE_VOICES = (
        u'cn', u'zh-cn', u'zh-tw', u'zh-yue'
    )

    JAPANESE_VOICES = (
        u'ja',
    )

    FR = (
        "fr",
    )

    IT = (
        'it',
    )


    def __init__(self, name, password):
        super().__init__(name, password)
        self.name = name
        self.password = password

    def speech(self, narration, lang, voice=None, **kwargs):
        """
        Returns the get HTTP response by doing a GET to
        /v1/synthesize with text, voice, accept
        """

        resp = gTTS(text = narration, lang = lang)
        resp.save('/tmp/google.mp3')

        content = open('/tmp/google.mp3', 'rb').read()

        return content, 'mp3'

    def voices(self, lang):

        lang = lang.lower()

        if lang in 'cn' or lang in 'zh-cn':
            return Google.CHINESE_VOICES

        if lang in 'en':
            return Google.ENGLISH_VOICES

        if lang in 'ja' or lang in 'jp':
            return Google.JAPANESE_VOICES

        if lang in 'fr':
            return Google.FR

        if lang in 'it':
            return Google.IT

        return []


def main():
    username = "test123"
    password = "test123"

    google = Google(username, password)
    content, extension = google.speech("I like the project", lang='en-uk')

    with open("/tmp/google1." + extension, 'wb') as fp:
        fp.write(content)

if __name__ == '__main__':
    main()






