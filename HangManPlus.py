import random
import Design

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

word = {

    "e" : {
        "a" : ["camel", "eagle", "gecko", "horse", "koala", "lemur", "otter", "tiger", "whale", "zebra"],
        "f" : ["apple", "berry", "chery", "grape", "guava", "lemon", "mango", "melon", "olive", "peach"],
        "c" : ["chile", "egypt", "japan", "kenya", "malta", "nepal", "qatar", "spain", "sudan", "yemen"]
    },

    "m" : {
        "a" : ["beaver", "cougar", "donkey", "gopher", "magpie", "monkey", "rabbit", "salmon", "shrimp", "turkey"],
        "f" : ["banana", "cashew", "cherry", "citrus", "grapes", "orange", "papaya", "pepper", "tomato", "walnut"],
        "c" : ["brunei", "canada", "greece", "haiti", "mexico", "poland", "serbia", "sweden", "turkey", "uganda"]
    },

    "h" : {
        "a" : ["alpacas", "buffalo", "cheetah", "giraffe", "jackal", "leopard", "octopus", "ostrich", "panther", "tamarin"],
        "f" : ["avocado", "bananas", "figsaps", "jackfruit", "kumquat", "papayas", "passion", "pumpkin", "spinach", "tomatos"],
        "c" : ["algeria", "armenia", "austria", "belgium", "estonia", "finland", "germany", "hungary", "morocco", "romania"]
    }

}

while True:

    while True:
        choice = input("\nChoose a difficulty ( easy(E) - medium(M) - hard(H) ) or close(C): ").lower().strip()
        dif_let = choice[0]
        if dif_let == "e" or dif_let == "m" or dif_let == "h":
           break
        elif dif_let == "c":
            exit()
        else:
            print(Design.shape1("\nYou must choose a difficulty among ( easy(E) - medium(M) - hard(H) )")) 


    while True:
        cat = input("\nChoose a category ( animal(A) - fruit(F) - country(C) ): ").lower().strip()
        cat_let = cat[0]
        if cat_let == "a" or cat_let == "f" or cat_let == "c":
            sec_word = random.choice(word[dif_let][cat_let])
            game = "_" * len(sec_word)
            break
        else:
            print(Design.shape1("\nYou must choose a category among ( animal(A) - fruit(F) - country(C) )"))

    display = list(game)
    tries = 6    
    guessed_letters = []
    right_letters = []
    while tries != 0:

        while True:
            print("\n"+HANGMAN_PICS[6-tries])
            Design.shape3("".join(display))
            print(f"Guessed letters: { " - ".join(guessed_letters) } ")
            print(f"You have {tries} tries remaining",end="\n\n")
            if "_" not in display:
                print(f"\n     ---<( You won {Design.hands("clap")} )>---\n")
                exit()
            guess = input("Guess a letter: ").lower().strip()
            if guess.isalpha() and len(guess) == 1 :
                if guess in sec_word and guess not in guessed_letters and guess not in right_letters:
                    num = 0
                    for let in sec_word:
                        if let == guess:
                            display[num] = guess
                            right_letters.append(guess)
                        num += 1
                    print(Design.shape1(f"Good guess {Design.correct()}"))
                    break
                elif guess in guessed_letters or guess in right_letters:
                    print(Design.shape1("You already guessed this letter"))
                else:
                    print(Design.shape1(f"Wrong guess {Design.wrong()}"))
                    guessed_letters.append(guess)
                    tries -= 1
                    break
            else:
                print(Design.shape1("You must enter a singal letter"))
    else:
        print(f"\n     ---<( You lost in cause of out of tries, the word was ( {sec_word} ) )>---\n")
        exit()