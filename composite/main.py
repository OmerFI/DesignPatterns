# References
# https://youtu.be/iSG87hpAFhQ
# https://www.tutorialspoint.com/design_pattern/composite_pattern.htm

class Employee:
    def __init__(self, name: str, dept: str, salary: int) -> None:
        self.name = name
        self.dept = dept
        self.salary = salary
        self.subordinates = []

    def add(self, e) -> None:
        self.subordinates.append(e)

    def remove(self, e) -> None:
        self.subordinates.remove(e)

    def getSubordinates(self) -> list:
        return self.subordinates

    def __str__(self) -> str:
        return f"Employee :[ Name : {self.name}, dept : {self.dept}, salary :{self.salary} ]"


CEO = Employee("John", "CEO", 30000)

headSales = Employee("Robert", "Head Sales", 30000)

headMarketing = Employee("Michel", "Head Marketing", 20000)

clerk1 = Employee("Laura", "Marketing", 10000)
clerk2 = Employee("Bob", "Marketing", 10000)

salesExecutive1 = Employee("Richard", "Sales", 10000)
salesExecutive2 = Employee("Rob", "Sales", 10000)

CEO.add(headSales)
CEO.add(headMarketing)

headSales.add(salesExecutive1)
headSales.add(salesExecutive2)

headMarketing.add(clerk1)
headMarketing.add(clerk2)

print(CEO)
for headEmployee in CEO.getSubordinates():
    print(headEmployee)

    for employee in headEmployee.getSubordinates():
        print(employee)
