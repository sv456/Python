class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class CirLL():
    def __init__(self):
        self.head=None
        self.last=None

    #adding nodes
    def add_node(self):
        while True:
            ch=int(raw_input('1.Data entry\n2.Exit\n'))
            if ch==1:
                data=int(raw_input('enter data:'))
                new_node=Node(data)
                if self.head is None:
                    self.head=new_node
                    self.last=new_node
                    new_node.next=new_node
                else:
                    self.last.next=new_node
                    self.last=new_node
                    new_node.next=self.head
            else:
                break

    #Traversing
    def printList(self):
        tmp=self.head
        while True:
            ch=int(raw_input('Traversing:\n1.F\n2.exit\n'))
            if ch==1:
                print tmp.data
                tmp=tmp.next
            else:
                break

    #adding node at beginning
    def insert_first(self,data):
        if self.head is None:
            return
        new_node=Node(data)
        new_node.next=self.head
        self.last.next=new_node
        self.head=new_node

    #adding nodes at the end
    def insert_last(self,data):
        if self.head is None:
            return
        new_node=Node(data)
        self.last.next=new_node
        self.last=new_node
        self.last.next=self.head

    #splitting circular ll into 2 ll
    def split_cll(self,ll1,ll2):
        slow_p=self.head
        fast_p=self.head
        while(fast_p.next!=self.head and fast_p.next.next!=self.head):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
        if fast_p.next.next==self.head:
            fast_p=fast_p.next
        ll1.head=self.head
        if self.head.next!=self.head:
            ll2.head=slow_p.next
        fast_p.next=slow_p.next
        slow_p.next=self.head
        

if __name__=='__main__':
    ll=CirLL()
    ll.add_node()
    ll.printList()
    print
    
    ll1=CirLL()
    ll2=CirLL()
    ll.split_cll(ll1,ll2)
    ll1.printList()
    ll2.printList()
                   
