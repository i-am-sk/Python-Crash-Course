# Return values

def get_formatted_name(first, last) :
    """Return a full name, neatly formatted."""
    full_name = f"{first} {last}"
    return full_name.title()

developer = get_formatted_name("sai", "krishna")
print(developer)

## make an argument optional

def get_formatted_names(first, last, middle='') :
    if middle :
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


developer = get_formatted_names('sai', 'thokala', 'krishna')
print(developer)

developer = get_formatted_names('sai', 'krishna')
print(developer)

### Returning a dictionary

def build_person(first, last):
    """Return a dictionary of info of a person"""
    person = {
            'first' : first,
            'last'  : last,
        }
    return person

doctor = build_person('krishna', 'thokala')
print(doctor)


def build_person2(first, last, age = None, middle = ''):
    """Return a dictionary of info of a person"""

    if middle:
        person = {
            'first' : first,
            'last' : last,
            'middle' : middle
        }
    else:
        person = {
            'first': first,
            'last': last,
        }

    if age:
        person['age'] = age
    
    return person

engineering = build_person2('sai', 'krishna', 21)
robot = build_person2('Jackey', 'robot')
print(robot)

student = build_person2('sai', 'thokala', 21, 'krishna')
print(engineering)
print(student)

def greet_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name

while True:
    print("\nPlease tell your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = greet_formatted_name(f_name, l_name)
    print(formatted_name)



