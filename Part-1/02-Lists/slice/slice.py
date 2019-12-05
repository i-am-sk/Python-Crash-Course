

# Slice

languages = ['C#', 'Java', 'JavaScript', 'Golang', 'Python']
print(languages)


# Copying a slice

copy_languages = languages[:]

print(copy_languages)

# delete a slice

del languages

# print(languages)
# ==> NameError: name 'languages' is not defined


print(copy_languages[:3])

print(copy_languages[2:])

print(copy_languages[1:4])

print(len(copy_languages))

print(copy_languages[-1])

print(copy_languages[-5:])

print(copy_languages[-5:-1])

print(copy_languages[-3:-1])

print(copy_languages[:5:2])

print(copy_languages[:5:2])

print(copy_languages[1:5:2])

print(copy_languages[-5::2])

print(copy_languages[-5:-1:2])
