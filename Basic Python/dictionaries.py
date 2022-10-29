# dictionary = a changable, unordered collection of unique key:value pairs
#               fast because they use hashing, allow us to access a value quickly

capitals = {
    "USA":"Washington D.C",
    "India":"New Dehli",
    "China":"Beijing",
    "Russia":"Moscow"
}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("China")
# capitals.clear()

# print(capitals["Russia"])
# print(capitals.get("Germany"))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for keys, values in capitals.items():
    print(keys, values)