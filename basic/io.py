objects = open('hello.txt', 'w')
objects.write('funck python dificult')
print(objects.name)
objects.close()

fo = open('hello.txt', 'r')
str0 = fo.read()

print(str0)
