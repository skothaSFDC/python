class Employee:
    
    #variable when accessed using self can be assigned a value for each instance
    hikePercentage = 1.5
    #class level variable
    numberOfEmployees = 0
    #when a class has an __init__ by default all the methods will have class instance has the parameter
    def __init__(self,firstName,lastName,pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + lastName + '@gmail.com'
        self.pay = pay
    
        Employee.numberOfEmployees += 1
    #Method to return the full name
    def full_name(self):
        return '{} {}'.format(self.firstName,self.lastName)

    #method to calculate the total annual hike
    def calculate_hike(self):
      self.pay = int(self.pay * self.hikePercentage)

    #Methods with this annotation take class as aparameter instead of self(instance)
    @classmethod
    def createEmployees(cls,emp_Str):
        first,last,pay = emp_Str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def printEmployInfo(emp_Str):
        emp_1 = Employee.createEmployees(emp_Str)
        print(emp_1.firstName)
        print(emp_1.lastName)
        print(emp_1.email)
        print(emp_1.pay)

class Developer(Employee):
    hikePercentage = 2.5

dev_1 = Developer('Sai','Shetty',100000)
print(dev_1.pay)
dev_1.calculate_hike()
print(dev_1.pay)

#Developer.printEmployInfo('Sai-Sahani-50000')
