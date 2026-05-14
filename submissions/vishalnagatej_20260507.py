class Employee:
	def get(self):
		self.empno = int(input('Enter Employee Number : '))
		self.empname = input('Enter Employee Name : ')
		self.sal = float(input('Enter Salary : '))
		self.city = input('Enter City : ')
		self.grosspay = 0
		self.netpay  = 0
	def compute(self):
		da = 0.30 * self.sal
		hra = 0.20 * self.sal
		if self.city.lower() == "hyd":
			cca = 1000
		else:
			cca = 2500
		self.grosspay = self.sal + da + hra + cca
		pf = 0.08 * self.grosspay
		if pf > 2400:
			pf = 2400
		if self.grosspay < 10000:
			tax = 0.10 * self.grosspay
		else:
			tax = 0.15 * self.grosspay
		self.netpay = self.grosspay - pf - tax
	def display(self):
		print('Employee Number :', self.empno)
		print('Employee Name   :', self.empname)
		print('Salary          :', self.sal)
		print('City            :', self.city)
		print('Gross Pay       :', self.grosspay)
		print('Net Pay         :', self.netpay)
a = Employee()
a.get()
a.compute()
a.display()

