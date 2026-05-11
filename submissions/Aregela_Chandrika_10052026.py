'''
Repeat   prog7b  such  that
1) If  input  is   number , number  class  objects  should  be  added
2) If  input  is  string , string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8
'''



from prog7b import number, string
x = input("Enter number/string/exit : ")
if x.isdigit():
    obj1 = number(int(x))
    obj2 = number(int(x))
    obj3 = obj1 + obj2
    print("Addition =", obj3.n)
else:

    obj1 = string(x)
    obj2 = string(x)
    obj3 = obj1 + obj2
    print("Joined string =", obj3.s)
    
    
    
    
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
How  to  read  the  string
How  to  push  each  char  of  the  string  into  the  stack
How  to  remove   each  char  of  stack  and   concatenate  to  the  result
print('Reverse  string : '  ,  ??)


# Reverse string using linked list stack

class node:
    def __init__(self, x):
        self.info = x
        self.link = None

class stack:
    def __init__(self):
        self.top = None
    # Push operation
    def push(self, x):
        temp = node(x)
        temp.link = self.top
        self.top = temp
    # Pop operation
    def pop(self):
        x = self.top.info
        self.top = self.top.link
        return x
s = stack()
str1 = input("Enter string : ")
# Push each character into stack
for ch in str1:
    s.push(ch)
result = ''

# Remove each character from stack
# and concatenate to result
while s.top != None:

    result = result + s.pop()

print("Reverse string :", result)


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



# Parentheses matching using stack

class stack:
    def __init__(self):
        self.list = []
    def push(self, x):
        self.list.append(x)
    def pop(self):
        if self.list == []:
            return None
        return self.list.pop()

s = stack()
exp = input("Enter expression : ")
flag = True
for ch in exp:
    if ch == '(':
        s.push(ch)
    elif ch == ')':
        x = s.pop()
        if x == None:
            print("Invalid due to excess )")
            flag = False
            break
if flag == True:
    if s.list == []:
        print("Valid expression")
    else:
        print("Invalid due to excess (")