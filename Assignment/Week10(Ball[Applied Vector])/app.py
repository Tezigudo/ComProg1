import random
import time

from ball import Ball
from border import Border
from stage import Stage
from vector import Vector

TIME_STEP = 0.01
NUM_BALLS = 10
STAGE_WIDTH = 10
STAGE_HEIGHT = 10
COLORS = ["green", "red", "black", "blue", "purple"]

border = Border(Vector(0, 0), width=STAGE_WIDTH, height=STAGE_HEIGHT)
stage = Stage(border)
stage.init_screen()
for _ in range(NUM_BALLS):
    # random a position inside the stage area
    pos = Vector(random.randint(0, STAGE_WIDTH),
                 random.randint(0, STAGE_HEIGHT))

    # random velocity between -10 to 10 on each axis
    vel = Vector(random.random() * 20 - 10,
                 random.random() * 20 - 10)

    # use the acceleration of the earth's gravity
    acc = Vector(0, -9.8)

    ball = Ball(pos=pos, vel=vel, acc=acc)
    ball.color = random.choice(COLORS)
    stage.add_ball(ball)

while True:
    timestamp = time.time()
    stage.update(TIME_STEP)
    stage.render()
    # maintain the delay that makes each frame rendered at every TIME_STEP
    time.sleep(max(0, TIME_STEP - (time.time() - timestamp)))
