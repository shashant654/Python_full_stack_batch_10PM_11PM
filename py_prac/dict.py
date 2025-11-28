# dictionary => 

# => it is mutable and ordered .
# => it stores data in key-value pair .
# => keys must be unique and immutable .


# my_dict =  {
#                     "name": "Ujwal",
#                     "age": 24,
#                     "city": "Bangalore",
#                     "roll_no": 101
# }

# print(my_dict)




# my_dict =  {
#                     "name": {"Ujwal", "Ravi", "Rahul"},
#                     "age": 24,
#                     "city": "Bangalore",
#                     "roll_no": 101
# }

# print(my_dict)

# key => name , age, city, roll_no
# value => Ujwal, 24, Bangalore, 101


# my_listt = [11, 22, 33, [5, 6, 7], 55]
# print(my_listt)




# my_dict =  {
#                     "name": "Ujwal",
#                     "age": 24,
#                     "city": "Bangalore",
#                     "roll_no": 101
# }

# print(my_dict)
# print(my_dict["name"])  ## accessing value using key
# print(my_dict["age"])   ## accessing value using key
# print(my_dict["city"])  ## accessing value using key
# print(my_dict["roll_no"])  ## accessing value using key




# my_dict =  {
#                     "name": ["Ujwal", "Ravi", "Rahul"],
#                     "age": 24,
#                     "city": "Bangalore",
#                     "roll_no": 101
# }

# print(my_dict["name"])  

# print(my_dict["name"][1])  # Ravi



# Diction ary Methods:-


# # 1. keys()
# => it is used to access all keys in the dictionary .


# my_dict =  {
#                     "name": "Ujwal",
#                     "age": 24,
#                     "city": "Bangalore",
#                     "roll_no": 101
# }

# print(my_dict)
# print(my_dict.keys())  ## accessing all keys in the dictionary


# 2. values()
# => it is used to access all values in the dictionary .

# diwakar_dictionary =  {
#                     "name": "Ujwal",
#                     "age": 24,
#                     "city": "Bangalore",
#                     "roll_no": 101
# }

# print(diwakar_dictionary)
# print(diwakar_dictionary.values())  ## accessing all values in the dictionary

# 3. items()
# => it is used to access all items (key-value pairs) in the dictionary .


# diwakar_dictionary =  {
#                     "name": "Ujwal",
#                     "age": 24,
#                     "city": "Bangalore",
#                     "roll_no": 101
# }

# print(diwakar_dictionary)
# print(end="")
# print(diwakar_dictionary.items())  ## accessing all items (key-value pairs) in the


# print(diwakar_dictionary["city"].upper())  ## accessing all items (key-value pairs) in the dictionary


# 4. get()
# => it is used to access value using key in the dictionary .



# diwakar_dictionary =  {
#                     "name": "Ujwal",
#                     "age": 24,
#                     "city": "Bangalore",
#                     "roll_no": 101
# }

# print(diwakar_dictionary.get("name"))  ## accessing value using key in the dictionary




# name = "Suhani"
# print(name)

# name[2] = "z"  ## strings are immutable in python

# print(name)


# update() => it is used to update value of specific key in the dictionary .




# diwakar_dictionary =  {
#                     "name": "Ujwal",
#                     "age": 24,
#                     "city": "Bangalore",
#                     "roll_no": 101
# }

# diwakar_dictionary.update({"roll_no": 251})

# print(diwakar_dictionary)




# pop()



diwakar_dictionary =  {
                    "name": "Ujwal",
                    "age": 24,
                    "city": "Bangalore",
                    "roll_no": 101
}

diwakar_dictionary.pop("age")
print(diwakar_dictionary)

