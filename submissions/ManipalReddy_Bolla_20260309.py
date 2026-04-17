x=input("Enter any mixed case string : ").upper()
vowel='AEIOU'
found=''
for i in x:
    if i in vowel and i not in found:
        found+=i
print("Distinct Vowels : ",found)