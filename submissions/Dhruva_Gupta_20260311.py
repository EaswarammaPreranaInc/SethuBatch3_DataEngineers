Name-Dhruva Gupta
Roll Number-D238

a = [10,20,15,12,14,15,18,19,15,12,25]
try:
    i = -1
    while True:
        print(i := a.index(15, i + 1))
except:
    print(f'15 is found {a.count(15)} times')
2)
a=[10 , 20 , 20]
b=[15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
k=0
ans=[]
try:
    i=b.index(a[k])
    while True:
        ans.append(a[k])
        k=k+1
        i=b.index(a[k],i+1)
except:
    if(a==ans):
        print("True")
    else:
        print("False")

3)
# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b) #[10,20,15,18]
print(a  is  b) #False
print(a  ==  b) #True
c = a[:]
print(c) #[10,20,15,18]
print(a  is  c) #True
print(a  ==  c) #True
d = a
print(d) #[10,20,15,18]
print(a  is  d) #True
print(a  ==  d) #True