from tkinter import *

root = Tk()
root.title("Calculator App")
root.geometry("300x400")

# Variable to store input
data = StringVar()

# Function for button click
def btn_click(value):
    current_text = data.get()
    data.set(current_text + str(value))

# Function to evaluate expression
def calculate():
    try:
        result = eval(data.get())
        data.set(result)
    except:
        data.set("Error")

# Function to clear input field
def clear():
    data.set("")

# Input field frame
input_frame = Frame(root, width=300, height=50, highlightbackground="black", highlightthickness=1)
input_frame.pack(side=TOP, fill="x")

input_field = Entry(input_frame, textvariable=data, width=22, font=('times', 20, 'bold'), justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()

# Button frame
btn_frame = Frame(root)
btn_frame.pack()

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        if btn_text == "=":
            action = lambda: calculate()
        elif btn_text == "C":
            action = lambda: clear()
        else:
            action = lambda btn_text=btn_text: btn_click(btn_text)
        
        Button(btn_frame, text=btn_text, font=('times', 15, 'bold'), width=6, height=2, command=action).grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
