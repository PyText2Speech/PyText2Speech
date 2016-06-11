import requests
import wget
from text_to_speech.base import Speech


class Itri(Speech):

    NAME = 'ITRI'
    # Bruce
    # 中英切換男生語音(default)
    # Theresa
    # 中英切換女生語音
    # Angela
    # 中英切換小女孩語音
    # MCHEN_Bruce
    # 中英統合男生語音
    # MCHEN_Joddess
    # 中英統合女生語音
    # ENG_Bob
    # 英文男生語音
    # ENG_Alice
    # 英文女生語音
    # ENG_Tracy
    # 英文小男孩語音
    # TW_LIT_AKoan
    # 台語女生語音(文讀台)
    # TW_SPK_AKoan
    # 台語女生語音(白話台)
    # http: // tts.itri.org.tw / development / web_service_api.php

    LANGUAGES = ('en', 'zh-cn')

    ENGLISH_VOICES = (
        u'ENG_Bob', u'ENG_Alice', u'ENG_Alice', u'ENG_Tracy'
    )

    CHINESE_VOICES = (
        u'Bruce', u'Theresa', u'Angela', u'MCHEN_Bruce'
    )

    TAIWANESE_VOICE = (
        u'TW_LIT_AKoan', u'TW_SPK_AKoan'
    )

    def __init__(self, name, password, **kwargs):
        super().__init__(name, password, **kwargs)
        self.url = "http://tts.itri.org.tw/TTSService/Soap_1_3.php?wsdl"
        self.name = name
        self.password = password

    def speech(self, narration, lang, voice=None, **kwargs):
        """
        Returns the get HTTP response by doing a GET to
        /v1/synthesize with text, voice, accept
        """

        if not voice:
            voice = self.voices(lang)[0]

        volume = 10
        speed = 1
        headers = {'content-type': 'text/xml'}
        body = u"""<?xml version="1.0" encoding="utf-8"?>
            <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
            <ConvertText>
            <accountID>%s</accountID>
            <password>%s</password>
            <TTStext>%s</TTStext>
            <TTSSpeaker>%s</TTSSpeaker>
            <volume>%s</volume>
            <speed>%s</speed>
            <outType>wav</outType>
            </ConvertText>
            </soap:Body>
            </soap:Envelope>""" % (self.name, self.password, narration, voice, volume, speed)

        resp = requests.post(self.url, data=body.encode('utf-8'), headers=headers)

        body = """<?xml version="1.0" encoding="utf-8"?>
          <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
            <soap:Body>
              <GetConvertStatus>
              <accountID>test-for-r</accountID>
              <password>test1for1r</password>
              <convertID>%s</convertID>
              </GetConvertStatus>
            </soap:Body>
          </soap:Envelope>""" % (resp.text.split('</Result>')[0].split('&amp;')[2])

        resp = requests.post(self.url, data=body, headers=headers)

        while resp.text.split('</Result>')[0].split('&amp;')[2] != '2':
            from time import sleep
            sleep(0.5)
            print(1)
            resp = requests.post(self.url, data=body, headers=headers)

        resp = resp.text.split('</Result>')[0].split('&amp;')[4]
        wget.download(resp, out="/tmp/itri.wav")

        content = open('/tmp/itri.wav', 'rb').read()
        return content, 'wav'

    def voices(self, lang):
        lang = lang.lower()

        if lang in 'cn' or lang in 'zh-cn':
            return Itri.CHINESE_VOICES

        if lang in 'en':
            return Itri.ENGLISH_VOICES

        return []


def main():
    username = "test-for-r"
    password = "test1for1r"
    itri = Itri(username, password)
    content, extension = itri.speech(u"很高興參加這個project", u'zh-cn', voice = u'TW_SPK_AKoan')

    with open("/tmp/itri1." + extension, 'wb') as fp:
        fp.write(content)

if __name__ == '__main__':
    main()
