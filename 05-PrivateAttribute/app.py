# Private Attribute
class User:
    total = 0 
    def __init__(self, name, email, role): 
        self.name = name 
        self.email = email
        self.__role = role # private attribute di python memakai __role
        User.total += 1 

    def info(self): 
        return f"Hallo nama saya {self.name} email {self.email} posisi sebagai {self.__role} "

    def update_role(self, new_role):
        if self.__role != "user":
            self.__role = new_role

    def getRole(self):
        return self.__role

ilyas = User("ilyas", "trikhaqiqi@gmail.com", "user")
# print(ilyas.info())
# ilyas.update_role("moderator")
# ilyas.__role = "moderator"
# print(ilyas.info())

print(ilyas.__dict__)
print(ilyas._User__role)
print(ilyas.info())
ilyas._User__role = "moderator"
print(ilyas.info())

print(ilyas._User__role)
print(ilyas.getRole())
