import tkinter as tk
import random as rand

root = tk.Tk()
root.geometry("800x600")
root.title("Intel 8086 Simulator - 13390")
root.configure(background="#ecf0f1")
###########################################
#                 Funkcje                 #
###########################################

def placeItems(item, X_cord, Y_cord, bgC):
    for x in range(len(item)):
        item[x].config(width=8, bg=bgC, font="bold")
        item[x].place(x = X_cord, y = Y_cord)
        Y_cord = Y_cord + 40

def randomRegisterValue():
    for x in range(len(registersValue)):
        valText = registersTable[rand.randint(0,15)]+registersTable[rand.randint(0,15)]+registersTable[rand.randint(0,15)]+registersTable[rand.randint(0,15)]
        registersValue[x].config(text=valText)
    actionHistory.append("Generated new random registries\n")
    updateHistory()

def reset():
    for x in range(len(registersValue)):
        registersValue[x].config(text="0000")
    actionHistory.clear()
    History.delete(1.0,tk.END)


def moveRegisters(regFrom, regTo):
    regFrom = regFrom.get()
    regTo = regTo.get()
    if regFrom == regTo:
        actionHistory.append("Can't move same register\n")
        updateHistory()
    else:
        a = registers[regFrom-1].cget("text")
        b = registers[regTo-1].cget("text")
        temp = registersValue[regFrom-1].cget("text")
        registersValue[regTo-1].config(text=temp)
        registersValue[regFrom-1].config(text="0000")
        actionHistory.append(f"MOV {a}, {b}\n")
        updateHistory()

def exchangeRegisters(regA, regB):
    regA = regA.get()
    regB = regB.get()
    if regA == regB:
        actionHistory.append("Can't exchange same register\n")
        updateHistory()
    else:
        a = registers[regA-1].cget("text")
        val1 = registersValue[regA-1].cget("text")
        b = registers[regB-1].cget("text")
        val2 = registersValue[regB-1].cget("text")
        registersValue[regA-1].config(text=val2)
        registersValue[regB-1].config(text=val1)
        actionHistory.append(f"XCHG {a}, {b}\n")
        updateHistory()

def updateHistory():
    History.delete(1.0,tk.END)
    for x in range(len(actionHistory)):
        History.insert(tk.END,actionHistory[x])

def push(what):
    what = what.get()
    temp = registersValue[what-1].cget("text")
    stackmemory.append(temp)
    global stackpointer
    stackpointer = int(stackpointer,16) + 2
    stackpointer = hex(stackpointer).lstrip("0x")
    pointersValue[3].config(text=stackpointer)
    a = registers[what-1].cget("text")
    actionHistory.append(f"Pushed {a} to the stack\n")
    registersValue[what-1].config(text="0000")
    updateHistory()

def pop(where):
    where = where.get()
    a = registers[where-1].cget("text")
    b = stackmemory[-1]
    del stackmemory[-1]
    global stackpointer
    stackpointer = int(stackpointer,16) - 2
    stackpointer = hex(stackpointer).lstrip("0x")
    pointersValue[3].config(text=stackpointer)
    actionHistory.append(f"Popped {b} from the stack to {a}\n")
    registersValue[where-1].config(text=b)
    updateHistory()
###########################################
#          Struktura "na sztywno"         #
###########################################

actionHistory = []
stackmemory = []
stackpointer = "0"

registersTable = [
    "0","1","2","3",
    "4","5","6","7",
    "8","9","A","B",
    "C","D","E","F" 
]

registers = []
temp = tk.Label(text="AX")
registers.append(temp)
temp = tk.Label(text="BX")
registers.append(temp)
temp = tk.Label(text="CX")
registers.append(temp)
temp = tk.Label(text="DX")
registers.append(temp)

placeItems(registers,20,20,"#aaa")

registersValue = []
temp = tk.Label(text="0000")
registersValue.append(temp)
temp = tk.Label(text="0000")
registersValue.append(temp)
temp = tk.Label(text="0000")
registersValue.append(temp)
temp = tk.Label(text="0000")
registersValue.append(temp)

placeItems(registersValue,130,20,"#ccc")

