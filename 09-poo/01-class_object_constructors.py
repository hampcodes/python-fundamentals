class Person:
    def __init__(self, name, age, dni):
        self.name = name       # público
      

    def show_info(self):
        print("Name:", self.name)
       
   

p1 = Person("Henry")

p1.show_info()


print(p1.name)     # OK
