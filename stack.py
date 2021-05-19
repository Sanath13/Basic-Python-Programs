class Stack:
    def __init__(self):
        self.x = []			# create empty stack

    def is_empty(self):
        return self.x == []		#return whether stack is empty or not, returns 0 or 1

    def push(self,data):
        self.x.append(data)		#add data to the stack

    def pop(self):
        return self.x.pop()		#remove data from the stack


s = Stack()
while True:
    print("1 for push, 2 for pop and 3 to quit")
    do = int(input("What would you like to do?"))
    if do == 1:
        data = int(input("Enter an element:"))
        s.push(data)
    elif do == 2:
        if s.is_empty():
            print("Stack is empty")
        else:
            print("Popped value:",s.pop())
    elif do == 3:
        break


