'''
chapter06_scope package 생성 -> main.py

Scope : 범위

지역 변수 - 함수 내부에 정의된 변수
전역 변수 - 함수 외부에 정의된 변수
'''

emenies = 1         # 전역 변수

def increase_enemies():     # 함수 정의 시작
    enemies = 2             # 지역 변수인 enemies
    print(f"함수 내부의 적의 숫자는 {enemies}입니다.")

# increase_enemies()
# print(f"함수 외부의 적의 숫자는 {emenies}입니다.")

# 지역 변수 =/= 전역 변수

# 함수 정의
def drink_potion():
    potion_strength = 2     # 지역 변수
    print(potion_strength)

# print(potion_strength)    오류 발생함
# drink_potion()              # 함수 호출
# print(potion_strength)    오류 발생함
# 지역 변수가 선언되고, 이를 호출한다고 해서 이를 전역 상황에서 해당 변수를
# 참조하는 것은 불가능합니다.

# Global Scope

player_health = 10      # 전역 변수

# 함수 정의
def game():
    # 함수 내부에 함수 정의
    def drink_potion():
    #    player_health += 2  # 마찬가지로 전역 변수의 값을 바꾸는 것을
                            # 함수 내부에서 정의할 수 없습니다.

        global player_health        # global을 선언하고,
        player_health += 2          # 값을 바꿀 전역 변수 명을 쓰게 되면
    # 함수 내부의 함수 호출            # 함수 내에서 전역 변수의 값을
    drink_potion()                  # 바꿀 수 있습니다.
game()                              # 문제는
print(player_health)                # 함수가 호출될 때마다 전역 변수의 값이
                                    # 바뀌기 때문에 이를 추적하기 위해서는
                                    # 정확한 함수 호출 횟수를 알아야 한다는
                                    # 점입니다.
                                    # 이상을 이유로 함수가 전역 변수의 값을
                                    # 바꾸는 이러한 코딩 방식은
                                    # 선호되지 않습니다.
game()
print(player_health)
game()
print(player_health)
game()
print(player_health)
game()
print(player_health)
game()
print(player_health)
game()
print(player_health)








