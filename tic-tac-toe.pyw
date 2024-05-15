from tkinter import *
from types import DynamicClassAttribute

def cleard():
    tic1["text"] = ""
    tic2["text"] = ""
    tic3["text"] = ""
    tic4["text"] = ""
    tic5["text"] = ""
    tic6["text"] = ""
    tic7["text"] = ""
    tic8["text"] = ""
    tic9["text"] = ""

    tic1["state"] = NORMAL
    tic2["state"] = NORMAL
    tic3["state"] = NORMAL
    tic4["state"] = NORMAL
    tic5["state"] = NORMAL
    tic6["state"] = NORMAL
    tic7["state"] = NORMAL
    tic8["state"] = NORMAL
    tic9["state"] = NORMAL

def doit1():
    global temp
    if temp=="X":
        tic1["text"] = temp
        temp="O"
    else:
        tic1["text"] = temp
        temp="X"
    if tic1["text"] == "X":
        tic1["disabledforeground"] = "blue"
    elif tic1["text"] == "O":
        tic1["disabledforeground"] = "red"
    tic1["state"] = DISABLED
    winwin()
    arrowd()

def doit2():
    global temp
    if temp=="X":
        tic2["text"] = temp
        temp="O"
    else:
        tic2["text"] = temp
        temp="X"
    if tic2["text"] == "X":
        tic2["disabledforeground"] = "blue"
    elif tic2["text"] == "O":
        tic2["disabledforeground"] = "red"
    tic2["state"] = DISABLED
    winwin()
    arrowd()

def doit3():
    global temp
    if temp=="X":
        tic3["text"] = temp
        temp="O"
    else:
        tic3["text"] = temp
        temp="X"
    if tic3["text"] == "X":
        tic3["disabledforeground"] = "blue"
    elif tic3["text"] == "O":
        tic3["disabledforeground"] = "red"
    tic3["state"] = DISABLED
    winwin()
    arrowd()

def doit4():
    global temp
    if temp=="X":
        tic4["text"] = temp
        temp="O"
    else:
        tic4["text"] = temp
        temp="X"
    if tic4["text"] == "X":
        tic4["disabledforeground"] = "blue"
    elif tic4["text"] == "O":
        tic4["disabledforeground"] = "red"
    tic4["state"] = DISABLED
    winwin()
    arrowd()

def doit5():
    global temp
    if temp=="X":
        tic5["text"] = temp
        temp="O"
    else:
        tic5["text"] = temp
        temp="X"
    if tic5["text"] == "X":
        tic5["disabledforeground"] = "blue"
    elif tic5["text"] == "O":
        tic5["disabledforeground"] = "red"
    tic5["state"] = DISABLED
    winwin()
    arrowd()

def doit6():
    global temp
    if temp=="X":
        tic6["text"] = temp
        temp="O"
    else:
        tic6["text"] = temp
        temp="X"
    if tic6["text"] == "X":
        tic6["disabledforeground"] = "blue"
    elif tic6["text"] == "O":
        tic6["disabledforeground"] = "red"
    tic6["state"] = DISABLED
    winwin()
    arrowd()

def doit7():
    global temp
    if temp=="X":
        tic7["text"] = temp
        temp="O"
    else:
        tic7["text"] = temp
        temp="X"
    if tic7["text"] == "X":
        tic7["disabledforeground"] = "blue"
    elif tic7["text"] == "O":
        tic7["disabledforeground"] = "red"
    tic7["state"] = DISABLED
    winwin()
    arrowd()

def doit8():
    global temp
    if temp=="X":
        tic8["text"] = temp
        temp="O"
    else:
        tic8["text"] = temp
        temp="X"
    if tic8["text"] == "X":
        tic8["disabledforeground"] = "blue"
    elif tic8["text"] == "O":
        tic8["disabledforeground"] = "red"
    tic8["state"] = DISABLED
    winwin()
    arrowd()

def doit9():
    global temp
    if temp=="X":
        tic9["text"] = temp
        temp="O"
    else:
        tic9["text"] = temp
        temp="X"
    if tic9["text"] == "X":
        tic9["disabledforeground"] = "blue"
    elif tic9["text"] == "O":
        tic9["disabledforeground"] = "red"
    tic9["state"] = DISABLED
    winwin()
    arrowd()

