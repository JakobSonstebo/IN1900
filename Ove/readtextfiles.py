
def extract_data(filename):
    with open(filename, 'r') as reader:
        reader.readline()
        months = []
        rainfall = []
        for line in reader:
            words = line.split()
            months.append(words[0])
            rainfall.append(float(words[1]))
    annual = (months.pop(-1), rainfall.pop(-1))
    return months, rainfall, annual

months, values, annual = extract_data('rainfall.dat')
print(f"The average rainfall of months:")
for month, value in zip(months, values):
    print(f"{month}: {value}")
print(f"The average rainfall of the year: {annual[1]}")
