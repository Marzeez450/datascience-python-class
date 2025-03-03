# num = 10
# float_number =30.10
# comp = 3 + 4j
# text ='I went to school yesterday'
# upper_case =text.upper()
# str_lenght =len(text)
# is_rainy = False
# is_cloudy = True
# name ="Olaide"
# print("Hello " + name)
# text = " oluyeye olaide " 
# str_lenght =len(name)

# print(type(num))
# print(type(float_number))
# print(type(comp))
# print(type(text))
# print(upper_case)
# print(str_lenght)
# print(type(is_rainy))
# print(type(is_cloudy))
# print(text[:20])
# print(type(30))
# print(type(25.50))
# print(type(3 + 4j))
# print(type(name))


# fruits = ["apple","banana","mango","watermelon" ]

# print(type(fruits))
# fruit = fruits.append("orange")

# fruit_remove =fruits.remove("apple")
# print(type(fruits))
# print(fruits)

# tup = (10, "Alice" , True, "James" , 3 + 4j, 5.45)

# unique_items ={3, 2, 2, 3, 9, 5, 10, 6, 5, 7, "Alice" ,True, 50.70, 3 + 4j}
# print(type(unique_items))
# print(unique_items) 

# person ={
#     "name": "Alice",
#     "age" : 30,
#     "gender" : "male",
#     "Height" : 50.90,
#     "is-single" : True
# }

# print(person.keys())
# print(person.items())
# print(person.values())


# result = None
# print(type(result))
# result = 10
# print(type(result)) 

# x = 10
# y = 3

# print("Addition:" , x + y)
# print("Subtraction:" , x - y)
# print("Multiplication:" , x * y)
# print("Division:" , x / y)
# print("Floor:" , x // y)
# print("Modulus:" , x % y)
# print("Exponential:" , x ** y)


# x = True
# y = False

# print(x and y)
# print(x or y)
# print(not x)

# if (10 < 3) and(5 > 2):
#     print("This conditin is True")
# elif (10 > 3) or (5 < 3):
#     print("This elif condition is True")
# else:
#     print("Both condition is not true")


# x = 10
# y = 3

# print(x == y)
# print(x != y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)

# fruits = ["apple" , "banana" ,"orange"]
# fruit_choice = input("Enter your fruit:")
# if fruit_choice in fruits:
#        print(f"Yes '{fruit_choice}' is in fruits")
# else:
#    print(f"There is not '{fruit_choice}'in fruits")



# #   BITWISE OPERATOR

# x = 5
# y = 3
# print(x & y)

 
# x = 20
# y =11
# print(x | y)


# x = 20
# y = 15
# print(x ^ y)

# x = 20
# # y = 15

# print(~x)

# x = 10
# y = 15
# print(x <<2)


# a = 10
# b = 20
# max_value = a if a > b else b
# print(max_value)


# a = 10
# b = 20
# max_value = print(f'{a} is less than {b} and {b} is greater than {a}') if (a < b) and (b > a) else print("The condition is false")

# x = 5
# x += 5
# print(f"After x += 5: {x}")

# x -= 5
# print(f"After x -=5: {x}")

# x *= 5
# print(f"After x *= 5:{x}")

# x /= 5
# print(f"After x /= 5:{x}")

# x //= 5
# print(f"After x //= 5:{x}")

# x %= 5
# print(f"After x %= 5: {x}")

# print(f"The remaining value for x is:{x}")


# text = "Hello, World"

# frst_txt = text[5]
# print("index 5" , frst_txt)

# first_slice = text[2:7]
# second_slice = text[:7]
# third_slice = text[3:]
# step_slice = text[::2]

# print("From index 2 - 6" , first_slice)
# print("From index 0 - 6" , second_slice)
# print("From index 3 to the end" , third_slice)
# print("Step the  index by 2" ,step_slice)

# text = "   Python is Good!    "

# low = text.lower()
# caps = text.capitalize()
# upper = text.upper()
# rep = text.replace("Good", "Great" )
# strip = text.strip()

# print(low)
# print(caps)
# print(upper)
# print(rep)
# print(strip)


# name = "John"
# age = "20"

# print("My name is " + name + " , I'm " + age +" years old")

# another_age = 20

# print("Your name is " + name + " and you will be " + str(another_age + 1) + " next year")

# rep = "Ha"
# print(rep * 4 )

# name = "Alice"
# age = 20

# print(f"My name is {name}, and I'm {age} years old")
# print(len(name))

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# gender = input("Enter your gender (Male/Female): ")
# print(type(name))

# print(f"Welcome {name} , you are {age + 1} years old and your gender is {gender}" )

# question = input("Have you eaten?(yes/no):").lower()
# printquestion == "yes"


# lst = [1, "apple" , 3, 5, 20.75,"banana" , 3 + 4j, True, False]
# lst.append
# pop_lst = lst.pop(7)
# lst.insert(1, "pine_apple")
# lst.remove(False)
# lst_index = lst[6]
# lst_slice = lst [2:7]

# print(lst_index)
# print(lst_slice)
# print(lst)
# print(pop_lst)
# print(lst.index(1))

# tup = (1, "apple" , 3, 5, 20.75,"banana" , 3 + 4j, True, False)

# tup_index = tup [6] #tuple indexing
# tup_slice = tup[:5] #tuple slicing

# print(tup_index)
# print(tup_slice)


# age = 5
# if age > 10:
#     print(f"Yes {age} is greater than ten")
# elif age >= 10:
#     print(f"Yes {age} is equal to 5")
# else:
#     print(f"No {age} is less than 10")


# grade = 80
# if grade >= 90:
#     print("Grade: A")
# elif grade >= 80:
#     print("Grade: B")
# else:
#     print("Grade: C")


