from tkinter import *          #install tkinter on cmd
from tkinter import messagebox
import os
import mysql.connector as ms

#Defining the window
ws=Tk()
ws.title('Reset Password')
ws.geometry('800x450')
ws.resizable(False,False)

icon=PhotoImage(file='jarvis logo.png')
ws.iconphoto(False,icon)

#MySQL Connection
mycon=ms.connect(user='root',host='localhost',
                 database='jarv',password='password',charset='utf8')#either change the database name or create a database called jarv
cursor=mycon.cursor()


#Background Image
bg=PhotoImage(file=r"remodeledbg.png") #insert the absolute path of the background image (not gif unfortunately) that we're using

#Registration Button
def reset():
    u1=entry1.get()
    u2=entry2.get()
    u3=entry3.get()
    sql='''select*from IDs;'''
    cursor.execute(sql)
    data=cursor.fetchall()
    count=0
    for x in data:
        if u1==x[0]:
            count+=1
            if u2!=u3:
                messagebox.showerror('Reset Password','Passwords do not match!')
                entry2.delete(0,END)
                entry3.delete(0,END)
                
            else:
                sql='''update IDs set Password = %s where Username = %s;'''
                rec=(u2,u1)
                cursor.execute(sql,rec)
                mycon.commit()
                messagebox.showinfo('Reset Password','Password changed!')
                ws.destroy()
                os.system(r"Jarvis.py")
            break
        else:
            continue
    if count==0:
        messagebox.showerror('Reset Password','Invalid Username!')
        entry2.delete(0,END)
        entry3.delete(0,END)
        entry1.delete(0,END)
        
    
#Defining the Show buttons
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


rcanvas.create_image(0,0,image=bg,anchor="nw")#inserting background

#Username block
rcanvas.create_text(315,200,text="Username:",font=("Times New Roman",13),fill="white")
entry1=Entry(ws,bg='#020030',fg='white')
rcanvas.create_window(430,200,window=entry1)

#Password block
rcanvas.create_text(300,240,text="New Password:",font=("Times New Roman",13),fill="white")
entry2=Entry(ws,show='*',bg='#020030',fg='white')
rcanvas.create_window(430,240,window=entry2)
button2=Button(ws,text="Show",command=show1,font=('Times New Roman',9),fg='white',bg='black')#Show Password
button2_w=rcanvas.create_window(530,240,window=button2)

#Confirm block
rcanvas.create_text(270,280,text="Confirm New Password:",font=("Times New Roman",13),fill="white")
entry3=Entry(ws,show='*',bg='#020030',fg='white')
rcanvas.create_window(430,280,window=entry3)
button3=Button(ws,text="Show",command=show2,font=('Times New Roman',9),fg='white',bg='black')#Show Password
button3_w=rcanvas.create_window(530,280,window=button3)


#Reset Button
button1=Button(ws,text="Reset",command=reset,font=("Times New Roman",20),fg='white',bg='black')
button1_w=rcanvas.create_window(350,300,anchor="nw",window=button1)




ws.mainloop()
