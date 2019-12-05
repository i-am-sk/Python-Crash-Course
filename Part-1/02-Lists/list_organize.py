# Organizing a list
# --> Sorting a list  === sort() and reversing a sortedlist by using === sort(reverse=True)
## --> Permanently  using sort() by dot(.)
## --> Temporarily  using sorted()  by === sorted(cars_list)

# --> Reversig a list
# --> Length of list


### --> Sorting a list

cars_list = ['toyota', 'skoda', 'audi', 'bmw', 'tesla']

cars_list.sort()

print(f"Sorted list is: {cars_list}")

cars_list.sort(reverse=True)

print(f"Reverse Sorted list is: {cars_list}")

#### --> Temporarily

print(sorted(cars_list))

#### -->  Permanently

cars_list.sort()
print(cars_list)


### --> Reversig a list

#  === Note: === the reverse doesn't sort backward alphabetically; it simply reverse the order of the list

cars_list.reverse()  # Reverse *IN PLACE*

print(f"Reverse ofthe list: {cars_list}")

### --> Length of list

print(f"The lenght of the list is : {len(cars_list)}")
