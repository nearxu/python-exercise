# set则可以堪称是list和dict的杂合.

s0 = set([1, 2, 3, 4])
print(s0)

s1 = set("qiwsir")
print(s1)

s2 = set([123, "google", "face", "book", "facebook", "book"])
print(s2)

s3 = {"facebook", 123}

print(s3)

# s4 = {"facebook", [1, 2, 'a'], {"name": "python", "lang": "english"}, 123}

# print(s4)

# set.add set.upate(s2)

a_set = {'a', 'i'}

print(a_set.add('hello'))

# b_set = {[1, 2]}

# print(a_set.update(b_set))

# pop pop(value) remove(value)

print(['[1,2,3]', 'h', 'o'].pop())

# #c是a的子集
# c<a  c.issubset(a)

# A、B的交集

a = set(['q', 'i', 's', 'r', 'w'])
b = set(['a', 'q', 'i', 'l', 'o'])
print(a & b)

print(a.intersection(b))

#symmetric_difference 差集

c = set(['q', 'i', 's', 'r', 'w'])
d = set(['a', 'q', 'i', 'l', 'o'])
print(c.symmetric_difference(d))
