import random
import hangman_words
#task-1: to generate random words from a given list everytime its compiled

for word in hangman_words.words:
    word=random.choice(hangman_words.words)
print(word)

#task-2: ask the user to guess a letter and assign the letter to a variable guess. and use the while loop to let the user guess again

game_over=False
correct_letters=[]
while not game_over:
    guess=input("enter a letter:").lower()
    if guess in correct_letters:
         print(f"you have already guessed the letter {guess}, try something else.")
    
    display= ""

#task-3: create a placeholder "letter" with the same length as the number of letters in the random chosen word

    placeholder= ""
    word_length=len(word)

    for position in range(word_length):
        placeholder+="_"
    

#task-4: check if the letter in the chosen word is one of the letters of the chosen word. if yes print right.
    lives=6

    for letter in word:

        if guess==letter:
                print(f"you have guessed the letter {guess}")
                display+=guess
                correct_letters.append(guess)
            
        
        elif letter in correct_letters:
            display+=letter
            
        else:
                display+="_"

    if guess not in word:
         print(f"you guessed the wrong letter {guess}. you lose a life.")
         lives-=1
         if lives==0:
              game_over=True
              print(f"it was the word {word}")
              print("you lose.")

#taske-5: change the while loop so that you can keep track of the previous correct letters in the display
    print(display)

#task-6: create a variable lives to keep the track of the number of lives remaining . set lives=6

    

    if "_" not in display:
        game_over=True
        print("you win")