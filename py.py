import turtle, random, winsound, time, sys

wn = turtle.Screen()
wn.title("SPACE WAR")
wn.bgcolor("black")

wn.setup(1000, 650)


star = turtle.Turtle()
star.shape("triangle")
star.color("white")
star.setheading(90)
star.goto(0, 0)

star1 = turtle.Turtle()
star1.shape("triangle")
star1.color("white")
star1.setheading(-90)
star1.goto(0, 0)


missiles = []


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 475:
            self.rt(60)

        if self.xcor() < -475:
            self.lt(60)

        if self.ycor() > 305:
            self.rt(60)

        if self.ycor() < -305:
            self.lt(60)


    def move_s(self):
        self.fd(self.speed)

        if self.xcor() > 475:
            self.rt(60)

        if self.xcor() < -475:
            self.lt(60)

        if self.ycor() > 305:
            self.rt(60)

        if self.ycor() < -305:
            self.lt(60)

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 2

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 0.5

    def deccelerate(self):
        self.speed -= 0.5

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=0)
        self.speed = 20
        self.status = "ready"
        self.status_two = "ready"

    def fire(self):
        if self.status == "ready":
            winsound.PlaySound("Gun+Shot2.wav", winsound.SND_ASYNC)
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "firing":
            self.fd(self.speed)

        if self.xcor() > 475 or self.xcor() < -475 or self.ycor() > 305 or self.ycor() < -305:
            self.goto(-1000, 1000)
            self.status = "ready"

    def fire2(self):
        if self.status_two == "ready":
            winsound.PlaySound("Gun+Shot2.wav", winsound.SND_ASYNC)
            self.goto(player2.xcor(), player2.ycor())
            self.setheading(player2.heading())
            self.status_two = "firing"

    def move2(self):
        if self.status_two == "firing":
            self.fd(self.speed)

        if self.xcor() > 475 or self.xcor() < -475 or self.ycor() > 305 or self.ycor() < -305:
            self.goto(-1000, 1000)
            self.status_two = "ready"


player = Player("triangle", "white", -250, 0)
player2 = Player("triangle", "white", 250, 0)
missile = Missile("circle", "white", 0, 0)
missile2 = Missile("circle", "white", 0, 0)


turtle.listen()
wn.onkeypress(player.turn_left, "Left")
wn.onkeypress(player.turn_right, "Right")
wn.onkeypress(player.accelerate, "Up")
wn.onkeypress(player.deccelerate, "Down")

wn.onkeypress(player2.turn_left, "a")
wn.onkeypress(player2.turn_right, "d")
wn.onkeypress(player2.accelerate, "w")
wn.onkeypress(player2.deccelerate, "s")

wn.onkeypress(missile.fire, "space")
wn.onkeypress(missile2.fire2, "q")

player2.setheading(-180)

player_lives = 3
player2_lives = 3

lives_pen = turtle.Turtle()
lives_pen.hideturtle()
lives_pen.penup()
lives_pen.color("white")
lives_pen.goto(-450, 270)
lives_pen.write("Player 1 Lives: " + str(player_lives), align="left", font = ("arial", 20, "bold"))

two_lives_pen = turtle.Turtle()
two_lives_pen.hideturtle()
two_lives_pen.penup()
two_lives_pen.color("white")
two_lives_pen.goto(250, 270)
two_lives_pen.write("Player 2 Lives: " + str(player_lives), align="left", font = ("arial", 20, "bold"))

win_pen = turtle.Turtle()
win_pen.hideturtle()
win_pen.penup()
win_pen.color("white")
win_pen.goto(0, 250)



game_over = False
while not game_over:
    player.move()
    player2.move_s()
    missile.move()
    missile2.move2()

    if player_lives <= 0:
        win_pen.write("Player 2 Wins!", align="center", font=("arial", 20, "bold"))
        time.sleep(3)
        sys.exit()

    if player2_lives <= 0:
        win_pen.write("Player 1 Wins!", align="center", font=("arial", 20, "bold"))
        time.sleep(3)
        sys.exit()

    if player2.distance(star1) < 20:
        missile2.goto(-1000, 1000)
        missile2.status = "ready"

        player2.goto(0, 0)

        player2.goto(random.randint(100, 300), random.randint(-4, 200))

        player2_lives -= 1


        two_lives_pen.clear()
        two_lives_pen.goto(250, 270)
        two_lives_pen.write("Player 2 Lives: " + str(player2_lives), align="left", font=("arial", 20, "bold"))

    if player.distance(star1) < 20:
        missile.goto(-1000, 1000)
        missile.status = "ready"

        player.goto(0, 0)

        player.goto(random.randint(-300, -100), random.randint(-100, 100))

        player_lives -= 1


        lives_pen.clear()
        lives_pen.goto(-450, 270)
        lives_pen.write("Player 1 Lives: " + str(player_lives), align="left", font=("arial", 20, "bold"))

    if missile2.distance(player) < 20:

        player_lives -= 1

        missile2.goto(-1000, 1000)
        missile2.status = "ready"


        winsound.PlaySound("Explosion+1.wav", winsound.SND_ASYNC)

        lives_pen.clear()
        lives_pen.goto(-450, 270)
        lives_pen.write("Player 1 Lives: " + str(player_lives), align="left", font=("arial", 20, "bold"))


    if missile.distance(player2) < 20:

        player2_lives -= 1

        missile.goto(-1000, 1000)
        missile.status = "ready"

        winsound.PlaySound("Explosion+1.wav", winsound.SND_ASYNC)

        two_lives_pen.clear()
        two_lives_pen.goto(250, 270)
        two_lives_pen.write("Player 2 Lives: " + str(player2_lives), align="left", font=("arial", 20, "bold"))


wn.mainloop()