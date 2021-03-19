# Inheritance, extened
class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def work(self):
        return f"{self.name} is working"

class Programmer(Employee): # Inheritance
    def __init__(self, name, email, level):
        super().__init__(name, email)
        self.level = level

    def debug(self): # extend -> adalah attribute atau method yang tidak dipunyai dari induk inheritance
        return "debuging"

employee = Employee("Ilyas", "trikhaqiqi@gmail.com")
print(employee.work())
# print(employee.debug()) error

programmer = Programmer("trikhaqiqi", "trikhaqiqi@company.com", "senior")
print(programmer.work())
print(programmer.debug())