class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class stack():
    def __init__(self):
        self.head=None

    def push(self):
        while True:
            ch=int(raw_input('1.Append data\n2.Exit\n'))
            if ch==1:
                data=int(raw_input('enter data to be appended:'))
                new_node=Node(data)
                if self.head==None:
                    self.head=new_node
                else:
                    new_node.next=self.head
                    self.head=new_node
            else:
                break

    def pop(self):
        tmp=self.head
        chk=self.head
        while True:
            ch=int(raw_input('1.Pop\n2.Exit\n'))
            if ch==1:
                if(self.is_empty()==0):
                    print 'Stack is empty'
                    return
                if chk is not None:
                    print chk.data,'is popped and deleted'
                    self.head=chk.next
                    tmp=None
                    chk=chk.next
                    tmp=chk
            else:
                break

    def traverse(self):
        tmp=self.head
        while(tmp):
            print 'stack',tmp.data
            tmp=tmp.next

    def is_empty(self):
        if self.head==None:
            return 0

if __name__=='__main__':
    lst=stack()
    lst.push()
    lst.traverse()
    lst.pop()
    lst.traverse()
