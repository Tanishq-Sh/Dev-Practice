inp_nums = []

while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    inp_nums.append(float(inp))
        
print(inp_nums)

print(sum(inp_nums)/len(inp_nums))