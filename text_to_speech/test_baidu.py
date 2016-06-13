import pytest

from .baidu import BaiduSpeech

#from .configs import server


def func(x):
    """this is sample"""
    return x + 1


def test_answer():
    """this is sample"""
    assert func(3) == 4


@pytest.fixture
def baidu():
    #return BaiduSpeech(name=server['BAIDU']['name'], password=server['BAIDU']['pwd'])
    return BaiduSpeech(name="hkOIhq0imbfhzxGsxq2HwYN7",
        password="27c99621b1c7b2777ce054442c15382b")

def test_token(baidu):
    token = baidu.token
    assert token != ''


def test_speech(baidu):
    content, extension = baidu.speech(u"很高興參加這個project", u'zh-cn')
    assert extension == 'mp3'