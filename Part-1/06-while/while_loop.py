 
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

#### ===

# The for loop takes a collection of items and executes a block of code once
# for each item in the collection.

# ===

# the while loop runs as long as, or while, a certain condition is true.

# ==> -->

quit_msg = "Help options for quiting"
quit_msg += "\nEnter 'quit' to end the program: "

msg = ''
while msg != 'quit':
    msg = input(quit_msg)
    if msg != 'quit':
        print(f"{msg}")


#### Using Flag ==> -->

flag = True

while flag :
    msg = input(quit_msg)
    if msg == 'quit':
        flag = False
    else:
        print(msg)


### Using 'break' to Exit a Loop ==> -->

while True:
    msg = input(quit_msg)

    if msg == 'quit':
        break
    else:
        print(msg)

### Using 'continue' in a Loop ==> -->

current_number = 0
while current_number < 10:
    current_number += 1 
    if current_number % 2 == 0:
        continue

    print(current_number)














