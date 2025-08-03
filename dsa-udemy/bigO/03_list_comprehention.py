prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list = [num ** 2 for num in prev_list if num < 0]
print(new_list)


sentence = 'My name is Tanishq'

def is_consonent(letter):
    vowel = 'aeiou'
    if letter.isalpha() and letter not in vowel:
        return True
    return False

new_sentence = [letter for letter in sentence if is_consonent(letter)]

print(new_sentence)


prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list = [num if num > 0 else 0 for num in prev_list]
print(new_list)
