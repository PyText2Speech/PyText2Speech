import subprocess
from text_to_speech.exceptions import SoxNotInstallError


def play(filename):
    command = ['play',  "{filename}".format(filename=filename)]
    try:
        subprocess.call(command)
    except FileNotFoundError as e:
        raise SoxNotInstallError("please find out how to install sox")

if __name__ == "__main__":
    play("/tmp/test.mp3")
