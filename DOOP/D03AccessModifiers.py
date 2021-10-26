class Employee:
    def __init__(self, ID, salary):
        self.ID = ID  # ID is a public property
        self.__salary = salary  # salary is a private property

    def displayID(self):
        print("ID:", self.ID)

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displayID()
# Steve.__displayID # this will generate an error
Steve.displaySalary()
print(Steve._Employee__salary)  # accessing a private property