def winwin():
    global xc, oc
    
    if tic1["text"]=="X" and tic2["text"]=="X" and tic3["text"]=="X":
        xc+=1
        cleard()
        xnt["text"] = xc
    elif tic4["text"]=="X" and tic5["text"]=="X" and tic6["text"]=="X":
        xc+=1
        cleard()
        xnt["text"] = xc
    elif tic7["text"]=="X" and tic8["text"]=="X" and tic9["text"]=="X":
        xc+=1
        cleard()
        xnt["text"] = xc
    elif tic1["text"]=="X" and tic4["text"]=="X" and tic7["text"]=="X":
        xc+=1
        cleard()
        xnt["text"] = xc
    elif tic2["text"]=="X" and tic5["text"]=="X" and tic8["text"]=="X":
        xc+=1
        cleard()
        xnt["text"] = xc
    elif tic3["text"]=="X" and tic6["text"]=="X" and tic9["text"]=="X":
        xc+=1
        cleard()
        xnt["text"] = xc
    elif tic1["text"]=="X" and tic5["text"]=="X" and tic9["text"]=="X":
        xc+=1
        cleard()
        xnt["text"] = xc
    elif tic3["text"]=="X" and tic5["text"]=="X" and tic7["text"]=="X":
        xc+=1
        cleard()
        xnt["text"] = xc
    
    if tic1["text"]=="O" and tic2["text"]=="O" and tic3["text"]=="O":
        oc+=1
        cleard()
        ont["text"] = oc
    elif tic4["text"]=="O" and tic5["text"]=="O" and tic6["text"]=="O":
        oc+=1
        cleard()
        ont["text"] = oc
    elif tic7["text"]=="O" and tic8["text"]=="O" and tic9["text"]=="O":
        oc+=1
        cleard()
        ont["text"] = oc
    elif tic1["text"]=="O" and tic4["text"]=="O" and tic7["text"]=="O":
        oc+=1
        cleard()
        ont["text"] = oc
    elif tic2["text"]=="O" and tic5["text"]=="O" and tic8["text"]=="O":
        oc+=1
        cleard()
        ont["text"] = oc
    elif tic3["text"]=="O" and tic6["text"]=="O" and tic9["text"]=="O":
        oc+=1
        cleard()
        ont["text"] = oc
    elif tic1["text"]=="O" and tic5["text"]=="O" and tic9["text"]=="O":
        oc+=1
        cleard()
        ont["text"] = oc
    elif tic3["text"]=="O" and tic5["text"]=="O" and tic7["text"]=="O":
        oc+=1
        cleard()
        ont["text"] = oc
    elif (tic1["text"]=="O" or tic1["text"]=="X") and (tic2["text"]=="O" or tic2["text"]=="X") and (tic3["text"]=="O" or tic3["text"]=="X") and (tic4["text"]=="O" or tic4["text"]=="X") and (tic5["text"]=="O" or tic5["text"]=="X") and (tic6["text"]=="O" or tic6["text"]=="X") and (tic7["text"]=="O" or tic7["text"]=="X") and (tic8["text"]=="O" or tic8["text"]=="X") and (tic9["text"]=="O" or tic9["text"]=="X"):
        cleard()

def resetd():
    cleard()
    global oc, xc, temp
    oc=0
    xc=0
    ont["text"] = 0
    xnt["text"] = 0
    temp="X"
    arrowd()

def arrowd():
    global temp
    if temp=="X":
        arrow1.place(x=100, y=20)
        arrow2.place_forget()
    elif temp=="O":
        arrow2.place(x=201, y=20)
        arrow1.place_forget()

root = Tk()
root.title("Tic-Tac-Toe")
root.geometry("320x480")
root.configure(bg="white")

i=0
temp="X"
a=""""""

xc=0
oc=0

tic1 = Button(root, text=a, height=3, width=6, bg="white", fg="black", font=("Calibiri Light", 12), command=doit1)
tic1.place(x=65, y=120)

tic2 = Button(root, text=a, height=3, width=6, bg="white", fg="black", font=("Calibiri Light", 12), command=doit2)
tic2.place(x=129, y=120)

tic3 = Button(root, text=a, height=3, width=6, bg="white", fg="black", font=("Calibiri Light", 12), command=doit3)
tic3.place(x=193, y=120)

tic4 = Button(root, text=a, height=3, width=6, bg="white", fg="black", font=("Calibiri Light", 12), command=doit4)
tic4.place(x=65, y=188)

tic5 = Button(root, text=a, height=3, width=6, bg="white", fg="black", font=("Calibiri Light", 12), command=doit5)
tic5.place(x=129, y=188)

tic6 = Button(root, text=a, height=3, width=6, bg="white", fg="black", font=("Calibiri Light", 12), command=doit6)
tic6.place(x=193, y=188)

tic7 = Button(root, text=a, height=3, width=6, bg="white", fg="black", font=("Calibiri Light", 12), command=doit7)
tic7.place(x=65, y=256)

tic8 = Button(root, text=a, height=3, width=6, bg="white", fg="black", font=("Calibiri Light", 12), command=doit8)
tic8.place(x=129, y=256)

tic9 = Button(root, text=a, height=3, width=6, bg="white", fg="black", font=("Calibiri Light", 12), command=doit9)
tic9.place(x=193, y=256)

xbel = Label(root, text="X", bg="white", fg="blue", font=("Calibri Light", 20)).place(x=98, y=40)
obel = Label(root, text="O", bg="white", fg="red", font=("Calibri Light", 20)).place(x=198, y=40)

xnt = Label(root, text=xc, bg="white", fg="black", font=("Calibri Light", 12))
xnt.place(x=101, y=70)
ont = Label(root, text=oc, bg="white", fg="black", font=("Calibri Light", 12))
ont.place(x=202, y=70)

arrow1 = Label(root, text="v", bg="white", fg="green", font=("Calibri Light", 12))
arrow1.place(x=100, y=20)
arrow2 = Label(root, text="v", bg="white", fg="green", font=("Calibri Light", 12))
# arrow2.place(x=432, y=80)

reset = Button(root, text="Reset", height=1, width=8, bg="white", fg="black", font=("Calibiri Light", 12), command=resetd)
reset.place(x=118, y=390)

clear = Button(root, text="Clear", height=1, width=8, bg="white", fg="black", font=("Calibiri Light", 12), command=cleard)
clear.place(x=118, y=360)

root.mainloop()