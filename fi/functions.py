# # funtions = reusable block, takes input , return output
# # def funtion_name(param1, param2 = default_value):
# #     #do something
# #     return result


# def add_numbers(a, b=8):
#     z = a + b
#     return z


# def word_count(filename):
#     with open(filename, "r") as f:
#         content = f.read()
#     words = content.split()
#     return len(words)


# result = word_count("hat.txt")
# print(result)


# funtions with no parameter
def health():
    print("Need water?? here is a glass of water")


def playy():
    print("Lets play BGMI!! Join mee...")


# args are the value pass to the funtions
def greet(name):
    print("hello,", name, "lets play games")


def honor_giving(name):
    print("hello,", name, "Giving you the honor")


# if no value passed py used default agruments
def naam(first_name, lastname="BOSS"):
    print(first_name + " " + lastname)


# naam("Yash")
# naam("Yash", "jaa")


# return send back a value to the function
def add(a, b):
    return a + b


# result = add(3, 5)
# print(result)


def skware(a):
    return a * a


# skresult = skware(5)
# print(skresult)


# *args when dont know how many argumnets will be passed
def tota(*args):
    print(*args)


def total(*args):
    return sum(args)


# tota(10, 20, 30, 40, 50)
# print(total(10, 20, 30, 40, 50))


# **kwargs when dont know how many named arguments will be passed
# accepts any number of keyword arguments as a dictionary


def details(**kwargs):
    print(kwargs)


# details(name="yash", age=27, work="AI Engineer", Identity="GOD")


def detail(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])


# detail(name="yash", age=27, work="AI Engineer", Identity="GOD")


def deta(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


deta(name="yash", age=27, work="AI Engineer", Identity="GOD")
