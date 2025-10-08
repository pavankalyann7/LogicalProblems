#input : aaabcccd
#output : a3b1c3d1
Input = "aaabcccd"
Results = '' 
a = Input[0]
b = 1
for i in range(1,len(Input)):
    if a == Input[i]:
        b+=1
    else:
        Results =Results+a+str(b)
        a = Input[i]
        b = 1
Results =Results+a+str(b)
print(Results)
# Input: "[(())]" → Output: Balanced
# Input: "[(])" → Output: Not Balanced
a = "[({"
b = "])}"
Input = "[{()}]" #6/2 = 3
for i in range(len(Input)//2):
    c = a.index(Input[i])
    if Input[i] == a[c] and Input[-1-i]==b[c]:
        pass
    else:
        print('unbalanced')
        break
else:
    print('balanced')
# Input: word1 = "horse", word2 = "ros" → Output: 3
# Input: word1 = "book", word2 = "back" → Output: 2
word = list("book")
fixed = word[:]
fixed = len(fixed)
wordsecond = list("back")
count = 0
s = 0
for i in range(fixed):
    if i>=len(wordsecond): #0>3 
        word.remove(word[i-s])
        s+=1
        count +=1
    elif word[i] == wordsecond[i]:
        pass
    elif word[i] != wordsecond[i]:
        word[i] = wordsecond[i]
        count+=1
print(count)
print(''.join(word))
'''
Write a program to find all leader elements in an array.
An element is called a leader if it is greater than all elements to its right.
Input: [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
'''
Input = [16,17,4,3,5,2]
Results = []
for i in range(len(Input)-1):
    if Input[i] > max(Input[i+1:]):
        Results.append(Input[i])
Results.append(Input[i+1])
print(Results)

