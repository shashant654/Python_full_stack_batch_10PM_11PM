

# write a program to print even , between this number to this number .
# write a program to print even , between 10 to 100 .


# for i in range(10, 101):
#                     if i % 2 == 0:
#                                         print(i)


# --------------------------------------------------------------

# def print_even_number(start, end):
#                     for i in range(start, end):
#                                         if i % 2 == 0:
#                                                             print(i)

# print_even_number(10, 21)


# def summ(a, b):

#                     print(a + b)


# summ(99,3)
# --------------------------------------------------------------




# create list = []

# 10, 20, 33, 44, 55,  => using input function

# [10, 20, 33, 44, 55, ]


# -------------------------------------------------------------



# my_listt = []

# for i in range(5):
#                     elements = int(input("enter the elements:"))
#                     my_listt.append(elements)
#                     print(my_listt)


# def print_my_friends_name():
#                     my_friend_list = []

#                     for i in range(4):
#                                         friends = input("enter your friends name: ")
#                                         my_friend_list.append(friends)
#                                         print(my_friend_list)

# print_my_friends_name()


# --------------------------------------------------------------


# average :-     (20 + 20 + 20 ) / 3 => 20 



# maths_marks = int(input("enter the maths marks: "))
# science_marks = int(input("enter the science marks:"))
# english_marks = int(input("enter your english_marks:"))

# total = maths_marks + science_marks + english_marks 

# average = total / 3

# print(average)


# ------------------------------------------------ 


def find_average_of_all_subject_marks(number_of_sub):
                    
           
           maths_marks = int(input("enter the maths marks: "))
           science_marks = int(input("enter the science marks:"))
           english_marks = int(input("enter your english_marks:"))
           
           total = maths_marks + science_marks + english_marks

           average = total / number_of_sub

           print(average)

find_average_of_all_subject_marks(3)









