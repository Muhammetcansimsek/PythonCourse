userName = input("Name:")

print(f"Hello {userName}, time to play Hangman!\n.............\n..........\n.......\n.....\n..\n.")

lives = 10

secretWord = "Metallica"
guess_string = ""

while lives > 0:
    
    for character in secretWord:
        if character in guess_string:
            print(character)
        else:
            print("**")
    
    guess = input("Guess a letter: ")
    guess_string += guess
    
    if guess not in secretWord:
        lives -= 1
        print(f"Wrong guess\nYou have {lives} live left")
        
        if lives == 0:
            print("YOU DIED MATE!")
            break
    