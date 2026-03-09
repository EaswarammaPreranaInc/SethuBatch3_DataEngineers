'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
a = input("Enter a string: ")
vowels = "AEIOUaeiou"
distinct_vowels = ""
for char in a:
    if char in vowels and char.upper() not in distinct_vowels:
        distinct_vowels += char.upper()
print('Distinct vowels:', distinct_vowels)

'''
Output:
Enter a string: RaMa RAo
Distinct vowels: AO'''

