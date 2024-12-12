from tkinter import *
import sqlite3


root = Tk()
root.title("Hotel Reservation ")
root.geometry('800x800')
root.configure(bg="#F5F5F5")

conn = sqlite3.connect('G:/pms/ffbackend.db')


root.configure(bg="#2e4053")

title_label = Label(root, text="Hotel Reservation", font=("Arial", 20, "bold"), bg="#2e4053", fg="white")
title_label.grid(row=0, column=1, columnspan=10, pady=20)

c = conn.cursor()

def submit():
    conn = sqlite3.connect('G:/pms/ffbackend.db')
    c = conn.cursor()
    c.execute("""INSERT INTO hotel_reser (f_name, l_name, age, gender, address, email, r_num, r_days, payment)
                 VALUES (:f_name, :l_name, :age, :gender, :address, :email, :r_num, :r_days, :payment)""",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'age': age.get(),
                  'gender': gender.get(),
                  'address': address.get(),
                  'email': email.get(),
                  'r_num': r_num.get(),
                  'r_days': r_days.get(),
                  'payment': payment.get()
              })

    conn.commit()
    conn.close()

    
    f_name.delete(0, END)
    l_name.delete(0, END)
    age.delete(0, END)
    gender.delete(0, END)
    address.delete(0, END)
    email.delete(0, END)
    r_num.delete(0, END)
    r_days.delete(0, END)
    payment.delete(0, END)

def query():
    conn = sqlite3.connect('G:/pms/ffbackend.db')
    c = conn.cursor()

    c.execute("SELECT *, oid FROM hotel_reser")
    records = c.fetchall()

    
    
    records_window = Toplevel(root)
    records_window.title("Guest Records")
    records_window.geometry("500x800")
    records_window.configure(bg="#333333")
    

    display_text = ""
    for record in records:
        display_text += f"Guest ID: {record[9]} \n                First Name: {record[0]} \n                Last Name: {record[1]} \n                Age: {record[2]} \n                Gender: {record[3]} \n                Address: {record[4]} \n                Email: {record[5]} \n                Room: {record[6]} \n                Days: {record[7]} \n                Payment: ₱{record[8]}.00\n"

    query_label = Label(records_window, text=display_text, anchor="w", justify=LEFT, bg="#333333", fg="white", font=("Arial", 12))
    query_label.pack(padx=10, pady=10)

    conn.commit()
    conn.close()

def delete():
    conn=sqlite3.connect('G:/pms/ffbackend.db')

    c=conn.cursor()
    c.execute("DELETE from hotel_reser WHERE oid=" + delete_box.get())

    delete_box.delete(0,END)
    conn.commit()
    conn.close()


def update():
    conn=sqlite3.connect('G:/pms/ffbackend.db')

    c=conn.cursor()

    record_id=delete_box.get()
    
    c.execute(""" UPDATE hotel_reser SET
        f_name=:first_name,
        l_name=:last_name,
        age=:age,
        gender=:gender,
        address=:address,
        email=:email,
        r_num=:room_number,
        r_days=:reservation_days,
        payment=:payment


        WHERE oid=:oid""",
        {
            'first_name':f_name_editor.get(),
            'last_name':l_name_editor.get(),
            'age':age_editor.get(),
            'gender':gender_editor.get(),
            'address':address_editor.get(),
            'email':email_editor.get(),
            'room_number':r_num_editor.get(),
            'reservation_days':r_days_editor.get(),
            'payment':payment_editor.get(),
            'oid':record_id
        
        })
    
    conn.commit()
    conn.close()

