prog stack2

class  stack:
	def  __init__(s): 
		s . list = [] 
	# s = stack()		
	def  isempty(s):  
		return  s . list == [] 
	
	def  push(s , x):
		s . list . append(x) 
		
	def  pop(s): 
		try:
			return  s . list . pop() 
		except: 
			return  None
	
	
	def  peek(s):
		try:
			return  s . list[-1] 
		except: 
			return  None
		
	def  disp(s):
		print('Stack :  ' ,  s . list)

	def   size(s):
		return  len(s . list)

def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  Stack')
        print('4. Last  element of stack')
        print('5. Number  of  elements  in  the  stack')
        print('6. Exit')

if  __name__ == '__main__':
	s = stack()
	while  True:
		menu()
		ch = int(input('Enter  choice : ' ))
		match  ch:
			case  1:
					x = eval(input('Enter  element  to  be  inserted : '))  
					s . push(x) 
					s . disp()  
			case  2:
					x = s . pop() 
					if  x == None:
							print('Stack  is  empty  , deletion  is  not  permitted')
					else:
							print('Deleted  element : '  ,  x)
					s . disp()  
			case  3:
					s . disp()  
			case  4:
					x = s . peek()
					if  x == None:
							print('Stack  is  empty')
					else:
							print('Last  element :  ' ,  x)
			case  5:
					print('Number  of  elements  :  ' ,  s . size())
			case  6: 
					exit()



#1st question


from stack2 import stack
str1 =input("enter string:")
s=stack()

for i in str1:
    s.push(i)
result=""
while not s.isempty():
    result+=s.pop()
print("reverse of string is:",result)


#2nd question

from stack2 import stack
str=input("Enter the string: ")
s=stack()

for i in str:
    if i == '(':
        s.push(i)
    elif i == ')':
        if s.isempty():
            print("excess ')' brackets ")
            exit()
        else:
            s.pop()
if s.isempty():
    print("valid parentheses")  
else:
    print("excess '(' brackets")
