class Node:
    def __init__(self, value):
        self.value = value

class CSLinkedList:
    # way 1 : Circular LL with 1 element
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
        
    # way 2 : Circular LL with 0 element
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
# way 1
# cslinkedlist = CSLinkedList(10)
# print(cslinkedlist.head.value)

# way 2
cslinkedlist = CSLinkedList()
print(cslinkedlist.head)
        