import numpy as np

def extract_data(filename):
    """Extracts data from a given file and stores values as floats in a list"""
    with open(filename, 'r') as reader:
        reader.readline()
        temp = []
        for line in reader:
            split = [float(x) for x in line.split()]
            for x in split:
                temp.append(x)
    return temp

def write_formatting(filename, list1, list2):
    """Writes a formatted table of two lists to a file"""
    with open(filename, "w+") as writer:
        writer.write(f"Temperatures in Oslo in degrees Celsius for October 1945 and 2014" + "\n")
        writer.write(f"1945     2014" + "\n")
        writer.write("-"*15 + "\n")
        for temp1, temp2 in zip(list1, list2):
            writer.write(f"{temp1:<9}{temp2}" + "\n")
    return

def print_temp_info(temp):
    """Prints mean, max and min values of a list"""
    mean = np.mean(temp)
    max = np.max(temp)
    min = np.min(temp)
    print(f"Mean temperature: {mean:.1f} degrees \nMax temperature: {max} degrees \nMin temperature: {min} degrees \n")
    return

# Stores data in two lists
oct_1945 = extract_data("temp_oct_1945.txt")
oct_2014 = extract_data("temp_oct_2014.txt")

# Writes formatted table to a file called "temp_formatted.txt"
write_formatting("temp_formatted.txt", oct_1945, oct_2014)

# Prints mean, max and min of each year
temps = { "1945":oct_1945, "2014":oct_2014}
for year in temps:
    print(f"Temperature information for October {year}:")
    print_temp_info(temps[year])

"""
Terminal >> temp_read_write.py
Temperature information for October 1945:
Mean temperature: 6.5 degrees
Max temperature: 11.6 degrees
Min temperature: 2.1 degrees

Temperature information for October 2014:
Mean temperature: 8.9 degrees
Max temperature: 13.6 degrees
Min temperature: 2.3 degrees
"""
