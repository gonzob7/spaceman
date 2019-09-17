from termcolor import colored, cprint
import random
import time
import sys


#This printFlush function makes it possible to make scrolling text, which makes the program a little more interactive:)
def printFlush(text):
    for c in text:
        print(c, end='')
        sys.stdout.flush()
        time.sleep(0.005)

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    return set(letters_guessed).issuperset(set(secret_word))
    pass

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''


    empty = []
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    for letter in secret_word:
        if letter in letters_guessed:
            empty.append(letter)
        else:
            empty.append("_")
    #string = empty.join
    #print(empty)
    return " ".join(empty)
    pass

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    if len(guess) > 1:
        printFlush("Error: Only one letter allowed per guess, try again!\n")
    elif guess.lower() in secret_word:
        return True
    else:
        pass
    return False

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (s
      ptring): the secret word to guess.
    '''
    #print(secret_word)
    attempts_left = 7
    solved = False

    #TODO: show the player information about the game according to the project spec
    printFlush(colored("Welcome to spaceman!\n","cyan"))
    printFlush(colored("The secret word contains: ","green"))
    secret_word_length = len(secret_word)
    printFlush(f'{secret_word_length} letters \n')
    printFlush(colored("You have 7 incorrect guesses, please enter one letter per round \n","red"))
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    letters_guessed = []
    while attempts_left > 0 and not solved:
        guess = input("Enter a letter: ")


        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        if is_guess_in_word(guess, secret_word):
            printFlush(colored("Letter in secret word!\n","cyan"))
            print('----------------------------------')

        else:
            printFlush("Wrong!\n")
            attempts_left -= 1
            printFlush(f"{attempts_left} attempts left!\n")
            print('----------------------------------')

        letters_guessed.extend(guess)

        #TODO: show the guessed word so far
        print(get_guessed_word(secret_word,letters_guessed))
        #TODO: check if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed):
            printFlush(colored("\nCongrats!!!! You win\n\n","green",attrs = ["bold","blink"]))
            break
    else:
        printFlush(colored("\nGame Over:(\n\n",'red', attrs = ['blink','bold']))




#TEST FUNCTIONS
def test_is_guess_in_word():
    assert is_guess_in_word('a', 'animal') == True, "GUESSED LETTER ISNT IN SECRET WORD"
    assert is_guess_in_word('l', 'animal') == True, "GUESSED LETTER ISNT IN SECRET WORD"

def test_is_word_guessed():
    assert is_word_guessed('cat', ['c','a','t']) == True, 'HAVENT GUESSED WORD'
    assert is_word_guessed('doggo', ['d','o','g']) == True, 'HAVENT GUESSED WORD'
#Run Tests
test_is_guess_in_word()
test_is_word_guessed()
#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
