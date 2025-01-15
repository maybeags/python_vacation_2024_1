class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """현재 수익을 출력합니다."""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """투입된 동전으로부터 계산된 총액을 반환합니다."""
        print("동전을 투입해주세요.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"{coin}는 몇 개입니까?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """지불이 성공했을 때 True를 반환하고, 돈이 부족하면 False를 반환합니다."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"여기 잔돈 {self.CURRENCY}{change}를 반환합니다.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("죄송합니다. 돈이 충분하지 않습니다. 돈을 반환합니다.")
            self.money_received = 0
            return False