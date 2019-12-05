# Dictionaries

student = {'name': 'Sai Krishna', 'Grade': 8.9}

print(
    f"Dictionaries : \n Student name is {student['name']}, \n {student['name']} grade is {student['Grade']}")

# A dictionary in python is a collection of *key-value pairs*. Each key is connected
# to a value,and you can use a key to access the value associated with that key.

# Adding New key-value pairs

student['mobile'] = 9100525170
student['age'] = 21

print(student)

# modifying values in a dict.

student['name'] = 'Tharun'

print(student)

# Using get() to Access Values

alien_0 = {
    'color': 'green',
    'speed': 'slow'
}

# === use the get() method to set a default value that will be returned,
# if the requested key doesn’t exist. ===

point_value = alien_0.get('points', 'No point value is aasigned')
print(point_value)


########### === Looping Through a Dictionary === ##################


user_0 = {
    'username': 'saikrishna',
    'first': 'Sai',
    'last': 'Krishna'
}

for key, value in user_0.items():
    print(f"\nKey: {key}, \nValue: {value}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


for key, value in favorite_languages.items():
    print(f"\nKey: {key}, \nValue: {value}")

print("\n")

for key, value in favorite_languages.items():
    print(f"{key.title()} favorite language is {value.title()}.")


# accessing only "key" of dict's using keys() method

for name in favorite_languages.keys():
    print(name.title())


# Here in below example we can access the "value" of "key"  while using a keys() method


friends = ['jen', 'sarah', 'edward', 'phil']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"{name.title()}, I see you love {language}")

# Sorting the key-value pairs in dict. by looping

for name in sorted(favorite_languages.keys()):
    language = favorite_languages[name].title()
    print(f" {name.title()}, your favorite language is {language}")


# accessing only "value" of dict's using values() method

print("\nList of languages used are:")
for value in favorite_languages.values():
    print(value.title())

# above apporach pulls all the value out without checking for repeats.
# For that we use set() method

# A "Set" is a collection in which each item must be unique:


print("\nList of languages used are:")
for value in set(favorite_languages.values()):
    print(value.title())

###### === NESTING === #############

# nesting is ===  storing multiple dict's in a list or
# a list of items as a value in a dictionary.


# A List of Dictionaries -->

print("\nA List of Dictionaries --> \n")

alien_0 = {
    'color': 'green',
    'points': 4
}

alien_1 = {
    'color': 'red',
    'points': 5
}

alien_2 = {
    'color': 'yellow',
    'points': 3
}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Making an aliens using code that automatically generates each alien


print("\n\n")
aliens = []

for alien_num in range(100):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'medium'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

print("...")

print(f"Total number of aliens generated is: {len(aliens)}")


# generating an aliens with different char's

aliens = []

for i in range(100):
    new_alien = {'color': 'green', 'points': 10, 'speed': 'fast'}
    aliens.append(new_alien)

for alien in aliens[:10]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 3
        alien['speed'] = 'slow'


for alien in aliens[10:30]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 6
        alien['speed'] = 'medium'


for alien in aliens[:3]:
    print(alien)

for alien in aliens[10:13]:
    print(alien)

for alien in aliens[30:33]:
    print(alien)


# List in a Dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra-cheese']
}

print(
    f"\nYou ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}


for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favorite languages are: ")
        for language in languages:
            print(f"\t {language.title()}")
    elif len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t {language.title()}")

 # A Dictionary in a Dictionary

users = {
    'saikrishna': {
        'first': 'Sai',
        'last': 'Krishna',
        'location': 'Hyderabad'
    },
    'tharunkumar': {
        'first': 'Tharun',
        'last': 'Kumar',
        'location': 'suryapet'
    }
}


for username, user_info in users.items():
    print(f"\nUserName: {username}")
    full_name = f"{user_info['first'].title()} {user_info['last'].title()}"
    location = user_info['location']

    print(f"\t Full Name: {full_name}")
    print(f"\t Location: {location.title()}")




