# Lists
# Commonly used to store the data
# Are MUTABLE
# Syntax [] used to create a list

shopping_list = ["bread", "chocolate", "avocado", "milk"]
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[0]) # bread
# print(shopping_list[-2]) # avocado

# Change list values
print(shopping_list)
shopping_list[0] = "orange"
# print(shopping_list)

# Add list values
shopping_list.append("ice cream")
# print(shopping_list)

# Remove a specified item
shopping_list.remove("orange")
# print(shopping_list)

# Mixed lists
mixed_list = [1, 2, 3, "one", "two", "three"]
print(mixed_list)
print(mixed_list[1:3]) # [2, 3]