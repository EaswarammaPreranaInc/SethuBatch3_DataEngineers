# Find  outputs (Home  work)
Def   f1():
	Yield  25
	Yield  10.8
	Yield  ‘Hyd’
# End of  generator
For  x  in  f1():
	Print(x)     #  25
                                10.8
                                Hyd
For  x  in  f1():
	Print(x)
For  x  in  f1():
	Print(x)

#  Find  outputs (Home  work)
L = [x * x   for   x   in   range(5)]
Print(l)     #   [ 0  ,  1  ,  4  ,  9  ,  16]
Print(type(l))  # <class ‘list’>

S = {x * x   for   x   in   range(5)}
Print(s)  #  {0  ,  1  ,  4  ,  9  , 16}
Print(type(s))    # <class ‘set’>

D = {x : x * x    for   x   in   range(5)}
Print(d)    #  {0 : 0  ,  1 : 1 , 2  :  4  ,3 :  9  , 4 :16}
Print(type(d))  # <class  ‘ dictionary ‘>

G = (x * x   for   x   in   range(5))
Print(g)   # 1,4,9,16
Print(type(g))    # <new genertor is created>

#  Find  outputs (Home  work)
Def  f1():
	Return  10
	Return  20
	Return  30
Def  f2():
	Yield  10
	Yield  20
	Yield  30
# End  of  the  function
Print(f1())
Print(f1())
Print(f1())
Print()
G = f2()
Print(next(g))   #  10
Print(next(g))   #   20
Print(next(g))   #   30
Print(next(g))

‘’’
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
‘’’
Def operations(a, b):
    Yield a + b
    Yield a – b
    Yield a * b
    
    If b != 0:
        Yield a / b
    Else:
        Yield “Division not possible”
X = int(input(“Enter first number: “))
Y = int(input(“Enter second number: “))

Gen = operations(x, y)

Print(“Results:”)
For i in gen:
    Print(i)


‘’’
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
‘’’

Def generate_numbers(x, y):
    While x <= y:
        Yield x
        X += 1

Start = int(input(“Enter start value: “))
End = int(input(“Enter end value: “))

For num in generate_numbers(start, end):
    Print(num, end=” “)

‘’’
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
‘’’


# Find  outputs
Def   f1():
        Yield   [10 , 20]
        Yield  {30 , 40 , 50}
        Yield  60  , 70 , 80 , 90
        Yield  100
# End  of  generator
g= f1()
For   x   in   g:
	Print(x)    #    [10 , 20]
                            #    {30 , 40 , 50}
                            #   60  , 70 , 80 , 90
                           #   100
	Print(type(x))    #   list
                                      #   set
                                      #   tuple


#  Find  outputs
From  timeit  import   timeit
Print(timeit(‘[x * x   for  x  in  range(500) ]’))
Print(timeit(‘( x * x   for  x  in  range(500) )’))



# Find  outputs
Import  sys
List = [x * x   for  x  in  range(10000)]
Gen = (x * x   for  x  in  range(100000000000000000000000000000000000000000000000))
Print(sys . getsizeof(list))
Print(sys . getsizeof(gen))



