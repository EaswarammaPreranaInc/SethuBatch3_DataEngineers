class Stack:
	def __init__(self):
		self.list=[]
	def push(self,x):
		self.list.append(x)
	def pop(self):
		if self.list==[]:
			raise ValueError
		else:
			return self.list.pop()
	def peek(self):
		if self.list==[]:
			return "no elements in list"
		else:
			return self.list[-1]
	def display(self):
		print("stack : ",self.list)
print("reverse string program")
n=input("enter string")
res=""
s=Stack()
for i in n:
	s.push(i)
while True:
	try:
		res+=s.pop()
	except :
		break
print("reversed String : ",res)

print("parnthesis Match program")
n=input("enter value : ")
open="([{"
close="})]"
brackets=["[]","{}","()"]
s1=Stack()
for i in n:
	try:
		if i in open:
			s1.push(i)
		elif i in close:
			res=s1.pop()
			if res+i in brackets:
				pass
			else:
				print("invalid")
				exit()
	except:
		print("invalid due excess ",i)
		exit()

if s1.list==[]:
	print("valid")	
else:
	print("invalid excess :",s1.list[0])
	