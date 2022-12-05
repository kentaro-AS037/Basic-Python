class Dice():

    def __init__(self):
        self.number = [i for i in range(6)]
    
    def set_number(self,n0,n1,n2,n3,n4,n5):
        self.number[0] = n0
        self.number[1] = n1
        self.number[2] = n2
        self.number[3] = n3
        self.number[4] = n4
        self.number[5] = n5
    
    def rolling(self,loc):

        if loc == 'E':
            self.set_number(self.number[3],self.number[1],self.number[0],self.number[5],self.number[4],self.number[2])
        elif loc == 'N':
            self.set_number(self.number[1],self.number[5],self.number[2],self.number[3],self.number[0],self.number[4])
        elif loc == 'S':
            self.set_number(self.number[4],self.number[0],self.number[2],self.number[3],self.number[5],self.number[1])
        elif loc == 'W':
            self.set_number(self.number[2],self.number[1],self.number[5],self.number[0],self.number[4],self.number[3])
    
    def show_top(self):
        return self.number[0]

dice = Dice()
set_list = list(map(int,input().split()))
dice.set_number(set_list[0],set_list[1],set_list[2],set_list[3],set_list[4],set_list[5])
set_loc = str(input())
for a in set_loc:
    dice.rolling(a)

print(dice.show_top())