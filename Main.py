from tkinter import *
from tkinter import messagebox
import os
import Jar_main_c as jarvis


ws=Tk()
ws.title('Jarvis')
ws.geometry('800x450')
icon=PhotoImage(file=r"jarvis logo.png")
ws.iconphoto(True,icon)
status=True

def launch():
    def history():
        ws2=Toplevel(wst)
        ws2.geometry('200x450')
        ws2.resizable(False,False)

        t2canvas=Canvas(ws2,width=200,height=450)
        t2canvas.pack(fill='both',expand=True)
        t2canvas.create_image(-300,0,image=bgt,anchor='nw')

        r1=open('history.txt','r')
        st=r1.read()
        t2canvas.create_text(100,50,text=st,font=('Times New Roman',11),fill="white")
        

    def cred():
        ws3=Toplevel(wst)
        ws3.geometry('300x450')
        ws3.resizable(False,False)
        t3canvas=Canvas(ws3,width=300,height=450)
        t3canvas.pack(fill='both',expand=True)
        t3canvas.create_image(-250,0,image=bgt,anchor='nw')

        r2=open('Credits.txt','r')
        st=r2.read()
        t3canvas.create_text(150,100,text=st,font=('Times New Roman',11),fill='white')

    wst=Toplevel(ws)
    wst.geometry('200x450')
    wst.resizable(False,False)

    tcanvas=Canvas(wst,width=200,height=450)
    tcanvas.pack(fill='both',expand=True)
    tcanvas.create_image(-300,0,image=bgt,anchor='nw')

    button2=Button(wst,text="Credits",font=("Times New Roman",14),command=cred,fg='white',bg='black')
    button2_w=tcanvas.create_window(100,200,anchor='center',window=button2)
    
    button4=Button(wst,text="Chat History",font=("Times New Roman",14),command=history,fg='white',bg='black')
    button4_w=tcanvas.create_window(100,260,anchor="center",window=button4)
            

    jarvis.jarvis()
    if status==True:
        button1["state"] = DISABLED
    else:
        button1["state"] = ENABLED
        
    
            
ws.resizable(False,False)
bg=PhotoImage(file=r"Jarvbg.png")
bgt=PhotoImage(file=r"remodeledbg.png")
rcanvas=Canvas(ws, width=800, height=450)
rcanvas.pack(fill="both",expand=True)

rcanvas.create_image(0,0,image=bg,anchor="nw")


button1=Button(ws,text='Launch',command=launch,font=("Times New Roman",20),fg='white',bg='black')
button1_w=rcanvas.create_window(400,360,anchor="center",window=button1)



ws.mainloop()








