#1
def f1(x , a = []):
    if  a  ==  []:
        a = [] # This reassigns 'a' to a NEW local list, so the default is NEVER modified
    a . append(x)
    print(a)
# End of the function
print('_defaults_ :  ' , f1.__defaults__) # _defaults_ :  ([],)
f1(3)                                     # [3]
print('_defaults_ :  ' , f1.__defaults__) # _defaults_ :  ([],)
f1(4 , [1 , 2 , 3])                       # [1, 2, 3, 4]
print('_defaults_ :  ' , f1.__defaults__) # _defaults_ :  ([],)
f1(4)                                     # [4]
print('_defaults_ :  ' , f1.__defaults__) # _defaults_ :  ([],)
f1(40 , [10 , 20 , 30])                   # [10, 20, 30, 40]
print('_defaults_ :  ' , f1.__defaults__) # _defaults_ :  ([],)
f1(5)                                     # [5]
print('_defaults_ :  ' , f1.__defaults__) # _defaults_ :  ([],)
f1([6 , 7 , 8])                           # [[6, 7, 8]]
print('_defaults_ :  ' , f1.__defaults__) # _defaults_ :  ([],)



#2
def f1(x , a = []):
    if   a == []:
        a = [] # Again, this creates a fresh local list every time 'a' is empty
    for i in range(x):
        a.append(i * i)
    return  a
# End of the function
print(f1(3))                          # [0, 1, 4]
print(f1(4 , [10 , 20 , 15 , 18]))    # [10, 20, 15, 18, 0, 1, 4, 9]
print(f1(5))                          # [0, 1, 4, 9, 16]
print(f1(a = [100 , 200 , 300], x = 6)) # [100, 200, 300, 0, 1, 4, 9, 16, 25]
print(f1(6))                          # [0, 1, 4, 9, 16, 25]