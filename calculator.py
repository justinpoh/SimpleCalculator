from tkinter import *

rootWidget = Tk()
rootWidget.title("Calculator")

labelWidget1 = Label(rootWidget, text="", borderwidth=10)
labelWidget1.grid(row=0, column=0, columnspan=3)

def onClick(number):
    currentText = labelWidget1['text']
    labelWidget1['text'] = currentText + str(number)

def onClickAddition():
    currentText = labelWidget1['text']
    labelWidget1['text'] = currentText + " + "

def onClickMinus():
    currentText = labelWidget1['text']
    labelWidget1['text'] = currentText + " - "

def onClickTimes():
    currentText = labelWidget1['text']
    labelWidget1['text'] = currentText + " * "

def onClickDivide():
    currentText = labelWidget1['text']
    labelWidget1['text'] = currentText + " / "

def isOperator(string):
    if ((string == "+") | (string == "-") | (string == "/") | (string == "*")):
        return True
    else:
        return False

def onClickResolve():
    currentText = labelWidget1['text']
    currentTextArr = currentText.split()
    length = len(currentTextArr)
    secondList = []
    if (length%2 == 0):
        labelWidget1['text'] = "Syntax Error!"
        return

    first = currentTextArr[0]
    index =  1
    # First settle the multiplication and division
    while(index < length):
        operator = currentTextArr[index]
        second = currentTextArr[index + 1]

        if (not isOperator(operator)):
            labelWidget1['text'] = "Syntax Error!"

        if ((operator == "*") | (operator == "/")):
            sum = 0
            if (operator == "*"):
                sum = int(first) * int(second)
            else:
                sum = int(first) / int(second)
            first = str(sum)
            index = index + 2
        else:
            secondList.append(first)
            secondList.append(operator);
            first = second
            index = index + 2
    secondList.append(first)


    # Now, we settle the remaining arithmetic
    length = len(secondList)
    first = secondList[0]
    index = 1
    while(index < length):
        operator2 = secondList[index]
        second2 = secondList[index + 1]
        sum2 = 0
        if (operator2 == "+"):
            sum2 = int(first) + int(second2)
        else:
            sum2 = int(first) - int(second2)

        first = str(sum2)
        index = index + 2

    labelWidget1['text'] = first





def onClickClear():
    labelWidget1['text'] = ""




numOfRows = 3
numOfCols = 3
firstNumber = 1
for i in range(1, numOfRows+1):
    for j in range(1, numOfCols+1):
        buttonWidget = Button(rootWidget, text=firstNumber, padx=20, pady=20, command=lambda t=firstNumber: onClick(t))
        buttonWidget.grid(row=i, column=j)
        firstNumber = firstNumber + 1

buttonWidget0 = Button(rootWidget, text="0", padx=20, pady=20, command=lambda: onClick(0))
buttonWidget0.grid(row=4, column=1)

buttonWidget1 = Button(rootWidget, text="+", padx=20, pady=20, command=onClickAddition)
buttonWidget1.grid(row=4, column=2)

buttonWidget4 = Button(rootWidget, text="-", padx=20, pady=20, command=onClickMinus)
buttonWidget4.grid(row=5, column=1)

buttonWidget5 = Button(rootWidget, text="*", padx=20, pady=20, command=onClickTimes)
buttonWidget5.grid(row=5, column=2)

buttonWidget6 = Button(rootWidget, text="/", padx=20, pady=20, command=onClickDivide)
buttonWidget6.grid(row=5, column=3)

buttonWidget2 = Button(rootWidget, text="=", padx=20, pady=50, command=onClickResolve)
buttonWidget2.grid(row=4, column=3, rowspan=2)

buttonWidget3 = Button(rootWidget, text="C", padx=70, pady=20, command=onClickClear)
buttonWidget3.grid(row=6, column=1, columnspan=3)




# a GUI is like a program with endless loop. Need to start the looping
rootWidget.mainloop()
