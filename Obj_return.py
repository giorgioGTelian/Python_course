def letter_count(text, letter):
    #your code goes here
    i = 0
    for x in text:
        if x == letter:
            i = i+1
    return i


text = input()
letter = input()
print(letter_count(text, letter))
