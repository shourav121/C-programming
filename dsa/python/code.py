from os import strerror
from string import printable


def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata3 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id {} Name {} Adeed sucessfully..and want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications','Id Already exists try another id...',parent=addroot)
        strr ='select * from studentdata3'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenmttable.insert('',END,values=vv)



    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('480x590+12+120')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.iconbitmap('iconfinder-499-student-education-graduate-learning-4212915_114945.ico')
    addroot.resizable(False,False)
    #----------------------------------------------------------- Add student Labels
    idlabel = Label(addroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter E-mail -:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text='Enter D.O.B :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
     
    ##---------------------------------------------------- Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()


    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    ###################------------------------------------------ add button
    submitbtn = Button(addroot,text='submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='green2',activeforeground='white',bg='red',command=submitadd) 
    submitbtn.place(x=138,y=456)
   
    addroot.mainloop()
def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id != ''):
            strr = 'select *from studentdata3 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (name != ''):
            strr = 'select *from studentdata3 where name=%s'
            mycursor.execute(strr, (name))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (mobile != ''):
            strr = 'select *from studentdata3 where mobile=%s'
            mycursor.execute(strr, (mobile))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (email != ''):
            strr = 'select *from studentdata3 where email=%s'
            mycursor.execute(strr, (email))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (address != ''):
            strr = 'select *from studentdata3 where address=%s'
            mycursor.execute(strr, (address))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (gender != ''):
            strr = 'select *from studentdata3 where gender=%s'
            mycursor.execute(strr, (gender))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (dob != ''):
            strr = 'select *from studentdata3 where dob=%s'
            mycursor.execute(strr, (dob))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif (addeddate != ''):
            strr = 'select *from studentdata3 where addeddate=%s'
            mycursor.execute(strr, (addeddate))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('480x590+12+120')
    searchroot.title('Student Management System')
    searchroot.config(bg='blue')
    searchroot.iconbitmap('iconfinder-499-student-education-graduate-learning-4212915_114945.ico')
    searchroot.resizable(False,False)
    #----------------------------------------------------------- Add student Labels
    idlabel = Label(searchroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text='Enter E-mail -:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(searchroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(searchroot,text='Enter D.O.B :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(searchroot,text='Enter Date :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
     
    ##---------------------------------------------------- Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()


    identry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    ###################------------------------------------------ add button
    submitbtn = Button(searchroot,text='submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='green2',activeforeground='white',bg='red',command=search) 
    submitbtn.place(x=150,y=510)

    searchroot.mainloop()
def deletestudent():
    cc = studenmttable.focus()
    content = studenmttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata3 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted successfully...'.format(pp))
    strr = 'select *from studentdata3'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)


def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata3 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified successfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata3'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenmttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('480x590+12+120')
    updateroot.title('Student Management System')
    updateroot.config(bg='blue')
    updateroot.iconbitmap('iconfinder-499-student-education-graduate-learning-4212915_114945.ico')
    updateroot.resizable(False,False)
    #----------------------------------------------------------- Add student Labels
    idlabel = Label(updateroot,text='Enter Id :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter Name :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text='Enter Mobile :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text='Enter E-mail -:',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(updateroot,text='Enter Address :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text='Enter Gender :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(updateroot,text='Enter D.O.B :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text='Enter Date :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel = Label(updateroot, text='Enter Time :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=480)
     
    ##---------------------------------------------------- Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()


    identry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry = Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=482)


    ###################------------------------------------------ add button
    submitbtn = Button(updateroot,text='submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='green',activeforeground='white',
                       bg='red',command=update)
    submitbtn.place(x=150,y=540)
    cc = studenmttable.focus()
    content = studenmttable.item(cc)
    pp = content['values']
    if(len(pp) !=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()

def showstudent():
    strr = 'select *from studentdata3'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)


def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenmttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenmttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
        dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
        df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
        paths = r'{}.csv'.format(ff)
        df.to_csv(paths,index=False)
        messagebox.showinfo('Notification', 'Student data is saved {}'.format(paths))

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
         root.destroy()   
                  
#######    CONNECTION OF DATABASE #########  CONNECTION OF DATABASE  ###########   CONNECTION OF DATABASE    ###########   CONNECTION OF DATABASE  #######  CONNECTION OF DATABASE ##########
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect Please try again')
            return
        try:
             strr = 'create database studentmanagementsystem3'
             mycursor.execute(strr)
             strr = 'use studentmanagementsystem3'
             mycursor.execute(strr)
             strr = 'create table studentdata3(id int,name varchar(20),mobile varchar(12),email varchar(50),address varchar(50),gender varchar(50),dob varchar(50),time varchar(40),date varchar(50))'
             mycursor.execute(strr)
             strr = 'alter table studentdata3 modify column id int not null'
             mycursor.execute(strr)
             strr = 'alter table studentdata3 modify column id int primary key'
             mycursor.execute(strr)
             messagebox.showinfo('Notification', 'database created and now yoy are connected Connected To The Database...', parent=dbroot)


        except:
            strr = 'use studentmanagementsystem3'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now You Are Connected To The Database...',parent=dbroot)
        dbroot.destroy()


    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('620x300+300+230') 
    dbroot.iconbitmap('iconfinder-499-student-education-graduate-learning-4212915_114945.ico') 
    dbroot.resizable(False,False)
    dbroot.config(bg='#1856D9')
    #----------------------------------------- connectdb Labels
    hostlabel = Label(dbroot,text="Enter Host : ",bg='cyan',font=('times',26,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='cyan',font=('times',26,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='cyan',font=('times',26,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #-----------------------------------------------connectdb entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',20,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=330,y=15)

    userentry = Entry(dbroot,font=('roman',20,'bold'),bd=5,textvariable=userval)
    userentry.place(x=330,y=77)

    passwordentry = Entry(dbroot,font=('roman',20,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=330,y=135)
    #------------------------------------------------------------------------Connectdb button

    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='green2',
                          activeforeground='white',command=submitdb)
    
    submitbutton.place(x=205,y=210)


    dbroot.mainloop()
################################################################################################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)
  #######    INTRO SLIDER #########   INTRO SLIDER  ###########   INTRO SLIDER     ###########   INTRO SLIDER  #######  INTRO SLIDER ###########   INTRO SLIDER  #######   INTRO SLIDER
import random
colors = ['red','grey','orange','purple','green','black','blue','brown',]
def IntroLabelColortick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(275,IntroLabelColortick)
def IntroLabelTick():
  global count,text
  if (count>len(ss)):
    count = 0
    text = ''
    SliderLabel.config(text=text)
  else:
    text = text+ss[count]
    SliderLabel.config(text=text)
    count += 1  
    SliderLabel.after(280,IntroLabelTick)
################################################################################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
root = Tk()
root.title("Student Management System")
root.config(bg='skyblue')
root.geometry('1374x725+0+0')
root.iconbitmap('iconfinder-499-student-education-graduate-learning-4212915_114945.ico')
root.resizable(True,False)
##################    FRAMES #########   FRAMES  ###########  FRAMES     ###########  FRAMES  #######   FRAMES ###########  FRAMES  #######   FRAMES
##-------------------------------------------------------------------------------- dataentry frame


DataEntryFrame =Frame(root,bg='skyblue',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=630)
frontlabel = Label(DataEntryFrame,text='---------------Welcome--------------',width=30,font=('arial',22,'italic bold'),bg='skyblue')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add student',width=25,font=('times',20,'bold'),bd=6,bg='#6BA6CF',activebackground='#5FC44A',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search student',width=25,font=('times',20,'bold'),bd=6,bg='#6BA6CF',activebackground='#5FC44A',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete student',width=25,font=('times',20,'bold'),bd=6,bg='#6BA6CF',activebackground='#5FC44A',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)


updatebtn = Button(DataEntryFrame,text='4. Update student',width=25,font=('times',20,'bold'),bd=6,bg='#6BA6CF',activebackground='#5FC44A',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('times',20,'bold'),bd=6,bg='#6BA6CF',activebackground='#5FC44A',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export Data',width=25,font=('times',20,'bold'),bd=6,bg='#6BA6CF',activebackground='#5FC44A',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)


exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('times',20,'bold'),bd=6,bg='#6BA6CF',activebackground='#5FC44A',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


##--------------------------------------------------------------------------------show data frame
ShowDataFrame =Frame(root,bg='skyblue',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=795,height=630)

#-----------------showdataframe------------------showdataframe-------------------showdataframe---------------
style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',forground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenmttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date','Added Time'),
                         yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenmttable.xview)
scroll_y.config(command=studenmttable.yview)
studenmttable.heading('Id',text='Id')
studenmttable.heading('Name',text='Name')
studenmttable.heading('Mobile No',text='Mobile No')
studenmttable.heading('Email',text='Email')
studenmttable.heading('Address',text='Address')
studenmttable.heading('Gender',text='Gender')
studenmttable.heading('D.O.B',text='D.O.B')
studenmttable.heading('Added Date',text='Added Date')
studenmttable.heading('Added Time',text='Added Time')

studenmttable['show'] ='headings'

studenmttable.column('Id',width=100)
studenmttable.column('Name',width=200)
studenmttable.column('Mobile No',width=200)
studenmttable.column('Email',width=300)
studenmttable.column('Address',width=400)
studenmttable.column('D.O.B',width=150)
studenmttable.column('Added Date',width=150)
studenmttable.column('Added Time',width=150)

studenmttable.pack(fill=BOTH,expand=1)


##################    SLIDER #########   SLIDER  ###########   SLIDER     ###########   SLIDER  #######    SLIDER #######   SLIDER  #######    SLIDER
ss ='Welcome To Student Management System'
count = 0
text = ''
#######################################################################################################################################################
SliderLabel = Label(root,text=ss,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=5,width=35,bg='cyan')
SliderLabel.place(x=382,y=0)
IntroLabelTick()
IntroLabelColortick()

##################    CLOCK  #########   CLOCK   ###########   CLOCK      ###########    CLOCK  #######     CLOCK #######    CLOCK  #######     CLOCK 
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=5,bg='cyan')
clock.place(x=0,y=0)
tick()
####### CONNECT DATABASE BUTTON #########   CONNECT DATABASE BUTTON  ###########   CONNECT DATABASE BUTTON   ##############   CONNECT DATABASE BUTTON
connectbutton = Button(root,text='Connect To Database',width=23,font=('chiller',20,'italic bold'),relief=RIDGE,borderwidth=5,bg='red2',
                       activebackground='green2',activeforeground='white',command=Connectdb)
connectbutton.place(x=1076,y=0)
root.mainloop()
