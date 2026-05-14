'''
Repeat   prog7b  such  that
1) If  input  is   number , number  class  objects  should  be  added
2) If  input  is  string , string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8
'''
from prog7b import Number, String

def process_input(data_list):
    result = None
    for item in data_list:
        if isinstance(item, int) or isinstance(item, float):
            # Create Number object
            obj = Number(item)
            if result is None:
                result = obj
            else:
                result = result + obj   # use overloaded + from Number class
        elif isinstance(item, str):
            # Create String object
            obj = String(item)
            if result is None:
                result = obj
            else:
                result = result + obj   # use overloaded + from String class
        else:
            print("Unsupported type:", type(item))
    return result
numbers = [10, 20, 30]
num_result = process_input(numbers)
print("Number result:", num_result)
strings = ["Hello", " ", "World"]
str_result = process_input(strings)
print("String result:", str_result)


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
# How  to  read  the  string
# How  to  push  each  char  of  the  string  into  the  stack
# How  to  remove   each  char  of  stack  and   concatenate  to  the  result
# print('Reverse  string : '  ,  ??)

class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        return None

    def is_empty(self):
        return len(self.list) == 0
def reverse_string(input_str):
    s = Stack()
    result = ""
    for ch in input_str:
        s.push(ch)
    while not s.is_empty():
        result += s.pop()
    return result
input_str = input("Enter a string: ")
reversed_str = reverse_string(input_str)
print("Reverse string:", reversed_str)


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
# How  to  read  the  expression  with  ()
# How  to  validate  the  expression  and  print  valid / invalid  msg      
class Stack:
    def __init__(self):
        self.list = []
    def push(self, item):
        self.list.append(item)
    def pop(self):
        if not self.is_empty():
            return self.list.pop()
        return None
    def is_empty(self):
        return len(self.list) == 0
def validate_parentheses(expr):
    s = Stack()
    for ch in expr:
        if ch == '(':
            s.push(ch)
        elif ch == ')':
            popped = s.pop()
            if popped is None:
                # Rule 8: Excess ')'
                print("Invalid: Excess ) found")
                return
    if s.is_empty():
        print("Valid expression")
    else:
        print("Invalid: Excess ( found")
expr = input("Enter an expression: ")
validate_parentheses(expr)
