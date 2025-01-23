'''
chapter15_file_study 패키지 생성
main.py 생성

1. 파일 입출력의 개요
    파이썬을 이용하여 컴퓨터에 저장된 파일을 읽어들이는 것과, 새로운 파일을 생성,
    컴퓨터에 저장하는 것이 가능.
    파일 입력(input) : 기존의 파일 내용을 읽어들이는 것
    파일 출력(output) : 기존 파일에 새로운 내용을 추가하거나
        새로운 파일을 출력하는 것

    1) 파일 열기
        실제로 어떤 파일을 열어본다는 의미가 x
        입출력 작업을 진행할 파일을 지정하는 것.
            -> 파일 입출력시 파일 열기 작업을 가장 먼저 수행해야 함.

            open() 함수를 사용
            형식 :
            (파일)객체명 = open(파일명, 모드)

            1)-1. 파일명
                파일명은 입출력을 수행할 파일을 의미.
                파일명만 작성할 수도 있고, 경로를 함께 작성할 수도 있음.
'''
import fileinput

# open("sample.txt")  #파일명만 작성하는 경우 파이썬 소스 코드 파일과 같은 경로에 존재하는 파일
# open("C:/sample.txt")   # 전체 경로를 작성하는 방법
# open("./sample.txt")    # 현재 디렉토리(.)를 기존으로 경로를 설정하는 방법
# open("../sample.txt")   # 상위 디렉토리(..)를 기준으로 경로를 설정하는 방법
'''
            1)-2. 모드
                파일을 여는 목적 / 파일 입력 혹은 출력을 위해서인지를 모드를 통해서 결정함.
+------+------+-----------+-------------+---------------------+---------------------+
| 분류 | 종류 |    의미   |     설명    | 파일이 없을 때 동작 | 파일이 있을 때 동작 |
+------+------+-----------+-------------+---------------------+---------------------+
| 입력 |  r   |    read   |     읽기    |      오류 발생      |         읽기        |
| 출력 |  w   |   write   |     쓰기    |      새로 생성      |      새로 생성      |
|      |  a   |   append  |     추가    |      새로 생성      |         추가        |
|      |  x   | exclusive | 배타적 추가 |      새로 생성      |      오류 발생      |
+------+------+-----------+-------------+---------------------+---------------------+ 
                입출력 모드를 생략하면 기본적으로 r 모드로 파일이 열립니다.
                w 모드나 a 모드와 같이 파일 출력을 목적으로 한다면 반드시 해당 모드를 명시해야 함.
                
                파일을 여는 목적을 결정하면, 어떤 파일인지 파일의 종류를 구분 해야 합니다.
                일반적으로는 텍스트 파일인지 아닌지로 결정됩니다.
                
+------+--------+-------------------------------------------+                
| 종류 |  의미  |                    설명                   |
+------+--------+-------------------------------------------+
|  t   |  text  |                텍스트 파일                |
|  b   | binary | 바이너리 파일(텍스트 파일 외의 모든 파일) |
+------+--------+-------------------------------------------+       
                열고자 하는 파일의 종류를 생략하면 기본적으로 t 모드
                바이너리 파일의 경우에는 반드시 b를 명시해야 함.        
                
                종합하여 사용도 가능 
+------+--------------------------------+
| 모드 |              설명              |
+------+--------------------------------+
|  rt  |     텍스트 파일 읽기 모드      |
|  rb  |    바이너리 파일 읽기 모드     |
|  wt  |     텍스트 파일 쓰기 모드      |
|  wb  |    바이너리 파일 쓰기 모드     |
|  at  |     텍스트 파일 추가 모드      |
|  ab  |    바이너리 파일 추가 모드     |
|  xt  |  텍스트 파일 배타적 추가 모드  |
|  xb  | 바이너리 파일 배타적 추가 모드 |
+------+--------------------------------+  

            2) 파일 닫기
                파일을 더 이상 사용하지 않거나 프로그램을 종료할 때 열어놓은 파일을 닫는 편이 안전.
                
            형식 :
            파일객체명.close()                       # open()은 함수인데 반해 .close()는 메서드라는 차이가 있습니다.
            
    3. 파일의 생성
'''
# file = open("myFile.txt", "wt")
# print("myFile.txt 파일이 생성되었습니다.")
#
# file.close()
'''
    4.with 문
        close() 메서드를 자동으로 호출할 수 있는 문법
        
    형식 :
        with open(파일명, 모드) as 파일객체:
            파일처리코드
'''
# with open("myFile2.txt", "wt") as file:
#     print("myFile2.txt 파일이 생성되었습니다.")

'''
2. 파일 출력
    1) 텍스트 파일 생성하기
'''
# file = open("hello.txt", "wt")
#
# file.write("hello\nnice to meet you.")
# file.close()
'''
    2) 텍스트 파일에 내용 추가하기
'''
# file = open("hello.txt", "at")
# file.write("\nMy name is Ahn Geunsu.")
# file.close()

