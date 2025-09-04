import tkinter as tkinter

root=tkinter()
root.title("Grade calculator")
root.geometry("500x500")

label = tkinter.Label(root, text="Enter your marks:")
label.pack()

entry = tkinter.Entry(root)
entry.pack()

def calculate_grade():
    marks = int(entry.get())
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "D"
    result_label.config(text=f"Your grade is: {grade}")

button = tkinter.Button(root, text="Calculate Grade", command=calculate_grade)
button.pack()

result_label = tkinter.Label(root, text="")
result_label.pack()

root.mainloop()
