import random


def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           O    |
          /|\\   |
          / \\   |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
          /     |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|\\   |
                |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
          /|    |
                |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
           |    |
                |
                |
        --------
        """,
        """
           ------
           |    |
           O    |
                |
                |
                |
        --------
        """,
        """
           ------
           |    |
                |
                |
                |
                |
        --------
        """
    ]
    return stages[tries]


def hangman():
    word_list = ["anand", "somay", "keshav", "shivam"]
    word = random.choice(word_list)
    guessed = False
    letters_guessed = []
    words_guessed = []
    tries = 6
    list_word = ["_"] * len(word)

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print("_ " * len(word))

    while not guessed and tries > 0:
        guess = input("Enter a letter or word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print("You already guessed that letter.")
            elif guess not in word:
                print("Letter not in word.")
                tries -= 1
                letters_guessed.append(guess)
            else:
                print("Good guess!")
                letters_guessed.append(guess)
                list_word = list("_" * len(word))
                for i in range(len(word)):
                    if word[i] == guess:
                        list_word[i] = guess
                if "_" not in list_word:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print("Word already guessed that word!")
            elif guess != word:
                print("Incorrect guess :(")
                tries -= 1
                words_guessed.append(guess)
            else:
                guessed = True
                list_word = list(word)
        else:
            print("Invalid input")

        print(display_hangman(tries))
        print(" ".join(list_word))

    if guessed:
        print("Congrats You Won....\nYou guessed the word!")
    else:
        print(f"Game Over...\nOut of tries. The word was '{word}'.")


hangman()
