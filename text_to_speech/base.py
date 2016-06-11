class Speech(object):
    def __init__(self, name, password, file_path=None):
        self.__file = file_path if file_path else '/tmp/out.mp3'
        pass

    # TODO: what parameter is suitable?
    def make_file(self, *kwarg, **kwargs):
        binary = self.speech(*kwarg, **kwargs)

    def speech(self, narration, lang, voice=None, **kwargs):
        """
        :param narration:
        :param lang:
        :param voice:
        :param kwargs:
        :return binary and type:
        """
        pass

    def meta(self):
        pass

    def voices(self, lang):
        return []

    def languages(self):
        return []

    def save(self, content):
        with open(self.__file, 'wb') as fp:
            fp.write(content)
