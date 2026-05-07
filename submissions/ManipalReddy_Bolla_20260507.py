#  Write  a  program  to  determine  total  and  average  of  student  and  gross pay  and  net  pay  of  teacher
from abc import *
class person(ABC):
    def get(self):
        self.number = int(input("Enter number: "))
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.gender = input("Enter gender: ")

    def disp(self):
        print(f"{self.number}\t{self.name}\t{self.age}\t{self.gender}", end='\t')

    @abstractmethod
    def compute(self):
        pass

class student(person):
    def get(self):
        super().get()
        self.marks = []
        for i in range(1, 4):
            m = int(input(f"Enter marks of subject {i}: "))
            self.marks.append(m)

    def compute(self):
        self.totalmarks = sum(self.marks)
        self.avgmarks = self.totalmarks / len(self.marks)

    def disp(self):
        super().disp()
        print(f"{self.totalmarks}\t{self.avgmarks:.2f}")

class teacher(person):
    def get(self):
        super().get()
        self.subject = input("Enter subject: ")
        self.salary = int(input("Enter salary: "))
        self.city = input("Enter city: ")

    def compute(self):
        da = self.salary * 0.50
        hra = self.salary * 0.20
        cca = 1000 if self.city == 'Hyd' else 800
        
        self.grosspay = self.salary + da + hra + cca
        
        pf = self.grosspay * 0.08
        if pf > 400:
            pf = 400

        if self.grosspay < 10000:
            tax = self.grosspay * 0.10
        else:
            tax = self.grosspay * 0.15
            
        self.netpay = self.grosspay - pf - tax

    def disp(self):
        super().disp()
        print(f"{self.subject}\t{self.salary}\t{self.grosspay}\t{self.netpay}")

def menu():
    print('\n1. Teacher')
    print('2. Student')
    print('3. Exit')

a = []
while True:
    menu()
    ch = int(input('Enter choice : '))
    
    if ch == 1:
        obj = teacher()
        obj.get()
        obj.compute()
        a.append(obj)
    elif ch == 2:
        obj = student()
        obj.get()
        obj.compute()
        a.append(obj)
    elif ch == 3:
        break
    else:
        print("Invalid choice, try again.")

print('\nTeachers')
for x in a:
    if isinstance(x, teacher):
        x.disp()

print('\nStudents')
for x in a:
    if isinstance(x, student):
        x.disp()

print('Good Bye')



#  Write  a  progran  to  add  num  class  objects  and  join  str  class  objects 
from abc import abstractmethod, ABC
class datatype(ABC):
    @abstractmethod
    def get(self):
         pass
    @abstractmethod
    def add(self, m, n):
        pass
    @abstractmethod
    def display(self):
        pass

class number(datatype):
    def get(self):
        self.x = int(input("Enter a number : "))
    
    def add(self, m, n):
        self.sum = m.x + n.x
        
    def display(self):
        print('Sum of the numbers : ', self.sum)

class string(datatype):
    def get(self):
        self.x = input("Enter a string : ")
    
    def add(self, m, n):
        self.join = m.x + n.x
        
    def display(self):
        print('Join of the two strings : ', self.join)

def menu():
    print('\n1. Add numbers')
    print('2. Join Strings')
    print('3. Exit')

# Main Logic
while True:
    menu()
    ch = eval(input('Enter choice : '))  
    
    if ch == 1:
        a = []
        for i in range(3):
            obj = number()
            a.append(obj)
    elif ch == 2:
        a = []
        for i in range(3):
            obj = string()
            a.append(obj)
    elif ch == 3:
        break
    else:
        print("Invalid Choice")
        continue
    print("For the first input:")
    a[0].get()
    print("For the second input:")
    a[1].get()
    a[2].add(a[0], a[1])

    # 3. Print the 3rd object
    a[2].display()

print('Good Bye')