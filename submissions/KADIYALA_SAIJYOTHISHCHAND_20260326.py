#  Find  outputs (Home  work)
def   f1(x , a = []):
        if  a  ==  []:
                a = []
        a . append(x)
        print(a)
#end  of  the  function
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1(3)#[3]
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1(4 , [1 , 2 , 3])#[1,2,3,4]
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1(4)#[4]
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1(40 , [10 , 20 , 30])#[10,20,30,40]
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1(5)#[5]
print('__defaults__  :  ' , f1.__defaults__)#([],)
f1([6 , 7 , 8])#[[6,7,8]]
print('__defaults__  :  ' , f1.__defaults__)#([],)


# Find  output (Home  work)
def     f1(x , a = []):
        if   a == []:
                a = []
        for  i   in   range(x):
                a . append(i * i)
        return  a
# End  of  the  function
print(f1(3))#[0, 1, 4]
print(f1(4 , [10 , 20 , 15 , 18]))#[10, 20, 15, 18, 0, 1, 4, 9]
print(f1(5))#[0, 1, 4, 9, 16]
print(f1(a = [100 , 200 , 300],   x = 6 ))#[100, 200, 300, 0, 1, 4, 9, 16, 25]
print(f1(6))#[0, 1, 4, 9, 16, 25]
