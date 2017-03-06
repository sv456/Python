class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL():
    def __init__(self):
        self.head=None
        self.last=None

    def add_node(self):
        while True:
            ch=int(raw_input('1.Data entry\n2.Exit\n'))
            if ch==1:
                data=int(raw_input('enter the data for the node:'))
                new_node=Node(data)
                if self.head is None:
                    self.head=self.last=new_node
                else:
                    self.last.next=new_node
                    new_node.prev=self.last
                    self.last=new_node
            else:
                break

    def traverse(self):
        if self.head is None:
            return
        tmp=self.head
        while tmp:
            ch=raw_input('enter f to traverse forward and r to traverse reverse:')
            if ch is 'f':
                print tmp.data
                tmp=tmp.next
            elif ch is 'r':
                print tmp.data
                tmp=tmp.prev
            else:
                print 'exiting'
                break

    def printList(self):
        tmp=self.head
        while(tmp):
            print tmp.data
            tmp=tmp.next

    def add_at_first(self,data):
        if self.head is None:
            return
        new_node=Node(data)
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

    def insert_after(self,ref,data):
        if ref is None:
            print 'prev node cannot be NULL'
            return
        new_node=Node(data)
        new_node.prev=ref
        new_node.next=ref.next
        ref.next.prev=new_node
        ref.next=new_node

    def push(self,data):
        if self.head is None:
            return
        new_node=Node(data)
        self.last.next=new_node
        new_node.prev=self.last
        self.last=new_node

    def insert_before(self,ref,data):
        if self.head is None:
            return
        new_node=Node(data)
        new_node.next=ref
        new_node.prev=ref.prev
        ref.prev.next=new_node
        ref.prev=new_node
        

if __name__=='__main__':
    ll=DLL()
    ll.add_node()
    ll.traverse()
    print 
    ll.printList()
    print ' '
    ll.add_at_first(5)
    ll.printList()
    print ' '
    ll.insert_after(ll.head.next,15)
    ll.printList()
    print ' '
    ll.insert_before(ll.head.next,25)
    ll.printList()
    print ' '
    ll.push(70)
    ll.printList()
    print ' '
    



