'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''


a = input("enter the strings:" )
vowels = "AEIOUaeiou"
distinct_vowels = ""    
for char in a:
    if char in vowels and char not in distinct_vowels:
        distinct_vowels += char
print("Distinct vowels in the string:", distinct_vowels)
