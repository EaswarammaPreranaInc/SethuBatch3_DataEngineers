def replaceOccurrence():
    n=input("enter String : ")
    s=""
    res=""
    for i in n:
        if i in s:
            res+="*"
        else:
            s+=i
            res+=i
    print(f'Result : {res}')
#replaceOccurrence()

a = '15:36:48'
print(a . split(':'))#['15','36','48']
print(a) #15:36:58

print("_____________________________________")
a = 'Hyd\nis green\tcity'
print(a . split(' ')) #['hyd\nis',green\tcity']
print(a . split()) #['hyd','is','green','city']
print(a . split('green')) #['hyd\is','city']
#print(a . split('')) # error
print("_________________________________________")
a = 'Hyd	is	green	city' #  There  is  tab  between  the  words
print(a . split('\t')) #['hyd,'is green','city']
print(a . split())#['hyd','is','green','city']
print(a . split(' '))#['hyd\tis\tgreen \tcity']
print("_______________________________________")
a= 'Hyd   is   green   city'  #  There  are  3  spaces  between  the  words
print(a . split())#['hyd','is','green','city']
print(a . split(' '))#['hyd','','','is','','',green,''t,'','city']

def sumstr(): 
        n=input("enter the str")
        a=n.split("+")
        sum=0
        for i in a:
            sum+=eval(i)
        print(sum)
#sumstr()

a = ['15' , '36' , '48']
print(':' . join(a))             #'15:36:48'
b = ('Hyd' , 'is' , 'green' , 'city')
print(' ' . join(b)) #'hyd is green city'
c = {'10' , '20' , '15' , '25' , '52'}
print(',' . join(c)) #'10,20,15,25,52'
d = ['www' , 'gmail', 'com']
print('.' . join(d)) #www.gmail.com
e = [15 , 36 , 48]
#print(':' . join(e))  error
f = ['Sankar' , 'Dayal' , 'Sarma']
print('' . join(f)) # 'SankarDayalSarma'
#g = range(5)
#print('-' . join(g)) #error

a = 'hyD  iS  grEen  cITy'
print(a . upper())  #'HYD IS GREEN CITY'
print(a . lower())  #'hyd is green city'
print(a . capitalize())#'Hyd is green city'
print(a . title()) #'Hyd Is Green City'
print(a . swapcase())#'HYd Is GReEN CitY'
print(a)  #hyD  iS  grEen  cITy
print('A7$a' . upper()) #A7$A

def ending():
     n=input("enter the String")
     res=""
     if(n.endswith("ing")):
         res+=n.replace('ing','ly')
     else:
          res=n+"ing"
     print(f'Result : {res}')
#ending()


def check():
     n=input("enter character : ")
     if(n.isalnum()):
          print("it is alphanumeric")
     if(n.isdigit()):
           print("it is digit")
     if(n.isupper()):
           print("it is uppercase")
     if(n.islower()):
           print("it is lowercase")
     if(n.isspace()):
           print("it is whitespaces")
     if(not n.isalnum() and not n.isdigit() and not n.isspace() and not n.islower() and not n.isupper()):
          print("it is special Character")
#check()


def sortalp():
     n=input("enter the string")
     a=list(n)
     a.sort()
     st=""
     for i in a:
          st+=i
     print(f"alphabetic order of '{n}' is :{st}")
#sortalp()


def sortalpnum():
     n=input("enter the string ")
     apl=[]
     num=[]
     for i in n:
          if(i.isalpha()):
               apl.append(i)
          elif(i.isdigit()):
               num.append(eval(i))
     apl.sort()
     n=''.join(apl)
     num.sort()
     for j in num:
          n+=str(j)
     print(f"value = {n}")     
#sortalpnum()
def reverseSentence():
   n=input("enter the string")
   l=n.split()
   res=""
   for i in range(len(l)-1,-1,-1):
        if i==0:
             res+=l[i]
        else:
             res+=l[i]+" "
   print(f"reversed sentence : {res}")
#reverseSentence()

def reverseWord():
     n=input("enter the string")
     res=""
     for i in range(len(n)-1,-1,-1):
          res+=n[i]
     print(f"reverse Word is : {res}")
reverseWord()