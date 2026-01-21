import random as r

class Numbers():
    def __init__(self):
        self.numbers = []
        self.final_num = ""

    def generator(self):
        for n in range(1,7):
            okey= r.randint(0,9)
            self.numbers.append(okey)
        for n in self.numbers:
            n = str(n)
            self.final_num+=n
        return self.final_num        
