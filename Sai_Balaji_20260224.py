
 from math import  sqrt , pow ,gcd,factorial
 a=10
 b=7
 print(f"{a} + {b} = {a+b}")
 print(f"{a} - {b} = {a-b}")
 print(f"{a} * {b} = {a*b}")
 print(f"{a} / {b} = {a/b}")
 print(f"{a} % {b} = {a%b}")
 m=max(a,b)
 print(f"max({a},{b}) = {m}")
 mi=min(a,b)
 print(f"min({a},{b}) = {mi}")
 s=sqrt(a)
 print(f"sqrt({a}) = {s}")
 p=pow(a,b)
 print(f"{a}^{b} = {p}")
 g=gcd(a,b)
 print(f"gcd({a},{b}) = {g}")
 f=factorial(a)
 print(f"fact({a}) = {f}")


 x=25
 y='Hyd'
 print(f"before swap : {x=}    {y=}")
 x ,y = y ,x
 print(f"after swap  : {x=} {y=}")



 x=eval(input("enter x : "))
 y=eval(input("enter y: "))
 print(f"{x} is largest") if x > y else print(f"{y} is largest")



 x=eval(input("enter x : "))
 y=eval(input("enter y: "))
 z=eval(input("enter z: "))
 print(f"{x} is largest") if x > y else print(f"{y} is largest") if y > z else print(f"{z} is largest")


 x=eval(input("enter x : "))
 y=eval(input("enter y: "))
 print(">") if x > y else print("<") if x < y else print("=")


 x=eval(input("enter x : "))
 print("1") if x > 0 else print("-1") if x < 0 else print("0")


 x=eval(input("enter x : "))
 print("even") if x % 2 == 0 else print("odd") 
