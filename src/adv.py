from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new new_player object that is currently in the 'outside' room.
new_player = Player('joe', room['outside'])
# Write a loop that:
#
# * Prints the current room name
print(f"Current Location:{new_player.current_room.name}")
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
command = ''
while command != 'q':
    command = input("Choose a direction to move . Enter n, s, e, or w:")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#CODE
directions = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}

while true:
	  print(str(new_player.current_room))
      choice = input("Which way, Gandalf? ")

	direction = directions[choice]

	try:
		# if command == 'n':
		# 	if new_player.current_room.n_to:
		# 		new_player.current_room = new_player.current_room.n_to
		# 	else:
		# 		print("Sorry, there isn't a room to the North. Please choose another direction.")
		# elif command == 's':
		# 	if new_player.current_room.s_to:
		# 		new_player.current_room = new_player.current_room.s_to
		# 	else:
		# 		print("Sorry, there isn't a room to the South. Please choose another direction.")
		# elif command == 'e':
		# 	if new_player.current_room.e_to:
		# 		new_player.current_room = new_player.current_room.e_to
		# 	else:
		# 		print("Sorry, there isn't a room to the East. Please choose another direction.")
		# elif command == 'w':
		# 	if new_player.current_room.w_to:
		# 		new_player.current_room = new_player.current_room.w_to
		# 	else:
		# 		print("Sorry, there isn't a room to the West. Please choose another direction.")
		# elif command == 'q':
		# 	exit(0)
	player.current_room = getattr(player.current_room, direction)
    
    except AttributeError:
		print("Sorry, no room in that direction. Please choose another direction.")