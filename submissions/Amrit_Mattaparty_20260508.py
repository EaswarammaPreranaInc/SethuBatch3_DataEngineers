#1
'''
Repeat prog7b such that
1) If input is number, number class objects should be added
2) If input is string, string class objects should be joined

1) Import number and string classes defined in prog7b but do no rewrite

2) Refer to prog8
'''

from prog7b import number, string

ch = input('Enter number/string : ')

if ch == 'number':
	a = [number(), number(), number()]
	a[0].get()
	a[1].get()
	a[2].add(a[0], a[1])
	a[2].display()
elif ch == 'string':
	a = [string(), string(), string()]
	a[0].get()
	a[1].get()
	a[2].add(a[0], a[1])
	a[2].display()
else:
	print('Invalid choice')



#2
#2
'''
Write a program to reverse a string using stack

1) Input: RAMA
   Output: AMAR

2) s.list = []

3) for loop
   ---------
   Iteration         s.list
   -------------------------
      1                ['R']
      2                ['R','A']
      3                ['R','A','M']
      4                ['R','A','M','A']

4) while loop
   -----------
   Iteration       s.pop()     result                         s.list
   -----------------------------------------------------------------
                                 ''
      1              'A'         ''+'A'='A'                  ['R','A','M']
      2              'M'         'A'+'M'='AM'                ['R','A']
      3              'A'         'AM'+'A'='AMA'              ['R']
      4              'R'         'AMA'+'R'='AMAR'            []

5) Hint: Reuse stack class defined in prog1b.py file but do not rewrite
'''

from prog1b import stack

s = stack()
str1 = input('Enter string : ')

for ch in str1:
	s.push(ch)

res = ''
while True:
	ch = s.pop()
	if ch is None:
		break
	res += ch

print('Reverse string : ', res)



#3
'''
Write a program to perform parentheses match

1) Is ((3 + 4) valid ? ---> No due to excess (

2) Is (3 * (4 + 5)) valid ? ---> Yes

3) Is (3 * (4 + 5))) + 6 valid ? ---> No due to excess ')'

4) Is 3 + 4 valid ? ---> Yes

5) Is ) 3 + 4 ( valid ? ---> No due to ) before (

6) What action to be made when character is '(' ? ---> Push '(' into the stack

7) What action to be made when character is ')' ? ---> Pop '(' from the stack

8) What action to be made when pop() method returns None ? ---> Print Excess ) msg and stop execution

9) What action to be made when end of the string is reached ? ---> Print valid msg when stack is empty and excess ( otherwise

10) Reuse stack class defined in prog1b.py file but do not rewrite
'''

from prog1b import stack

s = stack()
exp = input('Enter expression : ')

flag = True
for ch in exp:
	if ch == '(':
		s.push(ch)
	elif ch == ')':
		x = s.pop()
		if x is None:
			print('Invalid expression: Excess )')
			flag = False
			break

if flag:
	if s.pop() is None:
		print('Valid expression')
	else:
		print('Invalid expression: Excess (')