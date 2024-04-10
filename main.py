# Find the largest number in a list without max() in Python

my_list = [2, 8, 4, 1, 7]

largest_number = None

for number in my_list:
    if largest_number is None or largest_number < number:
        largest_number = number

# ✅ get the largest number
print(largest_number)  # 👉️ 8

# ✅ get the index of the largest number
print(my_list.index(largest_number))  # 👉️ 1