my_dict = {
    'name': 'Rose',
    'age': 28,
    'address': 'London'
}

def traverse_dict(detail_dict):
    
    for key in detail_dict:
        print(key, detail_dict[key])
        
traverse_dict(my_dict)