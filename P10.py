from tkinter import *
from tkinter import ttk
import mysql.connector


def sub():
    conn = mysql.connector.connect(user='root', password='root',
                                   host='localhost',
                                   database='pract_10', auth_plugin='mysql_native_password')

    Insert_query = "insert into register values('{0}','{1}','{2}','{3}','{4}');".format(firstname_entry.get(),
                                                                                      lastname_entry.get(),
                                                                                      gender_choice.get(),
                                                                                      grad.get(), Phone_entry.get())
    mycursor = conn.cursor()
    mycursor.execute(Insert_query)
    conn.commit()
    conn.close()


def clear_fun():
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    Phone_entry.delete(0, END)


screen = Tk()
screen.geometry("265x180")
screen.title("REGISTRATION FORM")
heading = Label(text="REGISTRATION FORM", fg="black")
heading.grid(row=1, column=1)

firstname_text = Label(text="First Name", ).grid(row=2, column=0)

firstname_entry = Entry(width="20")
firstname_entry.grid(row=2, column=1)

lastname_text = Label(text="Last Name", ).grid(row=3, column=0)

lastname_entry = Entry(width="20")
lastname_entry.grid(row=3, column=1)

gender = Label(text="Gender: ").grid(row=4, column=0)
gender_choice = StringVar()
male = Radiobutton(text='Male', variable=gender_choice, value='Male')
male.grid(row=4, column=1)
female = Radiobutton(text='Female', variable=gender_choice, value='Female')
female.grid(row=4, column=2)


graduation = Label(text="Graduation").grid(row=5, column=0)
grad = StringVar()
graduate = ttk.Combobox(width='17', textvariable=grad)
graduate['values'] = ('BCA', 'BA', 'BBA', 'BSc')
graduate.grid(row=5, column=1)
graduate.current(0)

Phone_text = Label(text="Phone No", ).grid(row=6, column=0)
Phone_entry = Entry(width="20")
Phone_entry.grid(row=6, column=1)

submit = Button(text="Submit", width="5", height="1", command=sub)
submit.grid(row=7, column=1)
clear = Button(text="Clear", width="5", height="1", command=clear_fun)
clear.grid(row=8, column=1)

screen.mainloop()
