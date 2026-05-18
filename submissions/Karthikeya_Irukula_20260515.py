 #Write  a  program  to  convert  prefix  to  postfix

class Stack:
	def __init__(self):
		self.list=[]
	def push(self,x):
		self.list.append(x)
	def pop(self):
		if self.list==[]:
			return None
			
		else:
			return self.list.pop()
			
	def peek(self):
		if self.list==[]:
			return None
		else:
			return self.list[-1]
	def display(self):
		print("stack : ",self.list)
	def size(self):
		return len(self.list)
	def isempty(self):
		if self.list==[]:
			return True
		else:
			return False

def  icp(op):
	if op=='+':
		return 2
	if op=='-':
		return 2
	if op=='*'or op=='/' or op=='%':
		return 3
	if op=='^':
		return 4
	if op==')':
		return 5
		
'''
icp('+')  --->  1
icp('/') --->  2
icp('^') --->  4
'''
def  isp(op):
		
	if op=='-' or op=='+':
		return 1
	if op=='*'or op=='/' or op=='%':
		return 2
	if op=='^':
		return 4
	if op==')':
		return 0
	if op=='#':
		return -1
	
'''
isp('-')  --->  1
isp('*')  --->  2
isp('^')  --->  3
isp('(')  --->  0
isp('#')  --->  -1
'''

# converting infix to prefix_____________________________________________________

def  convert(x):
	st=Stack()
	st.list.append('#')
	res=""
	
	for i in range(len(x)-1,-1,-1):
		if x[i] in ['+', '-', '*', '/', '%', '^', ')']:
			if icp(x[i])>isp(st.peek()):
				st.push(x[i])
			else:
				while icp(x[i])<=isp(st.peek()):
					res+=st.pop() 
				st.push(x[i])
		elif x[i]=='(':
			while st.peek()!=')':
				res+=st.pop()
			st.pop()
		else:
			res+=x[i]
	if st.size()>1:
		while st.peek()!='#':
			res+=st.pop()
	return res

i=input("enter infix :")
print(f'infix to prefix : {convert(i)}')

# postfix evaluation______________________________________________________________________
def evaluation(pf):
	b=Stack()
	for i in pf:
		if i.isdigit():
			b.push(int(i))
		else:
			op2=b.pop()
			op1=b.pop()
			if i=='+':
				res=op1+op2
				b.push(res)
			elif i=='-':
				res=op1-op2
				b.push(res)
			elif i=='*':
				res=op1*op2
				b.push(res)
			elif i=='^':
				res=op1**op2
				b.push(res)
			elif i=='/':
				res=op1/op2
				b.push(res)
			elif i=='%':
				res=op1%op2
				b.push(res)
	return b.pop()	
		

def pretopos(pre):
	pre=pre[::-1]
	s=Stack()
	for x in pre:
		if x.isalnum():
			s.push(x)
		else:
			op1=s.pop()
			op2=s.pop()
			s.push(op1+op2+x)
	return s.pop()
			
i=input("enter infix expression")
prefix=convert(i)
post=pretopos(prefix)
print(post)