import turtle
import os
import math

#set up screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300) #starting point
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600) #forward 600
    border_pen.lt(90)  #left 90
border_pen.hideturtle()

#create player turtle
player = turtle.Turtle()
player.color("yellow")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Move left and right
def move_left():
  x = player.xcor()
  x -= playerspeed
  if x < -280:
    x = -280
  player.setx(x)

def move_right():
  x = player.xcor()
  x -= playerspeed
  if x < -280:
    x = -280
  player.setx(x)

def fire_bullet():
  #make bullet more dynamic to be changable
  global bulletstate
  if bulletstate == "ready":
    #bullet just above player
    x = player.xcor()
    y = player.ycor()+10
    bullet.setposition(x, y)
    bullet.showturtle()
def isCollision(t1, t2):
  distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
  if distance < 15:
    return True
  else:
    return False


#Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

#Enemies
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, -250)

enemyspeed = 2

#player bullets
bullet = turtle.Turtle()
bullet.color("green")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.6, 0.6)

bullet.hideturtle()


bulletspeed = 20
#bullet ready to fire
bulletstate = "ready"

#game
while True;
  
  #move the enemy
  x = enemy.xcor()
  x -= enemyspeed
  enemy.setx(x)

  #restrick enemy
  if enemy.xcor() > 280:
    y = enemy.ycor()
    y -=30
    enemyspeed *= -1
    enemy.sety(y)

  if enemy.xcor() > -280:
    y = enemy.ycor()
    y -=30
    enemyspeed *= -1  
    enemy.sety(y)

  #move the bullet
  if bulletstate == "fire":
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

  #bullet reach border
  if bullet.ycor() > 280;
    bullet.hideturtle()
    bulletstate = "ready"

  #check collision with enemy
  if isCollision(bullet, enemy):
    bullet.hideturtle()
    bulletstate = "ready"
    bullet.setpoint(0, -400)
    #reset enemy
    enemy.setposition(-200, 250)

  #enemy hit player
  if isCollision(player, enemy):
    player.hideturtle()
    enemy.hideturtle()
    print ("Game Over")
    break
delay = raw_input("Press enter to finish.")
