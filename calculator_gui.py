from tkinter import *
from calculator_operations import *

root = Tk()
root.title("Scientific Calculator")

custom_font = ("Times New Roman", 14)

e = Entry(root, width=45, bd=8, font=('arial', 24, 'bold'), justify='right')
e.grid(row=0, column=0, columnspan=5)

def button_click(text):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(text))

def button_clear():
    e.delete(0, END)

def button_bksps():
    current = e.get()
    length = len(current) - 1
    e.delete(length, END)

def button_equal():
    ans = e.get()
    result = evaluate_expression(ans)
    e.delete(0, END)
    e.insert(0, result)

def sin():
    no = e.get()
    result = calculate_sin(no)
    e.delete(0, END)
    e.insert(0, result)

def cos():
    no = e.get()
    result = calculate_cos(no)
    e.delete(0, END)
    e.insert(0, result)

def tan():
    no = e.get()
    result = calculate_tan(no)
    e.delete(0, END)
    e.insert(0, result)

def lg():
    no = e.get()
    result = calculate_lg(no)
    e.delete(0, END)
    e.insert(0, result)

def ln():
    no = e.get()
    result = calculate_ln(no)
    e.delete(0, END)
    e.insert(0, result)

def sqrt():
    no = e.get()
    result = calculate_sqrt(no)
    e.delete(0, END)
    e.insert(0, result)

def x_factorial():
    no = e.get()
    result = calculate_factorial(no)
    e.delete(0, END)
    e.insert(0, result)

def reciprocal():
    no = e.get()
    result = calculate_reciprocal(no)
    e.delete(0, END)
    e.insert(0, result)

def pi():
    no = e.get()
    result = calculate_pi(no)
    e.delete(0, END)
    e.insert(0, result)

def euler():
    no = e.get()
    result = calculate_euler(no)
    e.delete(0, END)
    e.insert(0, result)

def division():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "÷")

def multiplication():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "×")

def addition():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "+")

def subtraction():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "-")

def open_parenthesis():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "(")

def close_parenthesis():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + ")")

def degree():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "°")

def modulus():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "%")

def exponentiation():
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + "^")
        
button_1 = Button(root, text='1', width=10, height=1, command=lambda: button_click(1), font=custom_font)
button_1.grid(row=6, column=1, padx=1, pady=1, sticky='ew')

button_2 = Button(root, text='2', width=10, height=1, command=lambda: button_click(2), font=custom_font)
button_2.grid(row=6, column=2, padx=1, pady=1, sticky='ew')

button_3 = Button(root, text='3', width=10, height=1, command=lambda: button_click(3), font=custom_font)
button_3.grid(row=6, column=3, padx=1, pady=1, sticky='ew')

button_4 = Button(root, text='4', width=10, height=1, command=lambda: button_click(4), font=custom_font)
button_4.grid(row=5, column=1, padx=1, pady=1, sticky='ew')

button_5 = Button(root, text='5', width=10, height=1, command=lambda: button_click(5), font=custom_font)
button_5.grid(row=5, column=2, padx=1, pady=1, sticky='ew')

button_6 = Button(root, text='6', width=10, height=1, command=lambda: button_click(6), font=custom_font)
button_6.grid(row=5, column=3, padx=1, pady=1, sticky='ew')

button_7 = Button(root, text='7', width=10, height=1, command=lambda: button_click(7), font=custom_font)
button_7.grid(row=4, column=1, padx=1, pady=1, sticky='ew')

button_8 = Button(root, text='8', width=10, height=1, command=lambda: button_click(8), font=custom_font)
button_8.grid(row=4, column=2, padx=1, pady=1, sticky='ew')

button_9 = Button(root, text='9', width=10, height=1, command=lambda: button_click(9), font=custom_font)
button_9.grid(row=4, column=3, padx=1, pady=1, sticky='ew')

button_0 = Button(root, text='0', width=10, height=1, command=lambda: button_click(0), font=custom_font)
button_0.grid(row=7, column=2, padx=1, pady=1, sticky='ew')

button_dot = Button(root, text='.', width=10, height=1, command=lambda: button_click('.'), font=custom_font)
button_dot.grid(row=7, column=1, padx=1, pady=1, sticky='ew')

