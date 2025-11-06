import numpy as np

myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
num = 0

def find_num(arr, num):
    
    for item in arr:
        if item == num:
            return True
    return False

print(find_num(myArray, num))