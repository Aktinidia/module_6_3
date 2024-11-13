class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrrr'


    def run(self, dx):
        self.x_distance += dx

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self.y_distance += dy

class Pegasus(Horse, Eagle):
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

       # super().run(10)
        # super().fly(10)

    def move(self, dx, dy):
        super().__init__(self.dx, self.dy)
        super().run(10)
        super().fly(10)

    def get_pos(self):
        return (self.x_distance, self.y_distance)


    def voice(self):
        print(self.sound)


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
