#closure 
'''
def outer():
    a = 10 
    def inner():
        return a
    return inner()
a = outer()
print(a)
'''
'''
from functools import reduce
a = [10,20,30,40,50,1,2,3,4]
b = map(lambda a:a**2,a)
print(list(b))
c = [10,20,30,40,50,1,2,3,4]
b = filter(lambda a: a%2== 0,c)
print(list(b))
a = [10,20,30,40,50,1,2,3,4]
b = reduce(lambda a,b:a+b,a)
print(b)
a = [10,20,30,40]
b = iter(a)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
'''