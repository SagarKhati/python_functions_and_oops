class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
class EmployeesList(list):
    def search(self, name):
        matching_employees = []
        for employee in self:
            if name in employee.fname:
                matching_employees.append(employee.fname)
        return matching_employees
class Employee(Person):
    all_employees = EmployeesList()
    def __init__(self, fname, lname, empid):
        Person.__init__(self, fname, lname)
        self.__empid = empid
        Employee.all_employees.append(self)
    def getEmpid(self):
        return self.__empid
e1 = Employee('Jack', 'simmons', 456342)
print(e1.fname, e1.lname)
print(e1.getEmpid())
#print(e1.__empid)  #AttributeError: 'Employee' object has no attribute '__empid'
