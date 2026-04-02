# Find outputs
def f1():
 a = 3
 if a:
  print(a) # 3 
  a = a - 1 # 2
  f1() 
  print('Hello')
  print('Hi')
  print(a)
 print('Bye')
# End of the function
a = 3
f1()
print('End')


'''
3
2
1
Bye 
Hello
Hi
0
Bye 
Hello
Hi
0
Bye 
Hello
Hi
0
Bye 
End
'''