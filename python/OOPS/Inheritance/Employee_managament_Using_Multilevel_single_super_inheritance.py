class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name=name
        self.salary=salary
    def show_details(self):
        print("Employee ID: ",self.id)
        print(f"Name: {self.name}")
        print("Salary: ",self.salary)

class Programmer(Employee):
    def __init__(self,id,name,salary,lang):
        super().__init__(id,name,salary)
        self.lang=lang
    def show_details(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print("Salary: ",self.salary)
        print("Programming Language: ",self.lang)


class TeamLeader(Programmer):
    def __init__(self,id,name,salary,lang,team_size):
        super().__init__(id,name,salary,lang)
        self.team_size=team_size
        
    def show_details(self):
        print(f"Employee ID: {self.id}")
        print(f"Name: {self.name}")
        print("Salary: ",self.salary)
        print("Programming Language: ",self.lang)
        print("Team Size: ",self.team_size)

emp = Employee(5,"pavan",40000)
emp.show_details()
print("--------------------------------")
pro=Programmer(1,"babu",50000,"python")
pro.show_details()
print("------------------------------")
tl=TeamLeader(2,"babbi",60000,"SQL",8)
tl.show_details()








"""
Employee ID:  5
Name: pavan
Salary:  40000
--------------------------------
Employee ID: 1
Name: babu
Salary:  50000
Programming Language:  python
------------------------------
Employee ID: 2
Name: babbi
Salary:  60000
Programming Language:  SQL
Team Size:  8
"""