import random

word_list = ["aadrvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range (word_length):
    placeholder += "_"
print (placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    
    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print (f"******* {lives} Remaining! *******")
        if lives == 0:
            game_over = True
            print ("******* You Lose! *******")
            print (f'****** The chosen word is "{chosen_word}"! *******')


    if "_" not in display:
        game_over = True
        print ("******* You Win! *******")