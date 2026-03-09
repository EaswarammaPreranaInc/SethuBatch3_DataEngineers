s1 = input("Enter any mixed string:  ")
result = ""

for ch in s1:
    if ch in "AEIOU"  and ch not in result:
       result  = result + ch
print(f'Distinct vowels:   {result}')  