"""Constructor adalah method yang ada didalam sebuah class tapi dijalankan pertama kali 
ketika saat membuat object dari suatu class, proses membuat object dari suatu class disebut 
dengan instance atau instansiasi
"""
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

# class User:
#     def __init__(self, name, email, role):
#         self.name = name
#         self.email = email
#         self.role = role

# ilyas = User("ilyas", "trikhaqiqi@gmail.com", "User")
# otong = User("otong", "otong@gmail.com", "admin")

# print(otong.name)
# print(otong.email)
# print(otong.role)


# class Mahasiswa:
#     #initializer
#     def __init__(self):
#         self.nim = "M0501001"
#         self.nama = "Uzumaki Saburo"
#         self.alamat = "Konohagakure"

#     # menampilkan isi atribut
#     def printMhs(self):
#         print(self.nim)
#         print(self.nama)
#         print(self.alamat)

# # membuat object dari class Mahasiswa
# objMhs = Mahasiswa()

# # memanggil method printMhs 
# objMhs.printMhs()

""" Contoh 3  | Cara define langsung"""
class Programmer:
    def __init__(self):
        self.name = "ilyas"
        self.role = "developer"
        self.email = "trikhaqiqi@gmail.com"

    # kalau ingin menampilkannya secara langsung
    def printProgrammer(self):
        print(self.name)
        print(self.role)
        print(self.email)

objectProgrammer = Programmer()
objectProgrammer.printProgrammer()

""" Contoh 4 | cara define diakhir """
class ITSupport:
    def __init__(self, name, role):
        self.name = name
        self.role = role

pegawai = ITSupport("irln", "IT Support")
print(pegawai.name)
print(pegawai.role)