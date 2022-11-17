# an example of a list
# name = [5, True, "string"]

# create a list of positions
enemy_positions = [5, 10, 15]

# reassign the list
enemy_positions = [5, 10, 15, 20]

print(enemy_positions)

# observe the length of the list
print(len(enemy_positions))

# access a single element in the list
print(enemy_positions[0])

# change the value at index 0 of the list
enemy_positions[0] = 6
print(enemy_positions)

# retrieve multiple elements of the list using slicing
print(enemy_positions[0:2])

# add an item to the end of the list
enemy_positions.append(25)
print(enemy_positions)

# insert an item at a specific index of the list
enemy_positions.insert(1,9)
print(enemy_positions)

# remove a specific item in the list
enemy_positions.remove(6)
print(enemy_positions)

# remove an item at a specific index of the list
del(enemy_positions[2])
print(enemy_positions)
