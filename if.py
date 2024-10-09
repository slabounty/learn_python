is_male = True
is_tall = True
if is_male:
    print("you are a male")
else:
    print("you are not a male")

is_male = False
is_tall = True
if is_male or is_tall:
    print("you are a male or you are tall")
else:
    print("you are not a male nor tall")

is_male = True
is_tall = False
if is_male and is_tall:
    print("you are a tall male")
else:
    print("you are either not tall or not male or both")

is_male = False
is_tall = False
if is_male and is_tall:
    print("you are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are not a male but you are tall")
else:
    print("you are not a male and not tall")

