import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# TODO - 1 : word_list 만드세요
word_list = ["apple", "banana", "camel"]
# TODO - 2 : chosen_word 적용하세요. + 테스트단어 print하세요
chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")
# TODO - 3 : 비어있는 display list를 만드세요.
display = []
# TODO - 4 : chosen_word의 문자 개수만큼 display에 "_"를 추가하세요.
for _ in chosen_word:
    display.append("_")

#-------------------------- 이 위는 아까 전 부분과 다를 바 없습니다 ------------------
# TODO - 5 : 남은 목숨 수를 추적하기 위한 lives라는 변수를 선언하고, 6으로 초기화하세요.
lives = 6
# TODO - 6 : end_of_game이라는 변수를 선언하고, False로 초기화하세요.
end_of_game = False

# while True:
    # 여기다가 코딩 작성하는 경우가 우리나라에는 많습니다.
while not end_of_game:
    print(stages[lives])
    guess = input("알파벳 입력 >>> ").lower()
    #TODO - 7 : 추측한 알파벳이 chosen_word에 없으면 lives 1 감소시키는 코드를 작성하세요.
    # 그리고 감소할 때마다 "당신의 기회는 {lives}번 남았습니다." 를 출력하세요.
    # 그리고 lives가 0이 되면 "모든 기회를 잃었습니다."를 출력하고 게임을 끝내세요.
    # 맞추면 display에 _를 해당 알파벳으로 바꾸는 코드를 작성하세요.
    # 그리고 모든 문자를 맞췄다면(즉 display에 _가 없다면), "정답입니다!"를 출력하고 게임을 끝내세요.
    for i in range(len(chosen_word)):
        # 추측한 알파벳이 맞다면 사용될 조건문
        if guess == chosen_word[i]:
            display[i] = guess
            print(" ".join(display))
        # 이거 밑에거 틀린 사례입니다// 제일 빠지기 쉬운 함정
        # else:
        #     lives -= 1
        #     print(f"당신의 기회는 {lives}번 남았습니다.")
        #     if lives == 0:
        #         print(f"모든 기회를 잃었습니다.")
        #         # break;
        #         end_of_game = True

    # 위의 함정 사례의 경우 알파벳 입력할 때마다 모든 인덱스에서 알파벳이 맞는지 아닌지 확인하는
    #조건문이 실행되기 때문에, 즉 반복문 내부에 조건문이 있기 때문에
    #guess를 한 번만 입력했음에도 lives가 여러 번 -=1이 이루어지게 됩니다.
    # 이상을 이유로 guess가 틀렸을 때의 조건문은 for 반복문 바깥에서 작성해야만 합니다.
    # guess가 전체 chosen_word에 하나라도 포함이 돼있는지를 확인하는 조건문을 작성하겠습니다.
    if guess not in chosen_word:    #즉, 단 하나의 알파벳도 일치하지 않으면, 이라는 의미
        lives -= 1
        print(f"당신의 기회는 {lives}번 남았습니다.")
        # lives가 감소하고 있는 중에 만약에 lives == 0이라면 while 반복문 종료돼야 함.
        if lives == 0:
            print("모든 기회를 잃었습니다.")
            print(f"정답은 {chosen_word} 입니다.")
            print(stages[0])
            end_of_game = True

    # 정답을 맞췄을 때 정답입니다 혹은 축하합니다 반복문을 종료시킬 수 있도록 코드를 작성

    if "_" not in display:
        print("정답입니다.")
        break
# TODO - 8 : 게임이 끝났을 경우, 정답을 출력해주세요.