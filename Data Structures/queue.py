class Queue():
    def __init__(self):
        self.items=[]

    def enqueue(self,data):
        self.items.insert(0,data)

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


