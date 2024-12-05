class Employe:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role: ",self.role)
        print("dept: ",self.dept)
        print("salary: ",self.salary)



class Engineer(Employe):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Ai Engineer", "IT", 12000)
eng1 = Engineer("Manoj",21)
eng1.showDetails()