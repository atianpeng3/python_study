'''
favorite_language = {}
active = True
while active:
    name = input("Please input your name : ")
    language = input("Please input your favotite language : ")
    favorite_language[name] = language.title()

    next_person = input("Is there another person? (yes/no) ")
    if next_person == "no":
        active = False

print("---done---")

for name, language in favorite_language.items():
    print(name + "'s favorite language is " + language + ".")
'''

num = 1
while num < 5:
    if num == 3:
        break
    print(num)
    num += 1
print("---end---")

num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print(num)
print("---end---")