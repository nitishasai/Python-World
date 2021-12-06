class Node:
    def __init__(self,data):
        self.data=data
        self.next=None             #node creation class

class LinkL:
    def __init__(self):
        self.head=None              #ll class

    def addbeg(self, data):
        new_n = Node(data)
        new_n.next = self.head
        self.head = new_n



    def addAft(self,data,x):
        new_n= Node(data)
        n=self.head
        while(n!=None):
            if x==n.data:
                break
            n=n.next
        if n !=None:
            new_n.next=n.next
            n.next=new_n




    def addbefo(self,data,x):
        new_n=Node(data)
        n=self.head
        if n.data==x:
            new_n.next=self.head
            self.head=new_n
        else:
            while(n.next!=None):
                if x==n.next.data:
                    break
                n=n.next
            if n!=None:
                new_n.next=n.next
                n.next=new_n



    def addend(self,data):
        new_n=Node(data)
        n=self.head
        while(n.next!=None):
            n=n.next
        n.next=new_n



    def printl(self):
        n=self.head
        while(n.next!=None):
            print(n.data,end="->")
            n=n.next

l=list(map(int,input().split()))
ll=LinkL()
for i in range(len(l)):
    if i%2==0:
        ll.addbeg(l[i])
    else:
        ll.addend(l[i])
ll.addAft(33,3)
ll.addbefo(33,4)
ll.printl()
