# method 1 swapping two number without third variable
# a = float(input("Enter the first Number : "))
# b = float(input("Enter the second Number : "))
# a = a+b
# b = a - b
# a = a - b
# print("After swapping the first Number is ",a)
# print("After swapping the first Number is ",b)

# method 2 swapping two number with third variable
# a = float(input("Enter the first Number : "))
# b = float(input("Enter the second Number : "))
# c = a
# a = b
# b = c
# print("After swapping the first Number is ",a)
# print("After swapping the first Number is ",b)

# method 3 swapping two number without third variable
a = float(input("Enter the first Number : "))
b = float(input("Enter the second Number : "))
a,b = b,a
print("After swapping the first Number is ",a)
print("After swapping the first Number is ",b)


