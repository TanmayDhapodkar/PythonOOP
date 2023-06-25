#Mehtod to display full name
#Each method in a class automatically takes the instance as first argument

class Employee:
    def __init__(self, first, last, pay):#init method knows as initialize, instance is self
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'#All instance variable created using init method
    
    def fullname(self):
        return format('{} {}'.format(self.first, self.last))

emp_1 = Employee('Tanmay', 'Dhapodkar', 34000)
emp_2 = Employee('Test', 'Name', 67000)

print(emp_1.email)
print(emp_2.email)   
print(emp_2.fullname())

#run methods using class name itself
emp_2.fullname() #no need to pass self
print(Employee.fullname(emp_1)) #Does not know what instance you have to put in

------------------------------------------------------------

#run methods using class name itself

class Employee:
    def __init__(self, first, last, pay):#init method knows as initialize, instance is self
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'#All instance variable created using init method
    
    def fullname(self):
        return format('{} {}'.format(self.first, self.last))

emp_1 = Employee('Tanmay', 'Dhapodkar', 34000)
emp_2 = Employee('Test', 'Name', 67000)

emp_2.fullname() #no need to pass self
print(Employee.fullname(emp_1)) #Does not know what instance you have to put in
