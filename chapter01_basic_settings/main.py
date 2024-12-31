# 여러분이름폴더 우클릭 -> new -> python package 클릭
# chapter01_basic_settings
# chapter01_basic_settings 우클릭 new -> python file 클릭
# main.py

# print("Hello, Python!")

# 주석(comment) : 컴퓨터가 아니라 사람이 읽을 수 있도록 정보를 제공하는 방법으로
#   주석 처리가 되어있는 부분은 파이썬 인터프리터가 코드로 인지하지 않음

# python : 귀도 반 로섬이라는 네덜란드 출신 개발자가 만든 언어로,
    # C 언어를 기반으로 함. -> 일반적인 영어를 기준으로 쉽게 프로그램을 작성할 수 있도록
    # 함을 목표로 함 -> 이상의 특징 때문에 많은 사람들이(개발자/비개발자 포함) 파이썬을
    # 학습하게 되었고, 이를 통해 다양한 라이브러리로 확장성이 높아져
    # 현대에 이르러서는 빅데이터 및 AI, 알고리즘 등을 파이썬으로 구동하는 경우가 많아짐

# 샵 누르고 작성하면 주석처리가 됩니다.
# 여기다가 그냥 작성을 하다가 주석 처리를 해야하는 경우도 있습니다. -> ctrl + /
'''
다중 주석 처리

위에서 저희가 배운 것은 print()입니다.
print("Hello, python!")이라고 했을 때 큰 따옴표는 출력되지 않았음을 확인할 수 있습니다.
'''
# print(1)
# print("1")
'''
25번 라인의 출력결과와 26번 라인의 출력 결과가 동일하기 때문에 구분이 어려울 수 있습니다.
이때문에 파이썬 사용자에게 필수적인 함수는 type()이 있습니다. 
'''
# print(type(1))              # ctrl + d 눌러보세요.
# print(type("1"))              # ctrl + d 눌러보세요.

# type에 따른 차이 검증

# print(1 + 2)                # 결과값 3
# print("1" + "2")            # 결과값 12
# print(2 + 1)                # 결과값 3
# print("2" + "1")            # 결과값 21
'''
산술 연산자

1. + : 더하기
2. - : 빼기
3. * : 곱하기
4. / : 나누기
5. % : 나머지
5까지는 다른 언어에서도 쓰이는 연산자입니다.
6. // : 몫
7. ** : 제곱
'''
print(3 / 2)        # 결과값 1.5
print(3 // 2)       # 결과값 1
print(type(3/2))    # float         -> 실수
print(type(3//2))   # int

'''
변수(variable) : 데이터(정보)를 담는 바구니

데이터는 자료형에 따라 결정됩니다.
bool : 참/거짓         (boolean의 축약어입니다)
int : 정수
float : 실수
string : 문자열
'''
# name1 = "안근수"
# name2 = '안근순'
# print(name1)
# print(name2)        # 파이썬에서는 큰따옴표와 작은따옴표를 구분하지 않습니다.
'''
대입 연산자
1. = : = 오른쪽에 있는 데이터를 = 왼쪽에 있는 변수에 대입한다는 의미.
    즉, 66번 라인의 해석은 "안근수"라는 string 타입의 데이터를
    name1이라는 변수에 대입해주겠다는 뜻입니다.
'''
# num = 1         # 변수 : 값이 변할 수 있습니다.
# print(num)
# num = num + 1   # = 왼쪽에 있는 num이라는 변수에 num(=1) + 1이라는 int 데이터를 '대입'
# print(num)      # 즉 num과 num+1이 동일하다는 의미가 아니라 데이터를 재대입했다는 의미
'''
그렇다면 동일하다는 의미를 지닌 기호는? -> ==

다중 string : 변수명 = 한 후에 작은 따옴표 세개를 입력하면 자동으로 여섯 개가 나옵니다.
    세개 후에 내용을 입력하시면 다중string이 적용됩니다.
'''
introduction = '''
안녕하세요.
제 이름은 안근수입니다.
여러분들의 python 강사이고,
영어교육과 출신으로 비전공자입니다.
비전공자분들도 부담없이 들을 수 있는 강의를 만들어가도록 하겠습니다.
'''
# print(introduction)
# name = "안근수"
# job = "코리아it 파이썬 강사"
# age = 37
#
# print(f"제 이름은 {name}이고, 직업은 {job}입니다. 나이는 {age}살입니다. 내년에는 {age+1}살이 됩니다.")
'''
지금까지 수업한 방식으로는 미리 데이터를 준비해놓고 변수에 대입을 합니다.
즉 실시간으로 데이터를 입력할 수 없습니다.

이상의 문제를 해결하기 위한 방법이 input() 함수입니다.
'''
# input("당신의 이름이 무엇입니까? >>> ")

'''
위와 같이 입력하면 콘솔창에 이름을 입력할 수 있도록 커서가 깜빡이는 것을 확인할 수 있습니다.
커서가 깜빡이는 곳에 이름을 입력하면 종료가 되어버리는 점도 확인할 수 있습니다.

즉, 데이터를 입력 받기는 했지만 변수에 저장하는 과정이 없었기 때문에 데이터가 휘발됩니다.
그렇다면 이름을 변수에 저장하기 위해서는 변수의 개념과 대입 연산자의 개념을 알고 있어야만 하겠습니다.
'''
name = input("당신의 이름은 무엇입니까? >>> ")
print(f"제 이름은 {name}입니다.")
'''
114번의 코드 라인을 분석하겠습니다. input()함수는 ()안에 있는 질문사항(프롬프트라고 보통 말합니다)을 
콘솔에 출력하여 사용자로 하여금 입력받을 수 있게끔 합니다.
사용자가 프롬프트에 맞는 정보를 입력하면, 그 데이터는 name 변수에 저장이 되고,
이를 print(name)을 통해 다시 불러올 수 있게 됩니다.
'''
age = 37
# print("제 이름은 안근수입니다. 나이는 " + age + "살입니다.")       -> 오류 발생합니다.
'''
f-string(formatted string) : f""로 실행하며 큰 따옴표 내에 정보를 작성하다가 특정한 변수를 불러낼 때는
    {}를 사용함.
    ex) print(f"제 이름은 안근수입니다. 제 나이는 {age}살입니다.")
'''
print(f"제 이름은 안근수입니다. 제 나이는 {age}살입니다.")
'''
chapter01_basic_settings 우클릭 -> new -> python package -> bandname_generator
bandname_generator 우클릭 -> new -> python file -> main.py 생성
'''