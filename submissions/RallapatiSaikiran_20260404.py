

# # Find  outputs (Home  work)
# def   f1():
# 	yield  25
# 	yield  10.8
# 	yield  'Hyd'
# # End of  generator
# for  x  in  f1():
# 	print(x) # 25 10.8 Hyd
# for  x  in  f1():
# 	print(x) # 25 10.8 Hyd
# for  x  in  f1():
# 	print(x) # 25 10.8 Hyd

# #  Find  outputs (Home  work)
# l = [x * x   for   x   in   range(5)]
# print(l) # [0,1,4,9,16]
# print(type(l)) # class 'list'

# s = {x * x   for   x   in   range(5)}
# print(s) # {0,1,4,9.16}
# print(type(s)) # <class 'set'>

# d = {x : x * x    for   x   in   range(5)}
# print(d) #{0:0,1:1,2:4,3:9,4:16}
# print(type(d)) # <class 'dict'>

# g = (x * x   for   x   in   range(5))
# print(g) # genrator at xxxx
# print(type(g)) #class generator

# #  Find  outputs (Home  work)
# def  f1():
# 	return  10
# 	return  20
# 	return  30
# def  f2():
# 	yield  10
# 	yield  20
# 	yield  30
# # End  of  the  function
# print(f1()) # 10
# print(f1()) # 10
# print(f1()) #10
# print() 
# g = f2()
# print(next(g)) #10
# print(next(g)) # 20
# print(next(g)) # 30
# print(next(g)) # stopIteration error

# '''
# Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

# Hint:  Use  generator  function  and  for  loop  to  iterate  over  the  generator
# '''
# try:
#     def cal(a,b):
#         yield f'Sum: {a+b}'
#         yield f'Sub: {a-b}'
#         yield f'Product: {a*b}'
#         yield f'Division: {a/b}'
#     a=int(input('Enter first Number : '))
#     b=int(input('Enter Second Number : '))
#     for x in cal(a,b):
#         print(x)
# except:
#     print('Division by Zero is not permitted')


'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''

def fun(count):
    count+=1
    yield count
a=int(input('Enter first Value : '))
b=int(input('Enter Second Value : '))
counter=a-1
while counter<b:
    counter=fun(counter)
    print(counter)




    
