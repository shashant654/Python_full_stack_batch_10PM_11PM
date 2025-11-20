# list => it can store multiple types of data.

# [11, 1.1, "Ravi", 66666]

# list methods :-

# 1. append() => it is used to add only single element at the end of any list . 

# my_listt = [11,22,33,44]
# print("before any operation", my_listt)
# my_listt.append(99)
# print("after operation", my_listt)
# my_listt.append(388,77)
# print("at the last :", my_listt)


# extend() => it is used to add multiple elements at the end of list .

# my_listt = [11,22,33,44]
# print("before any operation", my_listt)
# my_listt.extend([33333,99999])
# print("after operation", my_listt)
# my_listt.extend(33333,99999) #  list.extend() takes exactly one argument (2 given)
# print("at the last :", my_listt)


# insert() => by using insert() we can add element at any specific index.

# my_listt = [11,22,33,44]
# print("before any operation", my_listt)
# my_listt.insert(2, 999)
# print("after operation", my_listt)


# remove() => by using this method we can remove any specific element from the list.

# my_listt = [11,22,22,33,44]
# print("before any operation", my_listt)
# my_listt.remove(22) ## it takes only one argument.
# print("after operation", my_listt)


# pop() =>by default  this method can remove last element from the list. otherwise it can remove element from specific index.

# my_listt = [11,22,24,33,44]
# print("before any operation", my_listt)
# # my_listt.pop() 
# my_listt.pop(1)
# print("after operation", my_listt)


# index() => it can return the index of specific element from the list.

# my_listt = [11,22,24,33,44, 100, 1000,100]
# print("before any operation", my_listt)
# print("index of 24:", my_listt.index(24))  # it returns the index of specific element.
# print("index of 100:", my_listt.index(100))  # ValueError: 100 is not in list
# print("after operation", my_listt)


# count() => it can return the count of specific element from the list.

# my_listt = [11,22,24,33,44, 100, 1000,100]
# print("before any operation", my_listt)
# print("count of 100:", my_listt.count(100))  # it returns the count of specific element.
# print("after operation", my_listt)


# sort() => it can sort the elements of list in ascending order.

# my_listt = [11,22,24,33,44, 100, 1000,100,77]
# print("before any operation", my_listt)
# my_listt.sort()  # it sorts the list in ascending order.
# print("after operation", my_listt)


# reverse() => it can reverse the elements of list.


# my_listt = [11,22,24,33,44, 100, 1000,100,77]
# print("before any operation", my_listt)
# my_listt.reverse()  # it reverses the list.
# print("after operation", my_listt)


# copy() => it can create the copy of list.

# my_listt = [11,22,24,33,44, 100, 1000,100,77]
# print("before any operation", my_listt)
# my_second_list = my_listt.copy()  # it copies the list.
# print("after operation", my_second_list)



# my_listt = [11,22,24,33,44, 100, 1000,100,77]
# print("before any operation", my_listt)
# my_listt.clear()  # it clears the list.
# print("after operation", my_listt)