pointers = []
temp = tk.Label(text="SI")
pointers.append(temp)
temp = tk.Label(text="DI")
pointers.append(temp)
temp = tk.Label(text="BP")
pointers.append(temp)
temp = tk.Label(text="SP")
pointers.append(temp)
temp = tk.Label(text="DISP")
pointers.append(temp)

placeItems(pointers,20,267,"#aaa")

pointersValue = []
temp = tk.Label(text="0000")
pointersValue.append(temp)
temp = tk.Label(text="0000")
pointersValue.append(temp)
temp = tk.Label(text="0000")
pointersValue.append(temp)
temp = tk.Label(text="0000")
pointersValue.append(temp)
temp = tk.Label(text="0000")
pointersValue.append(temp)

placeItems(pointersValue,130,267,"#ccc")
#######################################
#           Zmienne wyboru            #
#######################################

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()

checkbuttonsA = [
    tk.Checkbutton(text="AX",variable=var1,onvalue=1),
    tk.Checkbutton(text="BX",variable=var1,onvalue=2),
    tk.Checkbutton(text="CX",variable=var1,onvalue=3),
    tk.Checkbutton(text="DX",variable=var1,onvalue=4)
]
checkbuttonsB = [
    tk.Checkbutton(text="AX",variable=var2,onvalue=1),
    tk.Checkbutton(text="BX",variable=var2,onvalue=2),
    tk.Checkbutton(text="CX",variable=var2,onvalue=3),
    tk.Checkbutton(text="DX",variable=var2,onvalue=4),
]
radioButtons = [
    tk.Radiobutton(text="Z rejestru do pamięci",variable=var3,value=1),
    tk.Radiobutton(text="Z pamięci do rejestru",variable=var3,value=2)
]
radioButtonsB = [
    tk.Radiobutton(text="Indeksowy",variable=var4,value=1),
    tk.Radiobutton(text="Bazowy",variable=var4,value=2),
    tk.Radiobutton(text="Indeksowo-bazowy",variable=var4,value=3)
]
radioButtonsC = [
    tk.Radiobutton(text="SI i BX",variable=var5,value=1),
    tk.Radiobutton(text="DI i BX",variable=var5,value=2),
    tk.Radiobutton(text="SI i BP",variable=var5,value=3),
    tk.Radiobutton(text="DI i BP",variable=var5,value=4)
]

placeItems(checkbuttonsA,485,300,"#bdc3c7")
placeItems(checkbuttonsB,650,300,"#bdc3c7")
placeItems(radioButtons,250,10, "#ecf0f1")
placeItems(radioButtonsB,250,120, "#ecf0f1")
placeItems(radioButtonsC,250,300, "#ecf0f1")

radioButtons[0].config(width=20,font=("Arial",12))
radioButtons[1].config(width=20,font=("Arial",12))

radioButtonsB[0].config(width=20,font=("Arial",12))
radioButtonsB[1].config(width=20,font=("Arial",12))
radioButtonsB[2].config(width=20,font=("Arial",12))

radioButtonsC[0].config(width=20,font=("Arial",12))
radioButtonsC[1].config(width=20,font=("Arial",12))
radioButtonsC[2].config(width=20,font=("Arial",12))
radioButtonsC[3].config(width=20,font=("Arial",12))

########################################
#               Przyciski              #
########################################

buttonRandom = tk.Button(root, text="Random", command=randomRegisterValue)
buttonRandom.place(x=20, y=565)

buttonReset = tk.Button(root, text="Reset", command=reset)
buttonReset.place(x=90, y=565)

buttonMove = tk.Button(root, text="MOVE", command=lambda:moveRegisters(var1,var2))
buttonMove.place(x=485, y=565)

buttonExchange = tk.Button(root, text="XCHG", command=lambda:exchangeRegisters(var1,var2))
buttonExchange.place(x=555, y=565)

buttonPush = tk.Button(root, text="Push", command=lambda:push(var1))
buttonPush.place(x=635, y=565)

buttonPop = tk.Button(root, text="Pop", command=lambda:pop(var1))
buttonPop.place(x=705, y=565)

buttons = [buttonRandom,buttonReset,buttonMove,buttonExchange,buttonPush,buttonPop]

for x in range(len(buttons)):
    buttons[x].config(width=8)

######################################
#              Historia              #
######################################
History = tk.Text(height=15,width=35)
History.place(x=485, y=10)





root.mainloop()