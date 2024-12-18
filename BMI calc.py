from tkinter import *
from tkinter.messagebox import *


def f():
    h = float(hei.get()) / 100
    m = int(mas.get())
    bmi = float(m/(h**2))
    il.delete(0, 1000000000)
    il.insert(0, f"Your BMI is {round(float(bmi))}")


root = Tk()
root["bg"] = "lime"
root.geometry("200x200+200+200")

hei = Entry(root, width=20, font="Aptos 12")
hei["bd"] = 2
hei.pack()
hei.insert(0, "           Enter you height")

mas = Entry(root, width=20, font="Aptos 12")
mas["bd"] = 2
mas.pack()
mas.insert(0, "       Enter you mass")

il = Entry(root, font="Aptos 12")
il["bd"] = 2
il.pack()
il.insert(0, "          Your BMI here")

but = Button(root, text="Calculate", command=f, width=10)
but.pack(pady=10)








    

root.mainloop()