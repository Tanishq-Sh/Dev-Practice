class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        
        
ll1 = LinkedList(10)
print(ll1, ll1.head.value, ll1.tail.value)