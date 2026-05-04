# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))     #True
print(issubclass(int , float))  #False
print(issubclass(str , object)) #True
print(issubclass(c1 , object))  #True
print(issubclass(c2 , object))  #True
a = c1()
b = c2()
print(issubclass(c1 , a))    #Error due to arg 1 should be class
print(issubclass(c2 , a))   #Error due to arg 2 should be class




# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3))  #True
print(issubclass(c4 , c2))  #True
print(issubclass(c4 , c1))  #True
print(issubclass(c4 , object))  #True
print(issubclass(c4 , (int , float , str , bool)))  #Error due to arg 2 should be tuple of classes
print(issubclass(c4 , (int , float , c1 , str , bool))) #Error due to arg 2 should be tuple of classes and not only one class in tuples of elements
print(issubclass(c4 , [int , float , c1 , str , bool])) #Error due to arg 2 should be tuple of classes and not only one class in list of elements




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
print(isinstance(25 , int))    #True
print(isinstance(10.8 , float))     #True
print(isinstance('Hyd' , str))      #True
print(isinstance(3 + 4j , complex)) #True
print(isinstance(True , bool))      #True
print(isinstance(True , int))       #True
print(isinstance('True' , str))     #True
print(isinstance(True , str))       #False
print()
a = c3()
print(isinstance(a , c3))   #True
print(isinstance(a , c2))   #True
print(isinstance(a , c1))   #True
print(isinstance(a , object))   #True
print(isinstance(a , c4))   #False
print(isinstance(a , (int  ,  float  ,  str  ,  bool))) #False
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))    #True
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))  #True
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))    #Error due to arg 2 should be tuples of types