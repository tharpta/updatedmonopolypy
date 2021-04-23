import random
class Player:
    """A player"""
    def __init__(self, name, bank=1700, pos=0):
        self.name = name
        self.bank = bank
        self.pos = 0 
        self.eliminated = False
        self.jailed = False


    def __repr__(self):
        """repr is used to compute the 'official' string representation of an object.
        if I comment this out it will show the memory location of the object. 
        """
        return self.name
    def roll(self):
        """rolls number and keeps track of doubles"""
        doubles_count = 0
        while doubles_count <=2:
            num1 = random.randint(1,6)
            num2 = random.randint(1,6)
            die_total = num1 + num2
            if num1 != num2 and self.jailed == False:
                self.move(die_total)
                break
            if num1 == num2:
                print("doubles")
                doubles_count +=1
            if doubles_count >2:
                print("go to jail")
                self.go_to_jail()
    def move(self, die_total):
        """moves player"""
        if self.pos < 40:
            self.pos += die_total
        if self.pos >= 40:
            self.pos = self.pos - 40
        print(f"{self.name} is at {self.pos}")
        return die_total

    def go_to_jail(self):

        print("you are in jail")
        self.pos = 10

    def buy_property(self, bank):
        pass
    def trade(self):
        pass



    
        #self.properties_owned = []
        #self.eliminated = False
    

