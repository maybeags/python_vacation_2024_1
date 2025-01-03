# random 모듈 import
import random # 단어를 임의적으로 하나 뽑기 위해서
# word_list 만들 것
word_list = [ "apple", "banana", "camel" ]
# chosen_word 만들 것
chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")
# 비어있는 list인 display 만들것
display1 = []            # 빈 리스트 만드는 법
display2 = []
# chosen_word 문자 개수만큼 display 내부에 "_"를 추가할 것
# 1. range()와 len()를 사용한 방식 : 일반 for
for _ in range(len(chosen_word)):                                        # 리스트명.append()
    display1.append("_")

# 2. 향상된 for문 -> 1, 2를 비교했을 때, _나 letter나 안쓰이는 것은 똑같습니다.
for letter in chosen_word:
    display2.append("_")

print(display1)
print(display2)

# 적어도 chosen_word에 있는 알파벳 종류만큼은 반복 횟수가 보장될거고,
# 중간에 알파벳 하나씩 맞춘다고 가정했을 때는 반복 횟수가 +1이 될겁니다
# -> 정확한 반복 횟수는 아직 모른다.
# 그렇다면 for / while문 중에 더 적합한 반복문은 뭐다? -> while
# while문을 작성한다는 것은 조건이 있다는 의미 -> 특정한 상황이 됐을 때
# while 반복문을 탈출 해야 합니다.
# display 안에 요소로 "_"가 없으면 반복문 탈출
while "_" in display1:
    guess = input("알파벳 입력 >>> ")
    # 이제 guess가 선택된 단어 중에 알파벳이 같으면 "_"를 guess 문자열로 바꿔줘야됩니다.



# input함수 적용한 guess 만들 것

print(guess)