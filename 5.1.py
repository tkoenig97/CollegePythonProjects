from tkinter import *

demoWind = Tk()

demoWind.title("Event Handling")
demoWind.geometry('200x50')
demoWind.configure(background="white")

inputText = StringVar()
btnText = StringVar()

enterLbl = Label(demoWind, text="Enter Text").grid(row=0, column=0)

entryArea = Entry(demoWind, textvariable=inputText).grid(row=0, column=1)


def showOnButton():
    btnText.set(inputText.get())


clickBtn = Button(demoWind, textvariable=btnText, command=showOnButton).grid(row=1, column=1)

btnText.set("Click Here")
demoWind.mainloop()
