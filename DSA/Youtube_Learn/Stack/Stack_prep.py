class Stack:

    #Constructor/Stack initializing
    def __init__(self):
        self.stack=[]

    #Check if stack is Empty
    def isEmpty(self):
        return self.stack==[]

    #Insert Element into Stack
    def push(self, data):
        self.stack.append(data)
        return f'{data} has been pushed'

    #delete/remove element from stack
    def pop(self):
        if self.isEmpty():
            return "Stack underflow"

        data = self.stack.pop()
        return f'{data} has been pooped'

    # Size of stack
    def size(self):
        return len(self.stack)

    #Display stack
    def see(self):
        return self.stack

if __name__=="__main__":
    obj = Stack()

    #Number of stack elements
    n = int(input("Enter number of stack elements: "))

    #Enter elements
    for i in range(n):
        data = int(input(f"Enter element {i+1}: "))
        obj.push(data)

    #Stack display
    print(f'\nStack Elements: {obj.see()}')

    #Poping elements
    pop_count = int(input("Enter number of pop elements: "))

    if pop_count > n or pop_count < 0:
        print("Stack underflow")

    for i in range(pop_count):
        print(obj.pop())

    # Final Stack Count
    print(f"\nStack Elements: {obj.see()}")

    #Final Size
    print(f"Stack Size: {obj.size()}")