import  re
print(re  .  sub('-'  ,  '/'  ,  '15 - Aug - 1947'))#"15/Aug/2025"
print(re  .  sub(' '  ,  ':'  ,  '18 52 36'))#"18:52:36"
print(re  .  sub('[0-9]'  ,  '$'  ,  'a7b8c6d5'))#"a$b$c$d$"
print(re  .  sub('[a-z]'  ,  '%'  ,  'a7b8G6d5'))#$7$8$6$5
print(re  .  sub('is'  ,  'was'  ,  'Hyd is his city'))#"Hyd was his city"
print(re  .  sub('a' , 'b' , 'Rama  Rao'))#"Rbmb Rbo"
################################################################################
import  re
print(re . split(','  ,  'Hyd,Pune,Chennai,Delhi,Vijayawada'))#[Hyd,Pune,Chennai,Delhi,Vijayawada]
print(re . split('-'  ,  '15-Aug-1947'))#['15','Aug','1947']
print(re . split(':'  ,  '18:52:46'))#['18','52','4''6']
print(re . split(' '  ,  'Hyd is green city'))#['Hyd','is' ,'green', 'city']
###############################################################################
import  re
print(re . subn('[a-z]'  ,  '#'  ,  'a7G9c5D8e'))#('#7G9#5D8#', 3)
print(re  .  subn(' '   ,  ':'  ,   '18 52 46'))#('18:52:46', 2)
print(re  .  subn('-'  ,  '/'  ,  '15-Aug-1947'))#('15/Aug/1947', 2)
print(re  .  subn('is'  ,  'was'  ,  'Hyd is his city'))#('Hyd was hwas city', 2)
print(re . subn('a' , 'b' , 'Rama rao'))#('Rbmb rbo', 3)
###############################################################################
import re
print(re . split('[.]'  ,  'www.gmail.com'))#['www', 'gmail', 'com']
print(re . split('.'  ,  'www.gmail.com'))#['', '', '', '', '', '', '', '', '', '', '', '', '', '']