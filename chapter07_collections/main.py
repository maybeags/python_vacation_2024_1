'''
컬렉션(Collection) : 여러 값을 하나의 이름으로 묶어서 관리하는 자료형

string의 경우 문자 하나 하나를 줄(str)로 묶어서 문자열로 출력하는데,
예를 들어 '다수의 다른 string을 관리하는 방법은 무엇일까?'에 관한 대답

여러 명의 프로필을 관리한다고 가정해보겠습니다.
'''
ahn_geunsu = "이름 : 안근수\n나이 : 38\n직업 : 파이썬 강사"
# print(ahn_geunsu)
kim_random = "이름 : 김랜덤\n나이 : 20\n직업 : 학생"
# print(kim_random)
'''
한 명 저장하는 데에는 문제가 없을 수 있지만 매번 변수 하나에 이름, 나이, 직업 등을 한 명 추가할
때마다 정리하는 것은 비효율적이고, 예를 들어 ahn_geunsu에서 직업만 조회하고 싶어도 전체 정보를 다
확인해야만 합니다.
이를 한꺼번에 관리하게 위한 방식으로 모음(collection)을 사용합니다.


종류
    1. list() 리스트 - 추가, 수정, 삭제가 언제나 가능 / a = [1, 2, 3] # 대괄호 사용
    2. tuple() 튜플 - 추가, 수정, 삭제가 불가능 / a = (1, 2, 3) #소괄호 사용
    3. set() 세트 - 중복된 값의 저장이 불가능 / a = {1, 2, 3} # 중괄호 사용
    4. dict() 딕트 - 키 + 값으로 관리 / a = {"name": "안근수, "age": 38} # 중괄호 사용
    
이 중, 1, 2번인 list와 tuple은 저장된 값의 순서가 있으며 이를 시퀀스(Sequence)라고 부릅니다.
즉, list는 저장 순서가 있고 추가/수정/삭제가 가능.
tuple은 저장 순서가 있고 추가/수정/삭제가 불가능.

1. list
    여러 값을 저장할 때 가장 많이 사용. 자료형이 서로 다르더라도 하나의 리스트에 저장 가능
    하나의 배열(파이썬 list와 비슷한 개념의 자료 구조)에 동일한 자료형만을 저장할 수 있는
    C와 Java에 비해 python이 가지는 장점이라고 할 수 있음.  
'''
# li = [ 4, 5, 6, "안근수" ]
# print(li)
'''
    1-1. list의 index와 slice
        list는 str과 동일한 방식의 index와 slice를 지원함.
        1) 인덱스와 마이너스 인덱스
'''
# print(li[0])
# print(li[1])
# print(li[2])
# print(li[3])
# print(li[-1])
# print(li[-2])
# print(li[-3])
# print(li[-4])
'''     
       2) slice
        str의 슬라이싱과 같이 '시작점:종료점:증감값'으로 이루어져 있음.
'''
# list_num1 = [100, 3.14, "hello"]            # list 생성 방법 1
# list_num2 = list([4, 5, 6, 7, 8, 9])        # list 생성 방법 2
# print(list_num1)
# print(list_num2[0:4:2])
'''
      3) list 요소의 추가와 삭제
        list에 새로운 요소를 추가할 때는 append()와 insert() '메서드'를 사용할 수 있습니다.
        기존 요소를 삭제할 때는 pop() 메서드를 사용합니다.
        
        .append() - 항상 마지막 인덱스에 요소를 추가하는 메서드
        .insert(위치, 값) - 정해진 위치(인덱스)에 해당 값을 추가하는 메서드
'''
# scores = [30, 40, 50]   # scores라는 list 내에 있는 int 데이터인 30, 40, 50과 같은 애들을
# print(scores)           # 요소(element)라고 합니다.
# scores.append(100)      # 함수와 달리 리스트명.메서드명(데이터)의 형태로 사용함.
# print(scores)
#
# scores.insert(0, 90)
# print(scores)
'''
       .pop()의 경우 빈 괄호로 사용하게 되면 맨 마지막 요소가 삭제됨.
       .pop(인덱스)로 작성하면 해당 인덱스의 요소를 삭제함.
'''
# scores.pop()
# print(scores)
# scores.pop(0)
# print(scores)

