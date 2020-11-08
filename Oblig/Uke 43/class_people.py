class Person(object):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def change_name(self, new_name):
        self.name = new_name

    def change_gender(self, new_gender):
        self.gender = new_gender

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'


# John
john = Person('John', 55, 'Male')
print(john)

# John becomes Anita
john.change_gender('Female')
john.change_name('Anita')
anita = john
print(anita)

"""
Terminal>>python class_people.py
Name: John, Age: 55, Gender: Male
Name: Anita, Age: 55, Gender: Female
"""