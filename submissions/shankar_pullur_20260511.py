def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():
				
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
'''fname = input('Enter  filename :  ')
with open(fname , 'w') as f:
	pass
#f . close()
'''


def   create2(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		list=[]
		while  line :=  input():
			list.append(line)	
				
			f . writelines(list)
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
'''fname = input('Enter  filename :  ')
with open(fname , 'w') as f:
	create(f)
#f . close()
'''

def display(f):
	try:
		data=f.read()
		print(data)
	except :
		print("file not found")

'''fname=input("enter file name : ")
print(f"{fname} file data")
try:
	with open(fname,'r') as f:
		display(f) 
except FileNotFoundError:
	print("file not found")
'''
'''  (Home  work)
Write  a  program  to  print  file  pagewise  and  page  length = 20   lines

File
-----
Rama  Rao
9247
+-$
Hyd is green city


1) Which  method  is  used  to  read  each  line  of  the  file  ?  --->  readline()

2) Which  function  is  used  to  print  each  line ?  ---> print()

3) How  long  is  the  procedure  repeated ?  --->  Until  end  of  the  file  is  reached

4) In  which  mode  is  file  opened ?  --->  read  mode

5) How  to  pause  execution  for  every  20  lines ?  --->  os . system('pause')  where  pause  is  a  dos  command

6) How  to  clear  the  20  lines   before  printing   next  20  lines ?  ---> os . system('cls')  where  cls  is  a  dos  command
'''
import os
def display(f):
	count=0
	while True:
		try:
			count+=1
			data=f.readline()
			print(data)
			if data=="":
				break
			if count%20==0:
				os.system('pause')
				os.system('cls')
		except EOFError:
		 break

'''fname=input("enter file name1" 
" : ")

with open(fname,'r') as f:
	display(f)
'''
# copying one file data to another
def copy(f1,f2):
	while data:=f1.readline():
	     f2.write(data)
'''
try:
	file1=input("enter filename to get data : ")
	f1=open(file1,'r')
	file2=input("enter filename to copy data : ")
	if os.path.isfile(file2):
		y=input(f"do you want you want overite {file2} (y/n)")
		if y.upper()=='Y':
			f2=open(file2,'w')
			copy(f1,f2)
			print("copy completed")
		else:
			print("copy cancelled")
	else:			
		f2=open(file2,'w')
		copy(f1,f2)
		print("copy completed")
except FileNotFoundError:
	print("file not found error!! task Incomplete")
'''



def copy(f1,f2):
	while data:=f1.readline():
	     f2.write(data)
'''try:
	file1=input("enter filename to get data : ")
	f1=open(file1,'r')
	file2=input("enter filename to copy data : ")
	f2=open(file2,'a')
	copy(f1,f2)
	print("data appended successfully")
except:
	print("file not exists")

'''


class  queue:
	def  __init__(q):
		q.list=[]
		
	# q = queue()		
	def  isempty(q):
		if q.list==[]:
			return True
		else:
			return False
	# q . isempty()	
	def  enqueue(q , x):  
		q.list.append(x)
	# q . enqueue(25)		
	def  dequeue(q):
		try:
			return q.list.pop(0)
		except: 
			return None
	# q . dequeue()			
	def  first(q):
		try:
			return q.list[0]
		except:   
			return  None
	# q . first()			
	def  last(q):
		try:
			return q.list[-1]
		except:  
			return  None
	# q . last()			
	def  disp(q):
		print('Queue  :  ' ,q.list)
	# q . disp()		
	def  size(q):
		return len(q.list)
	# q . size()		
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print2  queue')
        print('4. First  element of queue')
        print('5. Last  element of queue')
        print('6. Number  of  elements  in  the  queue')
        print('7. Exit')
# End of  the  function
#How  to  create  queue  class  object
'''
s=queue()

while  True:
	menu()
	ch = int(input('Enter  choice : ' ))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					s.enqueue(x)
					
		case  2:
					
					if  v:=s.dequeue():
						print('Deleted  element  : ' ,v)
						
					else:
						print('Queue  is  empty , deletion  is  not  permitted')
							
			
		case  3:
					s.disp()
		case  4:
					
					if  v:=s.first():
							print('First  element :  ' ,V)
							
					else:
						print('Queue  is  empty')
							
		case  5:
					
					if v:=s.last():
						print('Last  element :  ' ,v )
							
					else:
							print('Queue  is  empty')
							
		case  6:
					print('Number  of  elements  :  ' , s.size())
		case  7:
					break
	# End  of  match
#  End  of  while  loop



'''
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
		return 1
	if op=='-':
		return 1
	if op=='*'or op=='/' or op=='%':
		return 2
	if op=='^':
		return 4
	if op=='(':
		return 4
		
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
		return 3
	if op=='(':
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
def  convert(infix):
	st=Stack()
	st.list.append('#')
	res=""
	
	for x in infix:
		if x in ['+', '-', '*', '/', '%', '^', '(']:
			if icp(x)>isp(st.peek()):
				st.push(x)
			else:
				while icp(x)<=isp(st.peek()):
					res+=st.pop() 
				st.push(x)
		elif x==')':
			while st.peek()!='(':
				res+=st.pop()
			st.pop()
		else:
			res+=x
	if st.size()>1:
		while st.peek()!='#':
			res+=st.pop()
	return res
		
i=input("enter infix expression")
print(convert(i))








