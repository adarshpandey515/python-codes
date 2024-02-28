class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
    
    def insertbeg(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        else:
            new_node.next=self.head
            self.head=new_node
    def insert_index(self,data,index):
        new_node=Node(data)
        curr_node=self.head
        position=0
        if position == index :
            self.insertbeg(data)
        else:
            while(curr_node!=None and position+1!=index):
                position=position+1
                curr_node=curr_node.next
            if(curr_node!=None):
                new_node.next=curr_node.next
                curr_node.next=new_node
            else:
                print("index is not present")
    def insertend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return 
        curr_node=self.head
        while(curr_node.next):
            curr_node=curr_node.next
        curr_node.next=new_node
    def updatenode(self, val , index):
        curr_node=self.head
        position=0
        if position==index:
            curr_node.data=val
        else:
            while(curr_node!=None and position!=index):
                position+=1
                curr_node=curr_node.next
            if(curr_node!=None):
                curr_node.data=val
            else:
                print("Index is Not Present ")
    
    def delstart(self):
        if(self.head==None):
            return 
        self.head=self.head.next
    def delend(self):
        if self.head is None:
            return 
        curr_node=self.head
        while(curr_node.next):
            curr_node=curr_node.next
        curr_node.next=None
