# Create an empty list
my_list = []
print("my_list is an empty list:", my_list)

# append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("my_list after appending elements:", my_list)

# insert value at the second position
my_list.insert(2, 15)
print("my_list after inserting 15 at index 2", my_list)

# create a second list
my_list2 = [50, 60, 70]
print("my_list2 is a second list:", my_list2)

# extend the two lists
my_list.extend(my_list2)
print("my_list after extending with my_list2:", my_list)

# remove the last element from the list
my_list.pop()
print("my_list after removing the last element:", my_list)

# sort the list in ascending order
my_list.sort()
print("my_list after sorting:", my_list)

# find and print the index of 30 in the list
index_of_30 = my_list.index(30)
print(f"The index of 30 in the list is: {index_of_30}")

print("The end,that was fun!")
