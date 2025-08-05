class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self,data):
        if self.top ==None:
            self.top = Node(data)
        else:
            curr = Node(data)
            curr.next = self.top
            self.top = curr
            
    def pop(self):
        curr = self.top
        self.top= self.top.next
        return curr.data
        
    def peek(self):
        if self.top ==None:
            return None
        else:
            curr = self.top
            return curr.data

    def is_empty(self):
        return self.top ==None
        
    
N = int(input())
wait_list = list( map(int, input().split())) ####5,4,1,3,2
s=Stack()

check = 1
is_nice =True
while len(wait_list) !=0:
    if check == wait_list[0]:
        del wait_list[0]
        check+=1
    else:
        while s.peek() ==check:
            s.pop()
            check+=1
        s.push(wait_list[0])
        del wait_list[0]

while s.is_empty()==0:
    if s.pop() ==check:
        check+=1
    else:
        is_nice = False
        break
        



print("Nice" if is_nice else 'Sad')
