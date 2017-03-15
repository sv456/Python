class Dequeue():
    def __init__(self):
        self.items=[]
    def addRear(self,item):
        self.items.insert(0,item)
    def addFront(self,item):
        self.items.append(item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def isEmpty(self):
        if len(self.items)==0:
            return True
        return False
    def size(self):
        return len(self.items)


