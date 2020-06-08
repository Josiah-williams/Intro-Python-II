# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """ A class to hold room information.""" 
    def __init__(self, name, description  ):
        self.name = name
        self.description = description
        self.n_to = False
        self.s_to = False
        self.e_to = False
        self.w_to = False
def __str__(self):
        return f"Room name :{self.name}, Room description: {self.description}"