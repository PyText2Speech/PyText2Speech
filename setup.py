from setuptools import find_packages, setup

setup(
    name="pytext2speech",
    packages=find_packages(),
    version="0.0.1",
    description="",
    author="PyText2Speech",
    author_email="",
    url="https://github.com/PyText2Speech",
    download_url="",
    # keywords=["encoding", "i18n", "xml"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    entry_points={'console_scripts': [
        'text2speech = text_to_speech.__main__:main',
    ]},
    long_description="""\
Text to Speech package
-------------------------------------

Speech text integrate with google, IBM watson, Industrial Technology Research Institute of Taiwan, Baidu.

This version requires Python 3.
"""
)
