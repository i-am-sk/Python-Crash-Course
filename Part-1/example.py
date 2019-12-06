# Lists
# --> Accessing lists by for loop
# --> Modifying lists

names = ['Sai Krishna', 'Tharun Kumar', 'Srinivas',
         'Naga Jyothi', 'Sruthi', 'Vaishnavi']

print(f"Accessing Lists: \n {names[0]}")

for name in names:
    print(f"\t{name}")

names[-2] = 'Sai Durga'

for name in names:
    print(name)


names.append('Ranveer')
for name in names:
    print(name)

print('================')
names2 = ['Krishna', 'Kumar']

names.extend(names2)

for name in names:
    print(name)

names.insert(1, 'Rajini')

print('========')

for name in names:
    print(name)

copy_names = names

del names

print(f"====Copied names ====")
for copied_name in copy_names:
    print(copied_name)


# Poping a name remove permenantly out of the list
copy_names.pop()

pop_name = copy_names.pop()

print(f"Poped name can be access out of the loop: {pop_name}")

# Poping items using index postion
print("=======")
copy_names.pop(1)

for name in copy_names:
    print(name)

# Removing items by remove() method
print("======")

copy_names.remove('Ranveer')

for name in copy_names:
    print(name)

######## Organizing a list #######

# Sorting
print("=========")

names = copy_names[:]

# Sorting permanently by sort() method
copy_names.sort()

for name in copy_names:
    print(name)

# Sorting Temporarily by sorted() method

print(f"Names are sorted temporarily :")
print(sorted(names))



### List in reverse order
names.reverse()
print(names)


### finding length of list

print(len(names))


######  Working with lists ==========>  
print("==================>")
for value in range(1,10):
    print(value)

print(f"Even numbers")
for value in range(0,10,2):
    print(value)

squares = []

for value in range(1,10):
    square = value ** 2
    squares.append(square)

print(squares)

cubes = []

for value in range(1,10):
    cubes.append(value ** 3)

print(cubes)

print(f"min of cubes: {min(cubes)}, max of cubes: {max(cubes)}")

print(f"Sum of cubes: {sum(cubes)}")

quaraples = [value ** 4 for value in range(1,10)]

print(quaraples)


##### Using Multiple lists #####

availabe_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in availabe_toppings:
        print(f" Adding {requested_topping}.")
    elif requested_topping not in availabe_toppings:
        print(f"\tSorry, We don't have {requested_topping}.")

print(f"Finizhed") 


###### Dictionaries ################

print(" ################ Dictionaries -->-->")

alien_0 = {
    'color': 'red',
    'speed': 'medium',
    'points': 5
}

### Accessing a dict'ry

print(f" Dictionary value accessed is : {alien_0['color']}")

# adding new values 

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)


# Modifying values in dict

alien_0['x_position'] = 25

print(alien_0)


### using del to remove key-value pairs

del alien_0['speed']

print(alien_0)


# using get() method

alien_1 = {
    'color': 'red',
    'speed': 'medium',
}
print(alien_1.get('points', 'No points value assigned'))


##### Looping through Dict's

user_0 = {
    'username': 'saikrishna',
    'first': 'Sai',
    'last': 'Krishna'
}

for key, value in user_0.items():
    print(f"\tKey: {key}\n\tValue: {value}\n")

### Looping through all keys in a dict'ry

for key in user_0.keys():
    print(f"\tKeys : {key}")


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['jen', 'phil']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t {name.title()}, I see you love {language}!")

#### NESTING ==> -->

print("#### NESTING ==> -->")


## A List of Dict's


alien_1 = {
    'color': 'red',
    'points': 10,
    'speed': 'fast'
}

alien_2 = {
    'color': 'yellow',
    'points': 3,
    'speed': 'slow'
}

alien_3 = {
    'color': 'green',
    'points': 5,
    'speed': 'medium'
}

aliens = [alien_1, alien_2, alien_3]

aliens = []

for alien_number in range(100):
    new_alien = { 'color': 'red', 'points': 10, 'speed': 'fast'}
    aliens.append(new_alien)

for alien in aliens[:10]:
    if alien['color'] == 'red':
        alien['color'] = 'yellow'
        alien['speed'] = 'slow'
        alien['points'] = 3

for alien in aliens[10:30]:
    if alien['color'] == 'red':
        alien['color'] = 'green'
        alien['points'] = 5
        alien['speed'] = 'medium'


for alien in aliens[:32]:
    print(alien)



print(f"Total no of aliens: {len(aliens)}")
    
####### A list inside a dict'ry


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    elif len(languages) == 1:
        print(f"{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")


aliens = [alien_1, alien_2, alien_3]


for alien in aliens:
    print(alien)
    for k , v in alien.items():
        print(k, v)


#### Dict's in dict's

users = {
    'saikrishna': {
        'first': 'Sai',
        'last': 'Krishna',
        'location': 'hyderabad'
    },
    'tharun': {
        'first': 'tharun',
        'last': 'kumar',
        'location': 'hyderabad'
    }
}

for username , userinfo in users.items():
    print(f"UserName: {username}")
    fullname = f"{userinfo['first'].title()} {userinfo['last'].title()}"
    location = userinfo['location'].title()

    print(f"\tFullName: {fullname}")
    print(f"\tLocation: {location}") 








