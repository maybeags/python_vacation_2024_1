'''
chapter11_class_and_static -> main.py

1. 클래스 변수

    인스턴스 변수 : 인스턴스마다 서로 다른 값을 지니는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 :
        목적 - 인스턴스 마다 서로 다른 값을 저장
        접근 방식 - 인스턴스 접근(o)
                 - 클래스 접근(x)

    클래스 변수 :
        목적 : 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                 - 클래스 접근(o)

클래스 변수
'''
# class Korean:
#
#      # 인스턴스 변수의 경우 생성자 내부에 있었습니다. 클래스 변수의 경우에는
#     country = "한국"      # 그냥 다짜고짜 선언해서 초기화하면 클래스 변수
#     def __init__(self, name, age, address):    # 얘네는 인스턴스 변수
#         self.name = name            #인스턴스 변수1
#         self.age = age              #인스턴스 변수2
#         self.address = address      #인스턴스 변수3

# 객체 생성
# man = Korean(name="안근수", address="부산광역시 연제구", age=38)
#인스턴스 변수들을 확인(위에 필기 상으로는 인스턴스 변수 접근 방식)
# print(man.name)         # 객체명.인스턴스변수를 통한 접근
# print(man.age)
# print(man.address)
# 인스턴스인 man을 통해 클래스 변수에 한 번 접근해보겠습니다.
# print(man.country)      # 객체명.클래스변수를 통한 접근 -> (o)
# -> 객체명.클래스변수를 통해서 클래스 변수에 접근이 가능하지만 클래스 내부의 코드를
# 들여다보기 전까지는 country가 인스턴스 변수인지 클래스 변수인지 확인하는 것이 어렵다.
# print(Korean.country)   # 클래스명.클래스변수를 통한 접근 -> (o)
# 그래서 이상과 같은 표기를 통해서 클래스 변수에 접근하는 것이 더 바람직하다.
'''
클래스 메서드
'''
# class Korean2:
#     country = "대한민국"        # 클래스 변수 선언 및 초기화
#
#     @classmethod    # 이하의 메서드가 클래스 메서드임을 명시
#     def trip(cls, travelling_site): # 클래스 메서드에서 클래스 변수를 참조할 때는 cls를 명시
#         if cls.country == travelling_site:
#             print("국내 여행입니다.")
#         else:
#             print("해외 여행입니다.")

# 클래스 메서드 호출
# Korean2.trip("대한민국")    # 클래스 메서드의 호출은 클래스 변수를 참조하는 것이기 때문에
# Korean2.trip("미국")       # 객체를 생성하지 않고서 클래스명.메서드명()으로 호출하는 것이 가능
# # 객체 생성
# man2 = Korean2()
# man2.trip("중국")         # 객체명.클래스메서드명()으로 호출 가능 -> 하지만 마찬가지로 얘가 인스턴스 메서드인지
                         # 클래스 메서드인지 구분할 수가 없기 때문에 권장되는 방식의 코드 작성 요령이 아니다.
