# 2D = list of lists

drinks = ["cocacola", "sprite", "fanta", "the last"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice-scream"]

food = [drinks, dinner, dessert]
print(food[0][0])

for i in food:
    # print(i)
    for j in i:
        print(j)
    print("======")