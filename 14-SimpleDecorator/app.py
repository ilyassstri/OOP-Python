""" Simple Decorator

Sebuah fungsi bisa menerima fungsi yang lain.
decorator menambahkan behavior dari sebuah fungsi tanpa mengubah definisi asli fungsinya.

"""

def info(func):
    def wrapper():
        print("*" * 10)
        func()
        print("#" * 10)

    return wrapper

def say_hello():
    print("Hello World of python")

say_hello()
say_hello = info(say_hello)
say_hello() 

    