# set = collection which is unordered and unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bow", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(utensils.intersection(dishes))

# for x in dinner_table:
#     print(x)