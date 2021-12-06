class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None

    def delbeg(self):
        self.head=self.head.next

    def delend(self):
        n=self.head
        while(n.next.next is not None):
            n=n.next
        n.next=None

    def delpos(self,x):
        n=self.head

        while(n!=None):
            if x==n.data:
                break
            p=n
            n=n.next
        if n is not None:
            p.next=n.next
    def addend(self,data):
        new_n=Node(data)
        n=self.head
        if n is None:
            self.head=new_n
            return
        while(n.next!=None):
            n=n.next
        n.next=new_n

    def printl(self):
        n=self.head
        while(n!=None):
            print(n.data,end=" ")
            n=n.next
ll=LL()
l=list(map(int,input().split()))
for i in range(len(l)):
    ll.addend(l[i])
ll.printl()


ll.delend()
print()
ll.printl()

ll.delpos(3)
print()
ll.printl()

ll.delbeg()
print()
ll.printl()

