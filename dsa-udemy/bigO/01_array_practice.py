from array import *

# Create an array and traverse

my_array = array('i', [1,2,3,4,5])

print("--- Step 1 ---")
for item in my_array:
    print(item)
    
# Access individual elements through indices
print("--- Step 2 ---")
print(my_array[2])

# Append any value to the array using append method
print("--- Step 3 ---")
my_array.append(6)
print(my_array)

# Insert value in an array using insert method
print("--- Step 4 ---")
my_array.insert(2, 7)
print(my_array)

# Extend python array using extend() method
print("--- Step 5 ---")
my_array1 = array('i', [10,11])
my_array.extend(my_array1)
print(my_array)

# Add items from list into array using fromlist() method
print("--- Step 6 ---")
templist = [20,21,22]
my_array.fromlist(templist)
print(my_array)

# Remove any array element using remove() method
print("--- Step 7 ---")
my_array.remove(20)
print(my_array)

# Remove last element from array using pop() method
print("--- Step 8 ---")
my_array.pop()
print(my_array)

# Fetch any element through its index using index() method
print("--- Step 9 ---")
print(my_array.index(21))

# Reverse a python array using reverse() method
print("--- Step 10 ---")
my_array.reverse()
print(my_array)

# Get array buffer information through buffer_info() method
print("--- Step 11 ---")
print(my_array.buffer_info())

# Check number of occurrences of an element using count() method
print("--- Step 12 ---")
print(my_array.count(3))

# Convert an array to python list using tolist() method
print("--- Step 13 ---")
print(my_array.tolist())

# Slice elements from an array
print("--- Step 14 ---")
print(my_array[1:4])





