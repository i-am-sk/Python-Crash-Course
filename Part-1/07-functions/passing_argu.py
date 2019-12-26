### Passing arguments in python in multiple ways

# --> Postional arguments

def describe_pet(animal_type, animal_name) :
    print(f"I have an {animal_type.title()}")
    print(f"My {animal_type.title()} name is {animal_name.title()}\n")

describe_pet('hamster', 'harry')
describe_pet('Dog', 'jacky')

# --> Keyword Arguments

describe_pet(animal_name = 'Jacky', animal_type = 'hamster')

# --> Default values


def describe_pet(animal_type, animal_name = 'Jacky'):
    print(f"I have an {animal_type.title()}")
    print(f"My {animal_type.title()} name is {animal_name.title()}\n")

describe_pet('hamster', 'Roche')
describe_pet('Dog')

# When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values. This allows Python to 
# continue interpreting positional arguments correctly.

# --> Equivalent Function calls

# Using positional or keyword format for func() with default values
# both works perfect use which is ease to understand

describe_pet(animal_name='mike', animal_type='dog')
describe_pet(animal_type='hamster') 
