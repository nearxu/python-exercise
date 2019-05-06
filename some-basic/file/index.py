# some api from https://www.yiibai.com/python3/file_methods.html

# w 打开一个文件只用于写 w+ 该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除
# r r+ 以只读方式打开文件 这是默认模式
# open(filename,'w,w+,r,r+',encoding='utf-8') as fp:
#   fp.write(json.dumps(data,ensure_ascii = False))

fo = open('text.txt', 'r+')

print(fo.name)

str = 'hello my first write'

line = fo.write(str)

foread = open('text.txt', 'r+')

print(foread)

fo.close()
