from ball import Ball
from vector import Vector


def main():
    """
    This function run an entire program
    """
    step = float(input('Enter the time step in seconds: '))
    duration = float(input('Enter the time limit in seconds: '))
    pos_coor = input("Enter the ball's initial position vector (x,y): ")
    vel_coor = input("Enter the ball's initial velocity vector (x,y): ")
    acc_coor = input("Enter the ball's acceleration vector (x,y): ")
    # unpack the coordinate and map it into float then make it into vector object
    pos = Vector(*map(float, pos_coor.split(',')))
    vel = Vector(*map(float, vel_coor.split(',')))
    acc = Vector(*map(float, acc_coor.split(',')))

    ball = Ball(pos, vel, acc)

    time = 0
    while round(time, 2) < duration:
        '''
        loop untill time more than the duration
        '''
        # ball.show_time_pos_vel(time)
        print(
            f"Time={time:.2f} sec, pos=({self.pos.x:.2f},{self.pos.y:.2f}), vel=({self.vel.x:.2f},{self.vel.y:.2f})")

        ball.update(step)
        time += step


if __name__ == '__main__':
    main()
