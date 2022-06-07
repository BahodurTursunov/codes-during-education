import random


class Function:
    def __init__(self, state):
        self.per = state
    def change_state(self):
        while self.per != "\nБежать домой":
            print(self.per)
            random_state = random.randint(0, 2)
            rabbit = random.random()
            if random_state == 0:
                self.per = "\nПоиск добычи"
                print(self.per)
            if random_state == 1:
                self.per = "\nВыследить добычу"
                print("\nДобыча найдена", self.per)
                #if random_state > 0.6:

                print("rabbit_1 = " + str(rabbit_1.escape))
                print("rabbit = " + str(rabbit))

                if rabbit_1.escape > rabbit:
                    self.per = "\nПоиск добычи"
                    print("\nДобыча найдена", round(rabbit_1.escape, 3), round(rabbit, 3), "\nПоиск добычи")
                else:
                    self.per = "\nАтака"
                    print("\nДобыча найдена", round(rabbit, 3), self.per)
                    self.per = "\nБежать домой"
                    print("\nДобыча найдена", self.per)
                #else:
                    #continue
            elif random_state == 2:
                self.per = "\nУбежать от врага"
                print("\nЕсть враг", self.per)
class Fun_Rabbit:
    def __init__(self, escape):
        self.escape = escape
tiger = Function("\nПоиск добычи")
rabbit = random.random()
rabbit_1 = Fun_Rabbit(rabbit)
tiger.change_state()