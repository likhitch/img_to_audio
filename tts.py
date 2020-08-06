from gtts import gTTS
text=""
with open("sample.txt","r") as file:
    for line in file:
        text=text+line
speech=gTTS(text)
speech.save("1.mp3")