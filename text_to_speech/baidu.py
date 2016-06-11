# -*- encoding=utf8 -*-
import requests
from text_to_speech.exceptions import AuthenticationError, LanguageNotSupportError

from text_to_speech.base import Speech

from text_to_speech.configs import server

class BaiduSpeech(Speech):

    def __init__(self, name=server["BAIDU"].name, password=server["BAIDU"].pwd):
        super(BaiduSpeech, self).__init__(name, password)

        uri = "https://openapi.baidu.com/oauth/2.0/token"

        params = {
            'grant_type': 'client_credentials',
            'client_id': name,
            'client_secret': password,
        }

        resp = requests.get(uri, params=params).json()

        if 'error' in resp:
            raise AuthenticationError(resp['error_description'])

        self.token = resp['access_token']

    def speech(self, narration, lang, voice='', **kwargs):

        spd = kwargs.get('spd', 5)
        pit = kwargs.get('pit', 5)
        vol = kwargs.get('vol', 5)

        if 'zh' in lang:
            lang = 'zh'

        response = requests.get("http://tsn.baidu.com/text2audio", {
            "tex": narration.encode('utf-8'),
            "lan": lang,
            "tok": self.token,
            "ctp": 1,
            "spd": spd,
            "pit": pit,
            "vol": vol,
            "cuid": "xxx-xxx-xxx-xxx"
        })

        print(response)

        return response.content, 'mp3'

    def voices(self, lang):

        if 'zh' in lang:
            return ['Ann Li', '']

        return ['']

    def languages(self):
        return ["zh"]


if __name__ == "__main__":

    #baidu = BaiduSpeech("hkOIhq0imbfhzxGsxq2HwYN7", "27c99621b1c7b2777ce054442c15382b")
    baidu = BaiduSpeech()
    content = baidu.speech(u"很高興參加這個project", u'zh-cn')

    with open("/tmp/test." + extension, 'wb') as fp:
        fp.write(content)
