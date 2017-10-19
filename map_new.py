from items import *
from characters import *

room_stairs1 = {
    "name": "Stairs (First Floor)",

    "description":
    """ words""",

    "exits": {"down": "Stairs2", "west": "Reception"},

    "items": [],

    "NPCs": []
}

room_reception = {
    "name": "Reception",

    "description":
    """ words""",

    "exits": {"north": "Samantha", "south": "Armoury", "east": "Stairs1"},

    "items": [item_usb],

    "NPCs": [Jenifer]
}

room_samantha = {
    "name": "Samantha's Office",

    "description":
    """ words""",

    "exits": {"south": "Reception"},

    "items": [],

    "NPCs": [Samantha]
}

room_armoury = {
    "name": "the Armoury",

    "description":
    """ words""",

    "exits": {"north": "Reception"},

    "items": [],

    "NPCs": []
}


room_stairs2 = {
    "name": "Stairs (Ground Floor)",

    "description":
    """ words""",

    "exits": {"up": "Stairs1", "down": "Stairs3", "west": "Office Debra"},

    "items": [],

    "NPCs": []
}

room_office_debra = {
    "name": "Office (Debra's desk)",

    "description":
    """ words""",

    "exits": {"east": "Stairs2", "south": "Science", "north": "Break"},

    "items": [],

    "NPCs": []
}

room_science = {
    "name": "Science Lab",

    "description":
    """ words""",

    "exits": {"north": "Office Debra", "west": "Storage"},

    "items": [],

    "NPCs": [Stephen]
}

room_break = {
    "name": "the Break Room",

    "description":
    """ words""",

    "exits": {"south": "Office Debra", "west": "Meeting"},

    "items": [],

    "NPCs": [Debra]
}

room_meeting = {
    "name": "the Meeting Room",

    "description":
    """ words""",

    "exits": {"east": "Break", "south": "Office Bob"},

    "items": [],

    "NPCs": [Bob, Alexa]
}

room_office_bob = {
    "name": "Office (Bob's desk)",

    "description":
    """ words""",

    "exits": {"north": "Meeting", "west": "Toilet", "east": "Office Debra", "south": "Storage"},

    "items": [],

    "NPCs": []
}

room_storage = {
    "name": "the Storage Room",

    "description":
    """ words""",

    "exits": {"north": "Office Bob", "east": "Science"},

    "items": [],

    "NPCs": []
}

room_toilet = {
    "name": "the Toilet",

    "description":
    """ words""",

    "exits": {"east": "Office Bob"},

    "items": [],

    "NPCs": []
}

room_stairs3 = {
    "name": "Stairs (the Basement)",

    "description":
    """ words""",

    "exits": {"up": "Stairs2", "west": "Hallway east"},

    "items": [],

    "NPCs": []
}

room_hallway_east = {
    "name": "East Hallway",

    "description":
    """ words""",

    "exits": {"east": "Stairs3", "west": "Hallway west", "north": "Generator"},

    "items": [],

    "NPCs": []
}

room_generator = {
    "name": "Generator Room",

    "description":
    """ words""",

    "exits": {"south": "Hallway east"},

    "items": [],

    "NPCs": []
}

room_computer = {
    "name": "Computer Mainframe",

    "description":
    """ words""",

    "exits": {"south": "Hallway west"},

    "items": [],

    "NPCs": []
}

room_hallway_west = {
    "name": "West Hallway",

    "description":
    """ words""",

    "exits": {"north": "Computer", "east": "Hallway east", "south": "Vault"},

    "items": [],

    "NPCs": []
}

room_vault = {
    "name": "the Vault Room",

    "description":
    """ words""",

    "exits": {"north": "Hallway west"},

    "items": [],

    "NPCs": []
}


rooms = {
    "Stairs1": room_stairs1,  # first floor
    "Samantha": room_samantha,
    "Reception": room_reception,
    "Armoury": room_armoury,
    "Stairs2": room_stairs2,  # ground floor
    "Office Debra": room_office_debra,  # debra's desk
    "Office Bob": room_office_bob,  # bob's desk
    "Break": room_break,
    "Meeting": room_meeting,
    "Science": room_science,
    "Storage": room_storage,
    "Toilet": room_toilet,
    "Stairs3": room_stairs3,  # basement
    "Hallway east": room_hallway_east,
    "Hallway west": room_hallway_west,
    "Generator": room_generator,
    "Computer": room_computer,  # computer mainframe
    "Vault": room_vault,



}
