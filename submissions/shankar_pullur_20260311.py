'''
Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [10 , 20 , 30]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  True  becoz  elements  10 , 20 , 30  are  in  2nd  list

2) First  list :  [10 , 20 , 20]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  False  becoz   elements  10 , 20 , 30  are  not  in  2nd  list

3) First  list :  [2 , 2 , 5]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''

def sublist():
     try:
          sub=eval(input("enter the sublist"))
          li=eval(input("enter list"))
          count=0
          i=-1
          flag=True
          while count<=len(sub)-1:
               i=li.index(sub[count],i+1)
               count+=1

                    
                    
          print(flag)
     except:
          flag=False
          print(flag)
          
#sublist()
          
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)        #[10,20,15,18]
print(a  is  b) #False
print(a  ==  b) # True
c = a[:]        
print(c)        #[10,20,15,18]
print(a  is  c) #False
print(a  ==  c) # True
d = a           
print(d)       #[10,20,15,18]
print(a  is  d) #true
print(a  ==  d) # True
