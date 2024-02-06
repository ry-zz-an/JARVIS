from tkinter import *          #install tkinter on cmd
from tkinter import messagebox
import os
import mysql.connector as ms


ws=Tk()
ws.title('Register')
ws.geometry('800x450')
icon=PhotoImage(file=r"jarvis logo.png")
ws.iconphoto(False,icon)

#MySQL Connection
mycon=ms.connect(user='root',host='localhost',
                 database='jarv',password='password',charset='utf8')#either change the database name or create a database called jarv
cursor=mycon.cursor()


#Background Image
bg=PhotoImage(file=r"remodeledbg.png") #insert the absolute path of the background image (not gif unfortunately) that we're using

#Registration Button
def register():
    while True:
        u1=entry1.get()
        u2=entry2.get()
        u3=entry3.get()
        if u2!=u3:
            messagebox.showerror('Registration','Passwords do not match!')
            entry2.delete(0,END)
            entry3.delete(0,END)
        else:
            sql='''insert into IDs values(%s, %s)'''#change the table name or add a table called IDs
            rec=(u1,u2)
            cursor.execute(sql,rec)
            mycon.commit()  
            messagebox.showinfo('Registration','Registration Complete!')
            ws.destroy()
            os.system(r"Jarvis.py")
        break
    
def show1():
    if button2['text']=="Show":
        button2['text']="Hide"
    elif button2['text']=="Hide":
        button2['text']="Show"
    if entry2.cget('show')=='*':
        entry2.config(show='')
    elif entry2.cget('show')=='':
        entry2.config(show='*')
    
    
    
def show2():
    if button3['text']=="Show":
        button3['text']="Hide"
    elif button3['text']=="Hide":
        button3['text']="Show"
    if entry3.cget('show')=='*':
        entry3.config(show='')
    elif entry3.cget('show')=='':
        entry3.config(show='*')
    
    

    
rcanvas=Canvas(ws, width=800, height=450)
rcanvas.pack(fill="both",expand=True)


rcanvas.create_image(0,0,image=bg,anchor="nw")


#Username block
rcanvas.create_text(300,200,text="Username:",font=("Times New Roman",13),fill="white")
entry1=Entry(ws,bg='#020030',fg='white')
rcanvas.create_window(430,200,window=entry1)

#Password block
rcanvas.create_text(300,240,text="Password:",font=("Times New Roman",13),fill="white")
entry2=Entry(ws,show='*',bg='#020030',fg='white')
rcanvas.create_window(430,240,window=entry2)

#Confirm block
rcanvas.create_text(270,280,text="Confirm Password:",font=("Times New Roman",13),fill="white")
entry3=Entry(ws,show='*',bg='#020030',fg='white')
rcanvas.create_window(430,280,window=entry3)

button1=Button(ws,text="Register",command=register,font=("Times New Roman",20),fg='white',bg='black')
button1_w=rcanvas.create_window(350,300,anchor="nw",window=button1)

button2=Button(ws,text="Show",command=show1,font=('Times New Roman',9),fg='white',bg='black')
button2_w=rcanvas.create_window(530,240,window=button2)

button3=Button(ws,text="Show",command=show2,font=('Times New Roman',9),fg='white',bg='black')
button3_w=rcanvas.create_window(530,280,window=button3)
    
ws.mainloop()
