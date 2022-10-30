# str.format() = optional method that gives user
#                more control when displaying output

# animal = "cow"
# item = "moon"
#
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) #posiitonal argument
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) #keyword argument
#
# text = "The {} jumperd over the {}"
# print(text.format(animal, item))

# name = "Kien"
#
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) #left align
# print("Hello, my name is {:>10}. Nice to meet you".format(name)) #right align
# print("Hello, my name is {:^10}. Nice to meet you".format(name)) #center align


number = 1000

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:x}".format(number))
print("The number is {:e}".format(number))