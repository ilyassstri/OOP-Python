# Innner Function -> adalah fungsi/method yang berada di dalam method

""" Contoh 1 """
class Game:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def info(self):
        def print_title():
            print(f"Title : {self.title}")
        
        def print_price():   
            print(f"Price : {self.price}")

        print_title()
        print_price()
        

ilyas = Game("Cyberpunk", 120)
ilyas.info()

""" Contoh 2 """
# class Game:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price

#     def info(self):
#         def print_title():
#             return f"Title : {self.title}"
        
#         # def print_price():   
#         #     return f"Price : {self.price}"

#         return print_title
        
# ilyas = Game("Cyberpunk", 120)
# title = ilyas.info()
# print(title)
# print(title())
