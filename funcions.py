# current position
position = 0

# implement function for increasing player position
def move_player():
    global position # access the variable outside the function
    position += 1
    print(position)
    
# call the function
move_player()
