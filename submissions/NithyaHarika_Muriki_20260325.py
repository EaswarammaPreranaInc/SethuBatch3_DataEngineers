# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#'a  :  10  \t  b :  20
f1(b = 30 , a = 40)#a  :  30  \t  b : 40
f1(50 , 60)#error, because of * the args must be in keyword args only
f1(70 , b = 80)#error, because of * the args must be in keyword args only
f1(a = 15 , 25)#error, because of * the args must be in keyword args only

