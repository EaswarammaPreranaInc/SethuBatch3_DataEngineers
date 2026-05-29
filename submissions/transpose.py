'''
Write  a  program  to  find  transpose  a  matrix
     Eg:  a =  [[10 , 20 ,  30 , 40] , [50 , 60 , 70 , 80] , [90 , 100 , 110 , 120]]
	 Ouput :   [[10 , 50 , 90] , [20 , 60 , 100] , [30 , 70 , 110] , [40 , 80 , 120]]

1) Input :  a =  [[10 , 20 ,  30 , 40] , [50 , 60 , 70 , 80] , [90 , 100 , 110 , 120]]	 

2) Initilaization
    --------------
	b = []	   
	row = []

3) x = [10 , 20 ,  30 , 40]
    row = [10]	
	a =  [[20 ,  30 , 40] , [50 , 60 , 70 , 80] , [90 , 100 , 110 , 120]]	 

4) x = [50 , 60 , 70 , 80]
    row = [10 , 50]
	a =  [[20 ,  30 , 40] , [60 , 70 , 80] , [90 , 100 , 110 , 120]]	 
	
5) x = [90 , 100 , 110 , 120]
    row = [10 , 50 , 90]
 	a =  [[20 ,  30 , 40] , [60 , 70 , 80] , [100 , 110 , 120]]	 
	
6) b = [[10 , 50 , 90]]	
    row = []
	
7) x = [20 , 30 , 40]
    row = [20]
	a =  [[30 , 40] , [60 , 70 , 80] , [100 , 110 , 120]]	
 
8) x = [60 , 70 , 80]
    row = [20 , 60]
	a =  [[30 , 40] , [70 , 80] , [100 , 110 , 120]]	
 
9) x = [100 , 110 , 120]
    row = [20 , 60 , 100]
	a =  [[30 , 40] , [70 , 80] , [110 , 120]]	 
	
10) b = [[10 , 50 , 90] , [20 , 60 , 100]]	
    row = []
and  so  on	
'''
def  transpose(a):
    b=[]
    row=[]#How  to  create  a  list
    for x in a:
        a.append(x)
        return b
# End  of  the  function
a = eval(input('Enter  nested  list :  '))
b=a.transpose()#How  to  call  transpose()  function
print(a)#How  to  print  transpose
