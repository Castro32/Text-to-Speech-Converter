from gtts import gTTS
import os
from tkinter import Tk , Label, Entry, Button
def convert_to_speech():
    text= text_entry.get()
    language='en'
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("output.mp3")
    os.system("Start output.mp3")
    
#Gui main window
root=Tk()
root.title("Text-to-Speech-Converter")
root.geometry("600x300")
root.resizable(True,True)

label_style = {
    "font": ("Arial", 14),
    "fg": "blue",
    "bg": "lightgray",
    "pady": 10,
}

entry_style = {
    "font": ("Arial", 12),
    "width": 40,
    
}

button_style = {
    "font": ("Arial", 12),
    "bg": "green",
    "fg": "white",
    "pady": 5,
    "padx": 10,
}

#Gui Components
label = Label(root, text="Enter text:")
label.config(**label_style)
label.pack()

text_entry=Entry(root, **entry_style)
text_entry.pack()

convert_button = Button(root, text="Convert to Speech", command=convert_to_speech)
convert_button.pack()

root.mainloop()