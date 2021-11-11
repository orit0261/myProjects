import random

import pandas as pd
def move(direction):


def generate_apple():
    pass


class snake_df():
    def __init__(self,x,y):
        self.lis1=list()
        for i in range(1,4):
            for j in range(1,4):
                self.lis1[i][j]=0
        #self.lis1.append([x, y])

    def apple_check(self,x,y):
        if generate_apple(x, y):
            self.lis1[x][y] = 1
            x1 = random.randrange(N, M, step=1)
            y1 = random.randrange(N, M, step=1)
            self.lis1[x1][y1] = 2

        return True

    def move(self,direction):
        if direction=='left':
            if y+1<=N:
              self.apple_check(x,y+1)
              self.lis1[x][y+1]=1
            else:
               return 0

        elif direction=='right':
            if y-1<=N:
              self.apple_check(x,y-1)
              self.lis1[x][y-1]=1
            else:
               return 0

        elif direction=='up':
            if x-1>0:
              self.apple_check(x-1,y)
              self.lis1[x-1][y]=1
            else:
               return 0

        elif direction=='down':
            if x+1<N:
              self.apple_check(x+1,y)
              self.lis1[x+1][y]=1
            else:
               return 0
