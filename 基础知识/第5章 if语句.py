# 5.2 条件测试
age = 18
print(age == 18)
print(age < 18)
print(age > 18)
print(age >= 10 and age <= 20)
print(age <= 10 or age >= 20)
print(age <= 10 or age <= 20)

words = ['aa', 'bb', 'cc']
print('aa' in words)
print('dd' in words)
print('dd' not in words)

# 5.3 if语句
age = 18
if age < 14:
    print(1)
elif age < 18:
    print(2)
elif age == 18:
    print(3)
else:
    print(4)

age = 18
if age < 14:
    print(1)
elif age < 18:
    print(2)
elif age == 18:
    print(3)
elif age > 18:
    print(4)
