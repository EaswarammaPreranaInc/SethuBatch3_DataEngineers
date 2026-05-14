# '''
# Repeat   prog7b  such  that
# 1) If  input  is   number , number  class  objects  should  be  added
# 2) If  input  is  string , string  class  objects  should  be  joined
# 1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

# 2) Refer  to  prog8
# '''
from yerrolla_kalyani_20260507 import *
while True:
	try:
		obj_name=input("enter class name(number/string/exit):")
		classname=eval(obj_name)
		if classname==number:
			a=[number(),number(),number()]
			a[0].get()
			a[1].get()
			a[2].add(a[0],a[1])
			a[2].display()
		elif classname==string:
			a=[string(),string(),string()]
			a[0].get()
			a[1].get()
			a[2].add(a[0],a[1])
			a[2].display()
		elif classname==exit:
			break
		print("Good Bye")
	except:
		print("enter only (number/string/exit):")


		

	

'''
Write  a  program  to  reverse  a  string  using  stack
1) Input:  RAMA
    Output :  AMAR
2) s . list = []
3) for loop
    ---------
	Iteration         s . list
	-------------------------
	      1                ['R']       
	      2                ['R' , 'A']       
	      3                ['R' , 'A' , 'M']       
	      4                ['R' , 'A' , 'M' , 'A']       
4) whie loop
	-----------
    Iteration       s . pop()     result                                   s . list
	---------------------------------------------- ---------------------------------
	                                          ''
	      1                  'A'           '' + 'A' = 'A'                       ['R' , 'A' , 'M']
	      2                  'M'          'A' + 'M' = 'AM'                 ['R' , 'A' ]
	      3                  'A'          'AM' + 'A' = 'AMA'            ['R']
	      4                  'R'          'AMA' + 'R' = 'AMAR'        []==
5) Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''

from stack import *
result=""		#to store in reverse order we need an empty string 
s=stack()
string=input("Enter a string:")			# How  to  read  the  string
for x in string:
	s.push(x)# How  to  push  each  char  of  the  string  into  the  stack
	
while s.list:
	poped_element=s.pop()      # How  to  remove   each  char  of  stack  and   concatenate  to  the  result
	result+=poped_element       #How  to  remove   each  char  of  stack  and   concatenate  to  the  result
print('Reverse  string : '  ,result)




'''
Write  a  program  to  perform  parentheses  match
1) Is  ((3 + 4)  valid ?  --->  No  due  to  excess  (
2) Is  (3 * (4 + 5))  valid ?  --->  Yes
3) Is  (3 * (4 + 5))) + 6 valid ? ---> No  due  to  excess  ')'
4) Is  3 + 4  valid ? --->  Yes
5) Is  ) 3 + 4 (  valid ?  --->  No  due  to  )  before  (
6) What  action  to  be  made  when  character  is   '(' ?  --->  Push  '('  into  the  stack
7) What  action  to  be  made  when  character  is   ')' ?  ---> Pop  '('  from  the  stack
8) What  action  to  be  made  when  pop()  method  returns   None ?  --->  Print  Excess  )  msg  and  stop  execution
9) What  action  to  be  made  when  end  of   the  string   is  reached ? --->																					
																					Print  valid  msg  when  stack  is   empty  and  excess   (  otherwise
10) Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
from stack import stack
s=stack()
expression=input("enter the expression:")			# How  to  read  the  expression  with  ()
try:
	for x in expression:# How  to  validate  the  expression  and  print  valid / invalid  msg
		if x=="(":
			s.push(x)
		elif x==")":
			s.pop()
except IndexError:
		print(" Excess  ')'  p   Invalid execution")
else :

	if s.list==[]:   
		print("number of '(' and ')' are same i.e.,expression valid")	# How  to  validate  the  expression  and  print  valid / invalid  msg
	else:
		print("number of '(' are excess i.e.,expression Invalid")

