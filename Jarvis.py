from tkinter import *
import os

ws=Tk()
ws.title('Jarvis')
ws.geometry('800x450')
ws.resizable(False,False)

icon=PhotoImage(file=r"jarvis logo.png")
bg=PhotoImage(file=r"remodeledbg.png")
ws.iconphoto(False,icon)



def register():
    ws.destroy()
    os.system(r"register.py")
    

def login():
    ws.destroy()
    os.system(r"login.py")

def forgor():
    ws.destroy()
    os.system(r"forgor.py")

def delete():
    ws.destroy()
    os.system(r"delete.py")
    

rcanvas=Canvas(ws, width=800, height=450)
rcanvas.pack(fill="both",expand=True)



rcanvas.create_image(0,0,image=bg,anchor="nw")

rcanvas.create_text(410,50,text="J.A.R.V.I.S.",font=("Times New Roman",30),fill="white")

rcanvas.create_line(400,100,400,400,fill='white')

rcanvas.create_text(200,200,text="New User?",font=("Times New Roman",24),fill="white")

button1=Button(ws,text="Register",command=register,font=("Times New Roman",20),fg='white',bg='black')
button1_w=rcanvas.create_window(140,300,anchor="nw",window=button1)

rcanvas.create_text(600,200,text="Existing User?",font=("Times New Roman",24),fill="white")

button2=Button(ws,text="Login",command=login,font=("Times New Roman",20),fg='white',bg='black')
button2_w=rcanvas.create_window(550,300,anchor="nw",window=button2)

rcanvas.create_text(655,406,text="Forgot Password?",font=("Times New Roman",9),fill="white")

button3=Button(ws,text="Click Here",command=forgor,font=("Times New Roman",9),fg='white',bg='black')
button3_w=rcanvas.create_window(700,395,anchor="nw",window=button3)

rcanvas.create_text(85,406,text="Delete Account?",font=("Times New Roman",9),fill="white")

button4=Button(ws,text="Click Here",command=delete,font=("Times New Roman",9),fg='white',bg='black')
button4_w=rcanvas.create_window(130,395,anchor="nw",window=button4)


ws.mainloop()








