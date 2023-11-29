# function with Return Value
# Create a function called calculate_area that takes in the length and width of a rectangle and returns its area.
# funkcija su grąžinama reikšme
# Sukurkite funkciją, vadinamą calculate_area, kuri užima stačiakampio ilgį ir plotį ir grąžina jo plotą.


# def calculate_area(length: float, width: float) -> float:
#     area = length * width
#     return float(area)


# length = 5
# width = 10

# area = calculate_area(length, width)
# print("The area of the rectangle is:", area)


# length2 = 25
# width2 = 15

# area2 = calculate_area(length2, width2)
# print("The area of the rectangle is:", area2)

# Function with Default Parameters
# Create a function called power_value that takes in a base and an exponent (with a default value of 2) and returns the
# result of the base raised to the exponent.

# Funkcija su numatytaisiais parametrais
# Sukurkite funkciją, vadinamą power_value, kuri paima bazę ir eksponentą (kurio numatytoji reikšmė yra 2) ir grąžina
# pagrindo, pakelto į eksponentą, rezultatas.


# def power_value(base: int, exponent: int = 2) -> int:

#     return base**exponent


# result = power_value(5)
# print(result)
# result = power_value(2, 5)
# print(result)

# Function with Variable Number of Arguments
# Create a function called calculate_sum that takes in any number of arguments and returns their sum.

# Funkcija su kintamu argumentų skaičiumi
# Sukurkite funkciją, vadinamą calculate_sum, kuri priima bet kokį argumentų skaičių ir grąžina jų sumą.


# def calculate_sum(*args) -> int:
#     return sum(args)


# result = calculate_sum(1, 2, 3, 4, 5)
# print("Sum is:", result)


# Create a function called factorial that takes in a number n and computes its factorial using recursion.


# def factorial(x: int) -> int:
#     if x > 1:
#         rezult = x * factorial(x - 1)

#     else:
#         rezult = 1
#     return rezult


# print(factorial(5))


# Creating a list of squares of numbers from 1 to 10

# my_list = []
# for i in range(1, 11):
#     my_list.append(i**2)

# print(my_list)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares_num = [i**2 for i in my_list]
# print(squares_num)


# Filtering even numbers from a list from 1 to 10


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_num = [i for i in my_list if i % 2 == 0]
# print(even_num)


# Write a Python program to create a dictionary where keys are numbers from 1 to 5 and values are their cubes.

# my_dict = {}
# for num in range(1, 6):
#     my_dict[num] = num**3

# print(my_dict)

# my_dict = {i: i**3 for i in range(1, 6)}
# print(my_dict)

# Generate a list containing the squares of numbers from 1 to 20 but exclude numbers that are divisible by both 3 and 4.
# Sukurkite sąrašą, kuriame yra skaičių kvadratai nuo 1 iki 20, bet neįtraukite skaičių, kurie dalijami iš 3 ir 4.

# my_list = []
# for i in range(1, 21):
#     if i % 3 != 0 and i % 4 != 0:
#         my_list.append(i**2)

# print(my_list)


# def generate_squares():
#     squares_list = [i**2 for i in range(1, 21) if i % 3 != 0 and i % 4 != 0]
#     return squares_list


# result = generate_squares()
# print(result)




# Generate a list of tuples where each tuple contains the index and the value of the element from 
# the original list, but exclude elements with a value less than 10.
# original_list = [5, 15, 8, 20, 12, 7, 18]
 
# Output: [(1, 15), (3, 20), (4, 12), (6, 18)]

original_list = [5, 15, 8, 20, 12, 7, 18]
rezult_5 = [(i,x)]






# Create a dictionary where keys are the names from one list and values are the corresponding ages from another list, but only for names that have lengths greater than 4.
# names = ['Alice', 'Bob', 'Charlie', 'David'] ages = [25, 30, 35, 40]

# names = ["Alice", "Bob", "Charlie", "David"]
# ages = [25, 30, 35, 40]

# result = {names[x]: ages[x] for x in range(len(names)) if len(names[x]) > 4}
# print(result)


# variantas su zip

# def create_dict(names, ages):
#     result_dict = {name: age for name, age in zip(names, ages) if len(name) > 4}
#     return result_dict