

# a = 10

# if a % 2 == 0:
#                     print("this is even number")
# else:
#                     print("this is odd number")



# a = int(input("hii,Shivam enter your value to check even or odd:"))

# if a % 2 == 0:
#                     print("this is even number")
# else:
#                     print("this is odd number")



# input()  => it is used to take input from user .




# task: write a program to check givem number is even or odd using function .

# def check_even_odd(num):
#                     if num % 2 == 0:
#                                         print("this is even number :", num)
#                     else:
#                                         print("this is odd number :", num)


# print("hiii, start")

# check_even_odd(77)

# print("hii guys listen please ")


# for i in range(0, 12):
#                     if i == 7:
#                                continue
#                     print(i)


# check_even_odd(89)

# my_listt = ["Ravi","rohit", 44, 55, 88]

# for i in my_listt:
#                     if i == 44:
#                                         break
#                     print(i)


# check_even_odd(90)







# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Taking input from user
number = int(input("Enter a number: "))

# Calling the function and printing result
result = check_even_odd(number)
print(f"The number {number} is {result}.")
