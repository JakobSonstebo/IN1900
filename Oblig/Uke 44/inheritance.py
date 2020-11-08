# Oppgave a
class Mammal(object):
    def __init__(self):
        pass #:)

    def info(self):
        return f'I have hair on my body '

    def identity_mammal(self):
        print(f'I am a mammal')

# Oppgave b
class Primate(Mammal):
    def __init__(self):
        super().__init__()

    def info(self):
        return super().info() + f'and I have a large brain'

    def identity_primate(self):
        print(f'I am a primate')

# Oppgave c
class Human(Primate):
    def __init__(self):
        super().__init__()

    def info(self):
        return super().info() + f', also I understand math'

    def identity_human(self):
        print(f'I am a human')


class Ape(Primate):
    def __init__(self):
        super().__init__()

    def info(self):
        return super().info() + f', but I don\'t understand math'

    def identity_ape(self):
        print('I am an ape')


john = Human()
julius = Ape()

# John
print(john.info())
john.identity_mammal()
john.identity_primate()
john.identity_human()
# john.identity_ape()

print('\n')

# Julius
print(julius.info())
julius.identity_mammal()
julius.identity_primate()
julius.identity_ape()
# julius.identity_human()

print('\n')

# Oppgave d
print('Are John and Julius mammals, primates, humans, apes?')
for animal in [Mammal, Primate, Human, Ape]:
    print(f'John: {isinstance(john, animal)}, Julius: {isinstance(julius, animal)}')

"""
Terminal>>python inheritance.py
I have hair on my body and I have a large brain, also I understand math
I am a mammal
I am a primate
I am a human
I have hair on my body and I have a large brain, but I don't understand math
I am a mammal
I am a primate
I am an ape
Are John and Julius mammals, primates, humans, apes?
John: True, Julius: True
John: True, Julius: True
John: True, Julius: False
John: False, Julius: True
"""