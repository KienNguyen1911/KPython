# tuple = collection which is ordered and unchangable
#          used to group together related data

student = ("Kien", 20, "Male")

print(student.count("Kien"))
print(student.index("Male"))

for i in student:
    print(i)

if "Kien" in student:
    print("Kien is here!")