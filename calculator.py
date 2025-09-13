from tkinter import * 

def button_click(num):
    pass

def equals():
    pass

def clear():
    pass


window = Tk()

rows = 3
columns = 3 

btnnum = 0


equation_text = StringVar()

label = Label(window, text="equation_text", font=("Verdana", 40))
label.pack()

frame = Frame(window)


for row in range(rows):
    for column in range(columns):
        btnnum +=1 
        button = Button(frame, width=4, height=4, text=f"{btnnum}",
                        command= lambda : button_click(f'{i}'))
        button.grid(row=row, column=column)

btn_add = Button(frame, width=4, height=4, text="+",
                 command= lambda : button_click("+"))

btn_add.grid(row=0, column=3)

btn_multiply = Button(frame, width=4, height=4, text="*",
                 command= lambda : button_click("*"))

btn_multiply.grid(row=1, column=3)

btn_minus = Button(frame, width=4, height=4, text="-",
                 command= lambda : button_click("-"))

btn_minus.grid(row=2, column=3)

btn_divide = Button(frame, width=4, height=4, text="/",
                 command= lambda : button_click("/"))

btn_divide.grid(row=3, column=3)

btn_zero = Button(frame, width=4, height=4, text="0",
                 command= lambda : button_click("0"))

btn_zero.grid(row=3, column=0)

btn_dot = Button(frame, width=4, height=4, text=".",
                 command= lambda : button_click("."))

btn_dot.grid(row=3, column=1)

btn_equal = Button(frame, width=4, height=4, text="=",
                 command=equals)

btn_equal.grid(row=3, column=2)

frame.pack()


window.mainloop()