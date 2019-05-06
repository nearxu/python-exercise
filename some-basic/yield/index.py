
# can understand

def wait():
  print('start',)
  m =  yield 5
  print(m)
  d = yield 12
  print('we are together')

c = wait()

c.send('None')
c.send('Fighting')