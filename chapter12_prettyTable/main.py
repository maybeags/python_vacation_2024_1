'''
외부 패키지의 설치

좌측 상단 메뉴버튼(햄버거) -> file -> settings(설정 : ctrl + alt + s)
좌측 리스트에서 project : 프로젝트명으로 돼있는 부분 클릭
-> python interpreter
-> 좌상단에 + 눌러서 필요한 패키지 검색 및 설치
'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data

# PrettyTable 클래스의 객체
table = PrettyTable()

print(pokemon_data[24][1])