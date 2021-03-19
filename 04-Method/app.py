class User:
    total = 0 
    def __init__(self, name, email, role): 
        self.name = name 
        self.email = email
        self.role = role
        User.total += 1 

    # behavior untuk memperkenalkan diri
    def info(self): # self ini wajib dalam membuat method untuk suatu class
        return f"Hallo nama saya {self.name} email {self.email} posisi sebagai {self.role} "

    # mengupdate role atau mengubah state behavior dan enkapsulapsi
    def update_role(self, new_role):
        if self.role != "user": # enkapsulapsi
            self.role = new_role # tidak bisa diupdate sembarangan 

ilyas = User("ilyas", "trikhaqiqi@gmail.com", "user")
print(ilyas.info())
print("Contoh 1")
ilyas.update_role("moderator")
print("Contoh 2")
ilyas.role = "moderator"
print(ilyas.info())

# otong = User("otong", "otong@gmail.com", "admin")
# print(otong.info())
