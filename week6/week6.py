# import turtle
#
# #--setup--
# wn =turtle.Screen()
# wn.bgcolor("lightgreen")
#
# tess =turtle.Turtle()
#
# # --Functions--
# def drawpoly(someturtle,somesides,somesize):
#     angle = 360/somesides
#     for i in range(somesides):
#         someturtle.forward(somesize)
#         someturtle.left(angle)
#
# def drawSpiral(someturtle,angle):
#     size = 1
#     for i in range(100):
#         someturtle.forward(size)
#         someturtle.right(angle)
#         size = size + 2
#
# def drawEquitriangle(someturtle,sides,somesize):
#     drawpoly(someturtle,3,somesize)
#
# def drawStar(someturtle,sides):
#   for i in range(5):
#     someturtle.forward(350)
#     someturtle.right(144)
#
# def drawSprite(someturtle,legs,length):
#     angle = 360/legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.backward(length)
#         someturtle.left(angle)
#
# #-- Exercise --
# #--- Exercise 1--
# # tess.pensize(3)
# #
# # tess.pencolor("hotpink")
# # drawpoly(tess,8,50)
# # wn.exitonclick()
#
# #--Exercise 2--
#
# # tess.pencolor("blue")
# #
# # for i in range(20):
# #     drawpoly(tess,4,100)
# #     tess.left(18)
# #
# #
# # wn.exitonclick()
#
# #--Exercise 3--
# # tess.pencolor("blue")
# # tess.penup()
# # tess.goto(-150,0)
# # tess.pendown()
# # drawSpiral(tess,90)
# #
# #
# # tess.penup()
# # tess.goto(150,0)
# # tess.pendown()
# # drawSpiral(tess,89)
#
# #--exercies 4--
#
# # drawEquitriangle(tess,100)
#
# #--exercise 5__
#
# # tess.color("hotpink")
# # for i in range(5):
# #     drawStar(tess,50)
# # tess.penup()
# # tess.forward(350)
# # tess.right(144)
# # tess.pendown()
#
# #--exercise 6--
# drawSprite(tess,15,120)
#
#
# #--finish--
# wn.exitonclick()
