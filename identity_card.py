#add tkinter basic template
from tkinter import*
root=Tk()
root.title("mitul")
root.geometry("300x400")
root.configure(bg="white")
canvas = Canvas(root, width=300, height=400)
canvas.create_image(0, 0, anchor=NW)
canvas.create_rectangle(0, 0, 300, 55, fill="#1463B0")
canvas.create_rectangle(0, 345, 300, 400, fill="#1463B0")

label_heading = canvas.create_text(150, 90, font=('Times', '24', 'bold italic'), text="Identity Card")
label_name_tag = canvas.create_text(40, 165, font=('Times', '16', 'bold'), text="Name :")
label_grade_tag = canvas.create_text(40, 205, font=('Times', '16', 'bold'), text="Grade :")
label_subjects_tag = canvas.create_text(50, 250, font=('Times', '16', 'bold'), text="Subjects :")

#add label for name
lblname=Label(root)
#add label for grade
lblgrade=Label(root)
#add label for Subjects
lblsub=Label(root)

#add function
def myCardDetails():
    name = "mitul" 
    print(type(name)) 
    grade = 5
    print(type(grade)) 
    subjects = ["computer"] 
    print(type(subjects)) 
    lblname['text'] = name 
    lblgrade['text'] = grade 
    lblsub['text'] = subjects

#add button
button1=Button(root,text="show my id card",command=myCardDetails)
button1.configure(width=20, activebackground="#9EC6EE", relief=FLAT)
button1_window = canvas.create_window(150, 330, anchor=CENTER, window=button1)
label_name_window = canvas.create_window(120, 165, anchor=CENTER, window=lblname)
label_grade_window = canvas.create_window(90, 205, anchor=CENTER, window=lblgrade)
label_subjects_window = canvas.create_window(155, 252, anchor=CENTER, window=lblsub)
canvas.pack()

#tkinter basic template end statement

root.mainloop()