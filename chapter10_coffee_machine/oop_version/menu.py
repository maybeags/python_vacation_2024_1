class MenuItem:
    """각 메뉴 아이템들을 모델링합니다."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }


class Menu:
    """음료 메뉴를 모델링합니다."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """이용 가능한 모든 메뉴 아이템의 이름을 반환합니다."""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """특정 음료를 이름으로 메뉴에서 검색합니다. 해당 아이템이 존재하면 반환하고, 그렇지 않으면 None을 반환합니다."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("죄송합니다. 해당 아이템은 이용할 수 없습니다.")