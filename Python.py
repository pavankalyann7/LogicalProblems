#Check if a number is even or odd
'''
a ='even' if int(input())%2 == 0 else 'odd'
print(a)
#Find the largest of three numbers
first,second,third = 15,5,10
imgine = first
if imgine<second:
    imgine  = second
elif imgine < third:
    imgine = third
print(imgine)
#Check whether a year is a leap year or not
year = int(input('enter a year for checking leap year or not : '))
results = 'leap year'if year%4 == 0 and (year%100 !=100 or year%400 == 0) else 'not a leap year'
print(results)
#Check if a number is prime
number = int(input('Enter a number to check if it is prime: '))
result = ['prime' if number > 1 and all(number % i != 0 for i in range(2, (number // 2) + 1)) else 'not a prime']
print(result)
#Sum of digits of a number
num = 4567
results = 0
while num>0:
    results = results+num%10
    num = num//10
print(results)
#Reverse a number without type conversions
num = 4321
results = 0
while num>0:
    results = results*10 + num%10
    num//=10
print(results)
#Check if a number is a palindrome without type conversions
num = 123454321
backup = num
results = 0
while num>0:
    results = results*10 + num%10
    num//=10
results = 'palindrome' if results == backup else 'not a palindrome'
print(results)

#Find factorial of a number
num = 5
results = 1
for i in range(1,num+1): results = results*i
print(results)
#Fibonacci sequence up to N terms
first,second = 0,1
a = int(input('enter a number : '))
print(first,second,end=' ')
for _ in range(2,a): #unused loop variable
    print(first+second , end=' ')
    first,second = second , first+second
''' 

#Armstrong Number Check
a = 153
a ='armstrong' if (sum(int(i)**len(str(a)) for i in str(a)) == a) else 'not'
print(a)
#Print all prime numbers between 1 to N

#Count the frequency of each character in a string

#Check if two strings are anagrams

#Find the GCD and LCM of two numbers

#Check if a number is a perfect number

#Number pattern logic (like triangle, pyramid, diamond)

#Find the missing number in a list of 1 to N

#Count vowels and consonants in a string

#Check if brackets in a string are balanced

#list=[2, 4, 3, 7, 5, 8]
list_one=[2, 4, 3, 7, 5, 8]
target = 10
results = []
for i in range(len(list_one)):
    a = target-list_one[i]
    if a in list_one[i:]:
        results.append([list_one[i],a])
print(results)

a = (1, 3, 1, 5, 1, 3, 7, 3, 3)
b = a[0]
co = 1
c = []
d = []
for i in range(1,len(a)):
    if a[i] ==b:
        co = co+1
    else:
        c.append(co)
        d.append(b)
        b = a[i]
        co = 1
c.append(co)
d.append(b)
b = a[i]
co = 1
print(d[c.index(max(c))])
'''Write a Python program to find the index of the first and last occurrence of a specific element in a tuple.
 Input: t = (1, 2, 3, 2, 4, 2), element = 2
 Output: [1,5]
Write a program to count how many times each element appears in a tuple.
 Input: t = (1, 2, 2, 3)
 Output: {1: 1, 2: 2, 3: 1}
Write a Python program to flatten a tuple of tuples into a single tuple.
 Input: t = ((1, 2), (3, 4), (5,))
 Output: (1, 2, 3, 4, 5)
Write a Python program to group elements from a tuple based on type.
 Input: t = (1, 'a', 2.5, 'b', 3)
 Output: {int: [1, 3], str: ['a', 'b'], float: [2.5]}'''
t = (1, 2, 3, 2, 4, 2)
element = 2
results = []
for i in range(len(t)):
    if len(results)==0 and element == t[i]:
       results.append(i)
    elif element not in t[i+1:]:
        results.append(i)
print(results)
t = (1, 2, 2, 3)
results = {}
for i in t:
    if i not in results:
        results[i] = t.count(i)
print(results)
t = ((1, 2), (3, 4), (5,))
print(tuple(j for i in t for j in i))
t = (1, 'a', 2.5, 'b', 3)
results = {}
for i in t:
    if type(i) not in results:
        results[type(i)] = [i]
    else:
        results[type(i)].append(i)
print(results)
# Input: [1,2,3,4] 
# Output: [4,3,2,1] recursive

Input = [1,2,3,4]
def Reverse(Input,a = []):
    if len(Input) == 0:
        return a
    a.append(Input[-1])
    return Reverse(Input[:len(Input)-1],a)
a = Reverse(Input)
print(a)
def checking(a,b):
    def orinal(original):
        def inner(one):
      
            if a == '1234' and b == 'vcube':
                return original(one)
            return 'invalid credentials'
        return inner
    return orinal
@checking('1234','vcube')
def Display(num):
    return num
a = Display('hi this is from pyhon')
print(a)


# "Write a Python function to return the longest common prefix among a list of strings.
# input:Enter list of strings: ['flower', 'flow', 'flight']
# output:Longest common prefix: fl"
string = ['flower', 'flow', 'flight']
for i in range(len(string)):
    a = string[i][i]   
    count =0
    for j in range(len(string)):
        if string[j][i] == a:
            count +=1
    if count == len(string):pass

