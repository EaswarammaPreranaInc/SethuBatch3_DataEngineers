str=input("Enter any mixed case string: ")
s1=''
s=str.upper()
for i in range(len(s)):
    if s[i] == chr(65) or s[i]==chr(69) or s[i]==chr(73) or s[i]==chr(79) or s[i]==chr(85):
        if s[i] not in s1:
            s1 += s[i]
print(' Distinct Vowels : ', s1)
