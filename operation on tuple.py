# Create a tuple
my_tuple = (10, 20, 30, 40, 50)

# Accessing elements in the tuple
print("Accessing the elements:", my_tuple)

# Trying to update
new_tuple =(100,) + my_tuple[1:]
print("updated tuple is : ", new_tuple)

# Deleting a tuple (this will cause an error)
del my_tuple
print("Tuple deleted successfully.")

