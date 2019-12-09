### Lists using while loop ==> -->

unconfirmed_users = ['sai', 'krishna', 'tharun']

confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print(f"\nThe following users are confirmed: ")
for confirmed_user in confirmed_users:
        print(confirmed_user.title())

#### Removing items from lists using while by remove() method

pets = ['cat', 'dog', 'goldfish', 'cat', 'rabbit', 'parrot']

while 'cat' in pets:
    pets.remove('cat')

print(pets)

print("===========================")
#### === Dict using while loop === ###

responses = {}

flag = True

while flag:

    name = input("What is your name? ")
    response = input("which car you would like to buy? ")

    responses[name] = response

    repeat = input("\nWould you like to ask another person request? (y/N) ")
    if repeat == 'N':
        flag = False
    
print("\n\t ===Polling Results===")
for name, response in responses.items():
    print(f"{name.title()} Would like to buy {response.title()}.")






