'''
Repeat   prog7b  such  that
1) If  input  is   number , number  class  objects  should  be  added
2) If  input  is  string , string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8
'''
# prog7b.py
from abc import *
class parent(ABC):
    @abstractmethod
    def get(self):
        pass
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def disp(self):
        pass
class number(parent):
    def get(self):
        self.x = int(input("Enter a number : "))
    def add(self,a,b):
        self.x = a.x+b.x
    def disp(self):
        print('Sum of two numbers : ',self.x)
class string(parent):
    def get(self):
        self.s = input("Enter a string : ")
    def add(self,a,b):
        self.s = a.s+b.s
    def disp(self):
        print('Join of two strings : ',self.s)
def main():
    print("1.Number")
    print("2.String")
    print("3.Exit")
if __name__ == '__main__':
    while True:
        main()
        a=[]
        ch = int(input('Enter your choice : '))
        if ch == 1:
            a = [number(),number(),number()]
        elif ch == 2:
            a = [string(),string(),string()]
        elif ch == 3:
            break
        a[0].get()
        a[1].get()
        a[2].add(a[0],a[1])
        a[2].disp()
    print('Good bye')

# Code :
from prog7b import *
while True :
	try:
		s = input("Enter number / string / exit : ")
		data = eval(s)
		a = [data(),data(),data()]
		a[0].get()
		a[1].get()
		a[2].add(a[0],a[1])
		a[2].disp()
	except:
		break
print('Good Bye')



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
	      4                  'R'          'AMA' + 'R' = 'AMAR'        []

5) Hint:  Reuse  stack  class  defined  in  prog1b.py  file  but  do  not  rewrite
'''
# Code :

from stack import *
inp = input('Enter any string : ')
s = stack()
for x in inp:
    s.push(x)
res = ''
while not s.isempty():
    res = res + s.pop()
print('Reverse of the string : ',res)



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
# Code :

from stack import *
inp = input('Enter parentheses expression : ')
s = stack()
for x in inp:
    if x == '(':
        s.push(x)
    elif x == ')':
        if s.isempty():
            print(f'Invalid : Excess \')\'')
            exit()
        else:
            s.pop()
if s.isempty():
    print('Valid : ( and ) are matching')
else:
    print(f'Invalid :  Excess \'(\'')