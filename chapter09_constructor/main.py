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









