'''
chapter10_classes -> main

1. 클래스 도입의 필요성
'''
# 매개 변수가 6개인 함수를 하나 정의
# def student_info(name, department, professor, phone, address, grade):
#     print(name)
#     print(department)
#     print(professor)
#     print(phone)
#     print(address)
#     print(grade)
#
# name1 = "안근수"
# department1 = "영어교육과"
# professor1 = "David"
# phone1 = "010-7445-7113"
# address1 = "부산광역시 연제구"
# grade1 = "A"
# # 함수 호출
# student_info(name1, department1, professor1, phone1, address1, grade1)
'''
지금까지 배운 함수와 매개변수, 그리고 argument를 통해 6개의 변수를 처리했습니다. 하지만
만들어야 할 변수의 개수가 많고, 학생 한 명당 변수가 6개라면, 학생이 100명일 경우 600개의
변수를 처리할 필요가 있습니다.
'''
#student_info() 함수를 하나 호출하고, 내부에 여러분의 프로필을 작성하세요.
# student_info("김일", "학과명", "교수명", "폰번호", "주소", "점수")
'''
이상의 상황들(변수에 데이터들을 각각 대입, 혹은 함수에 argument를 직접 등록)을 벗어나기 위해
클래스와 객체 개념을 도입할 수 있습니다.

class란? : 객체를 만드는 도구 설계도 / 틀 / 청사진

    자동차 설계도 -> 클래스
    설계도를 통해 생성된 자동차들 -> 객체
    
    같은 설계도로 만든 자동차라 하더라도 서로 다른 옵션을 가질 수 있습니다.
    마찬가지로 같은 클래스로 만든 객체라 하더라도 객체들은 서로 다른 값을 가질 수 있습니다.
    
    인스턴스(instance) 역시 클래스를 이용해서 생성한 객체를 가리키는 용어입니다.
    객체와 인스턴스는 그 둘을 바라 보는 관점의 차이로 볼 수 있습니다.
    
    1. '자동차 설계도'로 만든 자동차는 객체(obejct)입니다.
    2. 자동차는 자동차 설계도 클래스의 인스턴스(instance)입니다.
    
1. 클래스 정의

클래스를 작성하는 것을 클래스 정의라고 합니다 -> 함수 정의를 생각하셔야합니다.

형식 :

class 클래스명(대문자로시작):
    본문
---------------------------------------
객체생성형식 :                            -> 함수 호출을 생각하셔야합니다.

객체이름 = 클래스명()
'''
# 클래스 정의 형식 예시
# class WaffleMachine:        # 클래스명은 대문자로 시작하고, upper camel case, Pascal case 변수는 snake_case
#     pass                    # 나중에 코드를 작성하겠다는 의미로 이 경우 실행시켜도 오류가 나지 않음
#
# # 객체 생성 예시
# waffle = WaffleMachine()    # 객체 생성
# print(waffle)
'''
print(waffle)을 실행시켰을 때 <__main__.WaffleMachine object at 0x000002AC780CDAF0>에서 object라고 표기된 점을
미루어 waffle은 WaffleMachine의 객체임을 확인할 수 있음.

클래스의 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야할 구성 요소를 지닙니다.
    객체를 생성하기 위해서 클래스는 객체가 가져야 할 '값'과 '기능'을 지녀야 합니다.
    
    값 = 속성(attribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 변수는 두 가지로 구분됩니다.
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수
        2) 인스턴스 변수 : 인스턴스 들이 개별적으로 가지는 변수
        
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 정적 메서드
        3) 인스턴스 메서드
        
    인스턴스 변수 : 클래스를 기반으로 만들어지는 모든 인스턴스들이 각각 따로 저장하는 변수를 의미
        모든 인스턴스 변수는 self라는 키워드를 앞에 붙여준다.
    인스턴스 메서드 : 인스턴스 변수를 사용하는 메서드
        인스턴스 변수값에 따라서 각 인스턴스(객체)마다 다르게 동작됩니다.
        인스턴스 메서드는 첫번째 매개변수로 self를 추가해야 합니다.
        
    인스턴스 변수
        인스턴스 변수의 정의 :
            인스턴스 변수는 일반적으로 클래스의 '생성자' 메서드(__init__) 내에서 self 키워드를 사용하여 정의됨.
'''
# class Pokemon:
#     # 생성자 정의
#     def __init__(self, number, name, type):     # self는 항상 있어야 하는 것. number, name, type을 매개변수로 받습니다.
#         self.number = number                    # 인스턴스 변수 1(생성자 내부에는 속성을 집어넣습니다)
#         self.name = name                        # 인스턴스 변수 2
#         self.type = type                        # 인스턴스 변수 3
#
#     # 메서드 정의 예시 1 - call1()
#     def display_info(self):
#         print(f"번호 : {self.number}\n이름 : {self.name}\n타입 : {self.type}")
#
#     # 메서드 정의 예시 2 - call3()
#     def display_info2(self):
#         return f"번호 : {self.number}\n이름 : {self.name}\n타입 : {self.type}"
#
# # 객체 생성 객체명 = 클래스명()
# pokemon1 = Pokemon(1, "이상해씨", "풀/독")
# pokemon2 = Pokemon(type="불꽃", number=4, name="파이리")     #keyword argument로 작성 -> 순서가 바뀌어도 상관x
# # pokemon3 = Pokemon()      #이건 오류 발생하는데, 생성자 정의 시에 매개변수를 다 채워넣지 않고 생성하려고 하기 때문
#
# print(pokemon1)
# pokemon1.display_info()
# print()
# print(pokemon1.display_info2())
#
# # 속성에 값 대입
# print(pokemon2.number)      # pokemon2 객체의 속성은 number 값을 조회
# pokemon2.number = 5         # 객체명.속성명 = 데이터         -> 변수 대입하는 것과 같은 방식으로 바꿀 수 있음
#
# # 한 객체의 속성을 직접 조회하는 방식
# print(pokemon2.number)
#
# pokemon2.name = "리자드"
#
# print(pokemon2.display_info2())

