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

# 한 변의 길이가 150인 정삼각형을 그리시오.
# for _ in range(3):
#     t.forward(150)
#     t.left(120)
# t.color(random.choice(colors))
# # 한 변의 길이가 150인 정사각형을 그리시오.
# for _ in range(4):
#     t.forward(150)
#     t.left(90)
# t.color(random.choice(colors))
# # 한 변의 길이가 150인 정오각형을 그리시오.
# for _ in range(5):
#     t.forward(150)
#     t.left(360 / 5)
# # 정삼각형부터 정십각형까지를 이상의 코드를 찹조하여 그리시오.
# t.color(random.choice(colors))
# for _ in range(6):
#     t.forward(150)
#     t.left(360 / 6)
# t.color(random.choice(colors))
# for _ in range(7):
#     t.forward(150)
#     t.left(360 / 7)
# t.color(random.choice(colors))
# for _ in range(8):
#     t.forward(150)
#     t.left(360 / 8)
# t.color(random.choice(colors))
# for _ in range(9):
#     t.forward(150)
#     t.left(360 / 9)
# t.color(random.choice(colors))
# for _ in range(10):
#     t.forward(150)
#     t.left(360 / 10)

# 이상의 코드가 반복되는 지점이 있는 것을 확인했으니 반복이 되는 사이클만큼만 복사를 해서 그 부분을 또 반복문을
# 돌려보겠습니다.
# for i in range(3, 11, ):         # range(시작값, 종료값, 증감값)
#     for _ in range(i):
#         t.forward(100)
#         t.left(360 / i)
#     t.color(random.choice(colors))

# n = 3
# for i in range(3, 11, ):
#     for _ in range(n):
#         t.forward(100)
#         t.left(360 / n)
#     t.color(random.choice(colors))
#     n += 1

# 도형을 그리는 반복문 부분을 함수화
# def draw_figures(angles):
#     # angles가 3 미만일 경우에는 실행이 안되야 한다는 잠재적인 문제점이 있습니다.
#     if angles < 3:
#         print("도형을 그릴 수 없어 실행할 수 없습니다.")
#     else:
#         for i in range(angles):
#             t.forward(100)
#             t.left(360 / angles)
#         t.color(random.choice(colors))

# draw_figures(10)

# 함수를 반복 실행
# for i in range(11):
#     draw_figures(i)

'''
    .heading() 메서드 :
        거북이가 바라보는 방향을 나타내는 속성이고 도(degree)단위로 나타남.
        
        해당 메서드는 콘솔창에 float으로 나타납니다.
        0도 : 동쪽
        90도 : 북쪽
        180도 : 서쪽
        270도 : 남쪽
        
    .setheading() 메서드 :
        특정 각도로 거북이를 회전시키는 메서드
        0도 : 동쪽
        90도 : 북쪽
        180도 : 서쪽
        270도 : 남쪽
'''
# t.forward(50)
# print(t.heading())
# t.left(90)
# t.forward(50)
# print(t.heading())
# t.left(120)
# print(t.heading())
# t.setheading(0)
# t.forward(100)

# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(t.heading() + 10)
#
# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(t.heading() + 10)
#
# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(t.heading() + 10)
#
# t.circle(100)
# t.color(random.choice(colors))
# t.setheading(t.heading() + 10)


# 그렇다면 반복되는 부분 만큼만 따와서 다시 반복을 돌려보겠습니다.
# 제 자리로 오는 것이 목표이고, 10도씩 꺾이니까 36번 반복
# for _ in range(360 // 10):
#     t.circle(100)
#     t.color(random.choice(colors))
#     t.setheading(t.heading() + 10)

# 이상의 4줄의 코드를 응용하여 draw_spirograph(size_of_gap)로 함수화하시오.
# def draw_spirograph(size_of_gap):
#     for _ in range(360 // size_of_gap):
#         t.circle(100)
#         t.color(random.choice(colors))
#         t.setheading(t.heading() + size_of_gap)
#
# draw_spirograph(30)


# 아까 위에서 함수화한 draw_figures를 참조하여 정삼각형부터 정십각형까지
# 도형마다 색깔이 임의적으로 바뀌면서, 점선으로 도형을 그릴 수 있도록 코드를 작성하시오.

# 점선을 그리는 함수를 정의할 필요가 있습니다
# 근데 이 함수는 t.forward(100)을 대신하는 함수여야 합니다.
def draw_dotted_lines():
    for _ in range(10):
        t.forward(5)
        t.penup()
        t.forward(5)
        t.pendown()

# draw_figures2도 t.forward(100)이 포함돼있으니 그것을 전부 점선 그리는 함수로 대체해서 수정해야합니다.
def draw_figures2(angles):
    # angles가 3 미만일 경우에는 실행이 안되야 한다는 잠재적인 문제점이 있습니다.
    if angles < 3:
        print("도형을 그릴 수 없어 실행할 수 없습니다.")
    else:
        for i in range(angles):
            draw_dotted_lines()
            t.left(360 / angles)
        t.color(random.choice(colors))

for i in range(11):
    draw_figures2(i)









screen.exitonclick()

