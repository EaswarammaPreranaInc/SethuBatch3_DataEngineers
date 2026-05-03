# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))#True
print(issubclass(int , float))#False
print(issubclass(str , object))#True 
print(issubclass(c1 , object)) # True 
print(issubclass(c2 , object)) # true
a = c1()
b = c2()
print(issubclass(b , a)) # error
print(issubclass(c2 , a)) #error

# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3)) # True
print(issubclass(c4 , c2)) # TRue
print(issubclass(c4 , c1)) # TRue
print(issubclass(c4 , object)) # true
print(issubclass(c4 , (int , float , str , bool))) # false
print(issubclass(c4 , (int , float , c1 , str , bool))) # false
print(issubclass(c4 , [int , float , c1 , str , bool])) #error

#  Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4:
        pass
#  End  of  the  class
print(isinstance(25 , int)) #True
print(isinstance(10.8 , float)) # TRue
print(isinstance('Hyd' , str)) #True
print(isinstance(3 + 4j , complex)) #True
print(isinstance(True , bool)) #True
print(isinstance(True , int)) #False
print(isinstance('True' , str)) #True
print(isinstance(True , str)) # False
print()
a = c3()
print(isinstance(a , c3)) #True
print(isinstance(a , c2)) # False
print(isinstance(a , c1)) # False
print(isinstance(a , object)) # False
print(isinstance(a , c4)) #False
print(isinstance(a , (int  ,  float  ,  str  ,  bool)))# False
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool))) # False
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool))) #False
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool])) #error