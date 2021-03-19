# Polymorphism -> banyak bentuk 
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def work(self):
        return f"{self.name} is working"

class Programmer(Employee): 
    def __init__(self, name, email, level):
        super().__init__(name, email)
        self.level = level

    def debug(self): 
        return "debuging"

    # 0veride -> menimpa
    def work(self):
        return f"{self.name} is writing code."

class UIDesigner(Employee):
    def __init__(self, name, email, level, tools):
        super().__init__(name, email)
        self.level = level
        self.tools = tools

    def work(self):
        return f"{self.name} is designing some new cool product"

employee = Employee("Ilyas", "trikhaqiqi@gmail.com")
programmer = Programmer("trikhaqiqi", "trikhaqiqi@company.com", "senior")
ui_designer = UIDesigner("Kukuh aldy", "kukuh@gmail.com", "senior", "Figma")
 
def working(system): # tidak peduli punya parameter apa yang penting mempunyai parameter work dari kelas parent
    print(system.work())

class Manager: # tapi jika ada method work lain masih bisa berjalan dan tidak membuat error
    def __init__(self, name):
        self.name = name

    def work(self):
        return f"{self.name} is managing"

manager = Manager("Namanya manager")
working(manager)

working(employee)
working(programmer)
working(ui_designer)