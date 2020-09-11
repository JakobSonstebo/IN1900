with open('oxygen.txt', 'r') as reader:
    reader.readline()
    weight = []
    ab = []
    for line in reader:
        weight.append(float(line.split()[1]))
        ab.append(float(line.split()[2]))

M = sum(m*w for m, w in zip(weight, ab))
print(f"{M:.4f} g/mol")

"""
Terminal>>python read_file_isotopes.py
15.9994 g/mol
"""
