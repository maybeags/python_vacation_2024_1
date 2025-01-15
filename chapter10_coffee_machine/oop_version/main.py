from menu import Menu                       # from 파일명(모듈명) import 클래스명
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#외부 모듈에서 import 해온 것을 토대로 객체를 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"어떤 음료를 드시겠습니까? {menu.get_items()} >>> ").lower()
    # 1. choice -> off / report / 오타났을 때
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)    # 음료 객체를 변수명 drink에 저장
        if drink == None: #choice에 오타 있으면 얘가 실행됩니다.
            continue                        #오타있으면 while 반복문의 맨처음으로 돌아감
        #그럼 여기 작성하는 부분은 -> choice에 오타가 없이 메뉴이름이 정확하게 적혔을 때

        # 자원이 충분한지 확인
        # 계산 -> 왜 바로 계산이냐면 make_payment 메서드 내에 process_coins가 있었기 때문
        # 다 통과하면 커피 만드는 거
        if coffee_maker.is_resource_sufficient(drink):
            # coffee_maker.is_resource_sufficient() 메서드를 확인해보면,
            # drink.ingredidents를 반복문 돌린다는 사실을 확인할 수 있습니다.
            # 이제 여러분들이 주의해서 코드를 작성해야 할 점은
            # 미리 작성된 메서드가 어떠한 자료형의 argument를 요구하는지입니다.
            # 즉, pop 버전에서처럼 동일하게 생각해서
            # drink.ingredients를 argument로 넣었다면 오류가 발생했을겁니다.
            # 이제 결제 관련 코드를 작성하셔야합니다 -> money_machine쪽 메서드들 확인해서 작성하세요.
            if money_machine.make_payment(drink.cost):
                # 커피 만들어야죠 -> coffee_maker
                coffee_maker.make_coffee(drink)