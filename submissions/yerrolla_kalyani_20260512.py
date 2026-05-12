# Write  a  program  to  implement  queue  using  list
class  queue:
	def  __init__(q):
		q.list=[] #How  to  initialize  queue  with  an  empty  list
	# q = queue()		
	def  isempty(q):
		return  q.list==[] #True  when  list  held  by  queue  is  empty  and  False  otherwise
	# q . isempty()	
	def  enqueue(q , x):  
		q.list.append(x) #How  to  append  'x'  to  the  list  held  by  object  'q'
	# q . enqueue(25)		
	def  dequeue(q):
		try:
			x=q.list.pop()
			return x #How  to  remove  first  element  of  the  list  held  by  object  'q'  and  returns  the  deleted  element
		except: 
			return  None
	# q . dequeue()			
	def  first(q):
		try:
			e=q.list[0]
			return e #How  to  return  first  element  of  the  list  held  by  object  'q'
		except:   
			return  None
	# q . first()			
	def  last(q):
		try:
			e=q.list[-1]
			return e # How  to  return  last  element  of  the  list  held  by  object  'q'
		except:  
			return  None
	# q . last()			
	def  disp(q):
		print('Queue  :  ' ,  q.list )#How  to  print  the  list  held  by  object  'q')
	# q . disp()		
	def  size(q):
		return  len(q.list) #number   of  elements  in   the  list  held  by  object  'q'
	# q . size()		
# End  of  the  class
def  menu():
        print('1. Insertion')
        print('2. Deletion')
        print('3. Print  queue')
        print('4. First  element of queue')
        print('5. Last  element of queue')
        print('6. Number  of  elements  in  the  queue')
        print('7. Exit')
# End of  the  function
q=queue() #How  to  create  queue  class  object
while  True:
	menu()
	ch = int(input('Enter  choice : ' ))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					q.enqueue(x) #How  to  insert  'x'  into  the  queue
					q.disp() #How  to  print  the  queue
		case  2:
					q.dequeue() #How  to  remove  element  of  the  queue
					if  q.isempty():
						print('Queue  is  empty , deletion  is  not  permitted')
					else:
							print('Deleted  element  : ' , q.isempty())
					q.disp()
		case  3:
					q.disp() #How  to  print  the  queue
		case  4:
					f=q.first() #How  to  obtain  first  element  of  the  queue
					if  f:
							print('Queue  is  empty')
					else:
							print('First  element :  ' , f)
		case  5:
					e=q.last() #How  to  obtain  last  element  of  the  queue
					if  e:
							print('Queue  is  empty')
					else:
							print('Last  element :  ' , e)
		case  6:
					print('Number  of  elements  :  ' ,  q.size())
		case  7:
					exit()
	# End  of  match
#  End  of  while  loop

# Write  a  program  to  implement  deque  using  list
class  deque:
	def __init__(dq):
		dq.list=[] #How  to  initialize  deque  with  an  empty  list
	#  dq = deque()		
	def isempty(dq):
		return  dq.list==[] #True  when  deque  is  empty  and  False  otherwise
	# dq . isempty()
	def ins_rear(dq , x):
			dq.list.append(x) #How  to  append  'x'  to  the  list  held  by  object  dq
	# dq . insrear(x)			
	def  ins_front(dq , x):
			dq.list.insert(0,x) #How  to  insert  'x'  at  the  begining  of  the  list  held  by   object  dq
	# dq . insfront(x)						
	def  del_front(dq):
			try:
				x=dq.list.pop(0)
				return x #How  to  remove  left  most  element  of  the  list  held  by  object  dq  and  returns  the  deleted  element
			except: 
				return  None
	# dq . delfront()										
	def  del_rear(dq):
			try:
				x=dq.list.pop()
				return x #How  to  remove  right  most  element  of  the  list  held  by  object  dq  and  returns  the  deleted  element
			except:  
				return  None
	def  disp(dq):
			print('Deque :  ' ,  dq.list) #How  to  print  the  list   held  by  object  dq
	# dq . disp()			
	def  size(dq):
			return  len(dq.list) #number  of  elements  in  the  list  held  by  object  dq
	# dq . size()			
	def  leftmost(dq):
			try:
				return  dq.list[0] #left  most  element  of  the  list  held  by  object  dq
			except: 
				return   None
	# dq . leftmost()
	def  rightmost(dq):
			try:
				return  dq.list[-1] #right  most  element  of  the  list  held  by  object  dq
			except: 
				return   None
	# dq . rightmost()				
#End of the class
def  menu():
	print('1. Insert  element  at  the  end  of  deque')
	print('2. Insert  element  at  the  begining  of  deque')
	print('3. Delete  left  most  element')
	print('4. Delete  right  most  element')
	print('5. Print  Deque')
	print('6. Print  left  most  element')
	print('7. Print  right  most  element')
	print('8. Number  of  elements  in  deque')
	print('9. Exit')
