#Automate the Employee details with init function

class Employee:
    def __init__(self, first, last, pay):#init method knows as initialize, instance is self
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'#All instance variable created using init method
        
#Create instances for the variables
 
emp_1 = Employee('Tanmay', 'Dhapodkar', 34000)
emp_2 = Employee('Test', 'Name', 67000)

print ('{} {}'.format(emp_1.first, emp_1.last))

print(emp_1.email)
print(emp_2.email)
        
