from items import *

room_Stairs1 = {
    "name": "Stairs (First Floor)",

    "description":
#insert description

    "exits": {"down": "Stairs2", "west": "Reception"},

    "items": []
}

room_reception = {
    "name": "Reception",

    "description":
#insert description

    "exits":  {"north": "Mallory", "south": "Armory", "east": "Stairs1"},

    "items": []
}

room_stairs2 = {
    "name": "Stairs (Ground Floor)",

    "description":
#insert description

    "exits": {"up": "Stairs1", "down": "Stairs3", "west": "Office Pam"},

    "items": []
}

room_office_pam = {
    "name": "Office (Pam's desk)",

    "description":
#insert description

    "exits": {"east": "Stairs2", "south": "Science", "north": "Break"},

    "items": []
}

room_science = {
    "name": "Science Lab",

    "description":
#insert description

    "exits": {"north": "Office Pam", "west": "Storage"},

    "items": []
}

room_break = {
    "name": "the Break Room",

    "description":
#insert description

    "exits": {"south": "Office Pam", "west": "Meeting"},

    "items": []
}

room_meeting = {
    "name": "the Meeting Room",

    "description":
#insert description

    "exits": {"east": "Break", "south": "Office Cyril"},

    "items": []
}

room_office_cyril = {
    "name": "Office (Cyril's desk)",

    "description":
#insert description

    "exits": {"north": "Meeting", "west": "Toilet", "east": "Office Pam", "south": "Storage"},

    "items": []
}

room_storage = {
    "name": "the Storage Room",

    "description":
#insert description

    "exits": {"north": "Office Cyril", "east": "Science"},

    "items": []
}

room_toilet = {
    "name": "the Toilet",

    "description":
#insert description

    "exits": { "east": "Office Cyril"},

    "items": []
}

room_stairs3 = {
    "name": "Stairs (the Basement)",

    "description":
#insert description

    "exits": {"up": "Stairs2", "west": "Hallway east"},

    "items": []
}

room_hallway_east = {
    "name": "East Hallway",

    "description":
#insert description

    "exits": {"east": "Stairs3", "west": "Hallway west", "north": "Generator"},

    "items": []
}

room_generator = {
    "name": "Generator Room",

    "description":
#insert description

    "exits": {"south": "Hallway east", "west": "Computer"},

    "items": []
}

room_computer = {
    "name": "Computer Mainframe",

    "description":
#insert description

    "exits": {"east": "Generator", "south": "Hallway west"},

    "items": []
}

room_hallway_west = {
    "name": "West Hallway",

    "description":
#insert description

    "exits": {"up": "Computer", "east": "Hallway east", "south": "Vault"},

    "items": []
}




rooms = {
    "Stairs1": room_stairs1, #first floor
    "Mallory": room_mallory,
    "Reception": room_reception,
    "Armory": room_armory,
    "Stairs2": room_stairs2, #ground floor
    "Office Pam": room_office_pam, #pam's desk
    "Office Cyril": room_office_cyril, #cryril's desk
    "Break": room_break,
    "Meeting": room_meeting,
    "Science": room_science,
    "Storage": room_storage,
    "Toilet": room_toilet,
    "Stairs3": room_stairs3, #basement
    "Hallway east": room_hallway_east,
    "Hallway west": room_hallway_west,
    "Generator": room_generator,
    "Computer": room_computer, #computer mainframe
    "Vault": room_vault,



}
