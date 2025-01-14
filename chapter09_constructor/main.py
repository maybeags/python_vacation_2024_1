'''
1. 생성자(Constructor)
'''
# 클래스 정의
# class Candy:
#
#     def set_info(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def get_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")
#
# # 객체 생성
# satang = Candy()        # satang 객체 생성 -> 생성자를 정의하지 않았기 때문에 빈값으로만 생성 가능
# satang.set_info("구형", "갈색")
# satang.get_info()
'''
satang이라는 인스턴스는 생성된 '이후'에 set_info() 메서드를 호출하여 "구형" 모양의,
"갈색" 사탕이라는 속성을 갖게 됩니다.

satang 인스턴스의 생성 과정
    1. 값이 없는 인스턴스를 생성
    2. 값을 저장할 수 있는 메서드 호출
    
그렇다면 처음부터 값(속성)이 있는 인스턴스를 생성하기 위한 방법은 무엇일까? -> __init__() 메서드

__init__() 메서드(생성자)는 인스턴스가 생성될 때 '자동으로 호출'되기 때문에 인스턴스 변수의 초기화 용도로
    사용, 즉 값이 있는 인스턴스를 생성할 수 있다는 의미.
'객체 생성과 동시에' 생성자가 호출됨 -> 초기값을 작성할 때 사용한다는 의미
형식 :
class 클래스명:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
'''
# class Candy2:
#
#     #생성자 정의  -> 그렇다면 최초에 대입하기 위한 set_info(self, shape, color) 메서드는 필요 x
#     def __init__(self, shape, color):
#         self.shape = shape
#         self.color = color
#
#     def get_info(self):
#         print(f"사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.")

