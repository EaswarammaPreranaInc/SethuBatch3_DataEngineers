# Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set
s=input()
b=''
n=''
for ch in s:
    if ch.lower() in 'aeiou':
        b+=ch
for x in b:
    if x not in n:
        n+=x
print(n)



