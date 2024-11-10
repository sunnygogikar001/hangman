
import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'development', 'function', 'variable', 'loop', 'condition']
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |   
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |   
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |   
           |
        """,
        """
           ------
           |    
           |    
           |    
           |   
           |
        """,
        """
           ------
           
           |    
           |    
           |   
           |
        """
    ]
    return stages[tries]

def hangman():
    word = choose_word()
    guessed = []
    tries = 6
    guessed_word = ['_'] * len(word)

    print("Welcome to Hangman!")
    
    while tries > 0 and '_' in guessed_word:
        print(display_hangman(tries))
        print("Word: " + ' '.join(guessed_word))
        print("Guessed letters: " + ' '.join(guessed))
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed:
            print("You've already guessed that letter.")
            continue
        
        guessed.append(guess)
        
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess!")
        else:
            tries -= 1
            print("Incorrect guess. You have {} tries left.".format(tries))
        
    if '_' not in guessed_word:
        print("Congratulations! You've guessed the word: " + word)
    else:
        print(display_hangman(tries))
        print("Sorry, you've run out of tries. The word was: " + word)

if __name__ == "__main__":
    hangman()
