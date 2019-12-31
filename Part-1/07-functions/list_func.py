### Passing a list to function

def greet_users(names):
    """Print a simple greeting to each user in the list"""

    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['sai', 'krishna', 'tharun']

greet_users(usernames)

### Modifying a list

unprintedDesigns = ['Robot', 'race car', 'website store']
completed_lists = []
print("\t\t\n==============================\n")

while unprintedDesigns:
    current_design = unprintedDesigns.pop()

    print(f"Printing model: {current_design.title()}")
    completed_lists.append(current_design)

print(f"The following models have been printed: ")
for completed_list in completed_lists:
    print(completed_list)

print("\t\t\n==============================\n")


completed_models = []
unprinted_models = ['Robot', 'race car', 'website store']

def print_models(unprinted_models, completed_models):

    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Printing {current_model.title()}.")
        completed_models.append(current_model)

def show_printed_design(completed_models):

    print("The following models have been printed: ")

    for completed_model in completed_models:
        print(completed_model)

print_models(unprinted_models[:], completed_models)
show_printed_design(completed_models)