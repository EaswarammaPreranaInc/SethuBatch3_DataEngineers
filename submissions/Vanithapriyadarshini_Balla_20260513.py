
#Write  a  function  to  return  average  of  numbers  in  the  file

def   avg(f):
	sum=0
	c=0
	for val in f:
		sum+=val
		c+=1
	return sum/c #How  to  return  average  of  numbers  in  the  file
#  End  of  the  function

fname=input("Enter file : ") #How  to  read  filename
try:
    f=open(fname,'r') #How  to  open  the  file
    f.avg() #How  to  print  average  of  numbers  in  the  file
    f.close() #How  to  close  the  file
except:
	print(f"{fname} does not exist")
	

import  os
def  copy(file):
	f3.write(file.read())#How  to  copy  data  from  file1  to  file2
#  End  of  the  function
#How  to  read  all  the  three  filenames
file1=input("Enter file1 : ")
file2=input("Enter file2 : ")
file3=input("Enter file3 : ")
if  os.path.isfile(file1) and os.path.isfile(file2):
	f1=open(file1,'r') #How  to  open  all  the  3  files
	f2=open(file2,'r')
	f3=open(file3,'w')
	copy(f1) #How  to  copy  from  file1  to  file3
	copy(f2)#How  to  copy  from  file2  to  file3
	f1.close()
	f2.close() 
	f3.close()#How  to  close  all  the  3  files
	print(F'{file1} and {file2}  are  merged  to  form  {file3}')
elif  os.path.isfile(file1):
	f1=open(file1,'r')
	f3=open(file3,'w')#How  to  open  1st  and  3rd  file
	copy(f1)#How  to  copy  from  file1  to  file3
	f1.close() #How  to  close  1st  and  3rd  files
	print(F'{file1}  is  copied  to  {file3}')
elif  os.path.isfile(file2):
	f2=open(file2,'r')
	f3=open(file3,'w') #How  to  open  2nd  and  3rd  file
	copy(f2) #How  to  copy  from  file2  to  file3
	f2.close() #How  to  close  2nd  and  3rd  files
	print(F'{file2}  is  copied  to  {file3}')
else:
	print('Both  the  files  are  not  existing')
	os.remove(file3) #How  to  delete  3rd  file
	

def  count_all(f):
	s=f.read()#How  to  read  whole  file  to  a  str  object
	a = []
	a.append(s.count("\n")) #How  to  append  number  of  lines  in  the  file  to  list  'a'
	a.append(len(s))#How  to  append  number  of  characters  in  the  file  to  list  'a'
	a.append(s.split()) #How  to  append  number  of  words  in  the  file  to  list  'a'
	a.append(s.count(' ')) #How  to  append  number  of  spaces  in  the  file  to  list  'a'
	a.append(s.append('\t')) #How  to  append  number  of  tabs  in  the  file  to  list  'a'
	a.append(s.count('.')+1) #How  to  append  number  of  sentences  in  the  file  to  list  'a'
	v=0
	c=0
	for ch in s:
		if ch in 'aeiouAEIOU':
			v+=1 
	a.append(v)
	for ch in s:
		if ch.isalpha() and (ch not in 'aeiouAEIOU'):
			c+=1
	a.append(c)
	#How  to  append  number  of  vowles  in  the  file  to  list  'a'
	#How  to  append  number  of  consonants  in  the  file  to  list  'a'
	return a #How  to  return  list
#  End  of   function
fname=input("Enter file name : ") #How  to  read  filename
f=open(fname,'r') #How  to  open  the  file
a=count_all(f) #How  to  call  count_all()  function
f.close() #How  to  close  the  file
b = ['Lines' , 'Chars' , 'Words' , 'Spaces' , 'Tabs' , 'Sentences' , 'Vowels' , 'Consonants']
for i in range(len(b)):
    print(b[i], "=", a[i]) #How  to  print  lists   'b'  and  'a'
	


#Write  a  function  to  search  for  a  word  in  the  file  and   return  number  of  times  it  is  found

def search(f ,  word):
	s=f.read()
	return s.count(word) #How  to  return  number  of  words  in  the  file
#End of  the  function
fname=input("Enter file name : ") #How  to  read  filename
try:
	f=open(fname,'r') #How  to  open  the  file
except:
    print(f"{fname} doesnot exists")
word=input("Enter word : ")
a=search(f,word) #How  to  print  number  of  times  word  is  found  in  the  file
f.close() #How  to  close  the  file


#Write  a  program  to  write  0! ,  1! , 2!, ...... n!  to  the  file
#Hint:  Use  math . factorial()  function

import  math
def  fact(f , n):
	for i in range(n+1):
		f.write(f"{i}! = {math.factorial(i)}\n")#How  to  write  i  and  i!  to  the  file  where  'i'  varies  from  0  to  n
# End  of  the  function
fname=input("Enter file : ") #How  to  read  filename
try:
	f=open(fname,'w')#How  to  open  the  file
	n=input("Enter n value : ") #How  to  read  value  of  'n'
	fact(f,n) #How  to  write  all  the  results  to  the  file
	f.close() #How  to  close  the  file
except:
	print(f"{fname} doesnot exists")
	
#  Write  functions  to  create  and  print  linked  list
class  node:
		def   __init__(self , x):  
				self . data = x   
				self . link = None  
		'''
		1) new = node(25)
		
		2) object  new  ---> 	 data = 25	 , link = None
		'''		
class  linked_list:
		def   __init__(a):
				a . first = None  
		'''
		1) a = linked_list()
		
		2) Object  'a'  --->  first = None
		'''
		def  isempty(a):
				return  a . first == None  
		# a . isempty()  --->  True / False
		def  disp(a):
				if  a . isempty():  
						print('Linked  List  is  empty')
				else:
						p = a . first
						while  p != None:
								print(p . data , end = '\t') 
								p = p . link
						print()
		# a . disp()					
		def  append(a , new):  
				if a.isempty():#How  to  append  a  node  to  empty  linked  list
					a.first=new
				else:
					p=a.first
					while p.link != None:
						p = p.link
					p.link = new #How  to  append  a  node  to  non-empty  linked  list
		# a . append(new)						
		def  create(a):
			n = int(input("How many nodes ? : "))
			for i in range(n):
				x = int(input("Enter element : "))
				new = node(x)
				a.append(new)
		# a . create()						
# End  of  the  class
a=linked_list() 
a.create()#How  to  create  linked  list
print('Linked  List  :  ' , end = '')
a.disp()#How  to  print  linked  list
