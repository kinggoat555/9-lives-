import random

lives  = 10
words = ["pizza","apple","plane","mouse","mouth","prime"]
secret_word =random.choice(words)
clue = list("?????")
heart_symbol = U'\u2764'
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word, clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index +=1
while lives > 0:
    print(clue)
    print('Lives Left: ' + heart_symbol  * lives)
    guess = input('guess a letter or the whole word: ')
    if guess == secret_word:
        guessed_word_correctly=True
        break
    if guess in secret_word:
        update_clue(guess,secret_word,clue)
    else:
          print('incorrect . you lose a life ')
          lives = lives - 1
if guessed_word_correctly:
    print("you won, your word was " + secret_word)
else:
    print("you lose, secret word was " + secret_word)