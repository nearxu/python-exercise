
for i in range(0, 5):
    print i
else:
    pass


# def func1():
#     global x
#     print 'x is '+x
#     x = 1


# x = 3
# func1()
# print x

# def say(msg, time=1):
#     print msg*time


# say('perter')
# say('perter', 4)

# l = [1, 2, 3]
# l.append(4)
# print l.count(4)


# l1 = [1, 2, 3]
# t = tuple(l1)
# print t
# print list(t)

class Person:
    Count = 0

    def __init__(self, name, age):
        Person.Count += 1
        self.name = name
        self.age = age

    def tell(self):
        print "name: %s , age: %s ," % (self.name, self.age),


# p = Person('perter', 25)

# print p.age

class Teacher(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def tell(self):
        Person.tell(self)
        print 'Salry: %d' % self.salary


class Student(Person):
    def __init__(self, name, age, mark):
        Person.__init__(self, name, age)
        self.mark = mark

    def tell(self):
        Person.tell(self)
        print 'mark: %d' % self.mark


print Person.__doc__
print Teacher.__doc__
print Student.__doc__

t = Teacher('mr li', 20, 9000)
s = Student('peter', 30, 30000)
members = [s, t]

for m in members:
    m.tell()
