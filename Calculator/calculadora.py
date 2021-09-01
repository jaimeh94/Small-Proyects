from tkinter import *
from typing import Collection

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

operation = ''
result = 0

#------------------Screen-----------------
numberScreen = StringVar()

screen = Entry(miFrame, textvariable=numberScreen)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background='black', fg='#03f943', justify='right')

#---------------keyboard-----------------
def numberPressed(num):
    global operation
    print(num +'\n'+ numberScreen.get())
    if (num == '0' and numberScreen.get() == '0'):
        pass
    elif numberScreen.get() == '0':
        numberScreen.set('')
        numberPressed(num)
    else:
        if operation != '':
            numberScreen.set(num)
            operation = ''
        else:
            numberScreen.set(numberScreen.get() + num)

#-------------Funtions---------------------
## --------------Sum-------------------
def Sum(num):
    global operation
    global result
    result += int(num)

    numberScreen.set(result)

    operation = 'sum'

#-----------------row1---------------------

button7 = Button(miFrame, text='7', width=3, command=lambda:numberPressed('7'))
button7.grid(row=2, column=1)
button8 = Button(miFrame, text='8', width=3, command=lambda:numberPressed('8'))
button8.grid(row=2, column=2)
button9 = Button(miFrame, text='9', width=3, command=lambda:numberPressed('9'))
button9.grid(row=2, column=3)
buttonDiv = Button(miFrame, text='/', width=3)
buttonDiv.grid(row=2, column=4)

#-----------------row2---------------------

button4 = Button(miFrame, text='4', width=3, command=lambda:numberPressed('4'))
button4.grid(row=3, column=1)
button5 = Button(miFrame, text='5', width=3, command=lambda:numberPressed('5'))
button5.grid(row=3, column=2)
button6 = Button(miFrame, text='6', width=3, command=lambda:numberPressed('6'))
button6.grid(row=3, column=3)
buttonMult = Button(miFrame, text='x', width=3)
buttonMult.grid(row=3, column=4)

#-----------------row3---------------------

button1 = Button(miFrame, text='1', width=3, command=lambda:numberPressed('1'))
button1.grid(row=4, column=1)
button2 = Button(miFrame, text='2', width=3, command=lambda:numberPressed('2'))
button2.grid(row=4, column=2)
button3 = Button(miFrame, text='3', width=3, command=lambda:numberPressed('3'))
button3.grid(row=4, column=3)
buttonRes = Button(miFrame, text='-', width=3)
buttonRes.grid(row=4, column=4)

#-----------------row4---------------------

buttonEqual = Button(miFrame, text='=', width=3)
buttonEqual.grid(row=5, column=1)
button0 = Button(miFrame, text='0', width=3, command=lambda:numberPressed('0'))
button0.grid(row=5, column=2)
buttonDot = Button(miFrame, text='.', width=3, command=lambda:numberPressed('.'))
buttonDot.grid(row=5, column=3)
buttonPlus = Button(miFrame, text='+', width=3, command=lambda:Sum(numberScreen.get()))
buttonPlus.grid(row=5, column=4)


raiz.mainloop()