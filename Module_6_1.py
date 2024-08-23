class Animal:
    def __init__(self, name, alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name
    def eat(self, food):
        if food.edable == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Plant:
    def __init__(self, name, edable=False):
        self.edable = edable
        self.name = name

class Mammal(Animal):
    pass


class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name, edable=False):
        self.edable=True
        self.name=name


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name) # Волк
print(p1.name) # Цветик семицветик
print(a2.name) # Хатико
print(p2.name) # апельсин

print(a1.alive) # волк живой True
print(a2.fed)   # Хатико сытый - False
a1.eat(p1)      # волк ест цветик
a2.eat(p2)      # хатико ест апельсин
print(a1.alive) # волк умер
print(a2.fed)   # хатико должен быть сыт