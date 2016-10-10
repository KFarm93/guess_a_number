print "I am thinking of a number between 1 and 10. You get 5 guesses."
guessedNumber = int(raw_input("Guess:"))
count = 0
while True:
    count = count + 1
    print "Nope! Guess again."
    print "You have guessed", count, "time(s)."
    guessedNumber = int(raw_input("Guess: "))
    if guessedNumber == 5:
        break

        while True:
            answer = raw_input("Would you like to play again? (y/n): ")
            if answer in ('y', 'n'):
                break
                print "Invalid input."
            if answer == 'y':
                continue
            else:
                print "Goodbye."
                break
    else:
    print "Out of guesses! You lose."
    while True:
        answer = raw_input("Would you like to play again? (y/n): ")
        if answer in ('y', 'n'):
            break
        print "Invalid input."
    if answer == 'y':
        continue
    else:
        print "Goodbye."
        break
