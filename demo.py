from gtts import gTTS
import os

# text ="James is the best"
# output = gTTS(text=text, lang='en', slow=False)
# output.save('output.mp3')

# os.system("afplay output.mp3")

text = open('demo.txt', 'r').read()
language='en'
output = gTTS(text=text, lang=language, slow=False)
output.save('fileoutput.mp3')
os.system("afplay fileoutput.mp3")