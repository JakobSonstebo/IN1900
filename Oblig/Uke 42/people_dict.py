def read_person_data(file):
    """Reads file and creates dictionary with structre name: {'Age': age, 'Gender': gender"""
    with open(file, 'r') as reader:
        people_dict = {}
        for line in reader:
            person = line.split(', ')
            name = person[0]
            age = person[1]
            gender = person[2].strip('\n')
            people_dict[name] = {'Age': age, 'Gender': gender}
    return people_dict


def write_person_data(dictionary, file):
    """Writes person data back to a new file in the same format as the original"""
    with open(file, 'w') as writer:
        for person in dictionary:
            age = dictionary[person]['Age']
            gender = dictionary[person]['Gender']
            print(f"{person}, {age}, {gender}", file=writer)
    return


p_dict = read_person_data('people_dict.txt')
write_person_data(p_dict, 'people_dict2.txt')

"""
Legger ved people_dict2.txt for referanse. 
"""