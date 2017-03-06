class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList():
    def __init__(self):
        self.head=None

        
    #rotating linked list
    def rotate_ll(self,num):
        tmp=self.head
        if tmp is None:
            return
        cnt=1
        while(cnt<=num-1 and tmp.next):
            tmp=tmp.next
            cnt+=1
        if tmp.next is not None:
            nxt=pt=tmp.next
            chk=1
        else:
            return
        
        while(nxt.next):
            nxt=nxt.next
            
        tmp.next=None
        nxt.next=self.head
        self.head=pt
        

    #swapping of nodes
    def swap_nodes(self,x,y):
        if x==y:
            return
        prevx=None
        currx=self.head
        while currx!=None and currx.data!=x:
            prevx=currx
            currx=currx.next

        prevy=None
        curry=self.head
        while curry!=None and curry.data!=y:
            prevy=curry
            curry=curry.next

        if currx is None or curry is None:
            return

        if prevx is None:
            self.head=curry
        else:
            prevx.next=curry

        if prevy is None:
            self.head=currx
        else:
            prevy.next=currx

        tmp=currx.next
        currx.next=curry.next
        curry.next=tmp

    def create_resultant_ll(self,list1,list2):
        if list1==None and list2==None:
            return 0
        lst=list()
        n1=0
        su1=0
        while(list1 is not None):
            su1+=(list1.data)*(10**n1)
            list1=list1.next
            n1+=1
            
        n2=0
        su2=0
        while(list2 is not None):
            su2+=(list2.data)*(10**n2)
            list2=list2.next
            n2+=1

        su=su1+su2
        num=su
        cnt=0
        while(num>0):
            n=num%10
            lst.append(n)
            num=num/10
            cnt+=1
        i=0
        while(i<cnt):
            new_node=Node(lst[i])
            if(self.head==None):
                self.head=new_node
                self.last=new_node

            else:
                self.last.next=new_node
                self.last=new_node
            i+=1
            
            

    def add_node(self):
        while(True):
            n=int(raw_input('1.For data entry \n2.Exit\n'))
            if n==1:
                d=int(raw_input('enter the data for node:'))
                new_node=Node(d)
                if(self.head==None):
                    self.head=new_node
                    self.last=new_node

                else:
                    self.last.next=new_node
                    self.last=new_node
            else:
                break

        
            
    #print list in reverse in group
    def reverse_pos(self,head,pos):
        cur=head
        prev=None
        nxt=None
        cnt=0
        while(cur is not None and cnt<pos):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        if nxt is not None:
            head.next=rerverse_pos(nxt,pos)

        return prev

    
    #detect and remove loop in linked list
    def remove_loop(self,loop_node):
        ptr1=ptr2=loop_node
        k=1
        while(ptr1.next!=ptr2):
            ptr1=ptr1.next
            k+=1
        ptr1.nxt=ptr2.nxt=self.head
        for i in range(k):
            ptr2=ptr2.next

        while(ptr1!=ptr2):
            ptr1=ptr1.next
            ptr2=ptr2.next

        while(ptr2.next!=ptr1):
            ptr2=ptr2.next

        ptr2.next=None
            
        
    def detect_loop(self):
        slow_p=fast_p=self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p=slow_p.next
            fast_p=fast_p.next.next
            if fast_p==slow_p:
                remove_loop(slow_p)
                return 1
        return 0
        
    #reversing a linked list
    def reverse_rec(self,cur,prev):
        if cur.next is None:
            self.head=cur
            cur.next=prev
            return
        nxt=cur.next
        cur.next=prev
        self.reverse_rec(nxt,cur)
            
    def reverse(self):
        if self.head is None:
            return
        self.reverse_rec(self.head,None)
        
        

    #traversing through linked list
    def printList(self):
        tmp=self.head
        while(tmp):
            print tmp.data
            tmp=tmp.next

    #inserting node in first position
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    #inserting after desired node
    def new_pos(self,prev_node,data):
        if prev_node==None:
            print 'not a correct entry'
            return
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    #inserting node at the end of linked list
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
            return
        tmp=self.head
        while(tmp.next):
            tmp=tmp.next
        if tmp.next==None:
            tmp.next=new_node
        else:
            return

    #deleting a node
    def del_node(self,data):
        tmp=self.head
        if tmp is not None:
            if tmp.data==data:
                self.head=tmp.next
                tmp=None
        while(tmp):
            if tmp.data==data:
                break
            prev=tmp
            tmp=tmp.next

        if tmp is None:
            return
        prev.next=tmp.next
        tmp=None

    #deleting node at a given position
    def del_pos_node(self,pos):
        cnt=0
        tmp=self.head
        if tmp is not None:
            if cnt==pos:
                self.head=tmp.next
                tmp=None
                return
        while(cnt!=pos):
            prev=tmp
            tmp=tmp.next
            cnt+=1

        if tmp is None:
            return
        prev.next=tmp.next
        tmp=None

    #for counting number of nodes in linked list
    def node_cnt(self):
        cnt=0
        tmp=self.head
        while(tmp):
            cnt+=1
            tmp=tmp.next
        return cnt

    #recursive way of finding a node based on the data
    def search(self,node,data):
        if node.data!=data:
            self.search(node.next,data)
        else:
            print data,'found'

    def search_node(self,data):
        self.search(self.head,data)


if __name__=='__main__':
    ll1=LinkedList()
    ll1.add_node()
    ll1.printList()
    ll2=LinkedList()
    ll2.add_node()
    ll2.printList()
    ll=LinkedList()
    ll.create_resultant_ll(ll1.head,ll2.head)
    ll.printList()
    print 'no. of nodes',ll.node_cnt()
    print '\n'
    ll.push(60)
    ll.printList()
    print 'no. of nodes',ll.node_cnt()
    print '\n'
    ll.new_pos(ll.head.next,4)
    ll.printList()
    print 'no. of nodes',ll.node_cnt()
    print '\n'
    ll.append(71)
    ll.printList()
    print 'no. of nodes',ll.node_cnt()
    print '\n'
    ll.del_node(4)
    ll.printList()
    print 'no. of nodes',ll.node_cnt()
    print '\n'
    ll.del_pos_node(2)
    ll.printList()
    print 'no. of nodes',ll.node_cnt()
    ll.search_node(60)
    print
    ll.swap_nodes(60,71)
    ll.printList()
    print '\n'
    ll.reverse()
    ll.printList()
    print '\n'
    ll.head=ll.reverse_pos(ll.head,2)
    ll.printList()
    print '\n'
    print ll.detect_loop()
    print '\n'
    ll.rotate_ll(4)
    ll.printList()
    
    
    
    
    
