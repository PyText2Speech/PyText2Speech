from text_to_speech.exceptions import LanguageNotSupportError, VoiceNotSupportError


class Speech(object):
    def __init__(self, name, password, file_path=None):
        self.__file = file_path if file_path else '/tmp/out.mp3'
        pass

    # TODO: what parameter is suitable?
    def make_file(self, **kwargs):

        lang = kwargs.get('lang', '')
        voice = kwargs.get('voice', '')

        self._validate_language(lang)
        self._validate_voices(voice, lang)

        binary, ext = self.speech(**kwargs)

        #TODO: save file

    def _validate_language(self, lang):

        if lang not in self.languages():
            raise LanguageNotSupportError("{} is not support".format(lang))

    def _validate_voices(self, voice, lang):

        if not voice:
            return

        if voice not in self.voices(lang):
            raise ("Voice {} is not support".format(voice))

    def speech(self, narration, lang, voice=None, **kwargs):
        """
        :param narration:
        :param lang:
        :param voice:
        :param kwargs:
        :return binary and type:
        """
        pass

    def voices(self, lang):
        return []

    def languages(self):
        return []

    def save(self, content):
        with open(self.__file, 'wb') as fp:
            fp.write(content)
