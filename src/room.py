# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    """ A class to hold room information.""" 
    def __init__(self, name, desc, n_to, e_to, s_to, w_to ):
        self.name = name
        self.desc = desc
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
	