button_equal = Button(root, text='=', width=10, height=1, command=button_equal, font=custom_font)
button_equal.grid(row=7, column=3, padx=1, pady=1, sticky='ew')

button_clear = Button(root, text='C', width=10, height=1, command=button_clear, font=custom_font)
button_clear.grid(row=1, column=4, padx=1, pady=1, sticky='ew')

button_bksps = Button(root, text='⌫', width=10, height=1, command=button_bksps, font=custom_font)
button_bksps.grid(row=2, column=4, padx=1, pady=1, sticky='ew')

button_sin = Button(root, text='sin', width=10, height=1, command=sin, font=custom_font)
button_sin.grid(row=2, column=1, padx=1, pady=1, sticky='ew')

button_cos = Button(root, text='cos', width=10, height=1, command=cos, font=custom_font)
button_cos.grid(row=2, column=2, padx=1, pady=1, sticky='ew')

button_tan = Button(root, text='tan', width=10, height=1, command=tan, font=custom_font)
button_tan.grid(row=2, column=3, padx=1, pady=1, sticky='ew')

button_lg = Button(root, text='lg', width=10, height=1, command=lg, font=custom_font)
button_lg.grid(row=1, column=0, padx=1, pady=1, sticky='ew')

button_ln = Button(root, text='ln', width=10, height=1, command=ln, font=custom_font)
button_ln.grid(row=1, column=1, padx=1, pady=1, sticky='ew')

button_sqrt = Button(root, text='√', width=10, height=1, command=sqrt, font=custom_font)
button_sqrt.grid(row=3, column=0, padx=1, pady=1, sticky='ew')

button_x_factorial = Button(root, text='x!', width=10, height=1, command=x_factorial, font=custom_font)
button_x_factorial.grid(row=4, column=0, padx=1, pady=1, sticky='ew')

button_reciprocal = Button(root, text='1/x', width=10, height=1, command=reciprocal, font=custom_font)
button_reciprocal.grid(row=5, column=0, padx=1, pady=1, sticky='ew')

button_pi = Button(root, text='π', width=10, height=1, command=pi, font=custom_font)
button_pi.grid(row=6, column=0, padx=1, pady=1, sticky='ew')

button_euler = Button(root, text='e', width=10, height=1, command=euler, font=custom_font)
button_euler.grid(row=3, column=1, padx=1, pady=1, sticky='ew')

button_division = Button(root, text='÷', width=10, height=1, command=division, font=custom_font)
button_division.grid(row=3, column=4, padx=1, pady=1, sticky='ew')

button_multiplication = Button(root, text='×', width=10, height=1, command=multiplication, font=custom_font)
button_multiplication.grid(row=4, column=4, padx=1, pady=1, sticky='ew')

button_addition = Button(root, text='+', width=10, height=1, command=addition, font=custom_font)
button_addition.grid(row=5, column=4, padx=1, pady=1, sticky='ew')

button_subtraction = Button(root, text='-', width=10, height=1, command=subtraction, font=custom_font)
button_subtraction.grid(row=6, column=4, padx=1, pady=1, sticky='ew')

button_open_parenthesis = Button(root, text='(', width=10, height=1, command=open_parenthesis, font=custom_font)
button_open_parenthesis.grid(row=1, column=2, padx=1, pady=1, sticky='ew')

button_close_parenthesis = Button(root, text=')', width=10, height=1, command=close_parenthesis, font=custom_font)
button_close_parenthesis.grid(row=1, column=3, padx=1, pady=1, sticky='ew')

button_degree = Button(root, text='°', width=10, height=1, command=degree, font=custom_font)
button_degree.grid(row=3, column=2, padx=1, pady=1, sticky='ew')

button_modulus = Button(root, text='%', width=10, height=1, command=modulus, font=custom_font)
button_modulus.grid(row=3, column=3, padx=1, pady=1, sticky='ew')

button_exponentiation = Button(root, text='^', width=10, height=1, command=exponentiation, font=custom_font)
button_exponentiation.grid(row=2, column=0, padx=1, pady=1, sticky='ew')

root.mainloop()