'''
인스턴스 변수와 인스턴스 메서드의 관계
- 인스턴스 변수는 객체의 데이터(값)를 저장합니다. 예를 들어 pokemon1 객체의 인스턴스 변수는 "이상해씨"라는 값을 가짐.
- 인스턴스 메서드는 이 데이터를 사용하여 동작을 수행합니다. 예를 들어 display_info() 메서드는 각 객체의 인스턴스 변수를
    사용하여 해당 객체의 번호 / 이름 / 타입을 출력함.
- 인스턴스 메서드는 self 키워드를 사용하여 객체의 인스턴스 변수에 접근할 수 있음. 이를 통해 객체 내부의 데이터에 접근 가능함.
'''
# 클래스 정의
# class Person:
#
#     # 이번에 이거 생성자가 아닙니다. 주의해서 보겠습니다.
#     def set_info(self, name, age, tel, address):
#         self.name = name
#         self.age = age
#         self.tel = tel
#         self.address = address
#
#     # 이름만 바꾸는 메서드 -> setter
#     def set_name(self, name):
#         self.name = name
#
#     # 이름만 조회하는 메서드 -> getter
#     def get_name(self):
#         return self.name
#
#     # 나이만, 연락처만, 주소만 바꾸는 setter들을 전부 작성하시오.
#     def set_age(self, age):
#         self.age = age
#
#     def set_tel(self, tel):
#         self.tel = tel
#
#     def set_address(self, address):
#         self.address = address
#
#     # 나이만, 연락처만, 주소만 조회하는 getter들을 전부 작성하시오.
#     def get_age(self):
#         return self.age
#
#     def get_tel(self):
#         return self.tel
#
#     def get_address(self):
#         return self.address
#
#     # display_info1를 call1()으로 작성하시오
#     def display_info1(self):
#         print(f"이름 : {self.name}")
#         print(f"나이 : {self.age}")
#         print(f"연락처 : {self.tel}")
#         print(f"주소 : {self.address}")
#
#     # display_info2를 call3()으로 작성하시오.
#     def display_info2(self):
#         return f"이름 : {self.name}\n나이 : {self.age}\n연락처 : {self.tel}\n주소 : {self.address}"

#실행 예
'''
이름 : 안근수
나이 : 38
연락처 : 010-7445-7113
주소 : 부산광역시 연제구
'''
#객체 생성
# person1 = Person() # 생성자를 클래스에 정의하지 않았기 때문에 pokemon1과 달리 소괄호 내에 아무런 값이 없어도 생성 가능

# 객체에 값 대입
# person1.set_info("안근수", 38, "010-7445-7113", "부산광역시 연제구")
# person1.display_info1()
# print(person1.display_info2())

'''
person1 객체의 이름, 나이, 전화번호, 주소를 수강생님 본인 것으로 바꾸시고, 각각 출력하는데,
제 이름은 안근수입니다.
나이는 38살이구요
연락처는 010-7445-7113입니다.
부산광역시 연제구에 살고 있습니다.

라고 나올 수 있도록
class 내부를 수정하지 말고 여기 밑에부터 작성하시오.
'''
# person1.set_name("김일")
# person1.set_age(20)
# person1.set_tel("010-1234-4567")
# person1.set_address("뉴욕주 뉴욕시")
# print(f"제 이름은 {person1.get_name()}입니다.\n나이는 {person1.get_age()}살이구요.")
# print(f"연락처는 {person1.get_tel()}입니다.\n{person1.get_address()}에 살고 있습니다.")
'''
응용 예제

다음 지시 사항을 읽고 책 제목과 저자 정보를 저장할 수 있는 Book 클래스를 생성하세요. -> 객체도 생성하시고, 실행 예를 구현하세요.
1. 다음과 같은 방법으로 book1과 book2 인스턴스를 생성하세요.
책 제목 = title
책 저자 = author

book1 = Book()      # book1 = Book("파이썬", "민경태") 가 아니라!!!!
book2 = Book()

2. set_title() / set_author() / set_info(전부다수정) / get_title() / get_author() / print_info() 메서드들 정의
    단, print_info() 메서드는 책 제목과 책 저자가 전부 나와야만 함.
    단, set_info() 메서드는 책 제목과 책 저자를 전부 입력할 수 있어야만 함.

실행 예

책 제목 : 파이썬
책 저자 : 민경태
책 제목 : 어린왕자
책 저자 : 생텍쥐페리
'''
class Book:

    # setter - call2() 형태였죠.
    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_info(self, title, author):
        self.title = title
        self.author = author

    # getter - call3() 형태였습니다.
    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_info(self):
        print(f"책 제목 : {self.title}\n책 저자 : {self.author}")

book1 = Book()
book2 = Book()

# 책 제목 / 저자를 입력하는 메서드를 호출
book1.set_title("파이썬")
book1.set_author("민경태")
# set_info() 사용한 예시 /  + keyword argument
book2.set_info(author="생텍쥐페리", title="어린왕자")

# 책 제목 / 저자를 출력하는 메서드를 호출
print(f"책 제목 : {book1.get_title()}")
print(f"책 저자 : {book1.get_author()}")

book2.get_info()            # chapter09_constructor package를 생성 -> main.py 생성하세요.

