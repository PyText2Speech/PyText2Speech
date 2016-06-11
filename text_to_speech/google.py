# -*- encoding=utf8 -*-


from gtts import gTTS

tts = gTTS(text='Hello 123', lang='en')
tts.save('test.mp3')
