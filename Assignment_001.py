l = [1, 2, 3]
init_tuple = ('Python',) * (l.__len__() - l[::-1][0])
print(init_tuple)
# Python Lab Assignment 01
# Different Operations on Dictionary, Tuple and List

#  LIST OPERATIONS
print("LIST OPERATIONS ")

my_list = [10, 20, 30, 40]

print("Original List:", my_list)

# Append
my_list.append(50)
print("After append:", my_list)

# Insert
my_list.insert(2, 25)
print("After insert:", my_list)

# Remove
my_list.remove(30)
print("After remove:", my_list)

# Pop
my_list.pop()
print("After pop:", my_list)

# Sort
my_list.sort()
print("After sort:", my_list)


# TUPLE OPERATIONS 
print("\n TUPLE OPERATIONS ")

my_tuple = (10, 20, 30, 20, 40)

print("Original Tuple:", my_tuple)

# Count
print("Count of 20:", my_tuple.count(20))

# Index
print("Index of 30:", my_tuple.index(30))

# Length
print("Length of Tuple:", len(my_tuple))

# Maximum
print("Maximum value:", max(my_tuple))

# Minimum
print("Minimum value:", min(my_tuple))


#  DICTIONARY OPERATIONS 
print("\n----- DICTIONARY OPERATIONS -----")

my_dict = {
    "Name": "Taksh",
        "Age": 17,
            "Course": "CSE"
 }
print("Original Dictionary:", my_dict)

 # Add a new key-value pair
my_dict["College"] = "ABC College"
print("After adding College:", my_dict)

 # Update a value
my_dict["Age"] = 19
print("After updating Age:", my_dict)

 # Access a value
print("Name:", my_dict["Name"])

 # Remove an itemmy_dict.pop("Course")
print("After removing Course:", my_dict)

# Display keys
print("Keys:", my_dict.keys())

# Display values
print("Values:", my_dict.values())