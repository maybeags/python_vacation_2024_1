# import문의 활용
from hangman_arts import *
from hangman_word_list import word_list
import random

# 함수 정의
def play_hangman():
    # 로고 출력
    print(logo)
    # random.choice를 이용하여 임의의 단어 추출
    chosen_word = random.choice(word_list)
    # print(f"테스트 단어 : {chosen_word}")
    # 비어있는 display list 선언 및 초기화
    display = []
    #반복문을 돌리기 위한 end_of_game 변수 선언 및 초기화
    end_of_game = False
    # lives 변수 선언 및 초기화
    lives = 6
    # display에 chosen_word의 문자 개수만큼 반복문을 돌리면서 "_"를 더해줍니다.
    for _ in chosen_word:
        display.append("_")
    #display에 "_"가 제대로 들어갔는지 확인하는 테스트 코드
    # print(display)
    # 반복문 시작
    while not end_of_game:
        #현재 lives 상황에 따른 hangman 그림 표시
        print(stages[lives])
        # 알파벳을 입력 받을 guess 변수 선언 및 input() 함수 적용 + .lower() 메서드 적용
        guess = input("알파벳 입력 >>> ").lower()
        # chosen_word의 길이(=display의 길이)만큼 반복문 돌립니다 -> 반복문 돌면서 guess와 chosen_word[i] 일치하는
        # 알파벳이 있는지 확인하기 위해서
        for i in range(len(display)):
            if guess == chosen_word[i]:
                display[i] = guess
                # list로 그대로 보는 방법
                # print(display)
                # .join을 이용해서 str으로 바꾸는 방법
        print(" ".join(display))

        # 반복문 바깥에서 guess가 chosen_word에서 하나도 일치하지 않는다면 lives -= 1해야함 -> 행맨 그림도 있어야겠네요.
        if guess not in chosen_word:
            lives -= 1
            print(f"틀렸습니다. 기회는 {lives}번 남았습니다.")
            if lives == 0:
                print(f"모든 기회를 잃었습니다. 정답은 {chosen_word}입니다.")
                # lives == 0이라면 반복문 종료
                print(stages[0])    # 현재 상황에서는 다리 두쪽 다 나오게 하려면 사용할 임시 방편
                end_of_game = True

        # 반복문 바깥으로 나와서 다 맞췄을 때에 해당하는 코드 작성

        # if not "_" in display:  #display list 안에 더이상 "_"가 없을 때
        if "".join(display) == chosen_word: #display를 .join()을 통해 str으로 만들었을 때 그 결과값이 chosen_word와 같을 때
            print("정답입니다.😃 축하합니다.")
            end_of_game = True

# 함수 호출
play_hangman()


