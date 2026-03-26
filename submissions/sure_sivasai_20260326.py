#1.Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('_defaults_  :  ' , f1._defaults_) 
f1(3)                                    
print('_defaults_  :  ' , f1._defaults_) 
f1(4 , [1 , 2 , 3])                      
print('_defaults_  :  ' , f1._defaults_) 
f1(4)
print('_defaults_  :  ' , f1._defaults_)
f1(40 , [10 , 20 , 30])
print('_defaults_  :  ' , f1._defaults_)
f1(5)
print('_defaults_  :  ' , f1._defaults_)
f1([6 , 7 , 8])
print('_defaults_  :  ' , f1._defaults_)
'''
_defaults_  :  ([],)

[3]
_defaults_  :  ([],)

[1, 2, 3, 4]
_defaults_  :  ([],)

[4]
_defaults_  :  ([],)

[10, 20, 30, 40]
_defaults_  :  ([],)

[5]
_defaults_  :  ([],)

[[6, 7, 8]]
_defaults_  :  ([],)
'''

#------------------------------------------

#2.Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))
print(f1(4 , [10 , 20 , 15 , 18]))
print(f1(5))
print(f1(a = [100 , 200 , 300],   x = 6 ))
print(f1(6))

'''
[0, 1, 4]
[10, 20, 15, 18, 0, 1, 4, 9]
[0, 1, 4, 9, 16]
[100, 200, 300, 0, 1, 4, 9, 16, 25]
[0, 1, 4, 9, 16, 25]
'''










