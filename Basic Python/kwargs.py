# **kwargs = parameter that will pack all arguments into dictionary
#           useful so that a function can accept a varying amount of keyword argumetns

def hello(**kwargs):
    print("hello", end=" ")
    # print("hello "+ kwargs['last']+" "+ kwargs['first'])
    for key, value in kwargs.items():
        print(value, end=" ")

hello(last="nguyen", middle="dong", first="kien")