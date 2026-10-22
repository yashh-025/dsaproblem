# stack implement  using linked list
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self,new_node): 
        new_node.next=self.top
        top=new_node 
    def print(self):
        if self.isempty():
           print("stack is empty...")
        else: 
            print("stack contains..")   
            temp=self.top
            while temp:
                st1.push(Node(temp.data))
                temp=temp.next  
st=stack()
st1=stack()
st.push(Node(10))         
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))

st.print()








        