#객체 생성
# satang2 = Candy2("정육면체", "흰색")
# satang2.get_info()
'''
이상에서 주목해야 할 점은 satang 인스턴스와 satang2 인스턴싀의 생성 방식 차이입니다 -> 한줄 줄였죠.

2. 소멸자(Destructor)
    인스턴스가 생성될 때 자동으로 생성자와 마찬가지로 인스턴스가 소멸될 때 호출되는 메서드가 있음.
    이를 소멸자라고 하며, 소멸자를 정의하는 메서드는 __del__()
'''
# class Sample:
#
#     #생성자 정의
#     def __init__(self):
#         print("인스턴스가 생성되었습니다.")
#
#     def __del__(self):
#         print("인스턴스가 소멸되었습니다.")
#
# # 객체 생성
# sample = Sample()
# # 소멸자 호출 방법
# del sample          # del 객체명 으로 소멸자를 원하는 시기에 호출할 수 있음.
# print("이 line 밑으로 프로그램이 종료됩니다.")
'''
기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하세요.

1. 클래스 USB를 만드시오.
2. 생성자를 정의하여 매개변수로 capacity를 받고, 
3. get_info() 메서드를 정의하시오.

main단계의 코드라인
usb = USB(64)
usb.get_info()

실행 예
64GB USB

'''
# 지시사항 1번
# class USB:
#     # 지시사항 2
#     def __init__(self, capacity):
#         self.capacity = capacity
#
#     # 지시사항 3    -> call1() 타입으로 작성
#     def get_info(self):
#         print(f"{self.capacity}GB USB")
#
# usb = USB(64)
# usb.get_info()
'''
생성자와 소멸자를 이용하여 서비스 안내 메시지를 출력하는 프로그램을 작성하시오.

class Service를 정의하고, 생성자를 통해 매개변수를 service로 받고,
print() 메서드를 정의하시오.

main 단계에서의 작성
s = Service("길 안내")
del s

실행 예
길 안내 Service가 시작되었습니다.
길 안내 Service가 종료되었습니다.
'''
# class Service:
#     # 생성자 정의 -> 아까 위에 것과 동일
#     def __init__(self, service):
#         self.service = service
#         print(f"{self.service} Service가 시작되었습니다.")
#
#     def __del__(self):
#         print(f"{self.service} Service가 종료되었습니다.")
#
#
# s = Service("길 안내")     # 생성자는 객체 생성과 동시에 호출된다.
# del s
'''
응용 예제

1. 다음 지시 사항을 읽고 이름을 저장하는 Person 클래스를 생성하시오.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오.
man = Person("james")
woman = Person("emily")
2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
james is born.
emily is born.

3. 다음과 같은 방법으로 man 인스턴스를 삭제하시오.
del man

4. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
james is dead.
'''
# class Person:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} is born.")
#
#     def __del__(self):
#         print(f"{self.name} is dead.")
#
# man = Person("james")
# woman = Person("emily")
#
# del man
# print(f"이 밑에서 프로그램 종료됩니다.")
'''
예제 1.
    학생들의 성적을 관리하는 Student 클래스를 작성하시오. 이 클래스는 
    학생의 이름, 학번, 성적을 인스턴스 변수로 갖습니다.
    
    지시 사항.
        1) Student 클래스를 정의하고 생성자를 통해 이름(name), 학번(student_id), 성적(grade)을
            초기화하시오.
        2) 학생의 프로필을 출력하는 인스턴스 메서드 print_grade()를 작성하시오.(call1()타입으로)
        3) 학생의 성적을 변경할 수 있는 인스턴스 메서드 set_grade()를 작성하시오.
        4) 세 명의 학생 인스턴스를 생성하고, 각 학생의 정보를 출력한 다음,
            성적을 변경하고 다시 출력하시오.
            
student1 = Student("김철수", 20250001, "A")

실행 예

학생 이름 : 김철수
학번 : 20250001
성적 : A

student2 이영희 / 20250002 / B
student3 박민수 / 20250003 / C

성적 변경 후
김철수 A+
이영희 A
박민수 B+로 성적 변경 후에 다시 학생 정보 출력하시오.
'''
# class Student:
#     # 생성자 정의
#     def __init__(self, name, student_id, grade):
#         self.name = name
#         self.student_id = student_id
#         self.grade = grade
#
#     # 성적 바꾸는 메서드 정의하시오      -> 여태까지 우리가 작성한 코드들 전체 검색하는 법 ctrl + shif + f
#     def set_grade(self, grade):
#         self.grade = grade
#
#     # 학생 속성 출력하는 메서드 정의하시오
#     def print_grade(self):
#         print(f"학생 이름 : {self.name}\n학번 : {self.student_id}\n성적 : {self.grade}")
#
# student1 = Student("김철수", 20250001, "A")
# student2 = Student("이영희", 20250002, "B")
# student3 = Student("박민수", 20250003, "C")
#
# student1.print_grade()
# student2.print_grade()
# student3.print_grade()
#
# # 성적 변경 메서드 호출
# student1.set_grade("A+")
# student2.set_grade("A")
# student3.set_grade("B+")
#
# print("성적 변경 후")
# student1.print_grade()
# student2.print_grade()
# student3.print_grade()
'''
예제 2. 은행 계좌를 관리하는 BanckAccount 클래스를 작성하시오. 이 클래스는 계좌 소유자 이름, 계좌 번호, 잔액을 인스턴스 변수로
    가집니다.
    
    지시 사항
    
    1. BankAccount 클래스를 정의하고, 생성자를 통해 owner, account_num, balance를 초기화하시오.
    2. 입금 기능을 하는 인스턴스 메서드(deposit())를 구현하세요 -> 입금 잔액을 받아 잔액을 증가시킵니다. // setter 응용
    3. 출금 기능을 하는 인스턴스 메서드(withdraw())를 구현하세요 -> 출금 금액을 받아서 잔액을 감소시킵니다.
        -> 잔액이 부족하면(0 미만이되면) 출금이 불가능하도록 작성해야 합니다.
    4. 계좌 정보를 출력하는 인스턴스 메서드 print_account_info()를 구현하세요 -> 실행 예 참조
    5. 두 개의 계좌를 생성하고, 입금과 출금을 수행한 후 계좌 정보를 출력하세요.
    
실행 예
계좌 소유자 : 홍길동
계좌 번호 : 123-456-789
현재 잔액 : 100000원                 (십만원)

계좌 소유자 : 신사임당
계좌 번호 : 987-654-321
현재 잔액 : 500000원                 (오십만원)

50000원이 입금되었습니다. 현재 잔액 : 150000원            # account1에 대한 입금(오만원 입금)
잔액이 부족하여 출금할 수 없습니다.                        # account1에서 200000원 출금 시도 실패 사례(이십만원 출금 실패사례)
100000원이 출금되었습니다. 현재 잔액 : 50000원            # account1에 대한 출금 (십만원 출금 성공)

100000원이 출금되었습니다. 현재 잔액 : 400000원           # account2에 대한 출금(십만원 출금)
200000원이 입금되었습니다. 현재 잔액 : 600000원           # account2에 대한 입금(이십만원 입금)

최종 계좌 정보
계좌 소유자 : 홍길동
계좌 번호 : 123-456-789
현재 잔액 : 50000원                 (오만원)

계좌 소유자 : 신사임당
계좌 번호 : 987-654-321
현재 잔액 : 600000원                 (육십만원)

'''
class BankAccount:
    # 생성자 정의
    def __init__(self, owner, account_num, balance):
        self.owner = owner
        self.account_num = account_num
        self.balance = balance

    # 입금 메서드 정의 -> setter 관련
    def deposit(self, money):
        self.balance += money
        print(f"{money}원이 입금되었습니다. 현재 잔액 : {self.balance}")

    # 출금 메서드 정의 -> setter 관련
    def withdraw(self, money):
        if self.balance - money >= 0:
            self.balance -= money
            print(f"{money}원이 출금되었습니다. 현재 잔액 : {self.balance}")
        else:
            print("잔액이 부족하여 출금할 수 없습니다.")

    # 계좌 정보 메서드 정의 -> getter 관련
    def print_account_info(self):
        print(f"계좌 소유자 : {self.owner}")
        print(f"계좌 번호 : {self.account_num}")
        print(f"현재 잔액 : {self.balance}")

account1 = BankAccount("홍길동", "123-456-789", 100000)
account2 = BankAccount(balance=500000, owner="신사임당", account_num="987-654-321")

account1.print_account_info()
print()
account2.print_account_info()
print()
account1.deposit(50000)
account1.withdraw(200000)
account1.withdraw(100000)
print()
account2.withdraw(100000)
account2.deposit(200000)
print("\n최종 계좌 정보")
account1.print_account_info()
print()
account2.print_account_info()
'''
chapter10_coffee_machine package 생성

github.com/maybeags/python_vacation_2024_1로 들어갑니다.
chapter10_coffee_machine로 들어가시면
coffee_machine_manual이 있습니다. 이거 전체 복사 하시고

chapter10_coffee_machine package 우클릭 -> new -> file -> coffee_machine_manual.txt 생성한 후에
붙여넣기 합니다.

chapter10_coffee_machine 우클릭 -> new -> package -> pop_version 생성
pop_version 우클릭 -> new -> python file -> main.py

'''



