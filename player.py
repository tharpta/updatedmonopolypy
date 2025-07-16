import random
from board import board
class Player:
    """A player"""
    def __init__(self, name, bank=1700, pos=0):
        self.name = name
        self.bank = bank
        self.pos = 0
        self.eliminated = False
        self.properties_owned = []

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
            print(f"{self.name} rolled {die_total}")
            if num1 != num2:
                self.move(die_total)
                break
            if num1 == num2:
                print(f"{self.name} rolled doubles!")
                doubles_count +=1
            if doubles_count >2:
                print(f"Slow down {self.name}! You rolled 3 doubles in a row! GO TO JAIL!")
                self.go_to_jail()
    
    def move(self, die_total):
        """moves player"""
        if self.pos < 40:
            self.pos += die_total
        if self.pos >= 40:
            self.pos = self.pos - 40
        print(f"{self.name} is at {board[self.pos].name}")
        return die_total

    def go_to_jail(self):
        print("you are in jail")
        self.pos = 10

    def buy_property(self, bank):
        #TODO: Make error handling more robust for each edge case
        if board[self.pos].owner == None and self.bank >= board[self.pos].price:
            board[self.pos].owner = self.name
            self.bank -= board[self.pos].price
            self.properties_owned.append(board[self.pos].name)
        else:
            print("Unable to purchase property")
    def trade(self):
        pass



    
        #self.properties_owned = []
        #self.eliminated = False
    
    def bankrupt(self):
        self.eliminated = True
        print(f"{self.name} has gone bankrupt and is eliminated from the game")
        return self.eliminated

