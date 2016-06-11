import pytest
from .baidu import BaiduSpeech


def func(x):
    """this is sample"""
    return x + 1


def test_answer():
    """this is sample"""
    assert func(3) == 4


def test_token():
    baidu = BaiduSpeech("hkOIhq0imbfhzxGsxq2HwYN7", "27c99621b1c7b2777ce054442c15382b")
    content = baidu.speech(u"很高興參加這個project", u'zh')
    assert str(content) == '<Response [200]>'