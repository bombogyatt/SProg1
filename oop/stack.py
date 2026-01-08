class Stack:

    def __init__(self):
        self.stack = []
        self.n = 0

    def isEmpty(self):
        if self.n == 0:
            return True
        else:
            return False
        
    def push(self, k):
        self.n += 1
        self.stack.append(k)

    def pop(self):
        if not self.isEmpty():    
            self.n -= 1
            return self.stack.pop()
        else:
            print("nemožno POP, prvků 0")

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[self.n - 1]
        


zasobnik = Stack()
print(zasobnik.isEmpty())
for i in range(5):
    zasobnik.push(i)
print(zasobnik.peek())
print(zasobnik.isEmpty())
for i in range(5):
    print(f'mažu {zasobnik.pop()}')
zasobnik.pop()


    