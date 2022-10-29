temp = int(input("what is temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today")
    print("go outside")
elif temp < 0 or temp > 30:
    print("the temperature is bad today")
    print("stay inside")

# not is reversed the condition in if-else statemetn