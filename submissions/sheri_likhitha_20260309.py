user_input=input("Enter a string: ")
vowels="aeiouAEIOU"
v=""
for char in user_input:
    if char in vowels:
        upper_char=char.upper()
        if upper_char not in v:
            v+=upper_char
print(f"Distinct vowels: {v}")            