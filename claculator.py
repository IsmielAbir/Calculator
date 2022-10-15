import tkinter as ab

calcu = ''

def add_calcu(symbol):
    global calcu
    calcu += str(symbol)
    result.delete(1.0, 'end')
    result.insert(1.0, calcu)


def eveluate_calcu():
    global calcu
    try:
        r = str(eval(calcu))
        calcu = ''
        result.delete(1.0, 'end')
        result.insert(1.0, r)
    except:
        clear()
        result.insert(1.0, 'Error')
        


def clear():
    global calcu
    calcu = ''
    result.delete(1.0, 'end')
    


root =ab.Tk()
root.geometry("300x250")

result = ab.Text(root, height=2, width=16, font=('Arial', 24))
result.grid(columnspan=5)



btn_1 =ab.Button(root, text='1', command=lambda: add_calcu(1), width=5, font=('Arial', 12))
btn_1.grid(row=2, column=1)

btn_2 =ab.Button(root, text='2', command=lambda: add_calcu(2), width=5, font=('Arial', 12))
btn_2.grid(row=2, column=2)


btn_3 =ab.Button(root, text='3', command=lambda: add_calcu(3), width=5, font=('Arial', 12))
btn_3.grid(row=2, column=3)


btn_4 =ab.Button(root, text='4', command=lambda: add_calcu(4), width=5, font=('Arial', 12))
btn_4.grid(row=3, column=1)


btn_5 =ab.Button(root, text='5', command=lambda: add_calcu(5), width=5, font=('Arial', 12))
btn_5.grid(row=3, column=2)


btn_6 =ab.Button(root, text='6', command=lambda: add_calcu(6), width=5, font=('Arial', 12))
btn_6.grid(row=3, column=3)


btn_7 =ab.Button(root, text='7', command=lambda: add_calcu(7), width=5, font=('Arial', 12))
btn_7.grid(row=4, column=1)


btn_8 =ab.Button(root, text='8', command=lambda: add_calcu(8), width=5, font=('Arial', 12))
btn_8.grid(row=4, column=2)


btn_9 =ab.Button(root, text='9', command=lambda: add_calcu(9), width=5, font=('Arial', 12))
btn_9.grid(row=4, column=3)

btn_0 =ab.Button(root, text='0', command=lambda: add_calcu(0), width=5, font=('Arial', 12))
btn_0.grid(row=5, column=2)


btn_plus =ab.Button(root, text='+', command=lambda: add_calcu('+'), width=5, font=('Arial', 12))
btn_plus.grid(row=2, column=4)

btn_mi =ab.Button(root, text='-', command=lambda: add_calcu('-'), width=5, font=('Arial', 12))
btn_mi.grid(row=3, column=4)

btn_mu =ab.Button(root, text='*', command=lambda: add_calcu('*'), width=5, font=('Arial', 12))
btn_mu.grid(row=4, column=4)

btn_di =ab.Button(root, text='/', command=lambda: add_calcu('/'), width=5, font=('Arial', 12))
btn_di.grid(row=5, column=4)


btn_open =ab.Button(root, text='(', command=lambda: add_calcu('('), width=5, font=('Arial', 12))
btn_open.grid(row=5, column=1)

btn_close =ab.Button(root, text=')', command=lambda: add_calcu(')'), width=5, font=('Arial', 12))
btn_close.grid(row=5, column=3)


btn_clear =ab.Button(root, text='C', command=clear, width=13, font=('Arial', 12))
btn_clear.grid(row=6, column=1, columnspan=2)

btn_equal =ab.Button(root, text='=', command=eveluate_calcu, width=13, font=('Arial', 12))
btn_equal.grid(row=6, column=3, columnspan=2)




root.mainloop()