class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
            
        
    def __str__(self):
        temp_node = self.head
        ret_str = ''
        while temp_node:
            ret_str += str(temp_node.value)
            if temp_node.next is not None:
                ret_str += ' <-> '
            temp_node = temp_node.next
        return ret_str
    
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            
    def reverse_travere(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            
    def search(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return (True, index)
            else:
                current_node = current_node.next
                index += 1
        return (False, None)
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for i in range(self.length-1, index, -1):
                current_node = current_node.prev
        return current_node 
    
    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self, index, value):
        
        if index < 0 or index >= self.length:
            return False
        
        if index == 0:
            self.prepend(value)
            return True
        
        if index == self.length - 1:
            self.append(value)
            return True
        
        new_node = Node(value)
        
        temp_node = self.get(index-1)
            
        new_node.prev = temp_node
        new_node.next =temp_node.next
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.head is None:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = 1
            self.tail = 1
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        if self.tail is None:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if self.length == 0:
            return None
        elif index < 0 or index >= self.length:
            return None
        elif index == 0:
            popped_node = self.pop_first()
        elif index == self.length - 1:
            popped_node = self.pop()
        else:
            popped_node = self.get(index)
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.prev = None
            popped_node.next = None
            self.length -= 1
            
        return popped_node
        
            
            
                
        
DLL = DoublyLinkedList()
DLL.append(10)
DLL.append(12)
DLL.prepend(0)
DLL.prepend(2)
# print(DLL.length)
# print(DLL)
# print("===traverse===")
# DLL.traverse() 
# print("===reverse traverse===")
# DLL.reverse_travere() 
# print("===search===")
# print(DLL.search(13))
# print("===get===")
# print(DLL.get(2))
# print(DLL.get(10))
# print("===set===")
# print(DLL.set(2, 11))
# print(DLL.get(2)) 
# print("===insert===")
# print(DLL.length)
# DLL.insert(3, 1000)
# print(DLL.length)
# DLL.insert(-1, 1000)
# print(DLL)
# print("===pop_first===")
# print(DLL, DLL.length)
# print(DLL.pop_first())
# print(DLL, DLL.length)
# print(DLL.pop_first())
# print(DLL, DLL.length)
# print("===pop===")
# print(DLL.pop())
# print(DLL, DLL.length)
print("===Remove===")
print(DLL)
removed_node = DLL.remove(3)
print(DLL, f"Removed Node: {removed_node}")
        