#end of  the  function
dq=deque() #How  to  create  deque  class  object
while  True:
	menu()
	ch = int(input('Enter Choice :   '))
	match  ch:
		case  1:
					x = eval(input('Enter  element  to  be  inserted : '))
					dq.ins_rear(x) #How  to  insert  'x'  at  the  end  of  deque
					dq.disp() #How  to  print  deque
		case  2:
					x = eval(input('Enter  element  to  be  inserted : '))
					dq.ins_front(x) #How  to  insert  'x'  at  the  begining  of  deque
					dq.disp() #How  to  print  deque
		case  3:
					d=dq.del_front() #How  to   remove  left  most  element  of  deque
					if  dq.isempty():
						print('Deque  is  empty  ,  deletion  is  not  permitted')
					else:
						print('Deleted  element :  ' , d)
					dq.disp() #How  to  print  deque
		case  4:
					d=dq.del_rear() #How  to   remove  right  most  element  of  deque
					if  dq.isempty():
						print('Deque  is  empty  ,  deletion  is  not  permitted')
					else:
						print('Deleted  element :  ' , d)
					dq.disp() #How  to  print  deque
		case  5:
					dq.disp() #How  to  print  deque
		case  6:
					l=dq.leftmost() #How  to  obtain  left  most  element  of  deque
					if  dq.isempty():
						print('Deque  is  empty')
					else:
						print('Leftmost  element :  ' , l)
		case  7:
					r=dq.rightmost() #How  to  obtain  right  most  element  of  deque
					if  dq.isempty():
						print('Deque  is  empty')
					else:
						print('Rightmost  element :  ' , r)
		case  8:
					print('Number  of  elements   :  ' , len(dq.list))
		case  9:
					exit()
	# End  of  match
# End  of  while  loop

def  icp(operator):
	if operator in ('+', '-'):
		return 1
	elif operator in ('*', '/'):
		return 2
	elif operator == '^':
		return 4
def isp(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    elif operator == '^':
        return 3
    elif operator == '(':
        return 0
    elif operator == '#':
        return -1
def  convert(infix):
	s.list.append('#') #How  to  push  '#'  into  the  stack
	postfix = '' 
	for ch in infix: #How  to  iterate  thru  infix  expression
		if  ch.isalnum():
			postfix+=ch #How  to  concatenate  the  operand  to  postfix  expression
		elif  ch==')':
			while stack[-1] != '(':
				postfix += s.pop() #Remove  each  operator  of  the  stack  and  concatenate  to  postfix  expression  and
			#repeat  this  process  until  '('  is  the  last  element  of  stack.
			s.pop() #Remove  '('  also  but  do  not  concatenate  to  postfix  expression
		else:
			while icp(ch)>isp(s.list[-1]): #Remove  each  operator  of  the  stack  and  concatenate  to  postfix  expression  and
				postfix+=s.pop()#repeat  this  process  until  icp > isp.
			s.push() #Push  the  operator  into  the  stack  as  soon  as   icp  >  isp
	#  End  of  for  loop
	while s.list[-1] != '#': #Remove  each  operator  of  the  stack  and  concatenate  to  postfix  expression  and  
		postfix+=s.pop() #repeat  '#'  is  the  last  element  of  stack
	return postfix #Finally  return  postfix  expression
#  End  of  the  function
infix=input("Enter Infix expression : ") #How  to  read  infix  expression
postfix=convert(infix) #How  to  convert  infix  expression  to  postfix  expression
print('Postfix  expression :  ' ,postfix )








from prog1a import stack
def  eval(postfix):
	for ch in postfix: #How  to  iterate  thru  postfix  expression
		if  ch.isdigit():
				s.push(int(ch)) #Convert  the  operand  to  integer  and  push  into  the  stack
		else:  
				y=s.pop() 
				x=s.pop()#How  to  remove  2  operands  from  the  stack,  perform  the  operation  on  the  deleted  operands
				s.push(x+y) #and  push  the  result  into  the  stack		
	# End  of  for  loop				
	return  s.list[0]
#  End  of  the  function
infix=input("Enter Infix : ") #How  to  read  infix  expression
s=stack() 
postfix=convert(infix)#How  to  convert  infix  to  postfix
print('Result : ' ,  eval(postfix))


def  convert(rev_infix):  #  Modify  the  function  to  convert  infix  to  prefix
	s = stack()  
	s . push('#') 
	prefix = ''  
	for  ch  in  rev_infix: 
		if  ch . isalnum():  
			prefix +=  ch  
		elif  ch == '(':
			while  s . peek()  !=  ')': 
					prefix  += s . pop()  
			s . pop() 
		else:
			while  icp(ch) <= isp(s . peek()):  
				prefix += s . pop()  
			s . push(ch)  
	#  End  of  for  loop
	while  s . peek() !=  '#':  
			prefix += s . pop() 
	return  prefix[::-1]
#  End  of  the  function
infix = input('Enter  infix  expression  :  ') 
rev_infix=infix[::-1]
prefix = convert(rev_infix)  
print('Postfix  expression :  ' , prefix)