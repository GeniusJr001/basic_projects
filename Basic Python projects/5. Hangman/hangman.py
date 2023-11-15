import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words).upper()
    #create a while loop that continues to iterate until there's no "-" in word
    while "-" in word or " " in word:
        word = random.choice(words)
        
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) #all the letters available to be used
    used_letters = set() #take in the values of letters that have been used
    lives = 10
    
    
    while len(word_letters) > 0 and lives > 0: #letting the code continue running until all letters have been guessed
        print("You have", lives ,"lives. ","You have used this letters: ", " ".join(used_letters)) #displaying used letters to player
        #creating a function that tells current word generation progress
        # what current word is (i.e w-rd)
        word_list = (letter if letter in used_letters else "-" for letter in word)
        print("Current word: ", " ".join(word_list))
        user_letter = input("Guess a letter: ").upper()
        #creating a loop that runs only if "user-letter" is not in used "used_letters" but in alphabet
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            elif user_letter not in word_letters:
                lives = lives-1
                print("letter not in word")
        
        #displaying that the letter as been used
        if user_letter in used_letters:
            print("You have used this letter. Try again!")
        else:
            print("invalid character! Try again!")
            
    
    if lives == 0:
        print("You died!! The word was", word)
    elif len(word_letters) == 0:
            print(f"YAY!, You won! {word}")   
    
        
hangman()

    
    