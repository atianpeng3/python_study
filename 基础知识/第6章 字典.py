favorite_language = {"a": "python", "b": "C++", "c": "java"}

for person, language in favorite_language.items():
    print(person + "'s favorite language is " + language.title() + '.')

for person in favorite_language:
    print(person + "'s favorite language is " + favorite_language[person].title() + '.')

for person in favorite_language.keys():
    print(person + "'s favorite language is " + favorite_language[person].title() + '.')

for language in favorite_language.values():
    print(language.title())

for person in sorted(favorite_language.keys(), reverse=True):
    print(person + "'s favorite language is " + favorite_language[person].title() + '.')

test_dic = {'list': [0, 1, 2], 'dict': {1: 'a', 2: 'b', 3: 'c'}}
print(test_dic)