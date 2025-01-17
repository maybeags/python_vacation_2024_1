'''
외부 패키지의 설치

좌측 상단 메뉴버튼(햄버거) -> file -> settings(설정 : ctrl + alt + s)
좌측 리스트에서 project : 프로젝트명으로 돼있는 부분 클릭
-> python interpreter
-> 좌상단에 + 눌러서 필요한 패키지 검색 및 설치 -> prettytable 검색해서 설치
'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data

# PrettyTable 클래스의 객체
table = PrettyTable()

# print(pokemon_data[24][1])

table.field_names = ["번호", "이름", "타입"] # 객체의 필드에 리스트 자료형을 대입
# print(table.field_names)
# pokemon1 = (1, "이상해씨", "풀/독")
# table.add_row(pokemon1)

# 일반 for문
# for i in range(len(pokemon_data)):
#     table.add_row(pokemon_data[i])

# 향상된 for문
for pokemon in pokemon_data:
    table.add_row(pokemon)

print(table)