import requests
from text_to_speech.base import Speech


class Watson(Speech):

    JAPANESE_VOICES = (
        u'ja-JP_EmiVoice',
    )

    ENGLISH_VOICES = (
        u'en-US_AllisonVoice', u'en-US_MichaelVoice', u'en-US_LisaVoice',
    )

    FR = (
        "fr-FR_ReneeVoice",
    )

    DE = (
        'de-DE_BirgitVoice', 'de-DE_DieterVoice',
    )

    IT = (
        'it-IT_FrancescaVoice',
    )

    def __init__(self, name, password):
        super().__init__(name, password)
        self.url = "https://stream.watsonplatform.net/text-to-speech/api"
        self.name = name
        self.password = password

    def speech(self, narration, lang, voice=None, **kwargs):
        """
        Returns the get HTTP response by doing a GET to
        /v1/synthesize with text, voice, accept
        """

        if not voice:
            voice = self.voices(lang)[0]

        accept = 'audio/wav'

        resp = requests.get(self.url + "/v1/synthesize",
                            auth=(self.name, self.password),
                            params={'text': narration, 'voice': voice,
                                    'accept': accept},
                            stream=False, verify=False
                            )

        return resp.content

    def voices(self, lang):
        lang = lang.lower()

        if lang in 'ja' or lang in 'jp':
            return Watson.JAPANESE_VOICES

        if lang in 'en':
            return Watson.ENGLISH_VOICES

        if lang in 'fr':
            return Watson.FR

        if lang in 'de':
            return Watson.DE

        if lang in 'it':
            return Watson.IT


if __name__ == '__main__':
    username = "adb36e85-0df9-446c-b168-741eb5439c50"
    password = "jxgksFkuZ74o"
    watson = Watson(username, password)
    content = watson.speech("I like the project", 'en')

    with open("/tmp/watson.wav", 'wb') as fp:
        fp.write(content)