# file = open("hello.txt", "at")
# file.write("\nI drank a cup of coffee.")
# print("hello.txt 파일에 내용이 추가되었습니다.")
# file.close()
'''

기본 예제

오늘의 스케줄을 입력하면 그 내용을 모두 파일에 보관하는 프로그램을 작성합니다.
스케줄을 입력하지 않고 enter를 누르면 프로그램을 종료됩니다.
생성되는 파일의 이름은 현재 날짜이고, 확장자는 txt입니다.
"2020-10-22.txt"와 같은 형식을 갖추고 있습니다.
'''
import time

# file = open(time.strftime("%Y-%m-%d")+".txt", "at")
# end_of_schedule = False
# while not end_of_schedule:
#     schedule = input("오늘의 스케줄을 입력하세요 >>> ")
#     # if schedule:
#     #     file.write(schedule + "\n")
#     # else:
#     #     end_of_schedule = True
#     if not schedule:
#         end_of_schedule = True      # 다음 반복이 실행되지 않음
#         # break                       # 135번 라인이 아예 실행되지 않음
#     file.write(schedule + "\n")
# print("오늘의 날짜에 스케줄을 추가했습니다.")
# file.close()
'''
    3. 파일 입력(input)
        1) 텍스트 파일 읽기
            1)-1. read() 메서드
            형식 :
                file.read(size)
'''
# file = open("hello.txt", "rt")
#
# str = file.read()   # size를 명시하지 않으면 전부 다 가지고 옵니다.
#
# print(str, end="🙌")  # keyword argument형태로 end 속성을 불러왔고,
#                     # 거기에 ""이라는 데이터를 대입
#
# file.close()
'''
파일과 동일한 모습으로 출력하기 위해서 print() 함수의 자동 줄바꿈 방지를 위한 end="" 속성 추가.
read() 메서드를 통해 전체를 읽으려면 메모리 공간이 많이 필요합니다. 읽어야 할 파일이 크다면
일부만 읽어들이는 작업을 반복하는 반복문을 통해 파일 전체를 읽어내도록 구현하는 편이 좋습니다.
'''
# file = open("hello.txt", "rt")
# end_of_text = False
# while not end_of_text:
#     str = file.read(1)      # 일부만 파일에 대입
#     if not str:
#         break
#     print(str, end="")      # 이 경우에는 str에 문자 하나씩 대입하고 출력하는 것을 반복합니다. 그렇기 때문 end=""이 필수
# file.close()
'''
            2) readline() 메서드
                텍스트 파일을 한 줄씩 읽어서 처리하는 메서드
                만약 파일이 종료되어 더 읽어들일 데이터가 없다면 빈 문자열("")을 읽어들입니다.
                반복문을 이용해서 여러 번 읽어들여야 할 때 파일 전체를 읽을 수 있습니다.
'''
# file = open("hello.txt", "rt")

# str = file.readline()           # 한줄만 읽음 -> 전체 읽고 싶으면 반복문 -> 끝이 어딘지 모른다 -> while 채용
# print(str)
#
# end_of_text = False
# while not end_of_text:
#     str = file.readline()
#     if not str:
#         end_of_text = True       # 위에 read는 break 적용했고, 여기서는 end_of_text = True 적용했습니다.
#     print(str, end="")
#
# file.close()
'''
            3) readlines() 메서드
                전체 라인을 읽어들여서 각 라인 단위로 '리스트'에 저장하는 메서드
'''

file = open("hello.txt", "rt")
lines = file.readlines()
# print(lines[0], end="")
# print(lines[1], end="")
# print(lines[2], end="")
# print(lines[3], end="")

# 일반 for문으로 작성하세요
# for i in range(len(lines)):
#     print(lines[i], end="")

# 향상된 for문으로 작성하세요
# for line in lines:
#     print(line, end="")
#
# file.close()

# 저거 잘 정리해서
'''
hello
nice to meet you.
My name is Ahn Geunsu.
I drank a cup of coffee.
로 정렬시켜보세요.
'''

'''
나라별 수도를 순차적으로 반복시켜 nation 리스트에 사전에 미리 저장해두었습니다.

nation 리스트의 내용을 이해하여 다음과 같은 nation.txt 파일을 '생성'하세요.

실행 예

생성된 nation.txt 파일의 내용은 다음과 같습니다.

Greece - Athene
Germany - Berlin
South Korea - Seoul
USA - Washington D.C
'''
nation = ["Greece", "Athene", "Germany", "Berlin", "South Korea", "Seoul", "USA", "Washington D.C"]

# file = open("nation.txt", "wt")
# 막 쓴 버전
# file.write(nation[0] + " - " + nation[1] + "\n")
# file.write(nation[2] + " - " + nation[3] + "\n")
# file.write(nation[4] + " - " + nation[5] + "\n")
# file.write(nation[6] + " - " + nation[7])
# file.close()
# 반복문 버전
with open("nation.txt", "wt") as file:
    # 리스트를 두 항목씩 반복하면서 파일에 작성할겁니다
    for i in range(0, len(nation), 2):
        file.write(nation[i] + " - " + nation[i+1] + "\n")















# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ["분류", "종류", "의미", "설명", "파일이 없을 때 동작", "파일이 있을 때 동작"]
# table.add_row(["입력", "r", "read", "읽기", "오류 발생", "읽기"])
#
# print(table)

