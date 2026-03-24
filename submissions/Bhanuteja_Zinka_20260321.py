(Home  work) 
 Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order (Ignoring  the  case) 
  
 Let  input  be  RamA    raO 
 What  is  the  output ?  --->  {'A' : 3 , 'O' : 1} 
  
 Hint:  Same  as  prog23a  with  minor  changes 
  
 a = input('Enter  mixed  case  string : ')  #   Reads  a  string 
 b = a . upper()  #  Converts string  to  uppercase 
 c = vowels 
 d = sorted(c)  #  Sorts  characters  of  the  uppercase  string  to  form  a  list 
 e = { }  # Empty  dictionary 
 for  ch  in   d:  # ch  is   each  char  of  the  list 
         if  ch . isalpha():  #  Is  ch  an  alphabet 
                 e[ch] = e . get(ch , 0) + 1   
 # End  of  for  loop 
 print(e) 
  
 ''' 
  
  
 # Find outputs  (Home  work) 
 def   f1(): 
         print('Hyd') 
         print('Sec') 
         print('Cyb') 
 # End  of  the  function 
 print('Begin') 
 x = f1() 
 print(x)---> #  
 Begin 
 Hyd 
 Sec 
 Cyb 
 print(type(x))---> <Class str> 
 print('End')---> End 
  
  
  
 # Find  outputs  (Home  work) 
 def  f1(): 
         return   10 , 20 , 30 
 # End  of  the  function 
 x = f1() 
 print(x)---> 10 , 20 , 30 
 print(type(x))--> <Class str> 
 a , b , c =  f1()    
 print(a)--> 10 
 print(b)--->20 
 print(c)--->30 
 print('for  loop')---> for loop 
 for  k   in   f1(): 
         print(k)--->10 , 20 , 30 
  
 # Find  outputs 
 def    f1(): 
         return  10 
         return  20 
         return  30 
 # End  of  the  function 
 print('Begin') 
 x = f1()   
 print(x)---> return 10 
              return  20 
              return  30 
 print('End')---> End 
 return   100---> return 100 
  
 #  Find  outputs 
 f1()  ---> Error 
 def   f1(): 
         print('Hello') 
 print(f1())   
 print(f1) 
  
 # Find  outputs  (Home  work) 
 print('Hello') 
 def  f1(): 
         print('f1  function') 
 #End  of   function 
 print('Hi') 
 print(f1()) 
 print(f1) 
 print('Bye') 
  
  
 ---> Hello 
      f1 function 
      Hi 
      f1 function 
      f1 
      Bye 
  
 #  Find  outputs 
 def    f1(): 
         print('Hyd') 
         print('Sec') 
         print('Cyb') 
 #End  of  the  function 
 print('Begin') 
 print(type(f1)) 
 print(id(f1)) 
 print('End') 
  
  
 --> Begin 
    <Class str> 
     address of f1 
     End 
     Hyd 
     Sec 
     Cyb