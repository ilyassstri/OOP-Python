"""Instance Variable VS Class Variable """
class User:
    total = 0 # Class variable
    def __init__(self, name, email, role): # Intance variable
        self.name = name # self -> berlaku untuk dirinya sendiri
        self.email = email
        self.role = role
        User.total += 1 # User mengacu kepada class user dan berlaku untuk semua

# Instance variable adalah nilai attribute yang dimiliki dan berlaku oleh masing masing object dan contohnya seperti dibawah ini
ilyas = User("ilyas", "trikhaqiqi@gmail.com", "User")
print(User.total)

otong = User("otong", "otong@gmail.com", "admin")
print(User.total)

mario = User("mario", "mario@gmail.com", "user")
print(User.total)

# Class variable nilainya berlaku dalam lingkup class dan sifatnya global
print(User.total)