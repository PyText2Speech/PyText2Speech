class TextToSpeechException(Exception):
    pass


class AuthenticationError(TextToSpeechException):
    """If password or username get problem, raise the exception"""


class LanguageNotSupportError(TextToSpeechException):
    """if the language is not support, raise the exception"""


class VoiceNotSupportError(TextToSpeechException):
    """if the voice is not support, raise the exception"""
