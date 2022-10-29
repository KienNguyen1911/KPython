name = "Kien Code 😊"

# slicing[start:stop:step]
first_name = name[:4]
# if you dont want to input start, default is 0
last_name = name[5:]
# if you dont want to input stop, default is from start to last
funky_name = name[0::3]
reversed_name = name[::-1]
# print(first_name)
# print(last_name)
# print(funky_name)
print(reversed_name)

website = "https://google.com"

slice = slice(8, -4)

print(website[slice])