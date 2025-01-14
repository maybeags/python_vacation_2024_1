from timeit import default_timer

MENU = {
    "에스프레소": {                              # 다 하신 분들은 라떼의 우유 양을 콘솔에 출력하시오
        "재료": {                               # 카푸치노의 가격을 콘솔에 출력하시오
            "물": 50,                           # 에스프레소의 물 양을 콘솔에 출력하시오
            "커피": 18,
        },
        "가격": 1.5,
    },
    "라떼": {
        "재료": {
            "물": 200,
            "우유": 150,
            "커피": 24,
        },
        "가격": 2.5,
    },
    "카푸치노": {
        "재료": {
            "물": 250,
            "우유": 100,
            "커피": 24,
        },
        "가격": 3.0,
    }
}
# print(MENU["라떼"]["재료"]["우유"])# 라떼 - 우유
# print(MENU["에스프레소"]["재료"]["물"])# 에스프레소 - 물
# print(MENU["카푸치노"]["가격"])# 카푸치노 - 가격
profit = 0
resources = {
    "물": 300,
    "우유": 200,
    "커피": 100,
}
# 함수들을 정의
# 자원이 충분한지 확인하는 함수
def is_resource_enough(order_ingredients):
    """DocString : 함수/클래스/메서드가 어떤 작동을 하는지 '사람들에게' 설명해주는 기능
    주문 받은 음료를 resources에서 재료 차감을 하고 난 후, 음료 만들기가 가능하면
    True 반환, 아니면 False반환
    :param order_ingredients:
    :return: True / False
    """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"죄송합니다. {item}이(가) 부족합니다.")
            return False
        return True # 굳이 else를 쓰지 않은 이유 : 위의 if문이 실행되지 않았다면 어차피 True기 때문에

# 동전을 처리하는 함수
def process_coins():
    """동전들을 입력 받아 전체 금액을 반환하는 함수"""
    print("동전을 넣으세요.")
    # 쿼터, 다임, 니켈, 페니 네 종류의 동전
    # 쿼터 = 0.25 달러
    # 다임 = 0.1 달러
    # 니켈 = 0.05 달러
    # 페니 = 0.01 달러
    # quarters, dimes, nickels, pennies, sum/total
    # 지역 변수가 너무 많은 예시
    # quarters = int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.25
    # dimes = int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.1
    # nickels = int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.05
    # pennies = int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.01
    # total = quarters + dimes + nickels + pennies
    # return total
    total = 0.0
    total = int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.25
    total += int(input("다임 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.1
    total += int(input("니켈 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.05
    total += int(input("페니 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.01
    return total

# 들어온 동전 금액과 가격을 비교하는 함수를 정의
def is_transaction_successful(money_received, drink_cost):
    """거래가 수락되면 True / 실패하면(동전의 총합이 음료 가격보다 적다면) False"""
    charge = money_received - drink_cost
    if charge >= 0:
        global profit       # 해당 함수가 전역변수인 profit의 값을 바꾸기 위해 사용되는 명령어
        profit += drink_cost
        print(f"잔돈 $ {charge}를 반환합니다.")
        return True
    else:
        print("죄송합니다. 돈이 충분하지 않습니다. 동전을 반환합니다.")
        return False

# main 단계
is_on = True
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>> ")
    # 만약에 choice가 off라면 반복문을 종료하는 코드를 입력하세요.
    if choice == "off":
        is_on = False
        # break
    elif choice == "report":
        # print(f"물 : {resources["물"]}\n우유 : {resources["우유"]}\n커피 : {resources["커피"]}\n수익 : {profit}")
        print(f"물 : {resources["물"]}")
        print(f"우유 : {resources["우유"]}")
        print(f"커피 : {resources["커피"]}")
        print(f"수익 : {profit}")
        # 메뉴명을 올바르게 입력했을 때 이루어지는 자판기의 처리 과정
        #   1. 해당 음료에서 소모되는 원재료의 양이 자판기 내에 충분히 있는지를 확인 True/False
        #   2. 동전을 넣는 process를 확인 -> 동전의 총합 -> 음료 가격보다 높으면 다음 과정으로 ->
        #   3. 자판기의 원재료에서 음료가 요구하는 원재료만큼 차감, 자판기의 수익을 더해야 함(음료 가격만큼) -> 음료 추출
    #여기에 입력할 조건문 : choice가 라떼, 에스프레소, 카푸치노 중 하나일 경우를 elif로 작성하시오.
    elif choice in ("에스프레소", "라떼", "카푸치노"):
        print(is_resource_enough(MENU[choice]["재료"]))
            # 다음 단계로 진행
    # 메뉴명에 오타가 있을 경우 -> 잘못 입력하셨습니다. 다시 입력해주세요가 출력돼야 함. else로 입력하시오.
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")