from  os . path  import  isfile
import  pickle
def menu():
    print('1. Print  binary  file')
    print('2. Print  ith  record  of  the  file')
    print('3. Number  of  records  in  the  file')
    print('4. Append  new  record  to  the  file')
    print('5. Exit')
class  emp:
	def  get(self):
			self.empno=int(input("enter employee Number : "))
			self.name=input("enter employee name : ")
			self.sal=int(input("enter employee salary : "))

	def  disp(self):
			print(self.empno,self.name,self.sal,sep="\t")	
# End  of  the  class
def  create(f):
	while True:
		e=emp()
		e.get()
		pickle.dump(e,f)
		ch = input('Do you want to add another record (Y/N) : ')
		if ch == 'N' or ch == 'n':
			break
def  display(f):
	f.seek(0)
	while(True):
		try:
			e=pickle.load(f)
			e.disp()
		except:
			break
		 
def  num_records(f):
	f.seek(0)
	count=0
	while(True):
		try:
			e=pickle.load(f)
			count+=1
		except:
			break
	return count

def  disp_ith_record(f , i):  
	f.seek(0)
	count=1
	while(True):
		try:
			e=pickle.load(f)
			if count==i:
				e.disp()
				return
				
		except:
			break
	print("record not found")	
def  append(f , e):
	e.get()
	pickle.dump(e,f)
	print("record appended")
# End  of  the  function

f=input("enter the filename : ")
if isfile(f):
	fe=open(f,'r+b')
else:
	fe=open(f,'w+b')
	create(fe)


while True:
	menu()
	ch = int(input('Enter choice: '))
	match  ch:
		case  1:
			display(fe)
		case  2:
			i = int(input('Enter  record  number : '))
			disp_ith_record(f,i)
		case  3:
			print('Number  of  records : ' ,num_records(fe))
		case  4:
			append(fe,emp())
		case  5:
			break


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
				


# End  of  the  class
l=sll()
l.create()
print('Number  of  nodes : ' ,l.length())
while True:
	i=eval(input("enter ith value you want: "))
	val=l.find(i)
	if val:
		print("data at ith value : ",val)
	else:
		print("no ith element")
	y=input("do you contiue (y/n) : ")
	if y=="n":
		break
	else:
		pass

while True:
	i=eval(input("search  value you want: "))
	val=l.search(i)
	if val:
		print(f"{i} found at address : {id(val)}")
	else:
		print(f"element {i} not found")
	y=input("do you contiue (y/n) : ")
	if y=="n":
		break
	else:
		pass

while True:
	i=eval(input("where you to insert want (0-at begin): "))
	x=eval(input("enter element :"))
	l.insert(i,x)
	l.display()
	y=input("do you contiue (y/n) : ")
	if y=="n":
		break
	else:
		pass


