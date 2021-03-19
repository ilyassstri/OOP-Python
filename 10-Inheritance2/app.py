# override
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
print(employee.work())

programmer = Programmer("trikhaqiqi", "trikhaqiqi@company.com", "senior")
print(programmer.work())

ui_designer = UIDesigner("Kukuh aldy", "kukuh@gmail.com", "senior", "Figma")
print(ui_designer.work())
