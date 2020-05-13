# 3.1 列表是什么
test = ['aa', 'bb', 'cc', 'dd']
print(test)
print(test[0])
print(test[0].title())
print("the first is " + test[0])
print(type(test))
print('\n')

# 3.2 修改、添加和删除元素
test = ['aa', 'bb', 'cc', 'dd']
print(test)
test[0] = '11'
print(test)

test.append('55')
print(test)
test.insert(0, '00')
print(test)

del test[0]
print(test)
pop_str = test.pop()    # 默认pop最后一个元素
print(pop_str)
print(test)
pop_str2 = test.pop(0)  # pop(index)
print(pop_str2)
print(test)
test.remove('bb')       # 根据具体值去删除元素，只删除第一个
print(test)
print('\n')

# 3.3 组织列表
test = ['c', 'b', 'a', 'd']
print(sorted(test))                 # sorted() 临时排序
test = ['c', 'b', 'a', 'd']
print(sorted(test, reverse=True))
test = ['c', 'b', 'a', 'd']
test.sort()                         # .sort() 永久排序
print(test)
test.reverse()                      # .reverse() 翻转
print(test)
test.reverse()
print(test)

print(len(test))
