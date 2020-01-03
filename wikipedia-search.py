#wikipedia-search.py
#install wikipedia library from pip - pip install wikipedia

import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo

def wiki_answer():
    question=entry.get()
    answer=wikipedia.summary(question)
    showinfo("Answer",answer)
    
root=Tk()
root.geometry("400x200")

question=StringVar()
entry=Entry(root,textvariable=question)
entry.grid(row=1,column=3,padx=20)

b1=Button(root,width=12,text="search",command=wiki_answer)
b1.grid(row=5,column=3)

root.mainloop()

