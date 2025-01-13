import random
from hangman_arts import *      # *
# : asterisk로 발음하고 의미는 : all
from hangman_word_list import *


chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")

display = []

for _ in chosen_word:
    display.append("_")

lives = 6
end_of_game = False

while not end_of_game:
    print(stages[lives])
    guess = input("알파벳 입력 >>> ").lower()

    for i in range(len(chosen_word)):

        if guess == chosen_word[i]:
            display[i] = guess
    print(" ".join(display))

    if guess not in chosen_word:
        lives -= 1
        print(f"당신의 기회는 {lives}번 남았습니다.")
        if lives == 0:
            print("모든 기회를 잃었습니다.")
            print(f"정답은 {chosen_word} 입니다.")
            print(stages[0])
            end_of_game = True

    if "_" not in display:
        print("정답입니다.")
        break
