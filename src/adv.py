from player import Player
from room import Room
from item import Item
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
name = input('\nWelcome to Adventure game, what shall we call you...? \n\n')


items = {
	"sword": Item("sword", "this is used to stab things"),
	"lantern": Item("Lantern", "this is helpful in the dark"),
	"shovel": Item("shovel", "This could be used to dig"),

 }


room['outside'].items.append(items["Lantern"])
room['overlook'].items.append(items["sword"])
room['narrow'].items.append(items["shovel"])



# Make a new new_player object that is currently in the 'outside' room.
new_player = Player('joe', room['outside'])

# Write a loop that:
# while True:
# * Prints the current room name

# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# CODE
commands = ['n', 's', 'e', 'w']


while commands :
	print(f"Current Location:{new_player.current_room.name}")
	command = input("Choose a direction to move. press q to escape ")
	user_command = command.lower().split(" ")
	if len(user_command) == 1:
		if command == 'n':
			if new_player.current_room.n_to is not False:
				new_player.current_room = new_player.current_room.n_to
			else:
				print("\nSorry, there isn't a room to the North. Please choose another direction.\n")
		elif command == 's':
			if new_player.current_room.s_to is not False:
				new_player.current_room = new_player.current_room.s_to
			else:
				print("\nSorry, there isn't a room to the South. Please choose another direction.\n")
		elif command == 'e':
			if new_player.current_room.e_to is not False:
				new_player.current_room = new_player.current_room.e_to
			else:
				print("\nSorry, there isn't a room to the East. Please choose another direction.\n")
		elif command == 'w':
			if new_player.current_room.w_to is not False:
				new_player.current_room = new_player.current_room.w_to
			else:
				print("\nSorry, there isn't a room to the West. Please choose another direction.\n")
		elif command == 'q':
			 exit(0)
		elif command == "i":
			new_player.print_items()
		else:
			   print("That is not a proper command.")
