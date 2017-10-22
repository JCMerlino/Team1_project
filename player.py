from items import *
from map_new import rooms

# the inventory of physical items the player is carrying
inventory = []

# a list of activities that the player has carried out, similar to inventory for non-physical items
story_progress = []

# Start game at the reception
current_room = rooms["Reception"]