import random

while True:
    secret_number = random.randint(1, 10)
    guesses_left = 5

    print "I am thinking of a number between 1 and 10. You get 5 guesses."

    while True:
        guessed_number = int(raw_input("Guess: "))
        guesses_left -= 1
        if guessed_number == secret_number:
            print "Correct!"
            break
        elif guessed_number > secret_number:
            print "%d is too high." % guessed_number
        else:
            print "%d is too low." % guessed_number
        if guesses_left == 0:
                print "You ran out of guesses!"
                break
        else:
            pass

    play_again = raw_input("Do you want to play again (Y or N)?")
    if play_again == "N":
        break
    else:
        pass
