a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))                    #True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))                    # False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))               #False
d = [10 , 0 , 20] 
print(all(d))               #False
e = []
print(all(e))               #True



a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))                      #True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))                       #False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))                       #True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))                      #False
e = []
print(any(e))                       #False


a = [10 , 20 , 30]
a . append('Hyd')
print(a)
print(len(a))
print(a[3])
print(a[3][0:1])
print(a[3][1:2])
print(a[3][2:3])
 
print("INSERT ELEMENTS____________________________________________")

a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)
print(a)     #[10,20,[50,60,70],30,40]
print(len(a))# 5 
print(a[2][0:])
print(a[2][0])
print(a[2][1])
print(a[2][2])

'''
Write  a  program  to  delete  'all'  occurences  of  'x'  from  the  list

Let  1st  input  be   [10 , 20 , 15 , 18 , 19 , 15 , 17 , 20 , 15 , 14]  and
2nd  input  be  15
What  is  the  output ?  ---> [10 , 20 ,  18 , 19 , 17 , 20 , 14]
'''
def removeAllOccurrence():
    try:
        n=[eval(x) for x in input("enter list values").split()]
        t=int(input("enter target to remove : "))
        i=0;
        while True:
            
                n.remove(t)
    except:
        print("list : ",n)
        
#removeAllOccurrence()


a = [10 , 20 , 15 , 18 , 12]
print(a . pop(2))            #15
print(a)
#print(a . pop(len(a)))       #error
print(a . pop(-3))           # 20
print(a)
#print(a . pop(-4))           # ERROR
print(a . pop())              # 12
print(a)                      #10,18
b = []
#b . pop()#error


'''
Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  --->  [15 , 14 , 18 , 19]

Element         count               Action
---------------------------------------------
  10                  3                       Ignore
  
  20                  2                       Ignore
  
  15                  1                       [15]
  
  14                  1                       [15 , 14]
  
  18                  1                       [15 , 14 , 18]
  
  19                  1                       [15 , 14 , 18 , 19]
'''


def uniqueElements():
     n=[eval(x) for x in input("enter list values").split()]
     res=[]
     for i in n:
         if n.count(i) == 1:
              res.append(i)
     print(res)
#uniqueElements()
              
def identicalORNOT():
     n=[eval(x) for x in input("enter list values").split()]
     for i in range(len(n)-1):
          if n[i]!=n[i+1]:
               print("not identical :",n)
               return
     print("identical :",n)
#identicalORNOT()