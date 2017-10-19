from items import *
from characters import *

room_stairs1 = {
    "name": "Stairs (First Floor)",

    "description":
    """Stairs that lead from the first floor to the ground floor.""",

    "inspection":
    """We have millions of pounds in funding but we can't afford an elevator. Stairs are physically traumatic and worse, these stairs lead to the ground floor offices
where all the underlings scurry about.""",

    "exits": {"down": "Stairs2", "west": "Reception"},

    "items": [],

    "NPCs": []
}

room_reception = {
    "name": "Reception",

    "description":
    """Jenifer's office outside outside of Samantha's Office. Jenifer is sitting at her desk.""",

    "inspection":
    """Jenifer's office? I didn't think she got paid enough to earn herself an office. She has a lousy desk and a lousy computer. Not that she even uses them. She's also put her makeup everywhere. Does she actually work? 
Who knows... She's currently pretending to do something on the computer. Probably playing some stupid game to pass the time. What else is here... waste bin, fan, potted plant, window... yeah nothing else of importance.""",

    "exits": {"north": "Samantha", "south": "Armoury", "east": "Stairs1"},

    "items": [item_usb],

    "NPCs": [Jenifer]
}

room_samantha = {
    "name": "Samantha's Office",

    "description":
    """The Boss' office is large and filed with custom made furniture and has expensive carpet. The first floor windows provide natural lighting and a view over the street below. Samantha is sitting at her desk.""",

    "inspection":
    """Samantha's Office... The place where paychecks are crushed and lives are disregarded. Her large desk is shadowed only by her larger bookcase, probably compensating for her failing secret service. 
The computer is heavily used as shown by her sixth replacement keyboard this week and the secret alcohol stash is always hidden under her desk but it's not exactly a secret though. 
Her window has the lamest view of city life possible. Who actually wants to look outside and see depressed city workers going about their daily buisiness? 
Two chairs are always facing her desk. One for the person she's fireing and one for the person she's hiring to take their place. Of course they both sit there at the same time and it's supposed to strike fear into 
the new employees soul or somrthing. Her desk is cluttered with "important" uninportant things such as her mini big ben and electronic pencil sharpener. I think I see a small microphone on her desk. 
I wonder if that is for Samantha to record the wails of her employees as she fires them.""",

    "exits": {"south": "Reception"},

    "items": [item_recorder],

    "NPCs": [Samantha]
}

room_armoury = {
    "name": "the Armoury",

    "description":
    """The Armoury is where all registered weapons are stored. Only field agents are cleared to enter and each agent is assigned a unique code to enter the armoury.""",

    "inspection":
    """This is where the big boy toys are kept. On more than one occasion the beauties from this place have gotten me out of some sticky situations. We got assault rifles, submachine guns, shotguns, grenades 
and all kinds of stuff here. My personal favourite is the silenced pistol because it makes the cool psst sound when you shoot it. Speaking of which... I can't find it. Its missing from the rack but no one has logged it out...
WHO'S TAKEN MY GUN? I used that to shoot enough loads into people that I can somewhat unofficially claim it as my own.""",

    "exits": {"north": "Reception"},

    "items": [],

    "NPCs": []
}


room_stairs2 = {
    "name": "Stairs (Ground Floor)",

    "description":
    """Stairs that lead from the ground floor to the first floor and basement.""",

    "inspection":
    """Whilst I hate stairs I can say that out of all of them these stairs are the worst. If you're going up you're either getting fired or getting shot at and if you're going down its because someone cough* Stephen cough* sent you 
down their against your own will because he's too lazy to do errands himself. Either way you only use these stairs if someone else wants you to.""",

    "exits": {"up": "Stairs1", "down": "Stairs3", "west": "Office Debra"},

    "items": [],

    "NPCs": []
}

room_office_debra = {
    "name": "Office (Debra's desk)",

    "description":
    """The ground floor office that connects used rooms to the floor. The break room and science labs are connected to this part of the office.""",

    "inspection":
    """Debra's desk is here but of course she isn't. No body does any work here but me I swear. Her desk is a tip. Crips wrappers everywhere. Coffee cups overflowing from her rubbish bin. She has no sense of organisation. 
Her computer cables are everywhere. Wires are all over her floor and around her desk. Someone could easily trip over her power lead or any of the cables attached to her computer. It's a safety complaint waiting to happen.""",

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
