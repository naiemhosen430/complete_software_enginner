# ---------------------------------------------------<<1>>------------------------------------------------
# Count Unique Elements:
# Write a function that takes a list as input and returns the count of unique elements using a set.

# solution
# def count_unique_elements(list):
#     return len(set(list))

# data = count_unique_elements([5,7,9,74,6,45,84,5,4,56])
# print(data)

# Completed

# ---------------------------------------------------<<2>>------------------------------------------------

# Remove Duplicates:
# Given a list, create a function to remove duplicate elements from the list using a set.

# solution
# def remove_dublicate(listdata):
#     new_set = set(listdata)
#     return list(new_set)

# data = remove_dublicate([5,58,54,8,5,4,5,45,5])
# print(data)

# completed

# ---------------------------------------------------<<3>>------------------------------------------------
# Set Operations with Strings:
# Write a function that takes two strings and returns a set containing common characters between them.

# solution
# def common_character(string1, string2):
#     set1 = set(string1)
#     set2 = set(string2)

#     return set1.intersection(set2)
# data = common_character('assddas',"aasasdsdd")
# print(data)

# Completed

# ---------------------------------------------------<<4>>------------------------------------------------

# Power Set Generation:
# Implement a function that generates the power set of a given set. The power set is the set of all 
# subsets, including the empty set.

# solution
def power_set(setdata):
    to_list = list(setdata)
    


# ---------------------------------------------------<<5>>------------------------------------------------
# Set Intersection of Multiple Sets:
# Create a function that finds the intersection of multiple sets. The input can be a list of sets, and 
# the function should return a set containing elements common to all sets.