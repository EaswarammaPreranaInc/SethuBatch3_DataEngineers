 # sub()  function  demo  program (Home  work)
import  re
print(re  .  sub('-'  ,  '/'  ,  '15 - Aug - 1947'))
print(re  .  sub(' '  ,  ':'  ,  '18 52 36'))
print(re  .  sub('[0-9]'  ,  '$'  ,  'a7b8c6d5'))
print(re  .  sub('[a-z]'  ,  '%'  ,  'a7b8G6d5'))
print(re  .  sub('is'  ,  'was'  ,  'Hyd is his city'))
print(re  .  sub('a' , 'b' , 'Rama  Rao'))

'''
Output:
15 / Aug / 1947
18:52:36
a$b$c$d$
%7%8G6%5
Hyd was his city
Rbm b Rbbo
'''

 #  subn()  finction  demo  program  (Home  work)
import  re
print(re . subn('[a-z]'  ,  '#'  ,  'a7G9c5D8e'))
print(re  .  subn(' '   ,  ':'  ,   '18 52 46'))
print(re  .  subn('-'  ,  '/'  ,  '15-Aug-1947'))
print(re  .  subn('is'  ,  'was'  ,  'Hyd is his city'))
print(re . subn('a' , 'b' , 'Rama rao'))

'''
Output:
('#7G9#5D8#', 4)
('18:52:46', 2)
('15/Aug/1947', 2)
('Hyd was his city', 1)
('Rbm b rbo', 3)
'''

#  split()  function  demo  program  (Home  work)
import  re
print(re . split(','  ,  'Hyd,Pune,Chennai,Delhi,Vijayawada'))
print(re . split('-'  ,  '15-Aug-1947'))
print(re . split(':'  ,  '18:52:46'))
print(re . split(' '  ,  'Hyd is green city'))

'''
Output:
['Hyd', 'Pune', 'Chennai', 'Delhi', 'Vijayawada']
['15', 'Aug', '1947']
['18', '52', '46']
['Hyd', 'is', 'green', 'city']
'''

# Find  outputs
import re
print(re . split('[.]'  ,  'www.gmail.com'))
print(re . split('.'  ,  'www.gmail.com'))

'''
Output:
['www', 'gmail', 'com']
['www', 'gmail', 'com']
'''