# Constructor adalah method yang ada didalam sebuah class tapi dijalankan pertama kali ketika saat membuat object dari suatu class, proses membuat object dari suatu class disebut dengan instance atau instansiasi
# class ini sudah menambahkan attribute

""" Contoh 1 """
# class User:
#     def __init__(self):
#         print("Memcetak object baru")

# # ilyas, otong
# # mempunyai atribut name, email, role

# ilyas = User()
# otong = User()

""" Contoh 2 """
# ilyas, otong
# mempunyai atribut name, email, role

class User:
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

ilyas = User("ilyas", "trikhaqiqi@gmail.com", "User")
otong = User("otong", "otong@gmail.com", "admin")

print(otong.name)
print(otong.email)
print(otong.role)


