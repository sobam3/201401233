import turtle as t
import random

def b1():               #함수 b1을 정의합니다.
    while -a< t.xcor() <a and -a< t.ycor()< a and ((t.xcor() < bx or t.xcor() > bx+ba) or (t.ycor() < by or t.ycor() > by+bb)) and ((t.xcor() < cx or t.xcor() > cx+ca) or (t.ycor() < cy or t.ycor() > cy+cb)):         # 장애물 블록1,2 벽을 을 제외한 영역일 경우 아래 행동을 취합니다.
        if ex< t.xcor() <ex+ea and ey< t.ycor()< ey+eb:     # 거북이가 불 장애물로 들어갈 경우 혼란에 빠져하면 밖으로 나갑니다.(360도 회전 후 뒤로 돌아 나갑니다.)
            t.lt(180+360)
            t.fd(20)
            t.left(random.randint(0,20))
        if dx< t.xcor() <dx+da and dy< t.ycor()< dy+db:     # 거북이가 모래 장애물로 지정된 영역을 지날경우 속도를 절반으로 줄입니다.
            t.forward(0.5)
        else:
            t.forward(1)
            
    X = t.xcor()        #현재 거북이의 X,Y 좌표를 미지수로 지정합니다.
    Y = t.ycor()
    #print(X, Y)
    gap = 1.5           #거북이의 위치에 대한 오차를 1.5로 지정합니다.


    if (bx-gap < X < bx+ba+gap) and (by-gap < Y< by+ bb+gap):   # 현재 거북이 위치가 오차를 포함하여 장애물 블록1에 위치하였다면 아래 조건을 미지수로 지정합니다.
        dx1 = X - (bx+ba)#오른쪽 방향으로 부딪힘
        dx2 = X - bx #왼쪽 방향으로 부딪힘
        dy1 = Y - by #위쪽 방향으로 부딪힘
        dy2 = Y - (by+bb) #아래쪽 방향으로 부딪힘

    elif (cx-gap < X < cx+ca+gap) and (cy-gap < Y< cy+ cb+gap): # 현재 거북이 위치가	 오차를 포함하여 장애물 블록2에 위치하였다면 아래 조건을 미지수로 지정합니다.
        dx1 = X - (cx+ca)#오른쪽 방향으로 부딪힘
        dx2 = X - cx #왼쪽 방향으로 부딪힘
        dy1 = Y - cy #위쪽 방향으로 부딪힘
        dy2 = Y - (cy+cb) #아래쪽 방향으로 부딪힘

    else:                                                       # 현재 거북이 위치가 오차를 포함하여 벽에 위치하였다면 아래 조건을 미지수로 지정합니다.
        dx1 = X - a #오른쪽 방향으로 부딪힘
        dx2 = X + a #왼쪽 방향으로 부딪힘
        dy1 = Y - a #위쪽 방향으로 부딪힘
        dy2 = Y + a #아래쪽 방향으로 부딪힘

    if (-gap < dy1< gap or -gap < dy2< gap) and (-gap < dx1< gap or -gap < dx2 < gap):  # 위에 제시된 조건이 모두 오차내에 있다면 뒤로 돌아 움직인 후 함수 처음으로 돌아갑니다.
        t.lt(180)
        t.fd(10)
        b1()

    q = t.heading()                 # 현재 거북이의 각도를 미지수 q로 지정합니다. 

    if  0<q<90:                     # 거북이의 각도의 범위가 1사분면일 경우, 입사각이 될 가능성이 있는 각 2개를 구합니다. /  ang2가 음수인 이유는 ang1이 45가 될 경우에 ang1과 ang2 두 각도를 구별하기 위해서 입니다.(각도가 45일 경우의 오류 방지)
        ang1 = q
        ang2 = ang1-90
        k = 1
    elif 90<q<180:                  # 거북이의 각도의 범위가 2사분면일 경우, 입사각이 될 가능성이 있는 각 2개를 구합니다.
        ang1 = 180-q
        ang2 = ang1-90
        k = 2
    elif 180<q<270:                  # 거북이의 각도의 범위가 3사분면일 경우, 입사각이 될 가능성이 있는 각 2개를 구합니다.
        ang1 = q-180
        ang2 = ang1-90
        k = 3
    elif 270<q<360:                  # 거북이의 각도의 범위가 4사분면일 경우, 입사각이 될 가능성이 있는 각 2개를 구합니다.
        ang1 = 360-q
        ang2 = ang1-90
        k = 4
    else:                           #거북이의 각도가 직각의 배수일 경우(90, 180, 270, 360) 뒤로 돌아서 함수 처음으로 돌아갑니다.
        t.lt(180)
        b1()


    if -gap < dy1< gap or -gap < dy2< gap :  # 거북이가 부딪힌 방향이 위, 아래일 경우 미지수 ang2가 입사각,반사각이 되기 때문에, 거북이를 ang1의 두배 만큼 돌려줘야 합니다.
        ang = ang1
    elif -gap < dx1< gap or -gap < dx2 < gap:  # 거북이가 부딪힌 방향이 위, 아래일 경우 미지수 ang1가 입사각,반사각이 되기 때문에, 거북이를 ang2의 두배 만큼 돌려줘야 합니다.
        ang = ang2
    else:                                       # 어느 경우도 아닐경우(오차범위를 초과하게 될 경우) 뒤로 돌아서 함수 처음으로 돌아갑니다.
        t.lt(180)
        b1()


    if  k == 1 or k == 3:                   #거북이의 각도가 1,3 사분면에 위치했을 경우 주어진 각도가 무엇이냐에 따라 왼쪽, 오른쪽을 결정합니다.
        if ang == ang1:
            t.right(2*ang)
        elif ang == ang2:
            t.left(2*ang*-1)                #음수였 ang2를 양수로 바꿔줍니다.

    elif k == 2 or k == 4:                   #거북이의 각도가 2,4 사분면에 위치했을 경우 주어진 각도가 무엇이냐에 따라 왼쪽, 오른쪽을 결정합니다.
        if ang == ang1:
            t.left(2*ang)
        elif ang == ang2:
            t.right(2*ang*-1)

    t.forward(5)                            # 거북이를 5 앞으로 움직입니다.
    b1()                                    # 함수 처음으로 돌아갑니다.


