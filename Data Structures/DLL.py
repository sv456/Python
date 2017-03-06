class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DLL():
    def __init__(self):
        self.head=None
        self.last=None

    #Adding new node
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

    #traversing through linkedlist
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

    #print data in all nodes
    def printList(self):
        tmp=self.head
        while(tmp):
            print tmp.data
            tmp=tmp.next

    #adding node at as first
    def add_at_first(self,data):
        if self.head is None:
            return
        new_node=Node(data)
        new_node.next=self.head
        self.head.prev=new_node
        self.head=new_node

    #adding node after a particular node
    def insert_after(self,ref,data):
        if ref is None:
            print 'prev node cannot be NULL'
            return
        new_node=Node(data)
        new_node.prev=ref
        new_node.next=ref.next
        ref.next.prev=new_node
        ref.next=new_node

    #adding a node at the end
    def push(self,data):
        if self.head is None:
            return
        new_node=Node(data)
        self.last.next=new_node
        new_node.prev=self.last
        self.last=new_node

    #adding a node before a particular node
    def insert_before(self,ref,data):
        if self.head is None:
            return
        new_node=Node(data)
        new_node.next=ref
        new_node.prev=ref.prev
        ref.prev.next=new_node
        ref.prev=new_node

    #deleting head node
    def del_head_node(self):
        if self.head is None:
            return
        tmp=self.head
        self.head=tmp.next
        self.head.prev=None
        tmp=None

   #deleting middle node 
    def del_mid_node(self):
        if self.head is None:
            return
        slow_p=self.head
        fast_p=self.head
        while(fast_p is not None):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
        tmp=slow_p
        tmp.prev.next=tmp.next
        tmp.next.prev=tmp.prev
        tmp=None

    #delete last node
    def del_last_node(self):
        if self.head is None:
            return
        tmp=self.last
        tmp.prev.next=None
        self.last=tmp.prev
        tmp.prev=None
        tmp=None
    
        
        

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
    ll.del_head_node()
    ll.printList()
    print ' '
    ll.del_mid_node()
    ll.printList()
    print ' '
    ll.del_last_node()
    ll.printList()
    print ' '
    



