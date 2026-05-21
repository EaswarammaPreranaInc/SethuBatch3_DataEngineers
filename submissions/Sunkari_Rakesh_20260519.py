# Identify  Error  (Home  work)
'''try:
	print('Hyd')
	print('Sec')
	print('Cyb')
     no expect block
    '''


#print(7 / 0)   # error
try:
	print(7 / 0)  
except  ZeroDivisionError:
	print('Division  by  zero  is  not  permitted')
#print(7 / 0)   # error
print('Bye')
'''
output:
Division  by  zero  is  not  permitted
Bye


'''

try:
        print('One')
        print('Two')
        print('Three')
#print('Four') indentation error
except:
		print('Five')
		print('Six')
		print('Seven')
print('Eight')

'''
one
two
Three
Eight
'''

try:
	print('try suite')
except:
	print('1st  default  except')
#except:
#	print('2nd  default  except') there can be only one except block


#print(int('10.8')) value Error 
#print(float('Ten')) value
#print(complex('True')) value 
print(bool('Ten'))   #True 
print(bool('')) # False
print(float('10.8')) # 10.8
print(float('25'))   # 25.0
print(int(10.8))     #10
#print(math.sqrt(-25)) # name error


from linkedList import *
class  sll(linked_list):
	def __init__(self):
		super().__init__()  
	def  length(a):
			count=0
			if a.first==None:
				return 0
			else:
				p=a.first
				while p:
					p=p.link
					count+=1
			return count
	def  find(a , i):
		if a.first==None:
			return None
		p=a.first
		count=1
		while p:
			if count==i:
				return p.data
			p=p.link
			count+=1
		
		return None
	def search(a,x):
		if a.first==None:
			print("linkedList is EMPTY")
		else:
			p=a.first
			while p:
				if p.data==x:
					return p
				p=p.link
			return None
	def insert(a,i,x):
		if i>a.length()+1:
			print("invalid ith element")
		elif i==0:
			new =node(x)
			new.link=a.first
			a.first=new
		else:
			p=a.first
			count=1
			while p.link!=None:
				if count==i:
					break
				p=p.link
			new =node(x)
			new.link=p.link
			p.link=new
	def  delete(a , i):
		if   i<1 or i>a.length():
			print("invalid node number")
		elif  i==1:
			x=a.first.data
			a.first=a.first.link
			return x
			#return a.first
		else:  
			count=1
			prev=None
			p=a.first
			while count < i:
				prev = p
				p = p.link
				count += 1
			
			
			prev.link=p.link
			return p.data
			
			#return a.first
	def copy(a):
		b=sll()
		b.create()
		p=a.first
		while p.link!=None:
			p=p.link
		p.link=b.first
	def __del__(a):
		p=a.first
		while p:
			data=p
			p=p.link
			
			del data
	def reverse(a):
		prev = None
		curr = a.first

		while curr:
			next = curr.link
			curr.link = prev
			prev = curr
			curr = next
		a.first = prev 

l=sll()
l.create()
l.display()
l.copy()        # copy method
l.display()     #
while  True:
	i = int(input('Enter  value  of  i  :  '))
	val=l.delete(i) 
	if   val==None:
			print(F'Node  {i}  does  not  exist')
	else:
			print('Data  of  deleted  node  is  ' ,  val)
			l.display()
	ch = input('Would  you  like  to  delete  another  node (Y  or   N) ?  :  ')
	if  ch == 'n'  or  ch == 'N':
		break




#Find  outputs (Home  work)
from  threading  import  Thread
def    f1():
	for  i  in  range(10):
		print('child  thread')
new = Thread(target = f1)
f1()
for  i  in  range(10):
        print('main  thread')
'''
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread
main  thread



'''

# Find  outputs  (Home  work)

def   f1():
        for  i  in  range(10):
                print('child  thread',i)
child = Thread()
child . start()
for  i   in   range(10):
        print('main  thread',i)

'''
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
main  thread
main  thread
main  thread
main  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread
child  thread

main  thread



'''


# Find  outputs (Home  work)

def    f1():
        for  i  in  range(10):
                print('Child  Thread')
child = Thread(target = f1)
child . start()
for  i  in  range(10):
        print('Main  Thread')
#child . start() error 


def reverse(a):
	next=a.first
	curr=prev=None
	while next:
		curr=next
		next=next.link
		curr.next=prev
		prev=curr.link
		curr=next
	curr.next=a.first


