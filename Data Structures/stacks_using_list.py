class Stack():
    def __init__(self):
        self.items=[]

    def is_empty(self):
        if len(self.items)==0:
            return True
        return False

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[(len(self.items)-1)]


