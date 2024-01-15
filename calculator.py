import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("300x275")

text_result = Text(root, height=2, width=17, font=("Arial", 24))
text_result.grid(columnspan=5)

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


btn1 = Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("arial", 14))
btn1.grid(row=2, column=1)
btn2 = Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("arial", 14))
btn2.grid(row=2, column=2)
btn3 = Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("arial", 14))
btn3.grid(row=2, column=3)
btn4 = Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("arial", 14))
btn4.grid(row=3, column=1)
btn5 = Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("arial", 14))
btn5.grid(row=3, column=2)
btn6 = Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("arial", 14))
btn6.grid(row=3, column=3)
btn7 = Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("arial", 14))
btn7.grid(row=4, column=1)
btn8 = Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("arial", 14))
btn8.grid(row=4, column=2)
btn9 = Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("arial", 14))
btn9.grid(row=4, column=3)
btn0 = Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("arial", 14))
btn0.grid(row=5, column=2)

btn_minus = Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("arial", 14))
btn_minus.grid(row=2, column=4)
btn_plus = Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("arial", 14))
btn_plus.grid(row=3, column=4)
btn_mul = Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("arial", 14))
btn_mul.grid(row=4, column=4)
btn_div = Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("arial", 14))
btn_div.grid(row=5, column=4)

btn_right_para = Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("arial", 14))
btn_right_para.grid(row=5, column=1)
btn_left_para = Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("arial", 14))
btn_left_para.grid(row=5, column=3)

btn_equals = Button(root, text="=", command=evaluate_calculation, width=12, font=("arial", 14))
btn_equals.grid(row=6, column=1, columnspan=2)
btn_clear = Button(root, text="C", command=clear_field, width=12, font=("arial", 14))
btn_clear.grid(row=6, column=3, columnspan=2)


root.mainloop()


