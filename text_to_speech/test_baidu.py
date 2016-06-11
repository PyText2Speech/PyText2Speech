import pytest
from .baidu import BaiduSpeech
from .configs import server


def func(x):
    """this is sample"""
    return x + 1


def test_answer():
    """this is sample"""
    assert func(3) == 4


def test_token():
    baidu = BaiduSpeech()
    content = baidu.speech(u"很高興參加這個project", u'zh')
    assert content != '' 