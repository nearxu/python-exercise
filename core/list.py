#!/usr/bin/env python
# coding=utf-8

# lists[:] lists[2:] list[:3] lists[0] 操作类似字符串
a = ["hello"]

b = a.append("world")

#len

c = [1, 2, 3]
d = [4, 5, 6]
print(c.append(d))

#list.insert(i,x) i index x value
# list .remove()
#list.pop() 删除最后一个 list.pop([i]) 删除 index value

# range

print(range(0, 10))

print(range(1, 10))

aliquot = []

for n in range(1, 100):
    if n % 3 == 0:
        aliquot.append(n)

print(aliquot)

others = [n for n in range(1, 100) if n % 3 == 0]

print(others)

squer = [x**2 for x in range(1, 10)]

print(squer)

classes = ['glass', 'apple', 'green leaf']
for (i, day) in enumerate(classes):
    print(day + ' is ' + str(i))
