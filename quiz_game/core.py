#quiz

questions = ("How many elements are in the periodic table? ",
            "which animal lays the largest eggs? ",
            "what is the most aboundant gas in the earth atmosphere? ",
            "how many bones are in the human body? ",
            "which plante in the solar sistem is the hottest? ")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. Nitrogen","B. Oxigen","C. Carbon","D. Hydrogen"),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Mars","D. Uranus"))

answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------")
    print(question)
    for option in options [question_num]:
        print(option)

    guess = input("enter (A, B, C, D)").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("correct!")
    else:
        print("incorrect!")
        print(f"{answers[question_num]} is the corret one")

    question_num += 1

    print("answerts: ", end ="")
    for answer in answers:
        print(answer, end="")
    print()

    print("guess: ", end="")
    for guess in guesses:
        print(guess, end="")
    print()

score = int(score / len(question) * 100)
print(f"your score is: {score}%")
