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

class Manager(Employee):
    #create a new initializer to accept the Employees
    def __init__(self,firstName,lastName,pay,employees=None):
        #just inherir the __init__ of Parent Class
        super().__init__(firstName,lastName,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_Employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_Employee(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_Employees(self):
        for emp in self.employees:
            print('----->', emp.email)            


emp_1 = Employee('Sai','Kotha',30000)
emp_2 = Employee('Sahani','Reddy',30000)

mgr_1 = Manager('Sahani','Shetty',50000,[emp_1])
print(mgr_1.firstName)
print(mgr_1.lastName)

mgr_1.add_Employee(emp_2)
print(mgr_1.print_Employees())


