# create a dictionary for key presses and actions
actions = {"r":1, "l":-1 }
print(actions)

# access the values in a dictionary by using keys
# method 1
print(actions["r"])
# method 2
print(actions.get("r"))

# change values in a dictionary via the key
actions["r"] = 2
print(actions)

# if the key does not exists, the dictionary will insert a new key and store the value
actions["u"] = 1
print(actions)

# access the list of keys from the dictionary
print(actions.keys())

# access the list of values from the dictionary
print(actions.values())

# access a list of (key, value) tuples from the dictionary
print(actions.items())

# remove a (key, value) pair from the dictionary
# method 1
del(actions["u"])
print(actions)

# method 2
actions.pop("r")
print(actions)

# check to see if a specific key exists in the dictionary
print("l" in actions)
