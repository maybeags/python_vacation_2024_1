'''
chapter03_continue 우클릭 new package -> for_sentences
for_sentences 우클릭 new python file -> main.py

1. for 반복문의 기본 개념
    정해진 구간 혹은 집합 내의 요소들을 순서대로 꺼내면서 반복 작업을 수행
    예를 들어 지난 시간에 String의 index개념을 배웠습니다. String의 경우에는 문자열의 문자 개수만큼
    반복이 진행된다고 해석할 수 있습니다.
    사실 Collections를 기준으로 반복문을 배우는 경우도 있지만 collection 관련 수업은 추후에 예정돼있습니다.

        1) 숫자 범위를 이용한 반복
            range() : 몇 번 반복할 것인가를 지정하는 함수 -> 특히 for문과 연계돼서 자주 쓰임
'''
# for i in range(5):
#     print(i)
# 1부터 10까지의 합을 구하는 반복문
# sum = 0
# for i in range(11):
#     sum += i
#
# print(f"1부터 10까지의 합 : {sum}")
'''
        range() 함수의 응용 :
            range((시작값), 종료값, (증감값))
            
            시작값 : 생략 가능, 생략할 경우에 0부터 시작
            종료값 : 명시하지 않으면 끝까지 진행
            증감값 : 생략 가능, 생략할 경우에 1씩 증가
'''
# for i in range(1, 10, 1):       # 종료값이 10인데 1부터 시작해도 9까지 나옵니다.
#     print(i)                    # 종료값 바로 앞까지 출력이 이루어짐

'''
        2) 문자열을 이용한 반복
            문자열의 경우 []를 통해 내부에 인덱스 넘버를 명시할 수 있다는 것을 지난 시간에 배웠습니다.
            그래서 in range()를 사용하는 방법과,
            향상된 for문을 사용하는 방법으로 문자를 하나씩 추출할 수 있습니다.
'''
# str_example = "Hello"
# # (1) in range를 이용하는 방법
# for i in range(len(str_example)):       # len() : () 안에 들어가는 요소의 길이를 반환하는 함수
#     print(str_example[i])

# print()
# print(str_example[0])
# print(str_example[1])
# print(str_example[2])
# print(str_example[3])
# print(str_example[4])
# (2) 향상된 for문을 사용하는 방법
# for letter in str_example:
#     print(letter)
'''
    for 반복문의 형식 :
    
for 변수 in 반복대상객체:
    반복실행문
    
반복대상객체(iterable) : 내부에 요소가 다수 들어가 있어 반복적으로 요소의 데이터를 다룰 수 있는 객체
    ex) str, list, tuple, set, dict -> 현재 저희는 str만 배웠습니다.
    
주의사항
    if 조건문과 마찬가지로 들여쓰기(indented writing)가 매우 중요합니다.
    프로그램(IDE)에 따라서 탭을 한 번 누른 것이 들여쓰기의 범위로 설정되는데,
    스페이스 바 기준 2번인 경우와 4번인 경우로 나뉩니다.
    
    예를 들어 파이참은 4번이 기본 설정으로 되어 있습니다.
    
        
    문자열에서 특정 문자의 개수 세기
'''
count_a = 0

for letter in "banana":
    if letter == "a":
        count_a += 1
        print(letter)           # a
    print(letter)               # b a n a n a

print(f"a의 개수 : {count_a}")
'''
reeborg's world #1

def turn_right():
    for _ in range(3):
        turn_left()

for _ in range(6):
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
reeborg's world #2

def turn_right():
    for _ in range(3):
        turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    jump()
    
reeborg's world # 3

def turn_right():
    for _ in range(3):
        turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        
def turn_right():
    for _ in range(3):
        turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal():
    while front_is_clear():
        move()
    jump()
    
reeborg's world # 4

def turn_right():
    for _ in range(3):
        turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    
    turn_left()
    
while not at_goal():
    if front_is_clear():
        move()
    else:    
        jump()
        
미로 찾기 우수법 형태를 코드로 구현 #1

def turn_right():
    for _ in range(3):
        turn_left()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_on_right() and not front_is_clear():
        turn_left()
    elif not wall_on_right():
        turn_right()
        move()
        
미로 찾기 우수법 형태를 코드로 구현 #2

def turn_right():
    for _ in range(3):
        turn_left()

while not at_goal():
    if wall_on_right():
        if front_is_clear():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()        
'''
