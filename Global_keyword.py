#using global keyword, this will print 200,200 . without global it will print 200, 300
x = 300

def myfunc():
  global x
  x = 200
  print(x)

myfunc()

print(x)