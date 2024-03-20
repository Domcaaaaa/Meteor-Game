import play
import random
width = 400
height = 300
character = play.new_image(
        image='space.jpg', 
        x=0, 
        y=0, 
        angle=0, 
        size=200, 
        transparency=100
    )



GO=play.new_text("Game Over", font_size= 90)
Q=play.new_text("stiskni q pro reset", font_size= 45, y= -100)

box = play.new_image(
        image='spaceship.png',
        x=0,
        y=-250,
        size = 20,
    )




ball = [
    play.new_image(y = random.randint(height, 600),x = random.randint(-width,width), image='meteor.png', size = random.randint(10,50)),
    play.new_image(y = random.randint(height, 600),x = random.randint(-width,width),  image='meteor.png', size = random.randint(10,50)),
    play.new_image(y = random.randint(height, 600),x = random.randint(-width,width),  image='meteor.png', size = random.randint(10,50)),
    play.new_image(y = random.randint(height, 600),x = random.randint(-width,width),  image='meteor.png', size = random.randint(10,50)),
    play.new_image(y = random.randint(height, 600),x = random.randint(-width,width),  image='meteor.png', size = random.randint(10,50))
]

   
score = 0
scoreboard =play.new_text(str(score) , font_size= 35, y = 200 , x = -300)

def falling():
    global score
    global scoreboard
    i = 0
    speed = 5 + score/10
    while i < len(ball):
        if ball[i].y > -height:
            ball[i].y += -speed
            ball[i].turn(175)
        if ball[i].y <= -height:
            ball[i].y = height
            ball[i].x = random.randint(-width,width)
            ball[i].y = random.randint(height, 600)
            score += 1
            scoreboard.words = str(score)
            ball[i].radius = random.randint(5, 20)
        i += 1
        speed += 1
        

def restart():
    global score
    GO.hide()
    Q.hide()
    i = 0
    score = 0
    scoreboard.words = str(score)
    while i < len(ball):
        ball[i].x = random.randint(-width,width)
        ball[i].y = random.randint(height, 600)
        i += 1
 

def movement():
    global score
    if box.x < width : 
        if play.key_is_pressed('d'):
                box.x += +5
    if box.x > -width :
        if play.key_is_pressed('a'):
            box.x = box.x - 5


def gameover():
    GO.show()
    Q.show()

@play.repeat_forever
def game_loop():
    i = 0
    o = 0
    while i < len(ball) :
        if ball[i].is_touching(box):
            gameover()
            o = 1    
        i += 1  
    if o == 0:
        movement()
        falling()   
    if play.key_is_pressed('q'):
        restart()   

play.start_program()