#Find number of emp in a class

class Employee:
    
    num_of_emp = 0
    raise_amount = 1.04 # Class variable
    
    def __init__(self, first, last, pay):#init method knows as initialize, instance is self
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'#All instance variable created using init method
        
        Employee.num_of_emp += 1
    
    def fullname(self):
        return format('{} {}'.format(self.first, self.last))
        
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) #Class variable is picked up using class 
        #self.pay = int(self.pay * self.raise_amount) #Instance variable used as to refer class variable

print(Employee.num_of_emp)

emp_1 = Employee('Tanmay', 'Dhapodkar', 50000)
emp_2 = Employee('Test', 'Name', 60000)
emp_3 = Employee('Name', 'Test', 100000)

print(Employee.num_of_emp)
