from tkinter import * 

def button_click(num):
    equation_text.set(equation_text.get() + str(num))
    window.update()

def equals():

    try:
        sum = str(equation_text.get())
        equation_text.set(eval(sum))
        window.update()
    except ZeroDivisionError:
        equation_text.set("Zero Div Err")
    except SyntaxError:
        equation_text.set("Invalid Syntax")

def clear():
    equation_text.set("")
    window.update()

def backspace():
    text = str(equation_text.get())
    equation_text.set(text[:-1])
    window.update()


window = Tk()

rows = 3
columns = 3 

btnnum = 0


equation_text = StringVar()

label = Label(window, textvariable=equation_text, font=("Verdana", 40),
              width=12, height=2)
label.pack()

frame = Frame(window)


for row in range(rows):
    for column in range(columns):
        btnnum +=1
        button = Button(frame, width=4, height=4, text=f"{btnnum}",
                            command= lambda num=btnnum: button_click(num))
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

btn_clear = Button(frame, width=4, height=4, text="C",
                 command=clear)

btn_clear.grid(row=0, column=4)

btn_backspace = Button(frame, width=4, height=4, text="⌫",
                 command=backspace)

btn_backspace.grid(row=1, column=4)



frame.pack()

window.title("Calculator")

window.config(background="grey")


window.mainloop()