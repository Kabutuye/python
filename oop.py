# #object-oriented programing
# class Person:
#     def __init__(self):
#         self.name = "Umuro"
#         self.gender = "Male"
#         self.age = 19
#
# person = Person()
# person.name = "Tiff mchelewa class"
# print(person.name)


class People:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


person1 = People("Umuro", "Male", 19)

person2 = People("Ella", "Female", 17)

print(f"I am {person1.name}, a {person1.gender} of {19} years and i have a sister called {person2.name} she is {person2.age} years")
