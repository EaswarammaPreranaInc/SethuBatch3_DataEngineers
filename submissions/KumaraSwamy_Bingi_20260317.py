def group_by_first_letter(data):
    b = []
    for word in data:
        if word[0] not in b:
            b.append(word[0])
            
    c = []
    for char in b:
        d = [word for word in data if word.startswith(char)]
        c.append(d)
        
    return c

input_list = ['Swathi', 'Anand', 'Srinivas', 'Zebra', 'King', 'Amar']
print(group_by_first_letter(input_list))
