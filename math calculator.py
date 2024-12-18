from tkinter import *
from tkinter.messagebox import showerror

root = Tk()
root.title("Calculator")
root["bg"] = "dark cyan"
s = True

def idle(text):
    global s
    if text == "C":
        s = False
        ent.delete(0, END)
    elif text == "=":
        try:
            r = eval(ent.get())
            ent.delete(0, END)
            ent.insert(END, r)
            s = True
        except:
            showerror("Error", "Syntax error")
            s = False
    else:
        if s:
            ent.delete(0, END)
            s = False
        ent.insert(END, text)




buttons = [(1, 0, "7", "gold"), (1, 1, "8", "gold"), (1, 2, "9", "gold"), (1, 3, "C", "lime"),
           (2, 0, "4", "gold"), (2, 1, "5", "gold"), (2, 2, "6", "gold"), (2, 3, "-", "lime"),
           (3, 0, "1", "gold"), (3, 1, "2", "gold"), (3, 2, "3", "gold"), (3, 3, "+", "lime"),
           (4, 0, "0", "gold"), (4, 1, "=", "lime"), (4, 2, "/", "lime"), (4, 3, "*", "lime"),]

ent = Entry(root, justify="left", width=20, font=("Comic Sans MS", 15), bg="linen")
ent.grid(row=0, column=0, columnspan=4, pady=10)

for (col,row,text,color) in buttons:
        button = Button(root, text=f"{text}", width=6, height=2, command=lambda t=text: idle(t), bg=color)
        button.grid(row=col, column=row, pady=2, padx=2)

root.mainloop()