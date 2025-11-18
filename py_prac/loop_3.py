# for i in range(5):
#                     print("first output", i)


# for i in range (0,5):
#                     print("second output",i)

# 0 => starting point , by default starting point will be 0
# 5 => ending point , Ending point will be excluded


# for i in range(13, 18):
#                     print(i)

# starting point => 13
# ending point => 18 , ending point will be excluded.

# output : 13, 14, 15, 16, 17


# for i in range(22, 27):
#                     print(i)

# ouput => 22, 23, 24, 25, 26


# three parameters for loop similar like three parameters slicing 

#           0    1   2   3  4    5
# listt = [ 22, 21, 23, 33, 44, 55]

# print(listt[0:3]) # 22, 21, 23

# starting point => 0
# ending point => 3 , excluded. 
# ouput => 22, 21, 23


#           0    1   2   3  4    5
# listt = [ 22, 21, 23, 33, 44, 55]

# print(listt[0:5:2])

# starting point => 0
# ending point => 5, excluded
# GAP => 2 , (N-1) , 2-1 => 1, we have to skip 1 element .
# NOTE:  By default gap = 1

# output => 22,23,44


# for i in range(2,21,2):
#                     print(i)

# starting point => 2
# ending point => 21 , excluded
# GAP => 2 , (N-1), 2 -1 => 1, we have to skip 1 element.

# 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20

# output => 2,4,6,8,10,12,14,16,18,20


# for i in range(5,51,5):
#                     print(i)


# for i in range(-2, 5):
#                     print(i)


for i in range(9,23,1):
                    print("first ouput",i)


for i in range(9,23):
                    print("second output", i)