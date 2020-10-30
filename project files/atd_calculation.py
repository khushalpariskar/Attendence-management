from tkinter import *
import threading
root=Tk()

sec=0;min=0;hr=0
def timer(sec,min,hr):
    print('%hr:%min:%sec')
    sec+=1
    if(sec>=59):
        sec=0
        min+=1
    if(min>=59):
        min=0
        hr+=1
    my_timer=threading.Timer(10.0,timer(sec,min,hr))

lbl1=Button(root,text='start',command=timer(sec,min,hr))
lbl1.pack()
lbl2=Button(root,text='stop')
lbl2.pack()


root.mainloop()