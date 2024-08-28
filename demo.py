from gtts import gTTS
import os
from tkinter import *

root = Tk()
canvas = Canvas(root, width=400, height=400)
canvas.pack()

entry= Entry(root)
#attach entry to the window
canvas.create_window(200, 180, window=entry)
#add button for tts and create function for tts
def tts():
  text = entry.get()
  language='en'
  output = gTTS(text=text, lang=language, slow=False)
  output.save('output.mp3')
  os.system("afplay output.mp3")

button = Button(text="Start", command=tts)
canvas.create_window(200, 230, window=button)

root.mainloop()
# text ="James is the best"
# output = gTTS(text=text, lang='en', slow=False)
# output.save('output.mp3')

# os.system("afplay output.mp3")

# text = open('demo.txt', 'r').read()
# language='en'
# output = gTTS(text=text, lang=language, slow=False)
# output.save('fileoutput.mp3')
# os.system("afplay fileoutput.mp3")