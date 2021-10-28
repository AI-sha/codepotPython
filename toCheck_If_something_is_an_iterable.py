nums = [1,2,3]

print(dir(nums))

# if the dir() function returns the dunder method:  __iter__ , then that means it is something that can be looped over and therefore
# is an iterable

# if dir returns both dunder methods __iter__ and __next__  then it is an iterator.
# It returns __iter__ as an iterator is also and iterable, i.e it will return self