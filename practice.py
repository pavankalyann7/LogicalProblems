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

#Prime
User_input = int(input("enter a number for checking its prime or not : "))
divisors_count = 0
for i in range(1,User_input+1):
    if User_input%i == 0: divisors_count+=1
if divisors_count==2:print("yes its prime")
else : print("no its not prime number")