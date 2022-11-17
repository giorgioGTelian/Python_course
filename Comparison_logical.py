# operators you will be looking at
# > >= < <= == != not or and

x_position = 10
end_position = 10

# -- comparison operators -- #
# check if you are at end position
is_at_end = x_position == end_position
print(is_at_end)

# check if you are at halfway position
is_at_halfway = x_position >= end_position / 2
print(is_at_halfway)

# -- logical operators -- #
# not operator
not_is_at_end = not is_at_end
print(not_is_at_end)

# and operator
score = 10
# game is over if score is larger than 10 and position is at the end
is_game_over = score >= 10 and is_at_end
print(is_game_over)

# or operator
score = 9
# game is over if score is larger than 10 or position is at the end
is_game_over = score >= 10 or is_at_end
print(is_game_over)