'''
2. 클래스 메서드
    : 클래스 변수를 사용하는 메서드
    
    특징 :
        1) 인스턴스 또는 클래스로 호출 -> 하지만 클래스 변수와 마찬가지로 클래스로 호출하는 것이 권장
        2) 생성된 인스턴스가 없어도 호출 가능
        3) @classmethod 데코레이터(decorator)를 표시하고 작성
            -> 그러면 자동으로 첫번째 매개변수로 cls가 적용됨
        4) 매개변수 self를 쓰지 않고 cls를 사용 -> self는 객체를 의미하기 때문.
        
    호출 방식 :
        클래스명.메서드명() -> self를 사용하지 않기 때문에 '인스턴스 변수에 접근이 불가능',
            cls를 통해 클래스 변수에만 접근 가능
            
Korean2 클래스에서 정의된 trip() 메서드는 클래스 메서드임을 알리는 @classmethod로 시작,
첫 번째 매개변수인 cls는 class의 축약어. 여기서는 클래스 Korean2를 의미함.
따라서 내부의 cls.country는 Korean2.country와 동일한 의미. 이를 클래스 내부에서는 cls.country로 표기
클래스 메서드는 인스턴스를 생성하지 않아도 클래스만으로 호출 가능. 즉, Korean2.trip(argument)로 호출 가능.

정적 메서드(static method)
    : 정적 메서드 또한 self를 사용하지 않음 -> 즉, 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미함.
        : 클래스 메서드와의 공통점 #1
      인스턴스를 생성하지 않아도 사용할 수 있음 -> 공통점 #2
      
    특징 :
        1. 인스턴스 또는 클래스로 호출 가능 -> 클래스 메서드와의 공통점
        2. 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와의 공통점
        3. @staticmethod 데코레이터를 표기하고 작성 -> 클래스 메서드와의 차이점
        4. 반드시 작성해야 할 매개변수(self, cls)가 없음 -> 클래스 메서드와의 차이점
        
정적 메서드는 self, cls를 다 사용하지 않기 때문에 인스턴스/클래스 변수를 모두 사용하지 않는 메서드를
정의하는 경우에 적합함. 정적 메서드는 클래스에 소속돼있지만 인스턴스에는 영향을 주지도 않고,
또 영향을 받지도 않음.
'''
# class Korean3:
#     country = "한국"          # 클래스 변수
#
#     @staticmethod             # 정적 메서드 선언
#     def slogan(str_example):             # self, cls가 자동 생성되지 않았습니다 -> 참조하지 않으니까요.
#         print("Imagine Your Korea🙌 " + str_example)
#
# Korean3.slogan("and Visit:)")
'''
기본 예제

가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스입니다.
'''
# class Bag:
#
#     count = 0               # 클래스 변수 선언 및 초기화
#
#     def __init__(self):     # 생성자 / 인스턴스 메서드에 해당한다는 것을 의미
#         Bag.count += 1      # 객체를 하나 생성 할 때마다 count가 1씩 증가
#         print("가방이 생산되었습니다.")   # 인스턴스 메서드가 클래스 변수를 불러낼 때는 '클래스명.클래스변수명'으로 접근
#
#     @classmethod
#     def sell(cls):
#         print("가방이 팔렸습니다.")
#         cls.count -= 1      # 클래스 메서드가 클래스 변수에 접근하기 때문에 Bag.count가 아니라 cls.count가 됩니다.
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count        # 클래스 변수를 main 단계에서 직접 참조하는 것이 보안상 좋지 않기 때문에
#                                 # 클래스 메서드를 생성(getter 형태로)하여 참조하는 방식
#
# print(f"현재 가방 개수 : {Bag.count}")    # 보안상 안좋은 사례
# print(f"현재 가방 개수 : {Bag.remain_bag()}") # 보안상 더 권장되는 사례
# # 객체 생성
# bag1 = Bag()
# print(f"현재 가방 개수 : {Bag.remain_bag()}")
# bag2 = Bag()
# bag3 = Bag()
# print(f"현재 가방 개수 : {Bag.remain_bag()}")
# bag1.sell()             # 인스턴스 메서드의 호출
# print(f"현재 가방 개수 : {Bag.remain_bag()}")
'''
응용 예제

1. 다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 생성하시오.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하세요.
man = Person("안근수")
woman = Person("안근순")

2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하세요.
안근수이(가) 태어났습니다.
안근순이(가) 태어났습니다.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하세요.
print(f"전체 인구수 : {Person.get_population()}")

4. 다음과 같은 방법으로 man 인스턴스를 삭제하세요.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성하세요.
RIP 안근수
'''
# class Person:
#     # 클래스 변수 선언해야합니다 -> get_population()
#     population = 0
#
#     # 생성자를 정의해야합니다 -> ~이(가) 태어났습니다 라고 출력이 되도록 작성해야합니다.
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#         print(f"{self.name}이(가) 태어났습니다.")
#
#     # 클래스 메서드를 정의해야 합니다 -> get_population()
#     @classmethod
#     def get_population(cls):
#         return cls.population
#
#     # 소멸자도 정의해야합니다. -> RIP ~ 라고 출력이되도록 작성해야 합니다.
#     def __del__(self):
#         Person.population -= 1
#         print(f"{self.name} RIP")
#
#
#
# #메인 단계 작성
# man = Person("안근수")
# print(f"전체 인구수 : {Person.get_population()}")
# woman = Person("안근순")
# print(f"전체 인구수 : {Person.get_population()}")
# del man
# print(f"전체 인구수 : {Person.get_population()}")
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
# print()
'''
클래스 변수 / 클래스 메서드 활용 예제

다음 지시 사항을 읽고 가게의 매출을 구할 수 있는 Shop 클래스를 작성하세요.

지시 사항.
1. Shop 클래스는 다음과 같은 변수를 가지고 있다.
    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 딕셔너리 요소를 지니는 리스트
    menu_list = [ {메뉴명1:가격1}, {메뉴명2:가격2} ]
    
    menu_list = [ {"떡볶이": 3000}, {"순대": 4000}, {"튀김": 500}, {"김밥": 2000} ]
    
2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성합니다.
Shop.sales("떡볶이", 1)       # 떡볶이을(를) 1개 판매
Shop.sales("김밥", 2)        # 김밥을(를) 2개 판매
Shop.sales("튀김", 5)        # 튀김을(를) 5개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f"매출 : {Shop.show_total_sales()}원")
'''
class Shop:
    total = 0
    menu_list = [{"떡볶이": 3000}, {"순대": 4000}, {"튀김": 500}, {"김밥": 2000}]

    @classmethod
    def sales(cls, menu, quantity):
        # list의 요소들이 dict이기 때문에 key를 가지고 참조해야 3000, 4000 이런 연산 가능한 값이 나옵니다
        # 리스트 내의 요소인 딕셔너리의 밸류 * quantity가 total에 더해져야합니다.
        # list 내부의 요소를 추출하는 방식 -> for 반복문
        for menu_dict in cls.menu_list:
            # print(type(menu_dict))
            # 여기서 또 for문 다시 돌려서 키와 값을 추출 가능 -> 하지만 menu_list의 형태를 보니 적절치않다
            if menu in menu_dict:   # menu_dict에서 조건문을 걸었는데, 기본적으로 key를 중심으로 탐색합니다.
                # 그렇다면 menu_dict에 있는 value를 찾기 위한 방법
                # print(f"메뉴 : {menu}\n가격: {menu_dict[menu]}")
                cls.total += (menu_dict[menu] * quantity)
                print(f"{menu}이(가) {quantity}개 판매")

    @classmethod
    def show_total_sales(cls):
        return cls.total


Shop.sales("떡볶이", 1)       # 떡볶이을(를) 1개 판매
Shop.sales("김밥", 2)        # 김밥을(를) 2개 판매
Shop.sales("튀김", 5)        # 튀김을(를) 5개 판매
print(f"매출 : {Shop.show_total_sales()}원")
'''
chapter12_prettyTable 생성하세요.
main.py
'''