# 교재에 없는 삭제 메서드 : .remove(값)을 하면 list 내의 해당 값을 찾아 삭제함.

# scores.remove(50)
# print(scores)
# # scores.remove(1110)       -> .remove()의 경우 argument로 정확한 값을 요구함.
# print(scores)

# list의 요소를 하나씩 뽑아 내는 반복문 - 일반 for문
# for i in range(len(scores)):
#     print(scores[i])
#
# print()
# # 향상된 for문
# for score in scores:
#     print(score)
'''
    2. tuple() : 저장된 값을 변경할 수 없는 list라고 생각하면 됩니다. 인덱스와 슬라이스를
        사용하지만 저장된 값 이외에는 추가 / 수정 / 삭제가 불가능.
        
        튜플은 소괄호를 통해 생성함
'''
# tuple_num1 = (1, 2, 3)          # 튜플 생성 방법 1
# tuple_num2 = tuple((4, 5, 6))   # 튜플 생성 방법 2
# tuple_num3 = 7, 8, 9            # 튜플 생성 방법 3
# print(tuple_num1)
# print(tuple_num2)
# print(tuple_num3)
# 복수의 변수 선언 및 초기화 하는 방법을 첫 시간에 배운 적이 있는데요
# a, b, c = 7, 8, 9
# print(a)
# print(b)
# print(c)
''' 
            튜플 생성 방법 3을 이용한다고 가정했을 때, 값이 하나 뿐인 튜플을 생성한다면
            tuple_num4 = 0이라고 입력할 경우 생기는 문제점은 무엇인가?
'''
# tuple_num4 = 0
# print(type(tuple_num4))
# tuple_num5 = 0,
# print(type(tuple_num5))
'''
        튜플에서의 인덱스 / 마이너스 인덱스
'''
tuple_num6 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# print(type(tuple_num6[1]))      # collection의 element에 type()함수를 먹이면 그 자료형이 추출됨
                                # 즉, tuple_num6[1]은 2라는 element를 가리키기 때문에 type()함수 적용시
                                # int로 출력됨.
tuple_num7 = "hello. ", "nice to meet you. ", "my name is ", "Ahn Geunsu", "I am ", "38", " years old."

# print(tuple_num7[0])
# print(tuple_num7[5])
# print(tuple_num7[-4])
# # 슬라이싱 적용
# print(tuple_num7[:-1:2])    # 시작값 -> 처음부터 / 종료값 - -1번지까지 : -1 번지 앞에서 끝이남 / 증감값 2
#
# new_str = "".join(tuple_num7)           # "".join()메서드 활용 -> tuple도 가능
# print(new_str)
'''
    3. set
        : 수학의 집합 개념을 구현한 자료형. list와의 차이점은 순서가 없기 때문에(비시퀀스) 인덱스 및
        슬라이싱 사용이 불가능. 중복된 값의 저장이 불가능.
        
        이를 활용하여 중복 제거용으로 사용하는 경우와, 교집합, 합집합, 차집합과 같은 집합 개념이 필요한 경우
        사용함.
        
        set을 사용하기 위해서는 중괄호({})를 사용합니다.
'''
# set_num1 = {1, 2, 3}        # 세트 생성 방법 1
# set_num2 = set({4, 5, 6})   # 세트 생성 방법 2
# print(set_num1)
# print(set_num2)

# 비어있는 li, tuple, set 생성
# li = []
# tu = ()
# se = {}
#
# print(type(li))
# print(type(tu))         # 이건 진짜 쓰일 일이 없죠
# print(type(se))

'''
    se = {} 형태로 비어있는 set을 만들게 됐을 경우 se는 사실 class dict이기 때문에, 비어있는 set를 만들기
    위해서는 세트 생성 방법 2를 사용해야만 함.
'''
# se2 = set({})           # 비어있는 세트를 생성 방법 1
# print(type(se2))
# se3 = set()             # 비어있는 세트를 생성 방법 2
# print(type(se3))
'''
    비어 있는 set를 생성할 때는 set() 함수를 어떻게든 이용 해야만 함.
    
    2) 특징
        1. 저장되는 순서가 없다 -> 인덱싱 / 슬라이싱 불가능
        2. 중복되는 값을 저장할 수 없다.
        3. 특히 2.의 특징으로 인해 set은 단독으로 쓰이기 보다는 list와 연계하여 많이 사용됨.
'''
# list_num5 = [ 1, 1, 2, 2, 3, 3, 3 ]
# print(list_num5)
# set_num5 = set(list_num5)       # 형변환 함수인 set()을 사용하고 그 안에 list_num5를 argument로 넣어 list -> set
# print(set_num5)                 # 중복 제거 된 것을 확인할 수 있음.
# list_num6 = list(set_num5)      # set()으로 중복 제거 후, list()를 이용하여 인덱스 / 마이너스 인덱스 / 슬라이싱을 재이용함.