t.speed(0)
t.bgcolor("dark green")


a=250                                       #울타리 벽 면적의 기준을 잡을 미지수를 지정합니다.
t.up()
t.goto(-a,-a)
t.down()
t.color("dark green")
t.fillcolor("khaki")
t.begin_fill()
for x in range(4):                              #울타리를 그립니다.
    t.fd(2*a)
    t.left(90)
t.end_fill()


# 장애물 모래 / 속도가 줄어듭니다.
dx = random.randint(-a+100, a-100)
dy = random.randint(-a+100, a-100)
da = random.randint(80, 100)
db = random.randint(80, 100)
t.up()
t.goto(dx, dy)
t.down()

t.color ("orange")
t.begin_fill()
for x in range(2):                              #장애물을 그립니다.
    t.fd(da)
    t.left(90)
    t.fd(db)
    t.left(90)
t.end_fill()

# 장애물 불 / 거북이가 정신없어하다가 밖으로 나옵니다.
ex = random.randint(-a+50, a-50)
ey = random.randint(-a+50, a-50)
ea = random.randint(50, 70)
eb = random.randint(50, 70)
t.up()
t.goto(ex, ey)
t.down()
t.color ("red")
t.begin_fill()
for x in range(2):                              #장애물을 그립니다.
    t.fd(ea)
    t.left(90)
    t.fd(eb)
    t.left(90)
t.end_fill()

# 장애물 블록1 / 벽처럼 부딫칩니다.
bx = random.randint(-a, a)                      #장애물 블록1을 만들기 위한 미지수를 지정합니다.
by = random.randint(-a, a)
ba = random.randint(150, 200)
bb = random.randint(150, 200)
while bx <= 0 <= bx+ba and by <= 0 <= by+ bb:   #만약 블록 영역에 0점이 포함된다면 다시 지정합니다.
    bx = random.randint(0, 200)
    by = random.randint(0, 200)
    ba = random.randint(50, 150)
    bb = random.randint(50, 150)
t.up()
t.goto(bx, by)
t.down()
t.color ("dark green")
t.begin_fill()
for x in range(2):                              #장애물을 그립니다.
    t.fd(ba)
    t.left(90)
    t.fd(bb)
    t.left(90)
t.end_fill()

# 장애물 블록2 / 벽처럼 부딫칩니다.
cx = random.randint(-a, a)                  #장애물 블록1을 만들기 위한 미지수를 지정합니다.
cy = random.randint(-a, a)
ca = random.randint(150, 200)
cb = random.randint(150, 200)
while cx <= 0 <= cx+ca and cy <= 0 <= cy+ cb:   #만약 블록 영역에 0점이 포함된다면 다시 지정합니다.
    cx = random.randint(0, 200)
    cy = random.randint(0, 200)
    ca = random.randint(50, 150)
    cb = random.randint(50, 150)
t.up()
t.goto(cx, cy)
t.down()
t.color ("dark green")
t.begin_fill()
for x in range(2):                              #장애물을 그립니다.
    t.fd(ca)
    t.left(90)
    t.fd(cb)
    t.left(90)
t.end_fill()


t.up()
t.goto(0,0)     
t.color("olive")
t.seth(random.randint(0,360))   #거북이의 각도를 무작위로 배정합니다.
t.down()
t.shape("turtle")               #거북이 모양을 
t.pensize(1)

t.speed(3)  #속도를 3으로 합니다.
b1()        #함수 b1을 실행합니다.
