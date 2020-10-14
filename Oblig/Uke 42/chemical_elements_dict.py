elements_10 = {1: '-', 2: 'Helium', 3: 'Lithium',4: 'Beryllium', 5: 'Boron', 6: 'Carbon',7: 'Nitrogen', 8: '-',9: 'Fluorine', 10: 'Neon'}
elements_10[1] = 'Hydrogen'
elements_10[8] = 'Oxygen'

elements_10_copy = elements_10.copy()
elements_10_copy.update({11: 'Sodium'})
print(elements_10)
print('\n')

elements_11 = elements_10
elements_11.update({11: 'Sodium'})
print(elements_10)

"""
Den første dictionarien er en kopi og den orginale vil derfor ikke bli påvirket når vi oppdaterer den. I det andre eksempelet gir vi bare elements_10
et ekstra navn, elements_11, så når vi endrer den endrer vi også den orginale.
"""
