# import numpy as np
# data = [[85, 90, 78] ,  # Student 1 → (Math, Science, English)
#  [72, 88 ,91] ,  # Student 2
#  [90, 95, 89] ,  # Student 3
#  [65, 70, 60]]  # Student 4
# '''
# Find the average marks of each student. 
# Find the average marks of each subject.
# Find the highest marks scored in Science. 
# Add 5 bonus marks to all students in English. 
# Find the student who scored the highest total marks.
# Find the lowest marks in Math. 
# Calculate the total marks scored by each student. 
# Find the overall class average across all subjects. 
# Replace all marks below 70 with 70 (grace marks). #
# Sort the students based on their total marks (ascending order).
# '''
# 1
# a = np.array(data)
# for i in a:
#     print(np.average(i))
# 2
# b = np.column_stack(data)
# for i in b:
#     print(np.average(i))
# 3
# b = np.array(data)
# print(np.max(b[:,1]))
# 4
# b = np.array(data)+[0,0,5]
# print(b)
# 5

# b = np.array(data)
# results = float('-inf')
# student = ''
# for i in range(0,len(b)):
#     if np.sum(b[i,:]) > results:
#         results = np.sum(b[i,:])
#         student = i+1    
# print(student)
# 6
# b = np.array(data)[:,1]
# print(np.min(b))
# 7
# a = np.array(data)
# for i in a:
#     print(np.sum(i))
# 8
# b = np.array(data).flatten()
# print(np.average(b))
# 9
# b = np.array(data).flatten()
# print(b)
# for i in range(len(b)):
#    if b[i]<70:
#       b[i] = 70
# results = b.reshape(4,3)
# print(results)
# b = np.array(data)
# for i in range(len(b)):
#     for j in range(i+1,len(b)):
#         if np.sum(b[i]) < np.sum(b[j]):
#             b[i],b[j] = b[j],b[i]
# print(b)
