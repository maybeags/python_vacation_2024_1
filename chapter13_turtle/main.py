'''
chapter13_turtle
main.py
'''
# turtle이라는 모듈을 사용하고, Turtle, Screen이라는 클래스를 사용한다는 의미
from turtle import Turtle, Screen
from random import Random

# 객체 생성
t = Turtle()        # Turtle 클래스의 객체 생성
screen = Screen()   # Screen 클래스의 객체 생성
random = Random()
t.shape("turtle")
t.color("white")
screen.bgcolor("black")
# t.forward(100)

colors = [
    "dodger blue",
    "peru",
    "dark khaki",
    "sea green",
    "crimson",
    "cornsilk",
    "pale violet red",
    "dark slate blue",
    "royal blue",
    "papaya whip",
    "khaki",
    "dark sea green",
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
    "tomato",
    "dark olive green",
    "mint cream",
    "sienna",
]
# 거북이 이동 방법
# t.forward(50)
# t.penup()
# t.forward(50)
# t.pendown()
# t.forward(50)
def draw_dotted_line():
    for _ in range(10):         # 그냥 반복을 10번하는거지
                                # 변수가 쓰지 않으므로 "_"를 썼습니다.
        t.forward(10)
        t.penup()
        t.forward(10)
        t.pendown()

# draw_dotted_line()

# draw_dotted_line을 수정하여, 반복횟수를 고정시키지 않고 그때그때 지정할 수 있도록
# 작성하시오.
# draw_dotted_line2를 정의하세요.

# def draw_dotted_line2(n):
#     for _ in range(n):
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#         t.pendown()
#
# draw_dotted_line2(20)

# draw_dotted_line3을 정의하여 반복 횟수를 입력 받아 그 횟수만큼 반복이 실행될 수 있도록 수정하시오.
# 1) main단계에서 input을 받아서 시행하는 방법
# 2) 함수 내에 input을 집어넣어서 argument없이 실행하는 방법

# 1)
# times = int(input("몇 번의 반복을 실행하시겠습니까? >>> "))
# def draw_dotted_line3(n):
#     for _ in range(n):
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#         t.pendown()
#
# draw_dotted_line3(times)
# 2)
# def draw_dotted_line4():
#     times = int(input("몇 번의 반복을 실행하시겠습니까? >>> "))
#
#     for _ in range(times):
#         t.forward(10)
#         t.penup()
#         t.forward(10)
#         t.pendown()
#
# draw_dotted_line4()


# 한 변의 길이가 150인 정사각형을 그리시오.
# for _ in range(4):
#     t.forward(150)
#     t.left(90)

# 한 변의 길이가 150인 정삼각형을 그리시오.
for _ in range(3):
    t.forward(150)
    t.left(120)

# 한 변의 길이가 150인 정오각형을 그리시오.




















screen.exitonclick()

