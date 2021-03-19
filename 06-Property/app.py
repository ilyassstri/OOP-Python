# Property

class User:
    total = 0 
    def __init__(self, name, email, role): 
        self.name = name 
        self.email = email
        self.__role = role
        User.total += 1 

    def info(self): 
        return f"Hallo nama saya {self.name} email {self.email} posisi sebagai {self.__role} "

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, new_role):
        if self.__role != "user":
            self.__role = new_role

ilyas = User("ilyas", "trikhaqiqi@gmail.com", "user") # kalo user sudah dirubah menjadi moderator maka baru bisa dirubah

print(ilyas.info())
ilyas.role = "super admin"
print(ilyas.info())
