from gtts import gTTS
import os

text ="James is the best"
output = gTTS(text=text, lang='en', slow=False)
output.save('output.mp3')

os.system("afplay output.mp3")