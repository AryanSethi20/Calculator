from tkinter import *
import parser

root = Tk()
root.title('Calculator')

def factorial():
    string1 = entry.get()
    num = int(string1)
    fact = num
    try:    
        for j in range(2, num):
            fact *= j
        clear()
        entry.insert(0, fact)
    except Exception:
        clear()
        entry.insert(0, "ERROR")

def calculate():
    original_expression = entry.get()
    try:
        exp = parser.expr(original_expression).compile()
        result = eval(exp)
        clear()
        entry.insert(0, result)
    except Exception:
        clear()
        entry.insert(0, "ERROR")

i=0
def numbers(num):
    if(entry.get()=="ERROR"):
        clear()
    global i
    entry.insert(i, num)
    i+=1

def operator(op):
    global i
    length = len(op)
    entry.insert(i,op)
    i+=length

def clear():
    entry.delete(0, END)

def undo():
    original_string = entry.get()
    if len(original_string):
        new_string = original_string[:-1]
        clear()
        entry.insert(0, new_string)
    else:
        clear()
        entry.insert(0, "ERROR")

#Adding the input field
entry = Entry(root)
entry.grid(row=1, columnspan=6, sticky=W+E)

#Adding the digits
Button(root, text="7", command= lambda :numbers(7)).grid(row=2, column=0)
Button(root, text="8", command= lambda : numbers(8)).grid(row=2, column=1)
Button(root, text="9", command= lambda : numbers(9)).grid(row=2, column=2)

Button(root, text="4", command= lambda :numbers(4)).grid(row=3, column=0)
Button(root, text="5", command= lambda :numbers(5)).grid(row=3, column=1)
Button(root, text="6", command= lambda :numbers(6)).grid(row=3, column=2)

Button(root, text="1", command= lambda :numbers(1)).grid(row=4, column=0)
Button(root, text="2", command= lambda :numbers(2)).grid(row=4, column=1)
Button(root, text="3", command= lambda :numbers(3)).grid(row=4, column=2)

#Adding the other buttons
Button(root, text="0", command= lambda :numbers(0)).grid(row=5, column=0)
Button(root, text="exp", command= lambda: operator(" ** ")).grid(row=5, column=2)
Button(root, text="AC", command= lambda: clear()).grid(row=5, column=1)

Button(root, text="/", command= lambda: operator(" / ")).grid(row=2, column=3)
Button(root, text="*", command= lambda: operator(" * ")).grid(row=3, column=3)
Button(root, text="-", command= lambda: operator(" - ")).grid(row=4, column=3)
Button(root, text="+", command= lambda: operator(" + ")).grid(row=5, column=3)

Button(root, text="%", command= lambda: operator(" % ")).grid(row=2, column=4)
Button(root, text="pi", command= lambda: operator(" * 3.1416")).grid(row=3, column=4)
Button(root, text="(", command= lambda: operator(" (")).grid(row=4, column=4)
Button(root, text="x!", command= factorial).grid(row=5, column=4)

Button(root, text="del", command= lambda: undo()).grid(row=2, column=5)
Button(root, text="^2", command= lambda: operator(" **2 ")).grid(row=3, column=5)
Button(root, text=")", command= lambda: operator(" ) ")).grid(row=4, column=5)
Button(root, text="=", command= lambda: calculate()).grid(row=5, column=5)

root.mainloop()
