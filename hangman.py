import random
from words import words
import string

def get_valid_word(words): #we have to make sure a valid word without spaces or anything is selected
    word = random.choice(words)
    while ' ' in word or '-' in word:
        word = random.choice(words)
        
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word that have already been guessed
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed
    lives = 6
    
    #getting user input 
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))
        #what current word is (i.e. W-R-)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input("Type something: ").upper() 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print("Letter is not in the word.")
                
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")
            
        else:
            print("Invalid character. Try again.")
    
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('You guessed the word', word, '!!')
            

hangman()