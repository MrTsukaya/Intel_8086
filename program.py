import tkinter as tk
import random as rand

root = tk.Tk()
root.geometry("800x600")
root.title("Intel 8086 Simulator - 13390")

###########################################
#                 Funkcje                 #
###########################################

def placeItems(item, X_cord, Y_cord, bgC):
    for x in range(len(item)):
        item[x].config(width=8, bg=bgC, font="bold")
        item[x].place(x = X_cord, y = Y_cord)
        Y_cord = Y_cord + 50

def randomRegisterValue():
    for x in range(len(registersValue)):
        valText = registersTable[rand.randint(0,15)]+registersTable[rand.randint(0,15)]+registersTable[rand.randint(0,15)]+registersTable[rand.randint(0,15)]
        registersValue[x].config(text=valText)
    actionHistory.append("Generated new random registries\n")
    updateHistory()

def reset():
    for x in range(len(registersValue)):
        registersValue[x].config(text="")
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

def push():
    print(1)

def pop():
    print(2)
###########################################
#          Struktura "na sztywno"         #
###########################################

actionHistory = []

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

placeItems(registers,10,10,"#aaa")

registersValue = []
temp = tk.Label()
registersValue.append(temp)
temp = tk.Label()
registersValue.append(temp)
temp = tk.Label()
registersValue.append(temp)
temp = tk.Label()
registersValue.append(temp)

placeItems(registersValue,110,10,"#ccc")

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

placeItems(pointers,10,250,"#aaa")

pointersValue = []
temp = tk.Label()
pointersValue.append(temp)
temp = tk.Label()
pointersValue.append(temp)
temp = tk.Label()
pointersValue.append(temp)
temp = tk.Label()
pointersValue.append(temp)
temp = tk.Label()
pointersValue.append(temp)

placeItems(pointersValue,110,250,"#ccc")
#######################################
#           Zmienne wyboru            #
#######################################

var1 = tk.IntVar()
var2 = tk.IntVar()

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
placeItems(checkbuttonsA,485,300,"#aaa")
placeItems(checkbuttonsB,650,300,"#aaa")

########################################
#               Przyciski              #
########################################

buttonRandom = tk.Button(root, text="Random", command=randomRegisterValue)
buttonRandom.place(x=10, y=565)

buttonReset = tk.Button(root, text="Reset", command=reset)
buttonReset.place(x=80, y=565)

buttonMove = tk.Button(root, text="MOVE", command=lambda:moveRegisters(var1,var2))
buttonMove.place(x=485, y=565)

buttonExchange = tk.Button(root, text="XCHG", command=lambda:exchangeRegisters(var1,var2))
buttonExchange.place(x=555, y=565)

buttonPush = tk.Button(root, text="Push", command=push)
buttonPush.place(x=635, y=565)

buttonPop = tk.Button(root, text="Pop", command=pop)
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