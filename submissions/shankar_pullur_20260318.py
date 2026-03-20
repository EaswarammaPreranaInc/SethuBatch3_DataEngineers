'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
def vowels():
    s=input("enter string")
    v="aeiouAEIOU"
    se=set()
    for i in s:
        if i in v:
            se.add(i)
    print(f"distinct vowels are : {''.join(se)}")
#vowels()

a = { }
#How  to  append  10 : 'Rama'  to  dictionary  'a'
a[10]='Rama'
#How  to  append  20 : 'Sita'  to  dictionary  'a'
a[20]='sita'
#How  to  append  15 : 'Rajesh'  to  dictionary  'a'
a[15]='sita'
#How  to  append  18 : 'Kiran'  to  dictionary  'a'
a[18]='Kiran'
print(a)

#  How  to  remove  key : value  pairs  of  dictionary  (Home  work)
a =  {'Empno'  :  25,  'Ename'  :  'Rama  Rao'  ,  'Sal'  :  1000.65  }
print(a)
#How  to  remove  'Sal' : 1000.65  from  dictionary  'a'
#del a['Sal']
a.pop('Sal',None)
print(a)


#  in  and  not  in  operators  (Home  work)
a =  {10 : 20 , 30 : 40 , 50 : 60 , 70 : 80}
print(30  in  a . keys())   #TUE
print(60  in  a . keys())   # FALSE
print(60  in  a . values())   #true
print(30  in  a . values())   #False
print(50  in  a)    # TRUE
print(20  in  a)    #False
print(70  not  in  a . keys()) # FALSE
print(40  not  in  a . values()) #False
print(25  not  in  a)  # True


a = input('Enter  dictionary  :  ')
print(a)     #10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(a)) #<CLASS 'str'>
b = eval(a)  
print(b)     #{10: 'A', 20: 'B', 15: 'C' , 20 : 'D'}
print(type(b)) #<class 'dict'>

'''
(Home  work)
Write  a  program  to  create  a  dictionary  with  emp  names  and  salaries

Hint:  Append  each  emp  name  and  salary  to  dictionary  'a'
'''
def employe():
    n=int(input("number employees you want : "))
    a={}
    for i in range(n):
        name=input("enter name : ")
        sal=float(input("enter salary : "))
        a[name]=sal
    print(a)
#employe()
s=input("enter string : ")
l1=s.split(',')
a={}
for i in l1:
    l2=i.split('=')
    a[l2[0]]=l2[1]
print(a)