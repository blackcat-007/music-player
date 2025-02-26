import tkinter as tk
import fnmatch
import os
from pygame import mixer
#design ui
canvas = tk.Tk()
canvas.title("life music player")
canvas.geometry("500x300")
canvas.config(bg='black')

rootpath="C:\\Users\\Pradipta Gupta\\OneDrive\\Documents\\fighter"
pattern="*.mp3"
'''prev_img=tk.PhotoImage(file="th (3).jpg")
play_img=tk.PhotoImage(file="th.jpg")
stop_img=tk.PhotoImage(file="th (5).jpg")
pause_img=tk.PhotoImage(file="th (1).jpg")
next_img=tk.PhotoImage(file="th 4).jpg")'''
#functions of buttons
mixer.init()
def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath+"\\"+listBox.get("anchor"))
    mixer.music.play()
def stop():
    
    mixer.music.stop()
    listBox.select_clear('active')
def next():
      next_song=listBox.curselection()
      next_song=next_song[0]+1
      next_song_name=listBox.get(next_song)
      label.config(text=next_song_name)
      
      mixer.music.load(rootpath+"\\"+ next_song_name)
      mixer.music.play()

      listBox.select_clear(0,'end')
      listBox.activate(next_song)
      listBox.select_set(next_song)
def prev():
      prev_song=listBox.curselection()
      prev_song=prev_song[0]-1
      prev_song_name=listBox.get(prev_song)
      label.config(text=prev_song_name)
      
      mixer.music.load(rootpath+"\\"+prev_song_name)
      mixer.music.play()

      listBox.select_clear(0,'end')
      listBox.activate(prev_song)
      listBox.select_set(prev_song)
def pause():
     if pauseButton["text"]=="pause":
          mixer.music.pause()
          pauseButton["text"]="play"
     else:
          mixer.music.unpause()
          pauseButton["text"]="pause"
#listbox
listBox=tk.Listbox(canvas,fg="cyan",bg="indigo",width=100,font=('ds-digital',12))
listBox.pack(padx=15,pady=15)
label=tk.Label(canvas,text='blue',bg="cyan",fg="magenta",font=('ds-digital',14))
#adding function buttons designs
top=tk.Frame(canvas,bg="blue")
top.pack(padx=10,pady=5,anchor='center')
prevButton=tk.Button(canvas,text="prev",bg='yellow',font=('ds-digital',10),command=prev)
prevButton.pack(pady=15,in_=top,side='left')

stopButton=tk.Button(canvas,text="stop",bg='red',font=('ds-digital',10),command=stop)
stopButton.pack(pady=15,in_=top,side='left')
playButton=tk.Button(canvas,text="play",bg='green',font=('ds-digital',10),command=select)
playButton.pack(pady=15,in_=top,side='left')

pauseButton=tk.Button(canvas,text="pause",bg='white',font=('ds-digital',10),command=pause)
pauseButton.pack(pady=15,in_=top,side='left')
nextButton=tk.Button(canvas,text="next",bg='cyan',font=('ds-digital',10),command=next)
nextButton.pack(pady=15,in_=top,side='left')

#adding song list
for root , dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)

canvas.mainloop()