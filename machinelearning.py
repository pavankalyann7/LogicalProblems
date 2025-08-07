#shallow copy #cop
a = [[10, 20], [30, 40]]
b = a[:]  
b[0][0] = 999
a[0][1]= 10000
print(id(a[0]),id(b[1]))
print("a:", a)
print("b:", b)
#deep copy
a = [[10, 20], [30, 40]]
b = a.copy()
b[1] =200
print(a,b)
