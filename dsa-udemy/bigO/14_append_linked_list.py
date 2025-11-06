class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList:
    
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        
        temp_node = self.head
        result = str()
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
            
        return result
    
    def append(self, value):
        
        new_node = Node(value)
        
        if self.head is None:
           self.head = new_node
           self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
        
    def prepend(self, value):
        
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            # temp = self.head
            # self.head = new_node
            # new_node.next = temp
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
        
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            
        self.length += 1
        return True
    
    def traversal(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            
    def search(self, value):
        current = self.head
        index = 0
        while current:
            if value == current.value:
                return True, index
            else:
                current = current.next
                index += 1
        return False, None
    
    def get(self, index):
        current = self.head
        
        if index < 0 or index >= self.length:
            return None
        
        for i in range(index):
            current = current.next
        return current
    
    def set(self, index, new_value):
        
        temp = self.get(index)
        if temp:
            temp.value = new_value
            return True
        return False
    
    def popfirst(self):
        
        if self.length == 0:
            return None
        popped_node = self.head
        
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        
        return popped_node.value
    
    def pop(self):
        
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            
            self.tail = temp
            temp.next = None
            self.length -= 1
        
        return popped_node
    
    def remove(self, index):
        
        if index >= self.length or index < 0:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length-1 or index == -1:
            return self.pop()
    
        prev_node = self.get(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        
        self.length -= 1
        
        return popped_node.value
        
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
# new_linked_list.prepend(0)
new_linked_list.insert(0, 4)
# print(new_linked_list.head.value, new_linked_list.tail.value, new_linked_list.length)
# print(new_linked_list)
# new_linked_list.traversal()
# print(new_linked_list.search(40))
# print(new_linked_list.get(4))
# print(new_linked_list.set(3, 60))
# print(new_linked_list)
# print(new_linked_list)

# print(new_linked_list.popfirst())
# print(new_linked_list)
# print(new_linked_list.popfirst())
# print(new_linked_list.popfirst())
# print(new_linked_list.popfirst())
# print(new_linked_list)

# print(new_linked_list.pop())
# print(new_linked_list)
# print(new_linked_list.pop())
# print(new_linked_list)
# print(new_linked_list.pop())
# print(new_linked_list)
# print(new_linked_list.pop())
# print(new_linked_list)
# print(new_linked_list.pop())
# print(new_linked_list)
# print(new_linked_list.pop())
# print(new_linked_list)

print(new_linked_list)
print(new_linked_list.tail.value)
print(new_linked_list.remove(2))
print(new_linked_list)
# print(new_linked_list.remove(1))
# print(new_linked_list)
print(new_linked_list.remove(0))
print(new_linked_list)
print(new_linked_list.tail.value)
# print(new_linked_list.remove(1))
# print(new_linked_list)
# print(new_linked_list.remove(5))
# print(new_linked_list)
new_linked_list.delete_all()
print(new_linked_list)
