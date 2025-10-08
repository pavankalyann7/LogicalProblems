user = int(input("enter a number :"))
a = [i for i in range(2,user) if all([i%j!=0 for j in range(2,(i//2)+1)])]
count = 0
results = []
while True:
    for i in range(len(a)):
        if user%a[i] == 0:
            results.append(a[i])
            user//=a[i]
            break
    else:
        break
print(results)
