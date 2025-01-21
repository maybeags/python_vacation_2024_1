'''
chapter14_exception 패키지 생성
main.py 파일 생성

1. 예외 처리의 필요성
    1) 예외 vs. 오류
        예외(exception) : 개발자가 직접 처리할 수 있는 문제
        오류(error) : 개발자가 처리할 수 없는 문제

    2) 예외 처리의 목적 :
        어떤 문제가 발생했을 때 그 문제를 해결해 주는 것이 아니라,
        발생된 문제로 인해 프로그램이 비정상적으로 종료되는 것을 막고,
        사용자에게 발생한 문제에 대해 정보를 전달하기 위함.
'''
# 2 / 0
'''
    2 / 0
    ~~^~~
ZeroDivisionError: division by zero
와 같은 방식으로 프로그램이 정상적으로 종료되지 않으며, 보기에 좋지도 않기 때문에,
예외를 처리하면 좋다.

2. 예외 처리
    1) 고전적인 예외 처리
'''
# a = int(input("나누는 수를 입력하세요 >>> "))
# b = int(input("나누어지는 수를 입력하세요 >>> "))
#
# if a == 0:
#     print("0으로 나눌 수 없습니다.")
# else:
#     print(f"b / a = {b/a}")
'''
어떤 값이든 0으로 나눌 수 없기 때문에 if a == 0을 통해 0으로 나누는 것을 아예
    시도할 수 없도록 예외 처리를 함.
    
여기서 생각할 수 있는 잠재적인 문제는 :
    1. 어떤 문제가 발생할 지 예상할 수 있어야 미리 대비할 수 있다.
    2. 어떤 문제가 발생할 지 예상할 수 있더라도 대비할 수 없는 경우가 있다.
    
    2. 예외의 종류
    
+------+---------------------+---------------------------------------------+
| 순번 |     예외 클래스     |                     의미                    |
+------+---------------------+---------------------------------------------+
|  1   |    BaseException    |              최상위 예외 클래스             |
|  2   |      Exception      |       대부분 예외 클래스의 슈퍼 클래스      |
|  3   |   ArithmeticError   |          산술 연산에 문제가 있을 때         |
|  4   |    AttributeError   |           잘못된 속성을 참조할 때           |
|  5   |       EOFError      | 파일에서 더 이상 읽어 들일 데이터가 없을 때 |
|  6   | ModuleNotFoundError |           import할 모듈이 없을 때           |
|  7   |  FileNotFoundError  |           존재하지 않는 파일일 때           |
|  8   |      IndexError     |          잘못된 인덱스를 사용할 때          |
|  9   |      NameError      |        잘못된 이름(변수)을 사용할 때        |
|  10  |     SyntaxError     |               문법이 틀렸을 때              |
|  11  |      TypeError      |   계산하려는 데이터의 유형이 잘못되었을 때  |
|  12  |      ValueError     |    계산하려는 데이터의 값이 잘못되었을 때   |
+------+---------------------+---------------------------------------------+
3. 예외 처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except 문
    
    형식 :
try :
    코드 작성 영역
except :
    예외 발생 시 처리 영역
'''
# try :
#     a = int(input("나누는 수를 입력하시오 >>> "))
#     b = int(input("나누어지는 수를 입력하시오 >>> "))
#     print(f"b / a = {b / a}")
# except :
#     print("예외가 발생했습니다.")
'''
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램입니다.
try / except 문을 사용하여 "예외가 발생하였습니다."를 출력할 수 있도록 작성하세요.
'''
# try:
#     height = input("키를 입력하세요 >>> ")     # 결과값이 str
#     height = round(height)                   # str을 round 처리할 수 없음 round의 결과값은 float
#     print(f"입력하신 키는 {height}cm로 처리됩니다.")
# except:
#     print("예외가 발생했습니다.")
'''
위의 코드를 실행하면 오류가 뜨는데, 디버깅을 하지 말고, 예외처리를 통해 지시사항대로 작성하시오.

        2) 특정 예외만 처리하는 방식
            try / except 문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가 처리됨.
            하지만 이상에서 본 것처럼 0으로 나누는 경우와, 정수가 아닌 값을 입력한 경우에
            서로 다른 메시지를 출력한다면, 개발자에게 예외를 처리할 수 있을 만한 정보를
            제공할 수 잇음.
            
            2)-1. 0으로 나누려고 하는 경우 -> 0으로 나눌 수 없습니다.
            2)-2. 정수가 아닌 값을 입력한 경우 -> 정수만 입력할 수 있습니다.
            해당 경우 except 문 뒤에 처리하고자 하는 예외를 모두 명시하면 됩니다.
'''
# a = int(float(input("나누는 수를 입력하세요 >>> ")))  # str -> float -> int
# b = int(input("나누어지는 수를 입력하세요 >>> "))   # str->int를 입력할 때 실수 입력하면 예외 발생
# print(f" b / a = {b/a}")
# 예외 예시 - ZeroDivisionError / ValueError
# try :
#     a = int(float(input("나누는 수를 입력하세요 >>> ")))
#     b = int(input("나누어지는 수를 입력하세요 >>> "))
#     print(f" b / a = {b / a}")
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except ValueError:
#     print("정수만 입력할 수 있습니다.")
'''
        거의 모든 예외는 Exception 클래스의 서브 클래스입니다. 따라서 모든 예외는 Exception의
        인스턴스가 됩니다. 다음과 같이 마지막에 작성하는 except 문에 Exception을 명시하면
        예상하지 못한 예외들도 모두 처리할 수 있게 됩니다.
        
형식 :

try :
    코드 작성 영역
except 예외클래스1:
    예외메시지1
excpet 예외클래스2:
    예외메시지2
.
.
.
except Exception:
    예외메시지n
    
3. 예외 메시지 처리하기

지금까지는 직접 예외 메시지를 만들어서 사용했지만, 기본적으로 예외 메시지를 이미 가지고 있는 경우도
있습니다. 디폴트 에러 메시지를 출력하는 방식에 대해서 학습합니다.

형식 :
try :
    코드 작성 영역
excpet 예외클래스 as 예외메시지:
    예외 발생 시 처리 영역
'''
# z = [10, 20, 30, 40, 50]
# try :
#     print(z[10])        # IndexError: list index out of range
# except IndexError as e:
#     print(e)
'''
    4. else / finally 문
        try / except문에 추가로 else와 finally문을 사용 할 수 있음.
        else : 예외가 발생하지 않으면 처리되는 구문
        finally : 예외 발생 여부와 관계없이 맨 마지막에 항상 처리되는 구문
        
형식 :
try :
    코드 작성 영역
except :
    예외 발생 시 처리 영역
else :
    예외가 없을 시 처리 영역
finally :
    언제나 실행되는 영역
'''
# try :
#     a = int(input("나누는 수를 입력하세요 >>> "))
#     b = int(input("나누어지는 수를 입력하세요 >>> "))
#     result = b / a
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else:
#     print(f"b / a = {result}")
# finally:
#     print("프로그램이 종료되었습니다.")
'''
    5. 강제로 예외 발생 시키기
        어떤 사람의 나이를 정수로 입력 받는 프로그램이 있다고 가정했을 때,
        컴퓨터 상으로는(그리고 파이썬 상으로는) -1000이 정수이기 때문에 예외가 발생하지 않습니다.
        하지만, -1000살이 될 수 없기 때문에 직접 예외를 발생시켜서 처리해야만 합니다.
            -> raise문
            
형식 :

raise 예외클래스()

또는

raise 예외클래스(예외메시지)

raise는 강제로 예외를 발생시킨다는 점에서 주로 사용되는 예외 클래스는 Exception입니다.
'''
# age = int(input("나이를 입력하세요 >>> ")) # 파이썬 상에서는 문제가 없지만 현실 세계에서 생기는 예외
# print(f"당신의 나이는 {age}살입니다.")      # -> 개발자가 직접 처리할 필요 있음
# try :
#     raise Exception("강제로 발생시킨 예외")  # 이 경우 멀쩡한 숫자를 입력해도 예외가 발생됩니다.
# except Exception as e:                      # 잘 생각해서 작성하세요 😢
#     print("발생한 예외 메시지는 다음과 같습니다.")
#     print(e)
'''
    6. 사용자 정의 예외 클래스
    
    음수를 입력받을 때 강제로 예외를 발생시키는 예외 클래스를 정의
'''
class NegativeAgeError(Exception):          # 상속
    """사용자 정의 예외 클래스 : 나이가 음수일 때 발생"""
    pass        # 예외를 발생시키기만 하면 되기 때문에 따로 코드 작성할 필요 없음
                # -> Exception의 속성 및 메서드를 상속
try :
    age = int(input("나이를 입력하세요 >>> "))
    if age < 0:
        raise NegativeAgeError("나이는 음수일 수 없습니다.")
except NegativeAgeError as e:
    print("발생한 예외 메시지는 다음과 같습니다.")
    print(e)
else:
    print(f"당신의 나이는 {age}살입니다.")
finally:
    print("프로그램이 종료되었습니다.")