def edit():
    editor=Tk()
    editor.title('Update Record')
    editor.geometry("400x400")
    editor.configure(bg="#333333")
    conn=sqlite3.connect('G:/pms/ffbackend.db')
   
    c=conn.cursor()

    record_id=delete_box.get()
    c.execute("SELECT* FROM hotel_reser WHERE oid="+record_id)
    records=c.fetchall()

    global f_name_editor
    global l_name_editor
    global age_editor
    global gender_editor
    global address_editor
    global email_editor
    global r_num_editor
    global r_days_editor
    global payment_editor
    
    

    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1,padx=20)
    age_editor=Entry(editor,width=30)
    age_editor.grid(row=2,column=1,padx=20)
    gender_editor=Entry(editor,width=30)
    gender_editor.grid(row=3,column=1,padx=20)
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=4,column=1,padx=20)
    email_editor=Entry(editor,width=30)
    email_editor.grid(row=5,column=1,padx=20)
    r_num_editor=Entry(editor,width=30)
    r_num_editor.grid(row=6,column=1,padx=20)
    r_days_editor=Entry(editor,width=30)
    r_days_editor.grid(row=7,column=1,padx=20)
    payment_editor=Entry(editor,width=30)
    payment_editor.grid(row=8,column=1,padx=20)
    
    f_name_label=Label(editor,text="First Name", bg="#333333", fg="white")
    f_name_label.grid(row=0,column=0,pady=(10,0))
    l_name_label=Label(editor,text="Last Name", bg="#333333", fg="white")
    l_name_label.grid(row=1,column=0)
    age_label=Label(editor,text="Age", bg="#333333", fg="white")
    age_label.grid(row=2,column=0)
    gender_label=Label(editor,text="Gender", bg="#333333", fg="white")
    gender_label.grid(row=3,column=0)
    address_label=Label(editor,text="Address", bg="#333333", fg="white")
    address_label.grid(row=4,column=0)
    email_label=Label(editor,text="Email", bg="#333333", fg="white")
    email_label.grid(row=5,column=0)
    r_num_label=Label(editor,text="Room Number", bg="#333333", fg="white")
    r_num_label.grid(row=6,column=0)
    r_days_label=Label(editor,text="Reservation Days", bg="#333333", fg="white")
    r_days_label.grid(row=7,column=0)
    payment_label=Label(editor,text="Payment", bg="#333333", fg="white")
    payment_label.grid(row=8,column=0)


    
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        age_editor.insert(0,record[2])
        gender_editor.insert(0,record[3])
        address_editor.insert(0,record[4])
        email_editor.insert(0,record[5])
        r_num_editor.insert(0,record[6])
        r_days_editor.insert(0,record[7])
        payment_editor.insert(0,record[8])
        

   
    save_btn=Button(editor,text="Save Record",command=update)
    save_btn.grid(row=10, column=0,columnspan=2,pady=10,padx=10,ipadx=140) 

   

    conn.commit()
    conn.close()       

'''

c.execute("""CREATE TABLE "hotel_reser" (
	"f_name"	TEXT,
	"l_name"	TEXT,
	"age"	INTEGER,
	"gender"	TEXT,
	"address"	TEXT,
	"email"	TEXT,
	"r_num"	INTEGER,
	"r_days"	INTEGER,
	"payment"	INTEGER

)""";

'''


f_name = Entry(root, width=30)
f_name.grid(row=1, column=1, padx=20)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=3, padx=20)
age = Entry(root, width=30)
age.grid(row=2, column=1, padx=20)
gender = Entry(root, width=30)
gender.grid(row=2, column=3, padx=20)
address = Entry(root, width=30)
address.grid(row=4, column=1, padx=20)
email = Entry(root, width=30)
email.grid(row=4, column=3, padx=20)
r_num = Entry(root, width=30)
r_num.grid(row=6, column=1, padx=20)
r_days = Entry(root, width=30)
r_days.grid(row=6, column=3, padx=20)
payment = Entry(root, width=30)
payment.grid(row=10, column=3, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=20, column=2, padx=20)




f_label = Label(root, text="First Name", bg="#2e4053", fg="white")
f_label.grid(row=1, column=0)
l_name_label = Label(root, text="Last Name", bg="#2e4053", fg="white")
l_name_label.grid(row=1, column=2)
age_label = Label(root, text="Age", bg="#2e4053", fg="white")
age_label.grid(row=2, column=0)
gender_label = Label(root, text="Gender", bg="#2e4053", fg="white")
gender_label.grid(row=2, column=2)
address_label = Label(root, text="Address", bg="#2e4053", fg="white")
address_label.grid(row=4, column=0)
email_label = Label(root, text="Email", bg="#2e4053", fg="white")
email_label.grid(row=4, column=2)
r_label = Label(root, text="Room Number", bg="#2e4053", fg="white")
r_label.grid(row=6, column=0)
r_days_label = Label(root, text="Reservation Days", bg="#2e4053", fg="white")
r_days_label.grid(row=6, column=2)
payment_label = Label(root, text="Payment", bg="#2e4053", fg="white")
payment_label.grid(row=10, column=2)




delete_box_label = Label(root, text="Select Item No.", bg="#2e4053", fg="white")
delete_box_label.grid(row=19, column=2, pady=10)


submit_btn = Button(root, text="Add Record", command=submit, bg="#d3d3d3", fg="black")
submit_btn.grid(row=14, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

query_btn = Button(root, text="Show Records", command=query, bg="#d3d3d3", fg="black")
query_btn.grid(row=14, column=2, columnspan=3, pady=10, padx=10, ipadx=70)


edit_btn = Button(root, text="Edit Record", command= edit, bg="#d3d3d3", fg="black")
edit_btn.grid(row=16, column=1, columnspan=2, pady=10, padx=10, ipadx=70)

delete_btn = Button(root, text="Delete Record", command=delete, bg="#d3d3d3", fg="black")
delete_btn.grid(row=16, column=2, columnspan=3,
pady=10, padx=10, ipadx=70)


root.mainloop()
