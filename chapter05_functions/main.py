from chapter04_hangman import *
from chapter04_hangman.hangman06_answer.hangman_answer import play_hangman

'''
chapter05_functions 패키지 생성 -> main

1. 함수(Function) : 특정 작업을 수행하는 코드 블럭을 정의하는 방법

예를 들어 '사진을 찍는다'라는 행위에 대해 생각해보면,
1) 주머니에서 폰을 꺼내고,
2) 잠금 화면을 풀고,
3) 카메라를 켜고,
4) 사진을 찍고자 하는 대상에 폰을 조준하고,
5) 셔터를 누른다.

라고 볼 수 있겠습니다. 그런데 컴퓨터는 시키는대로만 하기 때문에 사진을 찍기 위해서는 1) - 5)까지의 명령어를
입력해줘야만 합니다.
하지만 '사진을 찍는다'라는 함수 내에 1) - 5)의 명령어들을 미리 입력하고 나서, '사진을 찍는다'라는 명령어를
실행시키기만 하면 1) - 5)까지의 명령을 순서대로 수행하는 것을 함수의 개념이라고 볼 수 있습니다.

주요 수업 예시로는 reeborg's world에서 turn_right()를 정의하는 방법이었습니다.

함수 정의
def turn_right():
    turn_left()
    turn_left()
    turn_left()

함수 호출
turn_right()

2. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드
    3) 사용자 함수

3. 함수 용어 정리(멘토 파이썬에도 있습니다)
    1) 함수 정의 : 사용자 함수를 새로 만드는 것을 의미(def를 떠올리셔야 합니다. def : define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값/결과값/리턴값(return) : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미.
    
4. (사용자) 함수의 형식 :
def 함수_이름(매개변수):
    실행문
    
변수 = 함수_이름(argument)
'''
# 외부에서 실제로 우리가 만든 사용자 함수를 호출하는 사례 -> from -import와 합쳐서 생각할 것

# 함수 정의
def write_name(name):
    print(f"당신의 이름은 {name}입니다.")
# 함수 호출
write_name("안근수")