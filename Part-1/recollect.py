# List -->

names = ['sai', 'krishna', 'tharun']

print(names)

print(names[0], names[2])

print(f"My brother name is {names[2].title()}.")

# modifying list

names[1] = 'Prem'

print(names)

# adding to list

###  names[3] = 'pavan'

# above method is not possible

# adding a element to list using append() method and insert() method

names.append('pavan')

print(names)

# insert() allows us add ele at our own indexed postion

names.insert(1, 'krishna')

print(names)

# removing items form list

# --> by del and pop() and remove(value)

del names[2]

print(names)

# pop() just eliminates the ele from list but it can be saved to
# another ele

last_ele = names.pop()

print(f"element poped from list is: {last_ele}")

# remove ele by value from the list

names.remove('krishna')

print(names)

names.append('krishna')
names.append('srinivas')

print(names)

# poping a ele using an indexed position

names.pop(2)

print(names)

### Looping through a list

for name in names:
    print(name)
