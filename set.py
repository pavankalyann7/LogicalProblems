'''
1.Write a program to add a new element to a set.
 Input: {1, 2, 3}, element: 4
 Output: {1, 2, 3, 4}
2.Write a program to remove an element from a set if present.
Input: {1, 2, 3}, element: 2
Output: {1, 3}
3.Write a program to find the length of a set.
Input: {1, 2, 3, 4}
Output: 4
4.Write a program to check if an element exists in a set.
Input: {1, 2, 3}, element: 2
Output: True
5.Write a program to clear all elements of a set.
Input: {1, 2, 3}
Output: set()
6. Check if two sets are equal
 Input: {1, 2, 3}, {3, 2, 1}
 Output: True
7. Find the union of two sets
 Input: {1, 2}, {2, 3}
 Output: {1, 2, 3}
8. Find the intersection of two sets
 Input: {1, 2, 3}, {2, 3, 4}
 Output: {2, 3}
9.Find the difference between two sets
 Input: {1, 2, 3}, {2, 4}
 Output: {1, 3}
10.Find the symmetric difference between two sets
 Input: {1, 2, 3}, {3, 4, 5}
 Output: {1, 2, 4, 5}
11.Check if one set is a subset of another
 Input: {1, 2}, {1, 2, 3}
 Output: True
 12. Find common elements in three sets
 Input: {1, 2, 3}, {2, 3, 4}, {3, 5}
 Output: {3}
 13.Remove duplicates from a list using a set
 Input: [1, 2, 2, 3, 3, 3]
 Output: [1, 2, 3]
'''
Input=[1, 2, 2, 3, 3, 3]
empty = []
for i in Input:
    if i not in empty:
        empty.append(i)
print(empty)
