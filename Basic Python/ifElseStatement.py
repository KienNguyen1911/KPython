age = int(input("How old are you? "))

if age == 100:
    print("You are a century!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You have not been born yet!")
else:
    print("You are a teenager!")
