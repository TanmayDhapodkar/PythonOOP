#Method - Func associated with a class
class Employee: #Class is a blueprint of instances
    pass

#Unique instances of an Class
emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

#Instance Variable contains data that is unique to each instance

emp_1.first = 'Tanmay'
emp_1.last = 'Dhapodkar'
emp_1.email = 'dhapodkartanmay@company.com'
emp_1.pay = 35000

emp_2.first = 'Test'
emp_2.last = 'Name'
emp_2.email = 'TestName@company.com'
emp_2.pay = 76000

print(emp_1.email)
print(emp_2.pay)

#Above example is to manually create the instance variable and run through classes


