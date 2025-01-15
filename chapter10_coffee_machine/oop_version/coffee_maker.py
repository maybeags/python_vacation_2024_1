class CoffeeMaker:
    """커피를 만드는 기계를 모델링합니다"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """모든 자원의 보고서를 출력합니다."""
        print(f"물: {self.resources['water']}ml")
        print(f"우유: {self.resources['milk']}ml")
        print(f"커피: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """주문을 만들 수 있을 때 True를 반환하고, 재료가 부족하면 False를 반환합니다."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"죄송합니다. {item}가(이) 충분하지 않습니다.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """필요한 재료를 자원에서 차감합니다."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"여기 {order.name} ☕️입니다. 맛있게 드세요!")