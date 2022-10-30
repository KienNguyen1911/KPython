# index operator[] = gives access to sequence's element (str, list , tuples)

name = "kien Nguyen!"

if name[0].islower():
    name = name.capitalize()

first_name = name[:4].upper()
last_name = name[:5].lower()
last_chacter = name[:]

print(first_name)
print(last_name)
print(last_chacter)