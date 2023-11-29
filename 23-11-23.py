# Create a function calculate_total_salary that takes in the base salary and additional
# bonuses (as keyword arguments) for an employee. The function should consider a default bonus
# of 0 if none is provided. Use *args for handling multiple additional bonuses.

# # Test cases
# print(calculate_total_salary(50000))  # Test with only base salary
# print(calculate_total_salary(50000, 2000, 3000))  # Test with base salary and additional bonuses
# print(calculate_total_salary(50000, 2000, 3000, health_insurance=1000, travel_allowance=1500))  # Test with kwargs


# def calculate_total_salary(base_salary, *args, **kwargs):
#     additional_bonus = sum(args)
#     bonus = sum(kwargs.values())
#     total_bonus = additional_bonus + bonus

#     total_salary = base_salary + total_bonus
#     return total_salary


# print(calculate_total_salary(50000))
# print(calculate_total_salary(50000, 2000, 3000))
# print(
#     calculate_total_salary(
#         50000, 2000, 3000, health_insurance=1000, travel_allowance=1500
#     )
# )


# Create a function create_greeting that takes a person's name as a mandatory
# argument, a message as a default parameter, and any additional
# information as keyword arguments. The function should return a formatted greeting message.

# print(create_greeting("Alice"))  # Test with mandatory argument only
# print(create_greeting("Bob", "Hi"))  # Test with default parameter and mandatory argument
# print(create_greeting("Charlie", age=30, location="New York"))  # Test with additional keyword arguments


# def create_greeting(name: str, message="Hi", **kwargs: str) -> str:
#     additional_info = "additional_info: "
#     for key, value in kwargs.items():
#         additional_info = f"{key} is {value}\n "
#     greeting = f"{message} {name},\n {additional_info}"
#     return greeting


# print(create_greeting("Alice"))
# print(create_greeting("Bob", "Hello"))
# print(create_greeting("Charlie", age=30, location="New York"))


# Create a function generate_shopping_list that accepts a title for the
# list, defaulting to "My Shopping List," and any number of items using *args. The function should
# return a formatted shopping list with the title and items.


# def generate_shopping_list(*args, title="My shopping list") -> str:
#     shopping_list = {"title": title, "items": []}
#     if args:
#         items = []
#         i = 1
#         for arg in args:
#             items.append(f"{i}. {arg}")
#             i += 1
#         shopping_list["items"] = items

#     formatted_list = f"{shopping_list['title']}:\n"
#     formatted_list += "\n".join(shopping_list["items"])

#     return formatted_list


# print(generate_shopping_list("banana", "apple", "orange", "milk"))



def domain_name(url):
    replacements = ("www.", "http://", "https://")
    for item in replacements:
        url = url.replace(item, "")
    result = url.split(".")
    return result[0]