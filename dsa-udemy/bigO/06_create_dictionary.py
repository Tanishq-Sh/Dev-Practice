my_dict = {}
my_dict2 = dict()

print(my_dict)
print(my_dict2)

# creating dictionary using dictionary constructor
eng_sp = dict(one='uno',two='dos',three='tres')
print(eng_sp)

# creating dictionary using curly braces
eng_sp2 = {
    'one':'uno',
    'two':'dos',
    'three':'tres'
}
print(eng_sp2)

# creating dictionary using list of tuples
eng_sp_tup = [('one','uno'),('two','dos'),('three','tres')]
eng_sp3 = dict(eng_sp_tup)
print(eng_sp3)