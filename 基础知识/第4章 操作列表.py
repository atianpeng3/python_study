# 4.1 遍历整个列表
words = ['aa', 'bb', 'cc', 'dd']
for word in words:
    print(word)
    print("the word is : " + word + ".\n")
print("done.")

print("the last word is : " + word)         # !!!!!!!

# 4.3 创建数字列表
for value in range(1, 5):        # [a,b)
    print(value)

numbers = list(range(1, 5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

squares = [value**2 for value in range(1, 11)]
print(squares)

values = [1, 2, 3, 4, 5, 0]
print(min(values))
print(max(values))
print(sum(values))

# 4.4 切片
words = ['aa', 'bb', 'cc', 'dd']
print(words[1:3])
print(words[1:])
print(words[:3])
print(words[-2:])       # 最后2个word
for word in words[:3]:
    print(word)

words = ['aa', 'bb', 'cc', 'dd']
words_ = words
print(words)
print(words_)
words.append('ee')
words_.append('ff')
print(words)
print(words_)

words = ['aa', 'bb', 'cc', 'dd']
words_ = words[:]
print(words)
print(words_)
words.append('ee')
words_.append('ff')
print(words)
print(words_)

# 元组

dimensions = (1, 2)
print(dimensions[0])
print(dimensions[1])
print(dimensions)
for dimension in dimensions:
    print(dimension)
dimensions = (2, 4)
print(dimensions)
