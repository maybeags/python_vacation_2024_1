MENU = {
    "에스프레소": {
        "재료": {
            "물": 50,
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

profit = 0
resources = {
    "물": 300,
    "우유": 200,
    "커피": 100,
}

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
        return True  # 굳이 else를 쓰지 않은 이유 : 위의 if문이 실행되지 않았다면 어차피 True기 때문에


def process_coins():
    """동전들을 입력 받아 전체 금액을 반환하는 함수"""
    print("동전을 넣으세요.")
    total = int(input("쿼터 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.25
    total += int(input("다임 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.1
    total += int(input("니켈 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.05
    total += int(input("페니 동전을 몇 개 넣으시겠습니까? >>> ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """거래가 수락되면 True / 실패하면(동전의 총합이 음료 가격보다 적다면) False"""
    charge = money_received - drink_cost
    if charge >= 0:
        global profit
        profit += drink_cost
        print(f"잔돈 $ {charge}를 반환합니다.")
        return True
    else:
        print("죄송합니다. 돈이 충분하지 않습니다. 동전을 반환합니다.")
        return False

def make_coffee(drink_name, order_ingredients):
    """resources에 있는 재료에서 MENU["음료이름"]["재료"]들을 차감함. -> 차감은 무조건 이루어지죠
    -> is_resource_enough을 통과했기 때문에"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"{drink_name}☕이(가) 나왔습니다. 맛있게 드세요.😊")


logo = '''

 ██████╗ █████╗ ███████╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝
██║     ███████║█████╗  █████╗  
██║     ██╔══██║██╔══╝  ██╔══╝  
╚██████╗██║  ██║██║     ███████╗
 ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝

'''
is_on = True
print(logo)
while is_on:
    choice = input("어떤 음료를 드시겠습니까? 에스프레소/라떼/카푸치노 >>> ")
    if choice == "off":
        is_on = False
        print("자판기를 종료합니다.🙌")
        # break
    elif choice == "report":
        print(f"물 : {resources["물"]}\n우유 : {resources["우유"]}\n커피 : {resources["커피"]}\n수익 : {profit}")
    elif choice in ("에스프레소", "라떼", "카푸치노"):
        if is_resource_enough(MENU[choice]["재료"]):
            if is_transaction_successful(money_received=process_coins(), drink_cost=MENU[choice]["가격"]):
                make_coffee(choice, MENU[choice]["재료"])
    else:
        print("잘못 입력하셨습니다. 다시 입력해주세요.")