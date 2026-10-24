class Node:
    def  __init__(self, value):
        self.value=value
        self.next=None
class Lqueue:
    def __init__(self):

        self.front=self.rear=None
    def enqueue(self , new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node  
    def print(self):
        temp=self.front
        while temp:
            print(temp.value,end="->")
            temp=temp.next
que=Lqueue()
                               
que.enqueue(Node(23))
que.enqueue(Node(45))
que.enqueue(Node(56))
que.enqueue(Node(78))

que.print()