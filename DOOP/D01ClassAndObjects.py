class MyClass:
    pass


class Employee:
    ID = 3789
    salary = 2500
    department = "Human resources"


class Initializer:
    myid = 12  # class variables
    salary = 14
    department = "123"

    def __init__(self, myid, salary, department):
        self.myid = myid  # instance variables
        self.salary = salary
        self.department = department


# execute the function here first
Mark = Initializer(1, 2, "HR")
print("Mark")
print("ID :", Mark.myid)
print("Salary :", Mark.salary)
print("Department :", Mark.department)


# execute the function second
if __name__ == '__main__':
    obj = MyClass()
    print(obj)
    Steve = Employee()
    print("ID: ", Steve.ID)
    print("Salary: ", Steve.salary)
    print("Department: ", Steve.department)