'''
    set에는 인덱싱 / 마이너스 인덱싱 / 슬라이싱을 지원하지 않기 때문에 특정 요소만 추출하기 위해서는 형변환하는 과정(주로 list로)이
        필요함
        
    요소 관련 메서드
        .add() - set에 새로운 요소를 추가할 때
        .remove() - 기존 요소를 삭제 할 때
        .discard() - 기존 요소를 삭제할 때
'''
# set_num6 = {10, 20, 30}
# set_num6.add(50)
# print(set_num6)     # 순서가 없기 때문에 출력 결과가 순서대로 나오지 않을 수 있음
# set_num6.remove(50) # 순서가 없기 때문에 '값'을 정확히 입력해야 함.
# print(set_num6)

# 여기가 중요 .remove() vs. .discard()
# set_num6.remove(70)   # .remove()는 정확하지 않은 값을 넣을 경우 -> KeyError 발생
# set_num6.discard(70)    # .discard()는 요소에 정확한 값이 있지 않더라도 오류 발생하지 않음
'''
    4. dictionary - 말 그대로 사전의 의미를 생각하시면 됩니다. 종이 사전을 펴보게 되면,
    flower: 꽃
    dictionary: 사전
    등으로 기재돼있습니다. 즉 ':'을 기준으로 좌측과 우측이 나뉘어진 형태를 가지고 있는데, 딕셔너리는
    리스트, 튜플, 세트와 달리
    key: value의 구성으로 이루어져 있습니다.
'''
# dict_num1 = {
#     "이름": "안근수",
#     "나이": 38,
#     "주소": "부산광역시 연제구",
# }       # 맨마지막에 있는 ,의 의미는 혹시 key-value를 추가할 때 이전 라인에서 콤마 입력하고 엔터치고
        # 또 key: value 형태로 작성하기 번거로우니까 미리 쉼표를 찍어두는 게 또 뭐 개발자들끼리의 매너라고 합니다.
'''
와 같은 방식으로 작성합니다.
'''
# print(dict_num1)
# print(dict_num1["이름"])
'''
    딕셔너리는 인덱스는 존재하지 않지만 위와 같이 key를 인덱스와 유사하게 사용함.
    즉, key값을 알면 저장된 값(value)을 확인할 수 있는 구조.
'''
# list의 각 요소를 추출하기 위한 반복문
# li2 = [10, 20, 30, 40]
# 요소를 추출하기 위한 반복문
# for num in li2:
#     print(num)

# dictionary에서 같은 방식의 반복문을 활용하게 되면
# for i in range(len(dict_num1)):               index가 없기 때문에 오류
#     print(dict_num1[i])

# for key in dict_num1:
#     print(key)              # 그냥 print시키면 dict_num1의 key만 추출됨
#     print(dict_num1[key])   # value 추출법
#     print()
#
# # key 목록을 추출하는 메서드
# print(dict_num1.keys())
# # value 목록을 추출하는 메서드
# print(dict_num1.values())
#
# print(type(dict_num1.keys()))           # 이것을 확인해보면 얘네는 list가 아니기 때문에 인덱스가 없습니다.
# print(type(dict_num1.values()))
#
# keys = list(dict_num1.keys())           # index를 활용하기 위해서
# values = list(dict_num1.values())
#
# print(keys[1])
# print(values[2])
# '''
#     4-1. 딕셔너리 요소의 추가와 삭제
# '''
# dict_num1["직업"] = "코리아it아카데미 파이썬 강사"        # 기존에 없는 key를 입력하고, = value입력하면됨.
# print(dict_num1)
# # 하나의 key에 서로 다른 value를 저장할 수 없음 -> key 하나 당 value 하나
# dict_num1["직업"] = "코리아it아카데미 웹 개발 강사"
# print(dict_num1)
# # 삭제 방법
# dict_num1.pop("직업")     # key를 정확하게 입력해야 삭제 가능
# print(dict_num1)         # key 삭제하면 value도 같이 날아감

