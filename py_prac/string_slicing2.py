my_variable = "javascript"

my_name = "Ziyarat"

# 0 1 2 3 4 5 6 7 8 9
# j a v a s c r i p t

print(my_variable[9],my_name)
print(my_variable[0:6])
print(my_variable[3:9])
print(my_variable[ : 9])
print(my_variable[3: ])
print(my_name[0: 100])


# j    a  v  a  s  c  r  i  p  t
# -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

print(my_variable[-8: -1])
print(my_variable[-8: 9])
print(my_variable[9: 8])


print("Ziyarate ka question:", my_variable[-8: 0]) # nothing


print("Ziyarate ka question:", my_variable[9: 3]) # nothing

# print("ZIyarat")

print("without slicing => ",my_variable[0:9])
print("with slicing => ",my_variable[0:9:1])


print("with slicing => ",my_variable[0:9:2])

print("with slicing => ",my_variable[0:9:6])

