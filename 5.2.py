import tkinter as tk
import tkinter.scrolledtext as st

s = 0


def keyEvent():
    showText()


def showText():
    global s
    s1 = e1.get()
    if s1 != '':
        s = s + int(s1)
        txt.insert('insert', "Bill payed:" + v.get() + " " + e1.get() + "\n")
        e1.delete(0, 'end')


def showTotal():
    global s
    txt.insert('insert', "--------------------------------\n")
    txt.insert('insert', "Total spent:" + str(s) + "\n")


root = tk.Tk()
v = tk.StringVar()
v.set("Mortgage")

rb1 = tk.Radiobutton(root, text="Car Payment", padx=20, variable=v, value="Car Payment")
rb1.grid(row=0, column=0)
rb2 = tk.Radiobutton(root, text="Mortgage", padx=20, variable=v, value="Mortgage")
rb2.grid(row=0, column=1)
rb3 = tk.Radiobutton(root, text="Utilities", padx=20, variable=v, value="Utilities")
rb3.grid(row=0, column=2)

tk.Label(root, text="Amount Spent").grid(row=1, column=0)

e1 = tk.Entry(root)
e1.grid(row=1, column=1)
e1.bind("<Return>", keyEvent)
b1 = tk.Button(root, text="Add Bill Payed", command=showText, width=40)
b1.grid(row=1, column=2)
b2 = tk.Button(root, text="Total Amount Payed", command=showTotal, width=40)
b2.grid(row=2, column=2)
txt = st.ScrolledText(root, height=6)
txt.grid(row=3, column=0, columnspan=3)
root.geometry("600x200+300+300")

root.mainloop()
