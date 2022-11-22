
# current position
position = 0

# end position
end_position = 10

# enemy position
enemy_position = 15

# move forward until end position
while position < end_position:
    position += 1
    print(position)
    
    if position == enemy_position:
        print("Game over!")
        # exit loop
        break
    
    if position == end_position:
        print("You have reached the end")
