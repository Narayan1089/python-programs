# 1 batsmen, 1 innings, 1 batsmen -3 total_ballss,  random from 3 total_ballss 18 balls -
# any of the ball the batsmen gets wide or no ball, 1 extra ball and 1 extra run if wide or no ball. Total number of runs.


import random


class Cricket:
    total_balls = 18
    total_run = 0
    wide = ''
    no_ball = ''
    runs = [0, 1, 2, 3, 4, 5, 6, wide, no_ball]

    # print(random_run)
    for i in range(1, total_balls):
        random_run = random.choice(runs)
        if random_run == wide or no_ball:
            total_run = total_run+1
            total_balls = total_balls+1
        else:
            total_run = total_run+random_run
    print('Total balls:', total_balls)
    print('Total runs:', total_run)
