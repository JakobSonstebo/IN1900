def read_moon(file):
    """ Reads file and creates dict with density values for different elements in the moons atmosphere"""
    with open(file, 'r') as reader:
        reader.readline()
        elements = {}
        for line in reader:
            line_elements = line.split(";")
            for element in line_elements:
                element = element.split("-")

                # Key stripped and in upper case
                key = element[0].strip().upper()

                # Value formatted
                value = element[1]
                new_char = [',', '\n']
                for char in new_char:
                    value = value.replace(char, "")
                value = float(value)

                # Add to dict
                elements[key] = value
    return elements


print(read_moon('atm_moon.txt'))

"""
Terminal>> python atm_moon.py
{'HELIUM 4': 40000.0, 'NEON 20': 40000.0, 'HYDROGEN': 35000.0,
'ARGON 40': 30000.0, 'NEON 22': 5000.0, 'ARGON 36': 2000.0,
'METHANE': 1000.0, 'AMMONIA': 1000.0, 'CARBON DIOXIDE': 1000.0}
"""
