#perfect squares between 1 to 100
start = 1
end = 100
while start<=end:
    #here we write the logic of perfect square or not
    rs_of_num = start**0.5
    if int(rs_of_num) == rs_of_num:
        print(start)
    start+=1

#perfect quebe 
user_input = int(input("enter a number for checking perfect cube or not : "))
a = user_input**(1/3)
if round(a)**3 == user_input:
    print('perfect cube')
else:
    print('not perfect cube')

#absolute difference between sum of odd numbers and even numbers
start = 1
end = 100
sum_of_odd_number = 0
sum_of_even_number = 0
while start<=end:
    if start%2==0: #condition checking for even numbers
        sum_of_even_number+=start
    else:
        sum_of_odd_number+=start

    start+=1

absolute_difference = abs(sum_of_odd_number - sum_of_even_number)
print("Absolute Difference:", absolute_difference)