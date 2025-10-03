class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return str(self.val)
        
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
            
        self.length += 1
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.val)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result
    
    def prepend(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
        
    def insert(self, pos, val):
        new_node = Node(val)
        if pos > self.length or pos < 0:
            raise Exception("Index out of range")
        if pos == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif pos == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:    
            temp_node = self.head
            for _ in range(pos-1):
                temp_node = temp_node.next
                
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        
    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.val)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            
    def search(self, target):
        temp_node = self.head
        while temp_node:
            if temp_node.val == target:
                return True
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return False
    
    def get(self, index):
        if index == -1:
            return self.tail
        if index >= self.length or index < -1:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, new_val):
        node = self.get(index)
        if node:
            node.val = new_val
            return True
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        prev = self.get(index-1)
        popped_node = prev.next
        prev.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
        
        
cslinkedlist = CSLinkedList()
print(cslinkedlist.head, cslinkedlist.length)

cslinkedlist.append(10)
print(cslinkedlist.tail.val, cslinkedlist.length)
cslinkedlist.append(20)
print(cslinkedlist.tail.val, cslinkedlist.length)
cslinkedlist.append(3)
print(cslinkedlist.tail.val, cslinkedlist.length)

cslinkedlist.prepend(0)
cslinkedlist.prepend(-1)
print(cslinkedlist.tail.val, cslinkedlist.length)

cslinkedlist.insert(3, -3)
cslinkedlist.insert(0, -10)
cslinkedlist.insert(7, -30)

# out of range
# cslinkedlist.insert(10, -30)

print("===========")
print(f"final length {cslinkedlist.length}")
print(cslinkedlist.tail.val)

print(cslinkedlist)

# traverse
print("===========")
print("Traversing..")
print(cslinkedlist.traverse())

# search
print("===========")
print("Searching..")
print(cslinkedlist.search(-30))
print(cslinkedlist.search(-40))

# get
print("===========")
print("Getting..")
print(cslinkedlist.get(5))
print(cslinkedlist.get(-1))

# set
print("===========")
print("Setting..")
print(cslinkedlist.set_value(2, 50))
print(cslinkedlist)

# pop_first
print("===========")
print("Popping first..")
popped_node = cslinkedlist.pop_first()
print(f"popped node : {popped_node}")
print(cslinkedlist)

# pop_first
print("===========")
print("Popping..")
popped_node = cslinkedlist.pop()
print(f"popped node : {popped_node}")
print(cslinkedlist)

# remove
print("===========")
print("remove..")
popped_node = cslinkedlist.remove(1)
print(f"popped node : {popped_node}")
print(cslinkedlist)

# delete_all
print("===========")
print("deleting all..")
cslinkedlist.delete_all()
print(cslinkedlist)


