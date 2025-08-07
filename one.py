#1. Double each number in a list
a = [1,2,3,4,5,6]
print(list(map(lambda x:x+x,a)))
#3. Convert list of strings to uppercase
a = ['apple', 'banana', 'cherry']
print([''.join(i) for i in list(map(lambda x:[chr(ord(i)-32) for i in x],a))])
#4.Find One to Fifty Prime Number
