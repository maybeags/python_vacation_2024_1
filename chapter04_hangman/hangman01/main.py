'''
random : list 혹은 tuple 내부의 요소 중 하나를 임의적으로 선택하는 방법

random.choice(리스트명) : list 내부에 있는 단어 중 하나를 임의적으로 선택해주는 명령어
'''
import random
# numbers = [1,2,3,4,5,6,7,8,9,0]
# random_number = random.choice(numbers)
# print(random_number)
word_list = ["apple", "banana", "camel"]
#TODO - 1 : word_list에서 단어를 하나 임의적으로 선택하고,
# 해당 단어를 chosen_word라는 변수에 담으세요.

chosen_word = random.choice(word_list)

print(f"테스트 단어 : {chosen_word}")

#TODO - 2 : 사용자에게 알파벳을 하나 추측해서 입력하라고 요청하고, 이를 guess라는 변수에 담으세요.
'''
실행 예

알파벳 입력 >>> e
입력한 알파벳은 e입니다.
'''
guess = input("알파벳 입력 >>> ").lower()    # .lower() method : 대/소문자 중 무엇을 입력하더라도
print(f"입력한 알파벳은 {guess}입니다.")      # 결과값으로 소문자가 반환됨

#TODO - 3 : guess에서 입력한 문자 하나가 chosen_word의 string 중 하나와 일치하는 지를
# 반복문을 통해 확인할 수 있도록 작성하시오.(반복문과 조건문을 사용할 필요가 있습니다.)

for letter in chosen_word:
    # 여기 내부에 정답인지 오답인지 튀어나오는 조건문을 작성
    if letter == guess:
        print("정답")
    else:
        print("오답")

# for i in range(len(chosen_word)):
#     if chosen_word[i] == guess:
#         print("정답")
#     else:
#         print("오답")


'''
예를 들어 random.choice(word_list)의 결과값이 applie이고, guess에 a를 대입했다면
실행 예
알파벳 입력 >>> a
정답
오답
오답
오답
오답

이 출력되도록 코드를 작성하시면 됩니다.

'''
