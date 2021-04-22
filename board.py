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


baltic = Property("Baltic Avenue","purple",1,60,[4,20,60,180,320,450],None,False)
baltic.owner = "tyler"
print(baltic.rent_calc())
print(baltic.owner)
