# '''
# Input: n = 4
# Output:
# *      *
# **    **
# ***  ***
# ********
# ********
# ***  ***
# **    **
# *      *
# '''
# n = 4
# for i in range(1,n+1):
#     if i !=n:print('*'*i,' '*((n-i)*2),'*'*i,sep='')
#     else:print('*'*(i*2))
# for i in range(n,0,-1):
#     if i !=n:print('*'*i,' '*((n-i)*2),'*'*i,sep='')
#     else:print('*'*(i*2))
# '''
# Input: n = 4
# Output:
#    *   
#   * *  
#  *   * 
# *     *
#  *   * 
#   * *  
#    *   
# '''
# n = 4
# for i in range(1,n+1):
#     if i == 1:print(' '*(n-i),'*',sep='')
#     else : print(' '*(n-i),'*',' '*(((i-1)*2) -1),'*',sep='')
# for i in range(n-1,0,-1):
#     if i == 1:print(' '*(n-i),'*',sep='')
#     else : print(' '*(n-i),'*',' '*(((i-1)*2) -1),'*',sep='')
# '''
# Input: n = 5
# Output:
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
# '''
# n = 5
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()
'''
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
'''
# for i in range(5):
#     print(' '*(5-i),end='')
#     num = 1
#     for j in range(i+1):
#         print(num,end=' ')
#         num =num* (i-j)//(j+1)
#     print()
'''
 1  2  3  4  5
16 17 18 19  6
15 24 25 20  7
14 23 22 21  8
13 12 11 10  9
'''
rows = int(input("enter a rows number : "))
box = [[0 for i in range(0,rows)] for j in range(rows)]
#first row
start = 0
for fr in range(rows):
    start+=1
    box[0][fr] = start
#last column  
for lc in range(rows):
    box[lc][rows-1] = start
    start+=1
#last row
start = start-1
for lr in range(rows-1,-1,-1):
    
    box[rows-1][lr] = start
    start+=1
#first column
start -=1
for fc in range(rows-1,0,-1):
    box[fc][0] = start
    start+=1

#structure of spiral 
for i in range(len(box)):
    for j in box[i]:
        print(j ,end=' ')
    print()


