import random


class zombieSalyer:
    def __init__(self):
        print('zombie salyer created!')
        self.power = "MAX"

    def slay(self, zombie):
        zombie.injured()


class zombiee:
    aliveCounter = 0

    def __init__(self):
        zombiee.aliveCounter += 1
        self.isAlive = True
        self.Power = random.randint(1, 5)
        print(f'zombiee created! Ready to eat you brain {zombiee.aliveCounter} zombies')

    def get_power(self):
        return self.Power

    def injured(self):
        if self.isAlive:
            self.Power -= 1

        if self.Power < 1:
            self.die()
        else:
            print('zombiee power left', "*" * self.Power)

    def die(self):
        if self.isAlive: self.isAlive = False
        self.Power=0
        zombiee.aliveCounter-=1

        if zombiee.aliveCounter>0:
            print(f'zomibee teminated, {zombiee.aliveCounter} left alive')
        else:
            print('YOU WON!')

    def __del__(self):
        print(f'{self} OBJ collection to the void')


s1 = zombieSalyer()
z1 = zombiee()
z2 = zombiee()
while z1.get_power() > 0:
    s1.slay(z1)
while z2.get_power() > 0:
    s1.slay(z2)

del z1
del z2
