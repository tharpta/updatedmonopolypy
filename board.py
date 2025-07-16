class Property:
    """Property object"""
    def __init__(self, name, grouping, position, price, rent_tiers, owner, mortgaged):
        self.name = name
        self.grouping = grouping
        self.position = position
        self.price = price
        self.rent_tiers = rent_tiers
        self.owner = owner
        self.mortgaged = mortgaged
    def rent_calc(self):
        """Calculates rent"""
        if self.owner != None and self.mortgaged != None:
            if self.grouping == 'utility':
                pass
            if self.grouping == 'railroad':
                pass
            else:
                pass
        else:
            pass
    def purchase(self, buyer):
        
    def improve(self):
        """Add house/hotel"""
        pass
    def unimprove(self):
        """Sell house/hotel"""
        pass
    def mortgage(self):
        """mortgage property"""
        pass
    def unmmortgage(self):
        """unmortgage property"""
        pass
    


class Event:
    "Chance/Community Chest/ Go to Jail/ Free Parking/tax spots/visiting"
    def __init__(self,name,position,action):
        self.name = name
        self.position = position
        self.action = action


# baltic = Property("Baltic Avenue","purple",3,60,[4,20,60,180,320,450],None,False)
# baltic.owner = "tyler"
# print(baltic.rent_calc())
# print(baltic.owner)

#Purple Properties
mediterranean_avenue = Property("Mediterranean Avenue", "brown", 1, 60, [2, 10, 30, 90, 160, 250], None, False)
baltic_avenue = Property("Baltic Avenue", "brown", 3, 60, [4, 20, 60, 180, 320, 450], None, False)

# Light Blue Properties
oriental_avenue = Property("Oriental Avenue", "light_blue", 6, 100, [6, 30, 90, 270, 400, 550], None, False)
vermont_avenue = Property("Vermont Avenue", "light_blue", 8, 100, [6, 30, 90, 270, 400, 550], None, False)
connecticut_avenue = Property("Connecticut Avenue", "light_blue", 9, 120, [8, 40, 100, 300, 450, 600], None, False)

# Pink Properties
st_charles_place = Property("St. Charles Place", "pink", 11, 140, [10, 50, 150, 450, 625, 750], None, False)
electric_company = Property("Electric Company", "utility", 12, 150, [4, 10], None, False)  # Utility rent is 4x or 10x dice roll
states_avenue = Property("States Avenue", "pink", 13, 140, [10, 50, 150, 450, 625, 750], None, False)
virginia_avenue = Property("Virginia Avenue", "pink", 14, 160, [12, 60, 180, 500, 700, 900], None, False)

# Railroads
pennsylvania_railroad = Property("Pennsylvania Railroad", "railroad", 5, 200, [25, 50, 100, 200], None, False)
reading_railroad = Property("Reading Railroad", "railroad", 15, 200, [25, 50, 100, 200], None, False)
bo_railroad = Property("B&O Railroad", "railroad", 25, 200, [25, 50, 100, 200], None, False)
short_line = Property("Short Line", "railroad", 35, 200, [25, 50, 100, 200], None, False)

# Orange Properties
st_james_place = Property("St. James Place", "orange", 16, 180, [14, 70, 200, 550, 750, 950], None, False)
tennessee_avenue = Property("Tennessee Avenue", "orange", 18, 180, [14, 70, 200, 550, 750, 950], None, False)
new_york_avenue = Property("New York Avenue", "orange", 19, 200, [16, 80, 220, 600, 800, 1000], None, False)

# Red Properties
kentucky_avenue = Property("Kentucky Avenue", "red", 21, 220, [18, 90, 250, 700, 875, 1050], None, False)
indiana_avenue = Property("Indiana Avenue", "red", 23, 220, [18, 90, 250, 700, 875, 1050], None, False)
illinois_avenue = Property("Illinois Avenue", "red", 24, 240, [20, 100, 300, 750, 925, 1100], None, False)

# Yellow Properties
atlantic_avenue = Property("Atlantic Avenue", "yellow", 26, 260, [22, 110, 330, 800, 975, 1150], None, False)
ventnor_avenue = Property("Ventnor Avenue", "yellow", 27, 260, [22, 110, 330, 800, 975, 1150], None, False)
water_works = Property("Water Works", "utility", 28, 150, [4, 10], None, False)  # Utility rent is 4x or 10x dice roll
marvin_gardens = Property("Marvin Gardens", "yellow", 29, 280, [24, 120, 360, 850, 1025, 1200], None, False)

# Green Properties
pacific_avenue = Property("Pacific Avenue", "green", 31, 300, [26, 130, 390, 900, 1100, 1275], None, False)
north_carolina_avenue = Property("North Carolina Avenue", "green", 32, 300, [26, 130, 390, 900, 1100, 1275], None, False)
pennsylvania_avenue = Property("Pennsylvania Avenue", "green", 34, 320, [28, 150, 450, 1000, 1200, 1400], None, False)

# Dark Blue Properties
park_place = Property("Park Place", "dark_blue", 37, 350, [35, 175, 500, 1100, 1300, 1500], None, False)
boardwalk = Property("Boardwalk", "dark_blue", 39, 400, [50, 200, 600, 1400, 1700, 2000], None, False)

board = [
    Event("GO", 0, "collect_200"),
    mediterranean_avenue,
    Event("Community Chest", 2, "draw_card"),
    baltic_avenue,
    Event("Income Tax", 4, "pay_200"),
    pennsylvania_railroad,
    oriental_avenue,
    Event("Chance", 7, "draw_card"),
    vermont_avenue,
    connecticut_avenue,
    Event("Jail/Just Visiting", 10, "jail"),
    st_charles_place,
    electric_company,
    states_avenue,
    virginia_avenue,
    reading_railroad,
    st_james_place,
    Event("Community Chest", 17, "draw_card"),
    tennessee_avenue,
    new_york_avenue,
    Event("Free Parking", 20, "free_parking"),
    kentucky_avenue,
    Event("Chance", 22, "draw_card"),
    indiana_avenue,
    illinois_avenue,
    bo_railroad,
    atlantic_avenue,
    ventnor_avenue,
    water_works,
    marvin_gardens,
    Event("Go to Jail", 30, "go_to_jail"),
    pacific_avenue,
    north_carolina_avenue,
    Event("Community Chest", 33, "draw_card"),
    pennsylvania_avenue,
    short_line,
    Event("Chance", 36, "draw_card"),
    park_place,
    Event("Luxury Tax", 38, "pay_75"),
    boardwalk
]