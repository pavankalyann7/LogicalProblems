# #closure - revember local variable outside of the function even if function is finished.
# def closure():
#     count = 0
#     def inner_function():
#         nonlocal count
#         count+=1
#         return count
#     return inner_function #here returns right because inner function is still not finished ok that why ? if inner function you calling it then return its not closure
# a = closure()
# print(a())
# print(a())
# #####
# def closure():
#     count = 0
#     def inner_function():
#         nonlocal count
#         count += 1
#         return count
#     return inner_function

# a = closure()

# print(a.__closure__)          # shows closure cell info
# print(a.__closure__[0].cell_contents)  # shows count value
def permute(arr, path=[]):
    print(path)
    if not arr: #false 
        #print(path) 
        return
    for i in range(len(arr)): #3
        #print(arr[:i] + arr[i+1:], path + [arr[i]])
        #print(path)
        permute(arr[:i] + arr[i+1:], path + [arr[i]])
permute(['a','b','c'])
