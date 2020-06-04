# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    """ A class to hold player information,  e.g what room they are in currently"""

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def pickup_item(self, item):
        if self.current_room.items.count(item) > 0:
            self.items.append(item)
            self.current_room.items.remove(item)
            item.pick_up()
    else        
