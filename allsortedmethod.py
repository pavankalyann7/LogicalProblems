#bubble sort
a = [5, 1, 4, 2, 8]
for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)
#selecting sort
a = [5, 1, 4, 2, 8]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j] = a[j],a[i]
print(a)
#   