'''
응용 예제

list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그 list에서
2번째 요소를 출력하는 프로그램을 작성하세요.

실행 예
3번째 요소로부터 7번째 요소 = [30, 40, 50, 60, 70]
3번째 요소로부터 7번째 요소 중 2번째 요소 = 40
'''
list_original = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]       # 슬라이싱
# 빈 list 선언하고 나서 기존 list의 요소들을 for 반복문을 통해 추출하여 다시 대입
# list_sliced = []
# for i in range(2, 7, 1):
#     list_sliced.append(list_original[i])
#
# print(f"3번째 요소로부터 7번째 요소 = {list_sliced}")
# print(f"3번째 요소로부터 7번째 요소 중 2번째 요소 = {list_sliced[1]}")

# 기존 list를 바로 슬라이싱해서 새로운 list 변수에 대입하고, 그다음 새list[1]

sliced_list = list_original[2:7:1]
print(f"3번째 요소로부터 7번째 요소 = {sliced_list}")
print(f"3번째 요소로부터 7번째 요소 중 2번째 요소 = {sliced_list[1]}")
'''
사용자로부터 1에서 12사이의 월을 입력 받다, 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성하세요.(윤년은 고려x)
list로 작성하신 분은 dict / dict로 작성하신 분들은 list

실행 예
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일까지 있습니다.
'''
# month = input("1 ~ 12 사이의 월을 입력하세요 >>> ")
# last_date_dict = {
#     "1": 31,
#     "2": 28,
#     "3": 31,
#     "4": 30,
#     "5": 31,
#     "6": 30,
#     "7": 31,
#     "8": 31,
#     "9": 30,
#     "10": 31,
#     "11": 30,
#     "12": 31,
# }

# last_date_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(f"{month}월은 {last_date_dict[month]}일까지 있습니다.")
# print(f"{int(month)}월은 {last_date_list[int(month)-1]}일까지 있습니다.")

# 짧은 버전의 list를 쓴다는 것은 기본적으로 조건문 사용하라는 겁니다.
# last_date_short = [28, 31, 30]  # 1, 3, 5, 7, 8, 10, 12월은 31일 / 4, 6, 9, 11월은 30 / 2월 28일
#
# if int(month) == 2:
#     last_date = last_date_short[0]
# elif int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
#     last_date = last_date_short[1]
# elif int(month) in (4, 6, 9, 11):
#     last_date = last_date_short[2]
# else:
#     last_date = "오류"
#
# print(f"{month}월은 {last_date}일까지 있습니다.")
'''
수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사하기로 했습니다.
학생들이 원하는 장소를 입력 받아 동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3 명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하세요.

실행 예
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.
조사된 수학여행지는 ['제주', '민속촌']입니다.
'''
# 중복 제거를 위한 set -> set에 요소를 추가하는 메서드
# list -> list에 요소를 추가하는 메서드 -> 중복 제거를 위해 set으로 형변환
# student1 = input("희망하는 수학여행지를 입력하세요 >>> ")
# student2 = input("희망하는 수학여행지를 입력하세요 >>> ")
# student3 = input("희망하는 수학여행지를 입력하세요 >>> ")
#
# field_trip_set = set({})
# field_trip_set.add(student1)
# field_trip_set.add(student2)
# field_trip_set.add(student3)
#
# print(f"조사된 수학여행지는 {field_trip_set}입니다.")
# print(f"조사된 수학여행지는 {list(field_trip_set)}입니다.")

# field_trip_list = []
# for _ in range(3):
#     student = input("희망하는 수학여행지를 입력하세요 >>> ")
#     field_trip_list.append(student)
#
# field_trip_set2 = set(field_trip_list)
# field_trip_list_fianl = list(field_trip_set2)
#
# print(f"조사된 수학여행지는 {field_trip_set2}입니다.")
# print(f"조사된 수학여행지는 {field_trip_list_fianl}입니다.")

