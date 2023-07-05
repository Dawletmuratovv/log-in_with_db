from tkinter import *
import sqlite3

with sqlite3.connect('users.db') as db:
    cursor= db.cursor()
cursor.execute(
    '''
        Create table if not exists users(
            login text not null,
            password text not null
        )
    '''
)    
db.commit()
def add():
    Login = log_ent.get()
    Password = pas_ent.get() 
    cursor.execute(
        '''
            insert into users(login, password)
            values(?,?)
        ''',(Login, Password)
    )
    db.commit()
    log_ent.delete(0,END)
    pas_ent.delete(0,END)

def delete():
    log_ent.delete(0,END)
    pas_ent.delete(0,END)
    
login = Tk()
login.title('Authorization')
login.geometry('300x200')

log_lbl = Label(login, text= 'Login', font=('Roboto Bold', 14))
log_lbl.place(x=0, y=15)
log_ent = Entry()
log_ent.place(x=60, y=20)

pas_lbl = Label(login, text= 'Password', font=('Roboto Bold', 14))
pas_lbl.place(x=0, y=45)
pas_ent = Entry()
pas_ent.place(x=100, y=50)

save_btn = Button(text="Save", font=('Roboto Bold', 10,), command= add)
save_btn.place(x=100, y=75)
del_btn = Button(text="Delete", font=('Roboto Bold', 10,), command= delete)
del_btn.place(x=200, y=75)
    

login.mainloop()