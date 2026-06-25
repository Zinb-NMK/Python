class Stack:

    #Constructor
    def __init__(self):
        self.stack = []
        self.index = 0

    #Check is empty
    def isEmpty(self):
        return self.stack==[]

    #Pushing Element
    def push(self,data):
        self.stack.insert(self.index,data)
        self.index+=1 #index increment
        return f"{data} pushed to stack"

    #POP (Deleting the element from stack)
    def pop(self):
        self.index-=1
        data=self.stack.pop(self.index)
        return f"{data} popped from stack"

    #Size/ Length of stack
    def size(self):
        return len(self.stack)


# testing
if __name__=="__main__":
    obj=Stack()
    print(obj.push(1))
    print(obj.push(2))
    print(obj.push(3))
    print(obj.push(4))

    print(obj.pop())
    print(obj.pop())

    print(f"Size of Stack: {obj.size()}")

