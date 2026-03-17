words=eval(input("Enter the list: "))
seen=[]
output=[]
for word in words:
    first_char=word[0]
    if first_char not in seen:
        group=[x for x in words if x.startswith(first_char)]
        output.append(group)
        seen.append(first_char)
print(output)               