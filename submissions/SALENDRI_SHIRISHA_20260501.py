# Find  outputs
class  c1:
        pass
class  c2(c1):
        pass
# End of the class
print(issubclass(c2 , c1))
print(issubclass(int , float))
print(issubclass(str , object))
print(issubclass(c1 , object))
print(issubclass(c2 , object))
a = c1()
b = c2()
print(issubclass(b , a))
print(issubclass(c2 , a))


# Find outputs
class c1:
        pass
class  c2(c1):
        pass
class  c3(c2):
        pass
class  c4(c3):
        pass
print(issubclass(c4 , c3))
print(issubclass(c4 , c2))
print(issubclass(c4 , c1))
print(issubclass(c4 , object))
print(issubclass(c4 , (int , float , str , bool)))
print(issubclass(c4 , (int , float , c1 , str , bool)))
print(issubclass(c4 , [int , float , c1 , str , bool]))


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
print(isinstance(25 , int))
print(isinstance(10.8 , float))
print(isinstance('Hyd' , str))
print(isinstance(3 + 4j , complex))
print(isinstance(True , bool))
print(isinstance(True , int))
print(isinstance('True' , str))
print(isinstance(True , str))
print()
a = c3()
print(isinstance(a , c3))
print(isinstance(a , c2))
print(isinstance(a , c1))
print(isinstance(a , object))
print(isinstance(a , c4))
print(isinstance(a , (int  ,  float  ,  str  ,  bool)))
print(isinstance(a , (int  ,  float  ,  c3 , str  ,  bool)))
print(isinstance(a , (int  ,  float  ,  c1  ,  str  ,  bool)))
print(isinstance(a , [int  ,  float  ,  c3 , str  ,  bool]))
