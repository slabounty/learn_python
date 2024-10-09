# giraffe language
# all vowels map to "g"

def translate(phrase):
    translation = ""
    for letter in phrase:
        # if letter in "aeiouAEIOU":
        # if letter.lower() in "aeiou":
            # translation = translation + "g"
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate("dog"))
print(translate("cat"))

print(translate(input("Enter phrase to translate: ")))


