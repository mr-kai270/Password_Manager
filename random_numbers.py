import random as r

class Numbers():
    def __init__(self):
        self.numbers = []

    def generator(self):
        for n in range(1,7):
            okey= r.randint(0,9)
            self.numbers.append(okey)
        print(self.numbers)

okey =Numbers()
print(okey.generator())