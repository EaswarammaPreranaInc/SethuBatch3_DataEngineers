'''
prog7b:
#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects
from  abc  import  abstractmethod , ABC
class   datatype(ABC):  #  It  is  an  interface  as  every  method  in  the  class  is  abstract
	@abstractmethod
	def  get(self):
		pass
	@abstractmethod
	def  add(self , m ,  n):
		pass
	@abstractmethod
	def  display(self):
		pass
class   number(datatype):
	def  get(self):
			self . x = eval(input('Enter a number: ')) #  Adds  variable  'x'  to  object  self   with  user  input
	def  add(self , m , n):  #  self  is  object  a[2] ,  'm'  is  object  a[0]  and  'n'  is  object  a[1]
	    self . x = m . x + n . x  #  Adds  variable  'x'  to  object  self   with  the  sum  result
	def  display(self):
		print('Sum : ' , self . x) #  Prints  variable  'x'  of object  self
class   string(datatype):
	def  get(self):
		 self . x = input('Enter a string: ')  #  Adds  variable  'x'  to  object  self   with  user  input
	def  add(self , m , n):   #  self  is  object  a[2] ,  'm'  is  object  a[0]  and  'n'  is  object  a[1]
	     self . x = m . x + n . x  #  Adds  variable  'x'  to  object  self   with  the  join  result
	def  display(self):
		 print('Join : ' , self . x)  #  Prints  variable  'x'  of object  self
def   menu():
	print('1. Add  numbers')
	print('2. Join  Strings')
	print('3. Exit')
# End  of  the  function
if  __name__  ==  '__main__':
	while  True:
		menu()
		ch =  eval(input('Enter choice : '))
		if   ch == 1:
				a = [number() , number() , number()] #   List  of  3  number  class  objects
		elif  ch == 2:
				a = [string() , string() , string()] #  List  of  3  string  class  objects
		else:
				break   #  Moves  out  of  loop
		#  End  of  if  statement				
		a[0] . get() #  Reads  input  into  first  object  a[0]
		a[1] . get() #  Reads  input  into  2nd  object  a[1]
		a[2] . add(a[0] , a[1]) #   Adds  (or)  joins  the  two  objects  a[0]  and  a[1]  and  stores  the  result  in  3rd  object  a[2]
		a[2] . display() #  Prints  3rd  object  a[2]
	# end of  while  loop
	print('Good  Bye')
'''
'''
Repeat   prog7b  such  that
1) If  input  is   number , number  class  objects  should  be  added
2) If  input  is  string , string  class  objects  should  be  joined
3) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite
4) Refer  to  prog8
Sample output:
Enter number / string / exit : string
Enter any string : Hyder
Enter any string : abad
Join of the two strings : Hyderabad

Enter number / string / exit : number
Enter number : 10
Enter number : 20
Sum of the numbers : 30

Enter number / string / exit : exit
Good Bye
'''
from prog7b import number, string
while True:
    ch = input('Enter number / string / exit : ')
    if ch == 'number':
        a = [number(), number(), number()]   
    elif ch == 'string':
        a = [string(), string(), string()]   
    elif ch == 'exit':
        print('Good Bye')
        break
    else:
        print('Invalid Input')
        continue
    a[0].get()                 
    a[1].get()                 
    a[2].add(a[0], a[1])       
    a[2].display()            
    print()

'''
prog1b:
class  stack:
	def  __init__(s):  # 's'  is  stack  class  object
		s . list = []  #  Adds  variable  list  to  object  's'  with  an  empty  list
	# s = stack()		
	def  isempty(s):  # 's'  is  stack  class  object
		return  s . list == []   #  True  when  s . list  is  empty  and  False  otherwise
	def  push(s , x):  # 's'  is  stack  class  object  and  'x'  is  element  to  be  inserted  into  the  stack
		s . list . append(x)  #  Appends  'x'  to  the  list  held  by  object  's'
	def  pop(s):  # 's'  is  stack  class  object
		try:
			return  s . list . pop()  #  Removes  last  element  of  the  list  held  by  object  's'
		except: #  Executed  when  s . list  is  empty
			return  None
	# How  to  call  pop()  method ?  --->  x = s . pop()  --->  Deleted  element / None	
	def  peek(s):  # 's'  is  stack  class  object
		try:
			return  s . list[-1]  #   Last  element  of  the  list  held  by  object  's'
		except: #  Executed  when  s . list  is  empty
			return  None	
	def  disp(s):
		print('Stack :  ' ,  s . list)
	#  How  to  call  disp()  method ?  --->  s . disp()
	def   size(s):
		return  len(s . list)  #  Number  of  elements  in  the  list  held  by  object  's'
	# How  to  call  size()  method ?  --->  s . size()
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  Stack')
        print('4. Last  element of stack')
        print('5. Number  of  elements  in  the  stack')
        print('6. Exit')
# End of  the  function
if  __name__ == '__main__':
	s = stack()  #  Executes  constructor  of  stack  class
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
					x = eval(input('Enter  element  to  be  inserted : '))  #  'Hyd'
					s . push(x)  #  Inserts  'x'  into  the  stack
					s . disp()  #  Prints  stack
			case  2:
					x = s . pop()  # Removes  last  element  of  the  stack
					if  x == None:
							print('Stack  is  empty  , deletion  is  not  permitted')
					else:
							print('Deleted  element : '  ,  x)
					s . disp()  #  Prints  stack
			case  3:
					s . disp()  #  Prints  stack
			case  4:
					x = s . peek()  # Returns  last  element  of  the  stack
					if  x == None:
							print('Stack  is  empty')
					else:
							print('Last  element :  ' ,  x)
			case  5:
					print('Number  of  elements  :  ' ,  s . size())
			case  6: 
					exit()   #  Stops  execution
		# End  of  match
	# End  of  while  loop
# object  's'  --->   list = []


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
	      4                  'R'          'AMA' + 'R' = 'AMAR'        []

5) Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite

How  to  read  the  string
How  to  push  each  char  of  the  string  into  the  stack
How  to  remove   each  char  of  stack  and   concatenate  to  the  result
print('Reverse  string : '  ,  ??)
      
Sample output:
Enter any string : RAMA RAO
Reverse string : OAR AMAR
'''
from prog1b import stack
s = stack()          
str1 = input('Enter any string : ')
for ch in str1:
    s.push(ch)
result = ''
while not s.isempty():
    result = result + s.pop()
print('Reverse string : ', result)

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
How  to  read  the  expression  with  ()
How  to  validate  the  expression  and  print  valid / invalid  msg

Sample output:
Enter parentheses expression : ((3+4)
Invalid : Excess '('

Enter parentheses expression : (3*(4+5))
Valid : ( and ) are matching

Enter parentheses expression : (3*(4+5)))+6
Invalid : Excess ')'
'''
from prog1b import stack
s = stack()
exp = input('Enter parentheses expression : ')
for ch in exp:
    if ch == '(':
        s.push(ch)
    elif ch == ')':
        x = s.pop()
        if x == None:
            print("Invalid : Excess ')'")
            break
else:
    if s.isempty():
        print('Valid : ( and ) are matching')
    else:
        print("Invalid : Excess '('")