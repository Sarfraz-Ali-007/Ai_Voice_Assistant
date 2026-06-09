from gtts import gTTS

def speak(text):

    filename = "response.mp3"

    tts = gTTS(text=text)

    tts.save(filename)

    return filename
