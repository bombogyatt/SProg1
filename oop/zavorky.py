from stack import *

def zkontroluj_zavorky(data):
    correct = False
    zavorky = Stack()

    for i in range(len(data)):
        if data[i] == "(":
            zavorky.push("(")
        elif data[i] == ")":
            last_item = zavorky.peek()
            if last_item == "(":
                zavorky.pop()
            else:
                return False
                
    if zavorky.isEmpty():
        return True
    else:
        return False

    






vzorec = input("vloz matematický vzorec: ")
correct = zkontroluj_zavorky(vzorec)
print(f'{vzorec} -> {correct}')


