class Horse:
    # x_distance = 0
    # sound = 'Frrr'
    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'
        print('Инит лошади')
        super().__init__()

    def run(self, dx):
        self.x_distance += dx

class Eagle:
    # y_distance = 0
    # sound = 'I train, eat, sleep, and repeat'
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        print('Инит орла')

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)
    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


print(Pegasus.mro())
# nice_horse=Horse()
# nice_horse.run(5)
# nice_horse.run(4)
#
# strong_eagle = Eagle()
# strong_eagle.fly(7)
# strong_eagle.fly(2)
#


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
#
p1.voice()