from tkinter import *
root = Tk()
root.title("Check for Cardiovascular symptoms")
root.geometry("500x500")
from tkinter import messagebox


q1_rb = StringVar(value = "0")
q1 = Label(root, text = "Do you experience shortness of breath during routine activities?")
q1.place(relx = 0.5, rely = 0.1, anchor = CENTER)
q1_r1 = Radiobutton(root, text="yes", variable = q1_rb, value = "yes")
q1_r1.place(relx = 0.5, rely = 0.15, anchor = CENTER)
q1_r2 = Radiobutton(root, text="no", variable = q1_rb, value = "no")
q1_r2.place(relx = 0.5, rely = 0.2, anchor = CENTER)

q2_rb = StringVar(value = "0")
q2 = Label(root, text = "Do you feel any of these symptoms - confusion, disorientation or loss of memory")
q2.place(relx = 0.5, rely = 0.3, anchor = CENTER)
q2_r1 = Radiobutton(root, text="yes", variable = q2_rb, value = "yes")
q2_r1.place(relx = 0.5, rely = 0.35, anchor = CENTER)
q2_r2 = Radiobutton(root, text="no", variable = q2_rb, value = "no")
q2_r2.place(relx = 0.5, rely = 0.4, anchor = CENTER)

q3_rb = StringVar(value = "0")
q3 = Label(root, text = "Do you experience persistent wheezing/coughing that produces white or pink blood tinged mucus?", wraplength = 500)
q3.place(relx = 0.5, rely = 0.5, anchor = CENTER)
q3_r1 = Radiobutton(root, text="yes", variable = q3_rb, value = "yes")
q3_r1.place(relx = 0.5, rely = 0.55, anchor = CENTER)
q3_r2 = Radiobutton(root, text="no", variable = q3_rb, value = "no")
q3_r2.place(relx = 0.5, rely = 0.6, anchor = CENTER)

def check():
    score = 0
    if q1_rb.get() == "yes" :
        score = score + 1
        
    if q2_rb.get() == "yes" :
        score = score + 1
        
    if q3_rb.get() == "yes" :
        score = score + 1
        
    if score <= 1 :
        messagebox.showinfo("Result", "There is no need to visit a doctor")
    elif score >1 and score <= 2 :
        messagebox.showinfo("Result", "You might have to visit a doctor")
    elif score == 3 :
        messagebox.showinfo("Result", "You need to visit a doctor as soon as possible")
        
        
        
result = Button(root, text = "Check for Result", command = check)
result.place(relx = 0.5, rely = 0.7, anchor = CENTER)


root.mainloop()

