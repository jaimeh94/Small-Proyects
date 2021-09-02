from tkinter import *
from typing import Collection

raiz = Tk()

miFrame = Frame(raiz)

miFrame.pack()

operation = ''
last_operation = ''
result = 0

#------------------Screen-----------------
numberScreen = StringVar()

screen = Entry(miFrame, textvariable=numberScreen)
screen.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
screen.config(background='black', fg='#03f943', justify='right')

#---------------keyboard press-----------------
def numberPressed(num):
    global operation
    global last_operation
    print(num +'\n'+ numberScreen.get())
    if numberScreen.get() == '0':
        if num == '0':
            pass
        if num == '.':
            numberScreen.set(numberScreen.get() + num)
        else:
            numberScreen.set('')
            numberPressed(num)
    # elif numberScreen.get() == '0':
    #     numberScreen.set('')
    #     numberPressed(num)
    elif '.' in numberScreen.get() and num == '.':
        numberScreen.set(numberScreen.get())
    # elif (num != '.' and numberScreen.get() == '0'):
    #     numberScreen.set(num)
    else:
        if operation != '' and operation != 'waiting':
            last_operation=operation
            numberScreen.set(num)
            operation = 'waiting'
        else:
            # print('.' in numberScreen.get())
            numberScreen.set(numberScreen.get() + num)

#-------------Funtions---------------------
## --------------Sum-------------------
def Sum(num):
    global operation
    global result
    result += float(num)

    numberScreen.set(result)

    operation = 'sum'

##-------------Rest-------------------
def Rest(num):
    global operation
    global result
    # numberScreen.set('')
    if operation == '':
        result = float(num)
        operation = 'rest'
    else:
        result -= float(num)

        numberScreen.set(result)
        operation = 'rest'

##-------------Mult----------------------
def Mult(num):
    global operation
    global result
    if operation == '':
        result = float(num)
        operation = 'mult'
    else:
        result *= float(num)

        numberScreen.set(result)
        operation = 'mult'

##-------------Div-----------------------
def Div(num):
    global operation
    global result
    if operation == '':
        result = float(num)
        operation = 'division'
    else:
        if num == '0':
            numberScreen.set('Error: Div by 0')
        else:
            result /= float(num)

            numberScreen.set(result)
            operation = 'division'

##--------------Equal--------------------
def Equal(num):
    global last_operation
    global result
    global operation
    if last_operation == 'sum':
        Sum(num)
    elif last_operation == 'rest':
        Rest(num)
    elif last_operation == 'mult':    
        Mult(num)    
    elif last_operation == 'division':    
        Div(num)
    # elif last_operation == 'rest'    
    #     Sum(num)

    operation = ''
    last_operation = ''



#-----------------row0--------------------
buttonC = Button(miFrame, text='C', width=5, command=lambda:numberScreen.set('0'))
buttonC.grid(row=2, column=3)


#-----------------row1---------------------

button7 = Button(miFrame, text='7', width=5, command=lambda:numberPressed('7'))
button7.grid(row=3, column=1)
button8 = Button(miFrame, text='8', width=5, command=lambda:numberPressed('8'))
button8.grid(row=3, column=2)
button9 = Button(miFrame, text='9', width=5, command=lambda:numberPressed('9'))
button9.grid(row=3, column=3)
buttonDiv = Button(miFrame, text='/', width=5, command=lambda:Div(numberScreen.get()))
buttonDiv.grid(row=3, column=4)

#-----------------row2---------------------

button4 = Button(miFrame, text='4', width=5, command=lambda:numberPressed('4'))
button4.grid(row=4, column=1)
button5 = Button(miFrame, text='5', width=5, command=lambda:numberPressed('5'))
button5.grid(row=4, column=2)
button6 = Button(miFrame, text='6', width=5, command=lambda:numberPressed('6'))
button6.grid(row=4, column=3)
buttonMult = Button(miFrame, text='x', width=5, command=lambda:Mult(numberScreen.get()))
buttonMult.grid(row=4, column=4)

#-----------------row3---------------------

button1 = Button(miFrame, text='1', width=5, command=lambda:numberPressed('1'))
button1.grid(row=5, column=1)
button2 = Button(miFrame, text='2', width=5, command=lambda:numberPressed('2'))
button2.grid(row=5, column=2)
button3 = Button(miFrame, text='3', width=5, command=lambda:numberPressed('3'))
button3.grid(row=5, column=3)
buttonRes = Button(miFrame, text='-', width=5, command=lambda:Rest(numberScreen.get()))
buttonRes.grid(row=5, column=4)

#-----------------row4---------------------

buttonEqual = Button(miFrame, text='=', width=5, command=lambda:Equal(numberScreen.get()))
buttonEqual.grid(row=6, column=1)
button0 = Button(miFrame, text='0', width=5, command=lambda:numberPressed('0'))
button0.grid(row=6, column=2)
buttonDot = Button(miFrame, text='.', width=5, command=lambda:numberPressed('.'))
buttonDot.grid(row=6, column=3)
buttonPlus = Button(miFrame, text='+', width=5, command=lambda:Sum(numberScreen.get()))
buttonPlus.grid(row=6, column=4)

numberScreen.set('0')
raiz.mainloop()