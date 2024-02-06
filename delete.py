from tkinter import *
from tkinter import messagebox
import os
import mysql.connector as ms

ws=Tk()
ws.title('Delete User')
ws.geometry('800x450')
ws.resizable(False,False)

#MySQL Connection
mycon=ms.connect(user='root',host='localhost',
                 database='jarv',password='password',charset='utf8')#either change the database name or create a database called jarv
cursor=mycon.cursor()

    
icon=PhotoImage(file=r"jarvis logo.png")

bg=PhotoImage(file=r"remodeledbg.png")#background image here - use a png file ONLY

ws.iconphoto(False,icon)

def delete():
    u1=entry1.get()
    u2=entry2.get()
    sql='''select*from IDs;'''
    cursor.execute(sql)
    data=cursor.fetchall()  
    count=0
    for x in data:
        if u1==x[0]:
            count+=1
            if u2!=x[1]:
                messagebox.showerror('Login','Incorrect Password, Please Try Again.')
                entry2.delete(0,END)
                
            else:
                sql='''delete from IDs where Username=%s and Password=%s;'''
                
                rec=(u1,u2)
                cursor.execute(sql,rec)
                mycon.commit()
                messagebox.showinfo('Delete User','Deleted successfully!')
                ws.destroy()
                os.system(r"Jarvis.py")
            break
        else:
            continue
    if count==0:
        messagebox.showerror('Login','User does not exist.')
        entry1.delete(0,END)
        entry2.delete(0,END)

    
def show():
    if button2['text']=="Show":
        button2['text']="Hide"
    elif button2['text']=="Hide":
        button2['text']="Show"
    if entry2.cget('show')=='*':
        entry2.config(show='')
    elif entry2.cget('show')=='':
        entry2.config(show='*')



        
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
button2=Button(ws,text="Show",command=show,font=('Times New Roman',9),fg='white',bg='black')#Show Password
button2_w=rcanvas.create_window(530,240,window=button2)


button1=Button(ws,text="Delete",command=delete,font=("Times New Roman",20),fg='white',bg='black')
button1_w=rcanvas.create_window(350,300,anchor="nw",window=button1)


ws.mainloop()

