# Changing, Adding, and Removing Elements

## --> Modifying Elements in the list
## --> Adding Elements in the list

### ==> Appending Elements in the End of a list
### ==> Inserting Elements into a List
### ==> Removing an Item Using the del Statement
### ==> Removing an Item Using the pop() Method
### ==> Popping Items from any Position in a List
### ==> Removing an Item by Value using remove() method

## --> Removing Elements in the list


#### --> Modifying Elements in the list

languages = ["C#", "Java", "JavaScript", "Golang", "Python"]

print(languages)

languages[0] = "C"

print(languages)

print(f"{languages[0].title()} is the first Programming language I learned")

#### --> Adding Elements in the list
##### --> Appending Elements in the End of a list

# === The simplest way to add a new element to a list is to APPEND the item to the list === #

languages.append("C++")

print(f"{languages[-1].title()} is the Appened element to End of a list")

##### --> Inserting Elements into a List

# === Add an element in the list at any position by using the insert() ===

languages.insert(1, "Perl")

print(f"{languages[1].title()} is the inersted element using insert() method")

##### --> Removing an Item Using the del Statement

del languages[1]

print(languages)

# ==>  you can no longer access the value that was removed from the list after the del statement is used.  <==


##### --> Removing an Item Using the pop() Method

hard_language = languages.pop()

print(f"{hard_language.title()} is very hard to learn")

##### --> Popping Items from any Position in a List

hard_language = languages.pop(1)

print(f"{hard_language.title()} is very hard to learn")


##### --> Removing an Item by Value

languages.remove('Golang')

## Accessing a removed element

static_lang = 'C'

languages.remove(static_lang)

print(f"{static_lang.title()} is static language")
