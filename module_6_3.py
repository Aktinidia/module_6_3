class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, _cords, speed):
        _cords = [0, 0, 0]
        self.speed = speed


    def move(self, dx, dy, dz):
        _cords = [self.dx, self.dy, self.dz]
     #  ? где множителем будет являться speed
        if dz < 0:
            print("It's too deep, i can't dive :(")
     # измененния не вносятся

    def get_cords(self)
        print(f'X: {_cords[0]}, Y: {_cords[1]}, Z: <{_cords[1]}')

    def attack(self)
        if _DEGREE_OF_DANGER < 5:
            (print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True 