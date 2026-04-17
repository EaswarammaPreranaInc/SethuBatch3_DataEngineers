#1
'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
import  math
class  triangle:
        def  get(self):
                self . a = int(input('Enter the first side:'))
                self . b = int(input('Enter the second side:'))
                self . c = int(input('Enter the third side:'))

        def  test(self):
                if self . a + self . b > self . c and self . a + self . c > self . b and self . b + self . c > self . a:
                        pass
                else:
                        print('Not  a  triangle')
                        exit()
        def  area(self):
                s = (self . a + self . b + self . c) / 2
                area = math . sqrt(s * (s - self . a) * (s - self . b) * (s - self . c))
                return area
        def  peri(self):
                return self . a + self . b + self . c
# End of the class
sides = triangle()

sides . get()

sides . test()

area = sides . area()
perimeter = sides . peri()
print('Area : ', area)
print('Perimeter : ', perimeter)


#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):
		x = 10
		self . x = 20
		print(x) # 10
		print(self . x) # 20
		x += 5 # 15
		self . x += 7 # 27
	def   m2(self):
		print(x) # error , 'x' is not defined
		print(self . x) # 27
		self . x += 6
# End  of  the  class
a = c1()
a . m1()
a . m2()
print(a . x) # 33
print(self . x) # error
print(x) # error


#2
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
        def   get(self):
                #How  to  read  inputs  into  variables  x , y and z
                self . x = int(input('Enter the value of x:'))
                self . y = int(input('Enter the value of y:'))
                self . z = int(input('Enter the value of z:'))

        def   add(self , m , n):
                self . x = m . x + n . x
                self . y = m . y + n . y
                self . z = m . z + n . z

        def  disp(self):
                print(f'x = {self . x}')
                print(f'y = {self . y}')
                print(f'z = {self . z}')
                
		 
# End  of  the  class

#How  to  create  three  Test  class  objects  a , b  and  c
a = Test()
b = Test()
c = Test()

print('First  Object')
# How  to  read  inputs  into  object  'a'
a . get()

print('Second  Object')
#How  to  read  inputs  into  object  'b'
b . get()

c . add(a , b)

print('Addition  results')
c . disp()


#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a) # type and address of the object



#  Object  'a'  --->


#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):
			return  '25'
class   c2:
	def  __str__(self):
			return   35
class   c3:
	def  __str__(self):
			print('Hyd')
class   c4:
	def  __str__(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a) # 25
print(b) # 'Hyd' ; error , when called implicitly, the object returned in __str__() method needs to be a string
print(c) # error , when called implicitly, the object returned in __str__() method needs to be a string
print(d) # error , when called implicitly, argument in __str__() method can only be self and nothing else
print(b . __str__()) # 35
print(c . __str__()) # 'None' ; Hyd  
print(d . __str__(50)) # 50


#3
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender
'''
class   Student:
	def   get(self):
		How  to  read  roll  number  
		How  to  read  student  name  
		How  to  read  gender  
		How  to  read  marks  of  3  subjects
	def   compute(self):
		How  to  calculate  total  marks
		How  to  calculate  average  marks
		if  At  least  one  subject  is  below  40:
				How  to  initilaize  grade  to  'Fail'
		elif  average  is  above  >= 70%:
				How  to  initilaize  grade  to  'Distinction'
		elif  average  is  above  >= 60%:
				How  to  initilaize  grade  to  'First  class'
		elif  average  is  above  >= 50%:
				How  to  initilaize  grade  to  'Second  class'
		else:
				How  to  initilaize  grade  to  'Third  class'
	def  disp(self):
		print('Roll  Number  :  ' ,   ???)
		print('Student  Name  :  ' , ???)
		print('Gender  :  ' ,  ???)
		print('Total  Marks  :  ' , ???)
		print('Average  :  ' , ???)
		print('Grade  :  ' , ???)
	def   __str__(self):
		return  All  the   values  of  object  in  the  form  of  string
#End  of  the  class
class   Student:
        def get(self):
		#How  to  read  roll  number
                self . rno = int(input('Enter the Roll Number of the Student:'))
		#How  to  read  student  name
                self . name = input('Enter the Name of the Student:')
		#How  to  read  gender
                self . gender = input('Enter the Gender of the Student [M / F]:')
		#How  to  read  marks  of  3  subjects
                self . s1 = float(input('Enter Marks of Subject 1:'))
                self . s2 = float(input('Enter Marks of Subject 2:'))
                self . s3 = float(input('Enter Marks of Subject 3:'))
        def compute(self):
                #How  to  calculate  total  marks
                self . total = self . s1 + self . s2 + self . s3
                self . avg = (self . s1 + self . s2 + self . s3) / 3

                if self . s1 < 40 or self . s2 < 40 or self . s3 < 40:
                        self . grade = 'Fail'
                elif self. avg >= 70:
                        self . grade = 'Distinction'
                elif self . avg >= 60:
                        self . grade = 'First Class'
                elif self . avg >= 50:
                        self . grade = 'Second Class'
                else:
                        self . grade = 'Third Class'
        def disp(self):
                print('Roll Number:' , self . rno)
                print('Student Name:' , self . name)
                print('Gender:' , self . gender . upper())
                print('Total Marks:' , self . total)
                print('Average:' , self . avg)
                print('Grade: ' , self . grade)

        def   __str__(self):
                return f'{self . rno} {self . name} {self . gender} {self . total} {self . avg} {self . grade}'
#End  of  the  class
sdetails = Student()

#How  to  read  inputs  into  object
sdetails . get()

sdetails . compute()

#How  to  print  object  with  disp()  method
sdetails . disp()

#How  to  print  object  with  __str__()  method
print(sdetails . __str__())


#  Object  's'  --->
