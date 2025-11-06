my_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six'
}

my_dict2 = {
    0: 'zero',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six'
}

my_dict3 = {
    False: 'False',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six'
}

my_dict4 = {
    'False': False,
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six'
}

my_dict5 = {
    False: 'False',
    0: 'Zero'
}

# len function will return total num of key-value pairs
print(len(my_dict))

# all function
print(all(my_dict2)) # returns false if any key is zero
print(all(my_dict3)) # returns false if any key is false
print(all(my_dict4)) # returns true if all keys are not 0 or False even if a value is False

print("---\n")
# any function
print(any(my_dict2)) # returns true if any key is non-zero
print(any(my_dict3)) # returns true if any key is not-false
print(any(my_dict5)) # returns false if all the keys are zero/False

# sorted function
print(sorted(my_dict)) # returns sorted keys()