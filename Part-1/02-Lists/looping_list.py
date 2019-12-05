# Looping in lists

languages = ['C', 'Python', 'JavaScript', 'GoLang']

for language in languages:
    print(f"{language} is programming language")


# using the range func() 

for value in range(1, 10):
    print(value)
print("================")
for value in range(5):
    print(value)

# Using range() to make a list of numbers

numbers = list(range(1, 10))
print(numbers)

even_numbers = list(range(2, 10, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)


cubes = []
for i in range(1,9):
    cube = i ** 3
    cubes.append(cube)

print(cube)

quadraples = []
for i in range(1,10):
    quadraples.append(i**4)

print(quadraples)


#  min(), max() and sum()

print(f"min value:  {min(squares)}")
print(f"max value: {max(squares)}")
print(f"sum value:  {sum(squares)}")
squares = []

# List Comprehension same a range() for squares, triples and quadraples in one line

squares = [value**2 for value in range(1,11)]
print(squares)

cubes = []
cubes = [value ** 3 for value in range(1,11)]
print(cubes)