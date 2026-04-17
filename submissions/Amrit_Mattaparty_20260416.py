#1
# Find outputs (Home work)
class c1:
    x = 10
    def _init_(self):
        self.y = 20
a = c1()
b = c1()
a.x = 30
b.y = 40
print(b.x) # 10  (b.x reads class attribute x; b did not shadow x with b.x)
print(b.y) # 40
print(a.x) # 30  (a.x is an instance‑level override of class x)
print(a.y) # 20
print(c1.x) # 10  (class attribute x unchanged)
print('Object a : ', a._dict_) # Object a :  {'x': 30, 'y': 20}
print('Object b : ', b._dict_) # Object b :  {'y': 40}
print(c1._dict_) # c1 class dict with x=10, methods, etc. (x still 10).



#2
# Find outputs (Home work)
class c1:
    x = 10
    def _init_(self):
        self.y = 20
a = c1()
b = c1()
a.x += 1
b.y += 1
print(a.x) # 11  (a.x becomes an instance attribute after read + assignment)
print(a.y) # 20
print(b.x) # 10  (b did not write to b.x; it still reads class x)
print(b.y) # 21
print(c1.x) # 10  (class attribute x is unchanged)
print(a._dict_) # {'x': 11, 'y': 20}
print(b._dict_) # {'y': 21}
print(c1._dict_) # c1 class dict showing x=10.



#3
# Find outputs (Home work)
class c1:
    x = 10
    def m1(self):
        self.x = 20
a = c1()
a.m1()
print(c1.x) # 10  (class x unchanged)
print(a.x) # 20  (a.x is now an instance‑level shadow of c1.x)