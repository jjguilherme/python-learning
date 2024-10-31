import random

word_list = ["python", "hangman", "development", "challenge", "openai", "programming", "computer", "science", "algorithm", "variable"]

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = "_" * len(chosen_word)
print("Palavra:", placeholder)

lifes_remaining = 5

while lifes_remaining > 0 and "_" in placeholder:
    user_letter = input("Choose a letter: ").lower()

    if user_letter in chosen_word:
        for letter in range(len(chosen_word)):
            if chosen_word[letter] == user_letter:
                placeholder = placeholder[:letter] + user_letter + placeholder[letter+1:]
        print("Good Guess!")
    else:
        lifes_remaining -= 1
        print("Wrong guess! Attempts left:", lifes_remaining)

    print("Palavra atualizada:", placeholder)

if "_" not in placeholder:
    print("Congratulations! You guessed the word:", chosen_word)
else:
    print("Out of attempts. The word was:", chosen_word)
