import die
from player import Player
import board


def set_num_players():
    num_players = input("How many people will be playing: ")
    num_players = int(num_players)
    while num_players <2 or  num_players > 6:
        num_players = input("Only 2-6 players can join!: ")
        num_players = int(num_players)
    return num_players

def set_player_names(num_players):
    players = []
    for player in range(num_players):
        print(player)
        player_name = input("What is your name? ")
        players.append(player_name)
    return players

def set_income_tax():
    income_tax = input("How much money should be in income tax? ")
    income_tax = int(income_tax)
    return income_tax

def set_free_parking_amount():
    free_parking = input("How much money should be in free parking? ")
    free_parking = int(free_parking)
    return free_parking

def game_setup(test):
    """Sets up initial game and creates player objects
    test value can be set to add default game values to make it less annoying to add
    in players and set up a game during testing"""
    if test == False:
        num_players = set_num_players()
        players = set_player_names(num_players)
    if test == True:
        num_players = 4
        players = ["Tyler","Pepper","Blasto","Luke"]
    players_dict = {name: Player(name=name) for name in players}
    income_tax = set_income_tax()
    free_parking = set_free_parking_amount()
    return players_dict, income_tax, free_parking

def get_action():
    action = input("What would you like to do? ")
    if action not in ['roll','buy','trade','mortgage','unmortgage','improve','unimprove','bankrupt','end turn','help']:
        print("Invalid action, try again")
        get_action()
    return action

def game(players_dict, income_tax, free_parking):
    players = list(players_dict.keys())
    while True:
        for person_key,person_object in players_dict.items():
            if len(players) ==1:
                return 0
            if person_object.eliminated == False and len(players)>1:
                print(f"{person_key} It is your turn")
                turn_active = True
                #TODO: Add option to see bank balance and properties make it so user has to roll first based on rules.
                while turn_active == True:
                    action = get_action()
                    if action == 'roll':
                        person_object.roll()
                    if action == 'buy':
                        person_object.buy_property()
                    if action == 'trade':
                        person_object.trade()
                    if action == 'mortgage':
                        person_object.mortgage()
                    if action == 'unmortgage':
                        person_object.unmortgage()
                    if action == 'improve':
                        person_object.improve()
                    if action == 'unimprove':
                        person_object.unimprove()  
                    if action == 'bankrupt':
                        person_object.bankrupt()
                        turn_active = False
                        players.remove(person_key)
                    if action == 'end turn':
                        turn_active = False
                    if len(players) == 1:
                        print(f"{players[0]} has won the game!")
                        return 0

if __name__ == '__main__':
    replay = "yes"
    while replay == "yes":
        setup = game_setup(test=True)
        game(setup)
        replay = input("Play again? ")
    if replay == "no":
        print("Game over.")