# #Even number generating
# count = 0
# while count  < 10:
#     if count % 2 ==0:
#         count += 1
#         continue
#     count += 1
#     print(count)


# #odd number generating
# counter = 0

# while counter < 10:
#     if counter % 2 == 1:
#         counter += 1
#         continue

#     counter += 1
#     print(counter)


# num = 0

# while num < 20:
#     if num == 15:

#         break
#     num += 1
#     print(num)


# a = 20
# b = 10

# print(f"{a} is greater than 10") if a > 10 else print(f"{a} is not greater than 10")


# x = 5

# x += 5
# print(f"After x += 5: {x}")

# x -= 5
# print(f"After x -= 5: {x}")

# x *= 5
# print(f"After x *= 5: {x}")

# x /= 5
# print(f"After x /= 5: {x}")

# x //= 5
# print(f"After x //= 5: {x}")

# x **= 5
# print(f"After x **= 5: {x}")

# x %= 5
# print(f"After x %= 5: {x}")


# text = "I love Python"

# print(text[-2])

# print(text[:-1])

# print(text.upper())
# print(text.lower())
# print(text.replace("love", "like"))





# for i in range(20):
#     if i % 2 == 0:
#         print(i)


# lst = ["apple", "banana", True, 3 + 4j, 20.98, 20]

# for i in lst:
#     if i == 3 + 4j:
#         break
#     print(i)

# lst = ["apple", "banana", True, 3 + 4j, 20.98, 20]

# for i in lst:
#     if i == 3 + 4j:
#         continue
#     print(i)


# [print(i) for i in range(20) if i % 2 == 0]


# student = {
#     "name": "Alice",
#     "age": 24,
#     "gender": "male",
#     "height": 30.56,
#     "is_active": True
# }

# for stu_key in student.keys():
#     print(stu_key)

# for stu_value in student.values():
#     print(stu_value)

# for stu_item in student.items():
#     print(stu_item)

# [print(stu_item) for stu_item in student.items()]

# x = 20

# rang = {x: x**2 if x <= 20 else print("The condition is not true")}

# print(rang.items())


# person = {}

#CREATE OPERATION
# person["name"] = "Alice"
# person["age"] = 30
# person["gender"] = "male"
# person["marital_status"] = "single"

#RETRIEVE OPERATION
# retrieve_person = ["name"]

# #UPDATE OPERATION
# person["age"] = 32
# person["gender"] = "female"

#DELETE OPERATION
# del person["name"]
# del person["age"]
# del person["gender"]
# person["marital_status"]

# def greet(first_name, last_name):
#     print(f"Good morning {first_name} {last_name}!")

# greet("Alice", "John")

# def add(a, b):
#     return a + b

# print(add(5, 4))

# def about_me(name, age):
#     return f"My name is {name} and I am {age} years old"

# print(about_me("John", 20))


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def division(a, b):
#     if b <= 0:
#         return "Zero division error"
#     else:
#        return a / b

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = input("Enter your calculation choice: ")

# num_1 = float(input("Enter your first number: "))
# num_2 = float(input("Enter your second number: "))

# if choice == "1":
#     print(add(num_1, num_2))
# elif choice == "2":
#     print(subtract(num_1, num_2))
# elif choice == "3":
#     print(multiply(num_1, num_2))
# elif choice == "4":
#     print(division(num_1, num_2))
# else:
#     print("Invalid number")


# def add(*args):
#     return sum(args)
# print(add(10, 20, 30, 40, 20, 20))


# def person(**kwargs):
#     for key,value in kwargs.items():
#         print (f"{key}: {value}")
# print(person(name="Ade", age=24, occupation="Software-Engineering"))

# multiply = lambda a,b: a * b
# print(multiply(5, 3))


# import random
# print(random.randint(10000, 99999))

# lst = ["apple", "banana", "cherry", "mango", "pine-apple"]
# print(f"I like to eat {random.choice(lst)}")

# from math import sqrt
# from operations import add,  subtract

# print(sqrt(25))
# print(add(5, 10))
# print(subtract(20, 10))


# try:
#     division = 10 / 4
#     print(f"Division of number: {division}")
# except Exception as e:
#     print(f"An error occur: {e}")
# else:
#     print("The program run successfully.")
# finally:
#     print("I will always be execute")


# def check_age():
#     age = int(input("Enter your age: "))

#     if age < 18:
#         raise ValueError("You must be 18 years old")
#     else:
#         print("You are an adult.")

# try:
#     check_age()
# except ValueError as e:
#     print(f"An error occured: {e}")


# def division():
#     try:
#         num_1 = int(input("Enter your first number: "))
#         num_2 = int(input("Enter your second number: "))
#         if num_2 == 0:
#             raise ZeroDivisionError("You can't divide by Zero(0)")
#         else:
#             result = num_1 / num_2
#             print(f"Division of {num_1 / num_2} is: {result}")
#     except ZeroDivisionError as e:
#         print(f"An error occured: {e}")
#     except ValueError:
#         print("Input must be number.")
#     else:
#         print("Divisiom runs successfully.")
#     finally:
#         print("Execution completed")

# print(division())


#read mode

# file = open("python.txt", 'r')
# print(file.read())
# file.close()

#readlines mode

# file = open("python.txt", 'r')
# print(file.readlines())
# file.close()

#realine mode
# file = open("python.txt", 'r')
# print(file.readline())
# file.close()

# lines = ["Hello ","Python is good ", "I am currently learning python"]
# write_file = open("dump.txt", 'w')
# print(write_file.writelines(lines))
# write_file.close()

# with open("python.txt", 'r') as file:
#     print(file.read())

# with open("write.txt", 'w') as file:
#     file.write("Hello, I'm learning python at oic hub")

import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code: {response.status_code}")






















