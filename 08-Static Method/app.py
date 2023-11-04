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

    @classmethod
    def setTotal(cls, total): # cls itu mengacu ke user jadi bisa memakai cls atau memakai nama classnya
        User.total = total

    """ Membuat class method solusi dari constructor """
    @classmethod
    def from_string(cls, string_param):
        name, email, role = string_param.split("-")
        return User(name, email, role)

    """ Contoh Static method """
    # Perbedaan class method dan static method itu sama2 mengacu kepada nama kelas tapi tidak memiliki hubungan dengan cls, intance jadi tidak bisa ngakses
    @staticmethod
    def tweet(word):
        return word

ilyas = User("ilyas", "trikhaqiqi@gmail.com", "user")

tweet = User.tweet("Selamat sore, Saya sedang belajar OOP Python")
print(tweet)


