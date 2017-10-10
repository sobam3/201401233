import turtle as t
import random                           

each = input("몇개의 장미를 만들까요?") #w장미의 갯수를 물음
k=int(each)

t.speed(0)  	                        #속도 최대빠르기
t.bgcolor("dark Green")                 #배경색
t.hideturtle()                          #거북이 숨기기

for x in range(k):                      #꽃그리기 k회 반복
    size = random.randint(5,7)/12       #꽃의 크기 (전체적)
    y = random.randint(-360,360)        #꽃의 좌표
    z = random.randint(-360,360)
    t.up()
    t.goto(y, z)                        #좌표 이동
    t.down()
    m = random.randint(3,5)             #잎의 갯수
    q = random.randint(1,2)             #잎의 색깔
    if q==1:
        t.color("green")
        t.fillcolor("yellow green")
    if q==2:
        t.color("dark olive green")
        t.fillcolor("olive")

    w= random.randint(1,360)

    for x in range(1,m+1):              #잎 그리기
        d = random.randint(6,9) * size  #잎의 크기 (매번 다른 크기가 나오도록)
        a =((360/m)*x+w)                #잎의 회전각도 (매번 다른모양이 나오도록)
        
        t.begin_fill()
        
        t.setheading(a+270)              #좌측 잎
        t.forward(3.18*d/5)                 
        t.setheading(a+80)
        for x in range(9):
            t.forward(2*d)
            t.right(10)
        for x in range(10):
            t.forward(d)
            t.right(4)
        for x in range(10):
            t.forward(d)
            t.left(4)  
        t.setheading(a+180)
        t.forward(146.97*d/5)

        t.setheading(a+90)                #우측 잎
        t.forward(3.18*d/5)    
        t.setheading(a-80)
        for x in range(9):
            t.forward(2*d)
            t.left(10)
        for x in range(10):
            t.forward(d)
            t.left(4)
        for x in range(10):
            t.forward(d)
            t.right(4)
        t.setheading(a+180)
        t.forward(146.97*d/5)
        t.end_fill()

    #2 꽃잎  그리기

    q = random.randint(1,3)             #꽃잎의 색깔
    if q==1:
        t.color("black")
        t.fillcolor("white")
    if q==2:
        t.color("dark red")
        t.fillcolor("red")
    if q==3:
        t.color("black")
        t.fillcolor("dark red")

    s=80*size                           #꽃잎의 크기 관련 미지수  
    small=10*size 
    a=1.2
    d=0.3
    p=random.randint(1,360)             #꽃잎의 회전각도(매번 다르도록)

    t.up()
    for x in range(6):                  #꽃잎 그리기
        t.seth(230.294018625+p)
        t.fd(125.22537921683447*s/80)
        t.down()
        t. setheading(p)
        t.begin_fill()
        for x in range(9):
            t.forward(160*s/80)
            t.left(80)
        t.end_fill()
        s=s-(small*a)                       #미지수 변화
        a=a+d
        d=d-0.1
        t.up()
        t.goto(y,z)                         #중심으로 돌아가기
        
        
    

