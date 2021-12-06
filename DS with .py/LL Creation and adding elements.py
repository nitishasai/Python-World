class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #node class 

class LinkL:
    def __init__(self):
        self.head=None #ll class


    def addbeg(self, data):
        new_n = Node(data)
        if self.head is None:
            self.head = new_n
            return
        new_n.next = self.head
        self.head = new_n


    def addAft(self,data,x):
        new_n= Node(data)
        n=self.head
        if n is None:
            self.head = new_n
            return
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
        if n is None:
            self.head = new_n
            return
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
        if n is None:
            self.head = new_n
            return
        while(n.next!=None):
            n=n.next
        n.next=new_n



    def printl(self):
        n=self.head
        while(n!=None):
            print(n.data,end=" ")
            n=n.next

l=list(map(int,input().split()))
ll=LinkL()
ll.addbefo(3333,2)
ll.addAft(333,3)

for i in range(len(l)):
        ll.addbeg(l[i])
ll.printl()
