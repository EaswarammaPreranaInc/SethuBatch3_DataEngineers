#1) Public  and  Private  members  demo  program
class  Test:
	def  _init_(self):
		self.x = 10 #How  to  initialize  public  variable  'x'  to  10
		self.y = 20 #How  to  initialize  private  variable  'y'  to  20
	def  m1(self):
		print('m1  method')
		print(self.x) #How  to  print   variable  'x'
		print(self.y) #How  to  print  private  variable  'y'
		seld.__m2() #How  to  call    private  method   m2()
		print('Back to m1 method')
	def  __m2(self):
		print('__m2  method')
		print(self.x) #How  to  print   variable  'x'
		print(self.__y) #How  to  print  private  variable   'y'
# End  of  the  class
t = Test()
print('Outside')
print(t.x) #How  to  print  variable  'x'
print(t._Test__y) #How  to  print   variable  'y'
print(t . __y)
print(t . _dict_)
t.m1() #How  to  call  method  m1()
t._Test__m2() #How  to  call   method  m2()
t . __m2()
print('End')


# Object  't'  ---> x = 10, y=20




#2) find outputs
class  c1:
	def _init_(self):
		self.x = 10 #How  to  initialize  public  variable  'x'  with  10
		self.__x = 20 #How  to  initialize  private  variable  'x'  with  20
		self._x_ =30 #How  to  initialize  public  dunder  variable  'x'  with  30
	def  m1(self):
		print('public method')
	def  __m1(self):
		print('private method')
	def  _m1_(self):
		print('public Dunder method')
#  End  of  the  class
a = c1()
print(a.x) #How  to  print   variable  'x'
print(a._x_) #How  to  print  public  dunder  variable  'x'
print(a._c1__x) #How  to  print   private  variable  'x'
#print(a . __x)
a.m1() #How  to  call  public  method  m1()
a._m1_() #How  to  call  public  dunder  method  m1()
a._c1__m1() #How  to  call  private  method  m1()
a . __m1()







# Object  'a'   ---> x = 10 , _c1__x = 20, _x_ = 30

#3) outputs

Assume  that  addresses  of  objects   'a' , 'b' , 'c' , 'd'  and  'e'  are  1000 , 2000 , 3000 , 4000  and  5000  respectively
'''
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost')
# End  of  the  class
a = c1()#address  = 1000
a = None # 1000 is lost because no ref
b = c1()# address = 2000 
del    b #obj b is lost
c = c1() # address = 3000
c = c1() # address = 4000 (3000 is lost)
d = c1() # address = 5000
e = c1() # address = 6000
'''
4) Identify  Error 
class   c1:
	def  _del_(self , x):
		print('destructor : ' ,  x)
a = c1()
a . _del_(25)#Cannot be called directly 

#5) outputs 
class   c1:
	def  _del_(self , x = 35):
		print('destructor : ' , x)#destructor :  25
a = c1()
a . _del_(25)

#6) outputs 
class   c1:
	def  _del_(self):
			print('destructor')
			b = c1() #Recursion
a = c1()







#7) outputs
class   c1:
	def  _init_(self):
		print('constructor')#constructor, constructor ...
		del  self
	def  _del_(self):
		print('destructor')#destructor, destructor...
		b = c1()
a = c1()





#8) outputs
class   c1:
	def  _del_(self):
		print('1st  destructor')
	def  _del_(self):
		print('2nd  destructor')
	def  _del_(self):
		print('3rd  destructor')#3rd destructor
# End  of  the  class
a = c1()






#9) outputs 
class   c1:
	def   _init_(self):
		print('Object  is  created  at  address  :  ' , id(self))
	def   _del_(self):
		print(F'Object  at  address  {id(self)}  is  lost  ')
#end  of  the  class
c = b = a = c1()
del   a
print('Hello')#Hello
del   b
print('Hi')#Hi
del   c
print('Bye')#Bye
d = c1()
print('End')#End









#10) outputs
class  c1:
        def     _init_(self):
                print('Object  is  created  at  address  :  ' , id(self)) #Object is created at address : id1
Object is created at address : id2
Object is created at address : id3
        def     _del_(self):
                print(F'Object  at  address  {id(self)}  is  lost ')
#Object at address id3 is lost
Object at address id2 is lost
Object at address id1 is lost
# End  of  the  class
list = [c1() , c1() , c1()]
del  list









#11) outputs  
class   c1:
	def  _del_(self):
		print('destructor')#destructor
		return  25
a = c1()
print(a . _del_())#25
print('Hello')#Hello
del   a