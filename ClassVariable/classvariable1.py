#Class Variables

#Class variables are variables are shared among all instances of a Class
#Instance variable can be unique to each instance, class variable should be the same among instances

class Employee:
    
    raise_amount = 1.04 # Class variable
    
    def __init__(self, first, last, pay):#init method knows as initialize, instance is self
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'#All instance variable created using init method
    
    def fullname(self):
        return format('{} {}'.format(self.first, self.last))
        
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) #Class variable is picked up using class 
        #self.pay = int(self.pay * self.raise_amount) #Instance variable used as to refer class variable

emp_1 = Employee('Tanmay', 'Dhapodkar', 50000)
emp_2 = Employee('Test', 'Name', 60000)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)
print(Employee.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)
