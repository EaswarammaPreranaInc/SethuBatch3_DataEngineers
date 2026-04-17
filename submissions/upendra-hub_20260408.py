'''
Repeat  prog5a  such  that  methods  are  called  in  a  different  way
1) What  are  the  two  ways  to  call  a  method ?  ---> object . method()  and  classname . method(object)
2) Reuse  triangle  class  defined  in  prog5a  but  do  not  define  triangle  class  again

How  to  create  triangle  object
How  to  call  get()  method  in  another  way
How  to  call  test()  method  in  another  way
print('Area : ',  How  to  call  area()  method  in  another  way)
print('Perimeter: ',  How  to  call  peri()  method  in  another  way)

#prog5a
import  math
class  triangle:
	def  get(self):
		self . a = eval(input('Enter  first  side  of  triangle : '))
		self . b = eval(input('Enter  second  side  of  triangle : '))
		self . c = eval(input('Enter  third  side  of triangle : '))
	def  test(self):
		 if  self . a + self . b > self . c  and  self . b + self . c > self . a  and  self . c + self . a > self . b: 
				pass  
		 else:
				print('Not  a  triangle')
				exit()  
	def  area(self):
			s = (self . a + self . b + self . c) / 2
			return   math . sqrt(s * (s - self . a) * (s - self . b) * (s - self . c))
	def  peri(self):
			return  self . a + self . b + self . c 
# End of the class
if   __name__  ==  '__main__': #  True  when  prog5a  is  executed  and  False  when  prog5a  is  imported
	t = triangle() 
	t . get()  
	t . test() 
	print('Area : ',  t . area())  
	print('Perimeter : ', t . peri())  '''



from prog5a import triangle

if __name__=='__main__':
    t=triangle()

    triangle .get(t)
    triangle .test(t)

    print('Area : ', triangle .area(t))
    print('Perimeter : ', triangle .peri(t))







# What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student
s = student()
print(s . __dict__)#{}
s . get()
print(s . __dict__)#{'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55]}
s . compute()
print(s . __dict__)#{'rno': 25, 'sname': 'Rama Rao', 'gender': 'male', 'm': [52, 48, 55], 'tot': 155, 'avg': 51.666666666666664, 'grade': 'Second class'}





'''
Repeat  student  program  for  'n'  students

1) import  student  class  defined in  prog9a  but  do  not  rewrite
2) Use  list  of  objects

from  prog9a  import  student
How  to  read  number  of  students  into   variable  'n'
How  to  store  'n'  student  class  objects   in  list  'a'
How  to   read  each  student  data  into   the  object  held  by  the  list
How  to   store  results  in   each  object  held  by  the  list
How  to   print  each  object  held  by  the  list

class   student:
	def   get(self): 
		self . rno = int(input('Enter  roll  number : '))
		self . sname = input('Enter  student  name :  ')  
		self . gender = input(('Enter  gender (m/f) : '))   
		self . m = []  
		for  i  in  range(3): 
			marks = int(input(F'Enter  marks  of  subject  {i + 1}  :  '))
			self . m . append(marks) 
	def   compute(self): 
		self . tot = sum(self . m)  
		self . avg = self . tot / 3  
		if  min(self . m) < 40:   
				self . grade = 'Fail' 
		elif  self . avg >= 70:
				self . grade = 'Distinction'  
		elif  self . avg >= 60:
				self . grade = 'First  class' 
		elif  self . avg  >= 50:
				self . grade = 'Second  class'  
		else:
				self . grade = 'Third  class'  
	def  disp(self):  
		print('Roll  Number  :  ' ,  self . rno)
		print('Student  Name  :  ' , self . sname)
		print('Gender  :  ' ,  self . gender)
		print('Total  Marks  :  ' , self . tot)
		print(F'Average  :  {self . avg:.2f}')
		print('Grade  :  ' , self . grade)
	def   __str__(self):
		return  F'{self . rno}  \t {self . sname}  \t  {self . gender}  \t  {self . tot}  \t  {self . avg:.2f}  \t  {self . grade}' 

if  __name__ == '__main__': 
	s = student() 
	s . get()
	s . compute() 
	s . disp() 
	print(s)  '''

from prog9a import student

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details of student {i+1}")
    
    s = student()
    s.get()
    s.compute()
    
    students.append(s)

print("\nStudent Details:\n")

for s in students:
    print(s)






# Find  outputs  (Home  work)
class  Cat:
	def  talk(self):
		print('Meow Meow Meow ....')
class  Dog:
	def  bark(self):
		print('Bhow Bhow Bhow ....')
class  Goat:
	def  talk(self):
		print('Mehar  Mehar  Mehar  ....')
#end of the class
a = [Cat() , Dog() , Goat()]
for  x  in   a:
	if   hasattr(x , 'talk'):
		x . talk()
	else:
		x . bark()

'''
Meow Meow Meow ....
Bhow Bhow Bhow ....
Mehar  Mehar  Mehar  ...





'''
(Home  work)
Write  a  program  to  convert  a  dictionary  {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}  to  Emp  class  object
i.e.  object  should  contain  empno = 25 , ename = 'Rama  Rao' , Sal = 10000.0

Hint:  Use  setattr()  and  getattr()  functions
'''
class  Emp:
        pass
#End  of  the  class
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
How  to  convert  dictionary  to  object  'e'  with  for  loop
How  to  print  object  'e'  with  for  loop'''

class  Emp:
        pass
     
dict = {'Empno' : 25 , 'Ename' : 'Rama  Rao' , 'Sal' : 10000.0}
e = Emp() 
for  key, value  in  dict . items():
    setattr(e, key, value) 
for  key in  dict . keys(): 
    print(F'{key} : {getattr(e, key)}') 














