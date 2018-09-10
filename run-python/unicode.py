# coding=utf-8
# python的默认编码文件是用的ASCII码，你将文件存成了UTF-8！
# 存 unicode 读 utf-8
# Python提供了ord()函数获取字符的整数表示
# chr()函数把编码转换为对应的字符

print ord('A')
print chr(66)

print "ABC".encode('ascii')
# print "中文".encode('utf-8')
# %运算符就是用来格式化字符串的。
# 在字符串内部，%s表示用字符串替换
# %f 浮点数
# ，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值
# ，顺序要对应好。如果只有一个%?，括号可以省略
