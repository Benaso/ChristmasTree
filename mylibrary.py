import turtle as t
from turtle import *
import random as r

def breakLine(x, y, z, m, n):
    """x为波浪数目，y为范围内像素点距离，
    z为长度， m为turtle启动方向，n为第长度"""
    for j in range(0, x):
        for i in range(y):
            fd(z)
            right(16)
        seth(m)
        penup()
        fd(5)
        pendown()

def biasLeft(x, y, z, m):
    """左侧斜线"""
    seth(m)
    for i in range(y):
        fd(z)
        right(x)

def biasRight(x, y, z, m):
    """右侧斜线"""
    seth(m)
    for i in range(y):
        fd(z)
        left(x)


def guest(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(10)
        right(10)

def qu(x, y, z):
    penup()
    goto(x, y)
    seth(-z)
    pendown()
    for angel in range(5):
        fd(6)
        right(10)
    seth(-150)
    fd(20)

def drawCircle(x, y, r):
    """输出一个圆形"""
    pensize(2)
    pencolor('red')
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    fillcolor('red')
    for i in range(5):
        circle(20)
    end_fill()

def star(x, y, size):
    """生成星星"""
    pensize(2)
    pencolor("yellow")
    penup()
    goto(x, y)
    pendown()
    begin_fill()
    fillcolor("yellow")
    for i in range(5):
        left(72)
        fd(size)
        right(144)
        fd(size)
    end_fill()

def drawsnow():
    """随机生成雪花"""
    t.ht()
    t.pensize(2)
    for i in range(70):
        t.pencolor("white")
        t.pu()
        t.setx(r.randint(-350, 350))
        t.sety(r.randint(-80, 350))
        t.pd()
        dens = 6  # 雪花瓣数设为6
        snowsize = r.randint(1, 10)
        for j in range(dens):
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            t.right(int(360 / dens))  # 转动角度