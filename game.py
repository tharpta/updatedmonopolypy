import die
from player import Player
import board

def game_setup(test):
    """Sets up initial game and creates player objects
    test value can be set to add default game values to make it less annoying to add
    in players and set up a game during testing"""
    players = []
    if test == False:
        num_players = input("How many people will be playing: ")
        num_players = int(num_players)
        while num_players <2 or  num_players > 6:
            num_players = input("Only 2-6 players can join!: ")
            num_players = int(num_players)
        for player in range(num_players):
            print(player)
            player_name = input("what is your name? ")
            players.append(player_name)
    if test == True:
        num_players = 4
        players = ["Tyler","Kanye","Blasto","Luke"]
    players_dict = {name: Player(name=name) for name in players}
    return players_dict
    #for key, value in holder.items():
    #    print(value)
    
def game(players_dict):
    while True:
        for person_key,person_object in players_dict.items():
            if person_object.eliminated == False:
                person_object.roll()
                print(f"{person_key} It is your turn")


    print(players_dict)



if __name__ == '__main__':
    setup = game_setup(test=True)
    game(setup)


    pass



