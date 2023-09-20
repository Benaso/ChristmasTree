import mylibrary
import turtle as t
from turtle import *
import random as r
import time

speed("fastest")
screensize(bg='black')
t.title("圣诞快乐")
setup(800, 800)
pencolor('green')
pensize(10)
penup()
hideturtle()
goto(0,150)
showturtle()
pendown()


# 画出第一部分的树
mylibrary.biasLeft(3, 10, 13, -120)
penup()
goto(0, 150)
pendown()
mylibrary.biasRight(3, 10, 13, -60)
seth(-150)
penup()
fd(10)
pendown()
mylibrary.breakLine(3, 5, 12, -150, 5)

# 画出第二部分的树
penup()
goto(-55, 34)
pendown()
#左侧斜线
mylibrary.biasLeft(5, 10, 9, -115)
penup()
goto(55, 34)
pendown()
#右侧斜线
mylibrary.biasRight(5, 10, 9, -60)
#补充波浪线
seth(-120)
penup()
fd(10)
seth(-145)
pendown()
mylibrary.breakLine(4, 5, 12, -150, 5)

#画第三部分树
penup()
goto(-100, -40)
pendown()
#左侧斜线
mylibrary.biasLeft(3, 12, 7, -114)
penup()
goto(100, -40)
pendown()
#右侧斜线
mylibrary.biasRight(3, 12, 7, -62)
#补充波浪线
seth(-152)
penup()
fd(10)
pendown()
mylibrary.breakLine(6, 5, 10.5, -150, 8)

#第四部分树
penup()
goto(-120, -110)
pendown()
#左侧斜线
mylibrary.biasLeft(5, 7, 12, -120)
#右侧斜线
penup()
goto(120, -110)
pendown()
mylibrary.biasRight(5, 7, 12, -60)
#补充波浪线
seth(-150)
penup()
fd(10)
pendown()
mylibrary.breakLine(6, 6, 10, -143, 10)

#画出树干
#右侧线
penup()
goto(70, -180)
pendown()
seth(-75)
pensize(10)
pencolor("DarkOrange4")
circle(-40, 90)
#底线
penup()
goto(43, -228)
pendown()
seth(-180)
pensize(10)
pencolor("DarkOrange4")
fd(80)

#左侧竖线
penup()
goto(-40, -228)
pendown()
seth(160)
pensize(10)
pencolor("DarkOrange4")
circle(-40,90)

#添加额外绿色颜料
penup()
pencolor("lime green")
hideturtle()
goto(-60,40)
showturtle()
pendown()
seth(-90)
pensize(8)
circle(-20, 90)

penup()
pencolor("lime green")
hideturtle()
goto(-60,-40)
showturtle()
pendown()
seth(-88)
pensize(8)
circle(-30, 91)

penup()
pencolor("lime green")
hideturtle()
goto(-60,-40)
showturtle()
pendown()
seth(88)
pensize(8)
circle(-30, 91)

mylibrary.guest(-65, -152, 155)
mylibrary.guest(101, -149, 159)
mylibrary.guest(112, -109, 53)
mylibrary.guest(160, -140, 150)
mylibrary.qu(75, -121, 175)
mylibrary.guest(73, -85, 160)
mylibrary.guest(-40, -85, 160)
mylibrary.guest(88, -49, 50)
mylibrary.guest(120, -78, 146)
pencolor("lime green")
mylibrary.qu(-50, -70, 180)
pencolor("lime green")
mylibrary.qu(65, -35, 180)
pencolor("lime green")
mylibrary.qu(46, 15, 180)
pencolor("lime green")
mylibrary.guest(-60, 30, 120)
mylibrary.guest(-20, -20, 150)
mylibrary.guest(45, 40, 60)
mylibrary.guest(-30, 40, 170)
mylibrary.guest(-30, 110, 115)
mylibrary.guest(40, 90, 60)
mylibrary.guest(80, 50, 160)

#添加圆圈
mylibrary.drawCircle(10, 160, 80)

#添加星星

seth(-15)
mylibrary.star(-120, -70, 10)
seth(10)
mylibrary.star(100, -20, 10)
seth(-10)
mylibrary.star(10, 40, 10)
seth(30)
mylibrary.star(-80, 60, 10)
mylibrary.star(100, -150, 8)
mylibrary.star(-140, -150, 9)
mylibrary.star(20, 120, 10)
mylibrary.star(40, -140, 15)
mylibrary.star(-20, -100, 16)
mylibrary.star(-50, -80, 12)
mylibrary.star(-65, -165, 8)
mylibrary.star(-40, 20, 10)

mylibrary.drawsnow()

