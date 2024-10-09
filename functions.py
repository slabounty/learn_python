def say_hi():
    print("hello")

print("top")
say_hi()
print("bottom")

def say_hi_2(name):
    print("hello ", name)

say_hi_2("mike")
say_hi_2("steve")

def say_hi_3(name, age):
    print("hello " + name + " age = " + age)

say_hi_3("mike", "22")
say_hi_3("steve", "33")

def say_hi_4(name, age):
    print("hello " + name + " age = " + str(age))

say_hi_4("mike", 44)
say_hi_4("steve", 55)
