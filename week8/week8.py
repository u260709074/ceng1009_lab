# def GradeMark(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
# marks =[95,90,89.9,80,79.9,78,65,60,59.5,0]
# for mark in marks:
#     print("grade is ", GradeMark(mark))

# import turtle
#
#
#
#
# def chooseColor(height):
#     if height >=200:
#         return "red"
#     elif height >=100:
#         return "yellow"
#     else:
#         return "green"
#
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.pendown()
#     t.write(" "+str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#
#     t.forward(height+gap)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height = max(data)
#     num_bars = len(data)
#     border = 10
#     gap = (max_height + border)/25
#
#     wn = turtle.Screen()
#     wn.bgcolor("lightgreen")
#     right = 40 + num_bars + border
#     top = max_height + 4*border
#     wn.setworldcoordinates(-border, -border, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
#     wn.exitonclick()
#
# data =[65,233,155,36,220,35,379]
# barChart(data)
# import turtle
#
#
# def draw_bar(t, height):
#
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write("  " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.forward(10)
#
#
# def draw_bar_chart():
#
#     xs = [48, 117, 200, 240, -50, 160, 90, -120]
#
#     wn = turtle.Screen()
#     wn.setup(width=650, height=600)
#     wn.bgcolor("lightgreen")
#
#     t = turtle.Turtle()
#     t.pensize(3)
#
#     t.penup()
#     t.goto(-250, 0)
#     t.pendown()
#
#     for value in xs:
#
#         if value >= 200:
#             t.color("red")
#         elif 100 <= value < 200:
#             t.color("yellow")
#         else:
#             t.color("green")
#
#         draw_bar(t, value)
#
#     wn.mainloop()
#
#
# if __name__ == "__main__":
#     draw_bar_chart()

import math

# def findHypo(a,b):
#
#     hypot = (a**2 + b**2)**0.5
#     return hypot
#
#
#
#
# print(findHypo(3,4))




