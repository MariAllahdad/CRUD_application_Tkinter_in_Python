from tkinter import  *
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = 'hr',
    database = 'database_temp'
)

def Add():
    ID = txt.get()
    eName= txt2.get()
    sal = txt3.get()
    depart = txt4.get()
    dpt_id = 3
    dsg_id = 4
    cur = conn.cursor()
    cur.execute(f"insert into tbl_emp values ({ID},'{eName}',{sal},'{depart}',{dpt_id},{dsg_id})")
    conn.commit()
    txt.delete(0,END)
    txt2.delete(0,END)
    txt3.delete(0, END)
    txt4.delete(0, END)

def Read():
    cur = conn.cursor()
    print('All Record of Emplyees')
    cur.execute('select * from tbl_emp')
    DT = cur.fetchall()
    for i in DT:
        print(i)

def delete():
    ID = txt.get()
    cur = conn.cursor()
    cur.execute(f"delete from tbl_emp where id = {ID}")
    conn.commit()

def update():
    ID = txt.get()
    eName = txt2.get()
    sal = txt3.get()
    depart = txt4.get()
    cur = conn.cursor()
    cur.execute(f"update tbl_emp set emp_name = '{eName}' ,  salary = {sal} , dpt = '{depart}'  where id = {ID}")
    conn.commit()

win = Tk()
win.geometry('800x600')
win.title('CRUD Applicatin GUI Program')

lbl = Label(text='Emplyee ID.? ' , foreground='red',
            background='Yellow',font=('Arial',20),width=20,height=1, anchor='nw')
lbl.place(x=10,y=10)
txt = Entry(font=('Arial',20),foreground='black',background='Yellow')
txt.place(x='350',y='10')

lbl2 = Label(text='Emplyee Name.? ' , foreground='red',
            background='Yellow',font=('Arial',20),width=20,height=1, anchor='nw')
lbl2.place(x=10,y=80)

txt2 = Entry(font=('Arial',20),foreground='black',background='Yellow')
txt2.place(x='350',y='80')

lbl3 = Label(text='Emplyee Salary.? ' , foreground='red',
            background='Yellow',font=('Arial',20),width=20,height=1, anchor='nw')
lbl3.place(x=10,y=150)

txt3 = Entry(font=('Arial',20),foreground='black',background='Yellow')
txt3.place(x='350',y='150')

lbl4 = Label(text='Emplyee Depart.? ' , foreground='red',
            background='Yellow',font=('Arial',20),width=20,height=1, anchor='nw')
lbl4.place(x=10,y=200)

txt4 = Entry(font=('Arial',20),foreground='black',background='Yellow')
txt4.place(x='350',y='200')

btn = Button(text='Create',
       font=('Arial',20),
       foreground='black',
       background='Yellow',
       command = Add
             )
btn.place(x=100,y=300)

btn2 = Button(text='Read',
       font=('Arial',20),
       foreground='black',
       background='Yellow',
       command = Read
             )
btn2.place(x=250,y=300)

btn3 = Button(text='Delete',
       font=('Arial',20),
       foreground='black',
       background='Yellow',
       command = delete
             )
btn3.place(x=400,y=300)

btn4 = Button(text='Update',
       font=('Arial',20),
       foreground='black',
       background='Yellow',
       command = update
             )
btn4.place(x=550,y=300)




win.mainloop()