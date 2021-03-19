def info(func):
    def wrapper():
        print("*" * 10)
        func()
        print("#" * 10)

    return wrapper

@info # menjadi parameter untuk pemanggilan fungsi
def say_hello():
    print("Hello World of python")

say_hello() 
