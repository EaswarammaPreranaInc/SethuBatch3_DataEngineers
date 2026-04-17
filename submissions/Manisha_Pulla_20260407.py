'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  --->  sqrt(s * (s - a) * (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  --->  (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  ---> a + b + c
'''
'''
import math
class c1():
    
    def m1(self):
        self.x= eval(input("Enter 1st side:"))
        self.y= eval(input("Enter 2nd side:"))
        self.z= eval(input("Enter 3rd side:"))

    
    def area(self):
        # self.s=(self.x+self.y+self.z)/2
        if (self.x + self.y)>= self.z or (self.x + self.z)>= self.y or (self.z + self.y)>= self.x: 
            pass
        else:
            print("Not a triangle.")
    def area(self):
        s=(self.x+self.y+self.z)/2
        area = math.sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))
        return area
    
    def perimeter(self):
        perimeter =self.x+self.y+self.z
        return perimeter
a = c1()
a.m1()
b=a.area()
c = a.perimeter()
print("Area:",b )
print("Perimeter:",c )
'''
'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
'''
class test:
    def get(self):

        self.x= eval(input("Enter value of x:"))
        self.y= eval(input("Enter value of y:"))
        self.z= eval(input("Enter value of z:"))
        
    
    def add(self,m,n):
        self.m = m.x+n.x
        self.n = m.y + n.y
        self.o = m.z + n.z
   
   
    def disp(self):
        print("x:",self.m)
        print("y:",self.n)
        print("z:",self.o)


a = test()
b = test()
c = test()
print("First Object.")
a.get()
print("First Object.")
b.get()


c.add(a,b)
c.disp()
'''
'''
Write  a  program  to  determine  total , average  and  grade  of  a  student
Inputs  are  Roll Number , Stud  Name , Marks  of  3  subjects  and  Gender

class student:
    def get(self):
        self.roll = eval(input("Enter roll num: "))
        self.name= input("Enter name: ")
        self.gender = input("Enter gender: ")
        self.math=eval(input("Enter math marks:  "))
        self.sci=eval(input("Enter sci marks:  "))
        self.tel=eval(input("Enter tel marks:  "))
    
    
    def compute(self):
        self.total= self.math+self.sci+self.tel
        self.avg= (self.math+self.sci+self.tel)/3
        if self.math < 40 or self.sci < 40 or self.tel < 40:
            self.grade = "Fail"
        elif self.avg>=70:
            self.grade = "Distinction"
        elif self.avg>=60:
            self.grade = "First"
        elif self.avg>=50:
            self.grade = "Second"
        else:
            self.grade= "Third"
    
    
    def disp(self):
        print('Roll  Number  :  ' ,   self.roll)
        print('Student  Name  :  ' , self.name)
        print('Gender  :  ' ,  self.gender)
        print('Total  Marks  :  ' , self.total)
        print('Average  :  ' , self.avg)
        print('Grade  :  ' , self.grade)
a = student()
a.get()
a.compute()
a.disp()

#  Find  outputs (Home  work)
class  Date:
	pass
# End of the class
a =  Date()
a . dd = 15
a . mm = 8
a . yy = 1947
print(a)#<class '__main__.Date'>



#  Object  'a'  --->

#  Find  outputs (Home  work)
class   c1:
	def  _str_(self):
			return  '25'
class   c2:
	def  _str_(self):
			return   35
class   c3:
	def  _str_(self):
			print('Hyd')
class   c4:
	def  _str_(self , x):
			return   F'{x}'
#end of the class
a = c1()
b = c2()
c = c3()
d = c4()
print(a)#<class '__main__.c1'>
print(b)#<class '__main__.c2'>
print(c)#<class '__main__.c3'>
print(d)#<class '__main__.c4'>
print(b . _str_())#'35'
print(c . _str_())#Hyd
print(d . _str_(50))#50


