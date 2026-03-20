a  =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(len(a))  # 3
b = {}
print(len(b))  # 0


'''
What  does  len(dict)  do ?  --->  Returns  number  of  key : value  pairs  in  the  dictionary
'''

a = {10 : 20 , 30 : 40 , 50 : 60}
print(sum(a . keys()))    #90
print(sum(a . values()))  # 120
print(sum(a))             #90
#print(sum(a . items()))   #error


a = {10 : 20 , 30 : 25 , 40 : 5 , 7 : 28 , 9 : 50}
print(max(a . keys())) #40
print(min(a . keys())) #7
print(max(a . values())) #50
print(min(a . values())) #5
print(max(a . items()))  #(40,5)
print(min(a . items())) #(7,28)
print(max(a))   # 40
print(min(a))   #7



a = [ (10 , ' Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]
b = dict(a)
print(b)  #{10:'hyd',20:'sec',15:'cyb',20:'Pune'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])
d = dict(c)
print(d)    #{'R':'Red','G':'Green','B':'Blue','G':'Gray'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e))   #error
#f = [[10] , [20] , [30]]
#print(dict(f)) #error
#print(dict([10 , 20])) #error
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) #{10:[10,30],40:[50,60],70:[80,90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) # Error
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) #{(10,20):30,(40,50):60,(70,80):90}


a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())
print(b) #{5:'White',10:'Red',15:'Blue',18:'Yellow',20:'Green'}
c = sorted(a . values())
print(c)  #['Blue', 'Green',  'Red', 'White', 'Yellow']
d = sorted(a . items())
print(d) #[(5, 'White'), (10, 'Red'), (15, 'Blue'), (18, 'Yellow'), (20, 'Green')]
f  = sorted(a  , reverse = True) 
print(f)#[20, 18, 15, 10, 5]
print(a)#{10: 'Red', 20: 'Green', 15: 'Blue', 18: 'Yellow', 5: 'White'}

'''
Write  a  program  to  sort  dictionary  wrt  keys  (Home  work)

1) Let  input  be   {10 : 'A' , 20 : 'B' , 15 : 'C' , 5 : 'D' , 12 : 'E'}
    What  is  the  output ?  ---> {5 : 'D' , 10 : 'A' ,  12 : 'E' ,  15 : 'C' , 20 : 'B'}

2) Both  input  and  output  are  dictionaries

3) Hint:  Use  sorted()  function
'''
def sort():
    d=eval(input("enter dict values"))
    a=dict(sorted(d.items()))
    print(a)
#sort()

# Find  outputs (Home  work)
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
for  x , y   in  a . items():
       print(x , y , sep = ' ... ')  #10...hyd \n 20...sec\n 15...cyb
'''for  x , y   in  a . keys():       
       print(x , y , sep = ' ... ') #error
for  x , y   in  a . values():
       print(x , y , sep = ' ... ')#error
for  x , y   in  a:       
       print(x , y , sep = ' ... ')'''  #error


a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()
print(x)   #10
print(y)   #20
print(z)   #30
print()
x , y , z = a . values()
print(x)   #rama
print(y)   #Sita
print(z)   #rajesh
print()
x , y ,  z = a . items()
print(x)    #(10,'rama')

print(y)     #(20,'Sita')
print(z)      #(30,'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()
print(rno1 , sname1) #10 Rama
print(rno2 , sname2) #20 Sita
print(rno3 , sname3) #30 Rajesh

def frequencey():
      s=input("enter the string").upper()
      l=sorted(s)
      x={}
      for i in l:
            x[i]=x.get(i,0)+1
      print(x)
#frequencey()
            