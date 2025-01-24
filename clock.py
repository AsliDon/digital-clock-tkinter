from tkinter import *
import datetime

def date_time():
    # line to calculate time in time string
    time= datetime.datetime.now()
    # defining the time to the strings
    # %means ki hour min ya seconds
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    # config se wo data us jagah par chla jayega
    # text ki jgh upar hr ki value chad jayegi
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    # every time change
    # change data every second or milisecond(200 milisecond)
    # yahan pe har 200milisecond pe date_time function refresh hoga ya recall hoga
    lab_hr.after(200,date_time)

# line  to run the tkinter continuously
# code ki lines cloack=tk se clock.mainloop tk chlengi
clock = Tk()
# to change the title
clock.title(" Digital Clock ")
# for thee height and width
clock.geometry('1000x500')
#background color
clock.config(bg='black')
# hour wale block ki position dena font height and width of page and all
lab_hr=Label(clock,text='00',font=('Time New Roman',60,"bold"),
             bg='white',fg='black')
lab_hr.place(x=120,y=45,height=110,width=100)

# hour(text) wale block ki position dena font height and width of page and all

lab_hr_txt=Label(clock,text='Hour',font=('Time New Roman',22,"bold"),
             bg='white',fg='black')
lab_hr_txt.place(x=120,y=190,height=40,width=100)


# min wale block ki position dena font height and width of page and all
lab_min=Label(clock,text='00',font=('Time New Roman',60,"bold"),
             bg='white',fg='black')
lab_min.place(x=340,y=45,height=110,width=100)

# min wale(text) block ki position dena font height and width of page and all
lab_min_txt=Label(clock,text='Min',font=('Time New Roman',22,"bold"),
             bg='white',fg='black')
lab_min_txt.place(x=340,y=190,height=40,width=100)


# sec wale block ki position dena font height and width of page and all
lab_sec=Label(clock,text='00',font=('Time New Roman',60,"bold"),
             bg='white',fg='black')
lab_sec.place(x=560,y=45,height=110,width=100)
# sec(text) wale block ki position dena font height and width of page and all
lab_sec_txt=Label(clock,text='Sec',font=('Time New Roman',22,"bold"),
             bg='white',fg='black')
lab_sec_txt.place(x=560,y=190,height=40,width=100)

# am likhe wale block ki position dena font height and width of page and all
lab_am=Label(clock,text='00',font=('Time New Roman',50,"bold"),
             bg='white',fg='black')
lab_am.place(x=780,y=45,height=110,width=100)
# am likhe wale(txt) block ki position dena font height and width of page and all
lab_am_txt=Label(clock,text='AM/PM',font=('Time New Roman',22,"bold"),
             bg='white',fg='black')
lab_am_txt.place(x=780,y=190,height=40,width=100)


date_time()





clock.mainloop()
