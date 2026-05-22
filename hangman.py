import random
print("Welcome to Word Guess Game")
words = ["apple", "mango", "python", "laptop", "grapes"]
word = random.choice(words)
hidden_word = []
for letter in word:
    hidden_word.append("_")
used_letters = []
attempts = 6
while attempts > 0 and "_" in hidden_word:
    print("\nHidden Word:", " ".join(hidden_word))
    print("Attempts Left:", attempts)
    guess = input("Type a letter: ").lower()
    if guess in used_letters:
        print("Letter already used")
    else:
        used_letters.append(guess)
        if guess in word:
            position = 0
            for letter in word:
                if letter == guess:
                    hidden_word[position] = guess
                position += 1
            print("Nice! Correct Letter")
        else:
            attempts -= 1
            print("Letter Not Found")
if "_" not in hidden_word:
    print("\nCongratulations! You found the word:", word)
else:
    print("\nNo more attempts left")
    print("Correct word was:", word)
    



