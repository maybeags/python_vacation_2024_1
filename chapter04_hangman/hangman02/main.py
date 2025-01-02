import random

word_list = [ "apple", "banana", "camel" ]
chosen_word = random.choice(word_list)
print(f"테스트 단어 : {chosen_word}")

# len() : 문자열 혹은 collection의 총 개수를 int 형태로 반환하는 함수 -> hangman01 확인해보세요.

#TODO - 1 : 빈 list인 display를 만드세요.
display = []

#TODO - 2 : chosen_word의 문자 개수만큼 display에 "_"를 추가할겁니다.
# 예를 들어서 chosen_word = camel이라면 display = [ "_", "_", "_", "_", "_" ]가 돼야 합니다.
# 그런데 여기에 display.append()를 이용해야 하고, chosen_word의 문자 개수만큼 반복이 이루어져야 합니다.

# TODO - 2를 해결하기 위해서 알아야 하는 list 관련 method :
# 리스트명.append() : 리스트의 맨 마지막 인덱스에 () 안의 요소를 추가해주는 method
word_list.append("dictionary")
# print(word_list)
# 여기다가 코드 작성 해보세요.
for _ in range(len(chosen_word)):   # 강사가 어떤 의미로 i를 넣는지 혹은 _를 넣는지를 구분하는 이유
    display.append("_")             # i는 index의 축약어로 보통 str / list에서 순서를 표기할 때
                                    # 사용하는 이니셜입니다.
                                    # 하지만 22번 라인에서 i를 응용할 필요가 없기 때문에
                                    # 해당 반복문은 단지 chosen_word의 문자 개수만큼 반복을 하라는
                                    # 의미만 존재하여, 반복문에서 변수가 사용되지 않을 때는
                                    # '_'를 사용하여 표기하는 편입니다 -> 해외 기준
print(display)
# display[1] = "p"                    # list[인덱스넘버지정] = 데이터 하면 해당 위치에 데이터가 대입


#TODO - 3 : chosen_word str을 반복문을 돌려서, 만약 그 위치가 guess와 일치하면
# display에서 해당 위치에 _를 지우고 문자로 대치하세요.
# ex) chosen_word = applie인데, guess = p라면, display = [ "_", "p", "p", "_", "_" ]가 돼야 합니다.

guess = input("알파벳 입력 >>> ")

# chosen_word의 문자 개수만큼 반복문 실행
for i in range(len(chosen_word)):
    # guess와 chosen_word의 문자가 일치하는지 확인 -> 일치하면 display를 바꿔줄 예정
    if guess == chosen_word[i]:
        display[i] = guess

print(display)
'''
41 - 42 코드라인의 해석이 중요 :
    len(chosen_word)가 5라면 len(display) 도 5 여야 합니다.
    애초에 len(chosen_word)만큼 display.append("_")를 사전에 실행했기 때문에요.
    그렇다면 chosen_word[1]과 chosen_word[2] 가 "p"라면
    display[1]과 display[2]역시 p로 바뀔 수 있어야겠습니다. 그것을 구현한 코드가 41-42까지가 됩니다. 
'''