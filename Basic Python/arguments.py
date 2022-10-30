def hello(first, middle, last):
    print("Hello "+first+" "+middle+ " "+last )

hello(last="nguyen",middle= "dong",first="kien")

# *args = parameters that will pack all arguments into a tuple
#         useful so that a function can accept varying amount of arguments

def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(sum(1,2,3,4))