# field_trip_list_2 = []
# for _ in range(3):
#     field_trip_list_2.append(input("희망하는 수학여행지를 입력하세요 >>> "))
#
# print(f"조사된 수학여행지는 {set(field_trip_list_2)}")
# print(f"조사된 수학여행지는 {list(set(field_trip_list_2))}")

'''
사용자로부터 임의의 양의 정수를 하나 입력 받은 뒤 그 숫자만큼 '과일 이름'을 입력 받아
basket list에 저장하는 프로그램을 구현하세요.

실행 예
몇 개의 과일을 보관할까요? >>> 5
1번째 과일을 입력하세요 >>> 사과
2번째 과일을 입력하세요 >>> 바나나
3번째 과일을 입력하세요 >>> 체리
4번째 과일을 입력하세요 >>> 오렌지
5번째 과일을 입력하세요 >>> 망고
입력받은 과일들은 ["사과", "바나나", "체리", "오렌지", "망고"]입니다.
'''
# basket = []
# num = int(input("몇 개의 과일을 보관할까요 >>> "))
# for i in range(num):
#     fruit = input(f"{i+1}번째 과일을 입력하세요 >>> ")
#     basket.append(fruit)
#
# print(f"입력 받은 과일들은 {basket}입니다.")

# basket2 = []
# num2 = int(input("몇 개의 과일을 보관할까요 >>> "))
# for i in range(1, num2+1, 1):                       # 시작값, 종료값, 증감값을 이용한 방식
#     basket2.append(input(f"{i}번째 과일을 입력하세요 >>> "))
#
# print(f"입력 받은 과일들은 {basket2}입니다.")

'''
짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력 받고, 그 정수만큼 숫자를 입력받아 list에 저장하세요.
이후 저장된 숫자 중 짝수만 새로운 리스트에 저장하여 출력하는 프로그램을 작성하세요.

실행 예
몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력받은 숫자들 중 짝수는 [10, 20, 30]입니다.
'''
# even_nums = []
# for i in range(int(input("몇 개의 숫자를 입력할까요? >>> "))):
#     nums = int(input(f"{i+1}번째 숫자를 입력하세요 >>> "))
#     if nums % 2 == 0:
#         even_nums.append(nums)
#
# print(f"입력받은 숫자들 중 짝수는 {even_nums}입니다.")

# 전체 요소를 다 저장하는 리스트 / 짝수만 저장하는 리스트 하나 print() 짝수만 저장하는 애만 출력
# all_numbers = []
# even_numbers = []
# # 일반 for문
# for i in range(int(input("몇 개의 숫자를 입력할까요? >>> "))):
#     nums = int(input(f"{i+1}번째 숫자를 입력하세요 >>> "))
#     all_numbers.append(nums)
#
# # 향상된 for문 이용
# for number in all_numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
#
# print(f"입력받은 숫자들 중 짝수는 {even_numbers}입니다.")
'''
딕셔너리 기반의 연락처 관리

사용자로부터 3명의 이름과 전화번호를 입력 받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는 프로그램을 작성하세요.

실행 예
1번째 사람의 이름을 입력하세요 >>> 김일
1번째 사람의 전화번호를 입력하세요 >>> 010-1234-5678
2번째 사람의 이름을 입력하세요 >>> 김이
2번째 사람의 전화번호를 입력하세요 >>> 010-2345-6789
2번째 사람의 전화번호를 입력하세요 >>> 010-2345-6789
3번째 사람의 이름을 입력하세요 >>> 김삼
3번째 사람의 전화번호를 입력하세요 >>> 010-9876-5432

입력받은 연락처는 {'김일':'010-1234-5678', '김이':'010-2345-6789', '김삼':'010-9876-5432'}입니다.
'''
# 딕셔너리에 요소를 추가하는 방법
telephones = {}             # 비어있는 딕셔너리를 선언하는 방식
for i in range(3):
    dict_key = input("1번째 사람의 이름을 입력하세요 >>> ")
    dict_value = input("1번째 사람의 전화번호를 입력하세요 >>> ")

    telephones[dict_key] = dict_value

print(f"입력 받은 연락처는 {telephones}입니다.")