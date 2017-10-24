from items import *
from storyline import *
from characters import *

room_stairs1 = {
    "name": "Stairs (First Floor)",

    "description":
    """Stairs that lead from the first floor to the ground floor.""",

    "inspection":
    """We have millions of pounds in funding but we can't afford an elevator.
Stairs are physically traumatic and worse, these stairs lead to the ground floor offices
where all the underlings scurry about.""",

    "exits": {"down": ("Stairs2", None), "west": ("Reception", None)},

    "items": [],

    "NPCs": []
}

room_reception = {
    "name": "Reception",

    "description":
    """Jenifer's office outside of Samantha's Office. Jenifer is sitting at her desk.""",

    "inspection":
    """Jenifer's office? I didn't think she got paid enough to earn herself an office. She has a basic desk and a
virus filled computer. Not that she even uses them. She's also put her makeup everywhere. Does she actually do work? Who
knows... She's currently pretending to do something on the computer. Probably playing some stupid game to pass the
time. What else is here... waste bin, fan, ink cartridges, window... yeah nothing else of importance.""",

    "exits": {"north": ("Samantha", None), "south": ("Armoury", STORY_TALKED_TO_SAMANTHA), "east": ("Stairs1", STORY_TALKED_TO_SAMANTHA)},

    "items": [item_ink],

    "NPCs": [Jenifer]
}

room_samantha = {
    "name": "Samantha's Office",

    "description":
    """The Boss' office is large and filed with custom made furniture and has expensive carpet.
The first floor windows provide natural lighting and a view over the street below.
Samantha is sitting at her desk.""",

    "inspection":
    """Samantha's Office... The place where paychecks are crushed and lives are disregarded.
Her large desk is shadowed only by her larger bookcase, probably compensating for her failing secret service.
The computer is heavily used as shown by her sixth replacement keyboard this week and the secret alcohol stash
is always hidden under her desk but it's not exactly a secret though. Her window has the lamest view of city
life possible. Who actually wants to look outside and see depressed city workers going about their daily business?
Two chairs are always facing her desk. One for the person she's fireing and one for the person she's hiring to take
their place. Of course they both sit there at the same time and it's supposed to strike fear into the new employees
soul or somrthing. Her desk is cluttered with "important" uninportant things such as her mini big ben and electronic
pencil sharpener. I think I see a small microphone on her desk. I wonder if that is for Samantha to record the wails
of her employees as she fires them.""",

    "exits": {"south": ("Reception", None)},

    "items": [item_recorder],

    "NPCs": [Samantha]
}

room_armoury = {
    "name": "the Armoury",

    "description":
    """The Armoury is where all registered weapons are stored. Only field agents are cleared to enter and each agent
is assigned a unique code to enter the armoury.""",

    "inspection":
    """This is where the big boy toys are kept. On more than one occasion the beauties from this place have gotten me
out of some sticky situations. We got assault rifles, submachine guns, shotguns, grenades and all kinds of stuff here.
My personal favourite is the suppressed pistol because it makes the cool psst sound when you shoot it. Speaking of
which... I can't find it. Its missing from the rack but no one has logged it out...WHO'S TAKEN MY GUN? I used that to
shoot enough loads into people that I can somewhat unofficially claim it as my own.""",

    "exits": {"north": ("Reception", None)},

    "items": [],

    "NPCs": []
}


room_stairs2 = {
    "name": "Stairs (Ground Floor)",

    "description":
    """Stairs that lead from the ground floor to the first floor and basement.""",

    "inspection":
    """Whilst I hate stairs I can say that out of all of them these stairs are the worst. If you're going up you're
either getting fired or getting shot at and if you're going down its because someone cough* Stephen cough* sent you
down their against your own will because he's too lazy to do errands himself. Either way you only use these stairs
if someone else wants you to.""",

    "exits": {"up": ("Stairs1", None), "down": ("Stairs3", None), "west": ("Office Debra", None)},

    "items": [],

    "NPCs": []
}

room_office_debra = {
    "name": "Office (Debra's desk)",

    "description":
    """The ground floor office that connects used rooms to the floor. The break room and science labs are connected
to this part of the office.""",

    "inspection":
    """Debra's desk is here but of course she isn't. No body does any work here but me I swear. Her desk is a tip.
Crips wrappers everywhere. Coffee cups overflowing from her rubbish bin. She has no sense of organisation.
Her computer cables are everywhere. Wires are all over her floor and around her desk. Someone could easily
trip over her power lead or any of the cables attached to her computer. It's a safety complaint waiting to happen.
Yet she spends most of her time complaining about my unorganised and terrible ways of doing things. Thing is I get
things done, even if I may accidently kill a few people here and there whilst doing it.""",

    "exits": {"east": ("Stairs2", None), "south": ("Science", None), "north": ("Break", None), "west": ("Office Bob", None)},

    "items": [item_power_lead],

    "NPCs": []
}

room_science = {
    "name": "Science Lab",

    "description":
    """The Science Lab is filled with technology beyond normal comprehension. The Science Lab has direct access to the
storage room. Stephen sits at his lab desk""",

    "inspection":
    """Science Lab is a fancy name for Stephen's backstreet workshop. He once tried to create a mermaid by putting
a pig's head on a fish's body. The name just lets him get away with burning through cash and he justifies it under
"Scientific Research". All I know he spends enough time here for it to be his home. If anything judging by the ammount
of time he spends alone, he's probably researching how to create an artificial girlfriend. It would explain why there
are so many humanoid creatures floating around in tanks. Come to think of it thats a bit freaky but no one really knows
what he gets up to in here. We just assume he'll give us a boring explanation if we ask.""",

    "exits": {"north": ("Office Debra", None), "west": ("Storage", None)},

    "items": [],

    "NPCs": [Stephen]
}

room_break = {
    "name": "the Break Room",

    "description":
    """The break room is a medium sized room with a few tables and chairs as well as a small kitchen area.
Debra is standing by the kitchen area""",

    "inspection":
    """So I guess Debra's job description is actually "snack connoisseur" judging by the amount of time she spends here.
No wonder we never have any snacks. Actually I lie. We always have one snack at the bottom of the packet because break
room rules dictate the person who finishes a snack has to buy the next packet. So of course Debra always pigs out and
then the next person has to replace the snacks. She's currently by the kitchen area going through a packet of doughnuts
that Bob just bought this morning. Someone needs to talk to her about her eating habits. She's also got that awful mug
Jenifer bought her. Those two gossip like socially deprived mothers. You know. The ones who have a coffee with other
mums for the whole day. They bought matching BFF mugs but they are much closer than that. Unless anyone told you otherwise,
you'd assume they were a couple. Which apparently they don't mind because: "If there isn't a rumour you're gay for each
other, you're not real BFFs" which I don't understand but hey if they want to keep their relationship a "secret" who am I
to judge or say otherwise.""",

    "exits": {"south": ("Office Debra", None), "west": ("Meeting", None)},

    "items": [item_mugs],

    "NPCs": [Debra]
}

room_meeting = {
    "name": "the Meeting Room",

    "description":
    """The meeting room is where all important meetings take place. There is a large rectangular table with chairs all around
and a projector at one end of the room. Bob and Alexa are seated at the table.""",

    "inspection":
    """The imfamous meeting room. The phrase "What happens in Vegas stays in Vegas" easily applies to this room as well.
Usually this room is only used for important breifings so it's no wonder there is usually no one in here. However both Bob and
Alexa are at the table. I'm just going to stay away from that particular topic before I start a conversation I will regret.
This room has always been quite bland and the projector is practically falling apart now. The room has slowly degraded over the
years however I don't remember that camera in the corner. I hope it hasnt got anything to do with Bob and Alexa in the room.
""",

    "exits": {"east": ("Break", None), "south": ("Office Bob", None)},

    "items": [item_camera],

    "NPCs": [Bob, Alexa]
}

room_office_bob = {
    "name": "Office (Bob's desk)",

    "description":
    """The ground floor office that connects used rooms to the floor. The meeting room, toilets and storage room are connected
to this part of the office.""",

    "inspection":
    """Suprise suprise Bob isn't at his desk. The real mystery is how the hell this secret service manages to survive with
employees that litterally do nothing all day. Bob's in charge of documents and paperwork so his his desk is piled high with
the stuff and his rubbish bin is also filled with scrap paper and all kinds of junk. There seems to be an envelope stuck out
of the pile of documents. Wonder what that is for. There's a single scrap piece of paper on his keybaord. Perhaps it's his
login details. I'm suprised there isn't any alcohol in sight. This sort of job requires a truck load of motivation so I wonder
how he unwinds after it all.""",

    "exits": {"north": ("Meeting", None), "west": ("Toilet", None), "east": ("Office Debra", None), "south": ("Storage", None)},

    "items": [item_login, item_documents],

    "NPCs": []
}

room_storage = {
    "name": "the Storage Room",

    "description":
    """The storage room is for general storage that isn't of high enough importance to be locked in the vault. The room contains
many shelves and containers where all matter of items are kept.""",

    "inspection":
    """If I had a penny for every time I lost an item in here I'd probably be a millionaire. This is supposed to be an area for
work related storage but it seems no one cares about that. There is quite the range of things in here. Whoever organises this area
does an amazing job of it. With so many items entering and exiting this room per day its unbelievable that it can still be sorted.
The only part that isnt sorted is the miscelaneous technology cabinet. Right now it looks like someone dumped heat plate circuitry
outside it. Probably because it's full but I won't go find out in case I have to clear it up.""",

    "exits": {"north": ("Office Bob", None), "east": ("Science", None)},

    "items": [item_heat_plate],

    "NPCs": []
}

room_toilet = {
    "name": "the Toilet",

    "description":
    """Does this place really need a description?""",

    "inspection":
    """This place is suprisingly clean but I'm pretty sure there has been a lot of quickies that have happened here. You can almost
smell it. Nothing else really to say except its a toilet but there is some shiny things at the bottom of the bowl. They look like keys.
I think someone's diet plan is recommending questionable food choices.""",

    "exits": {"east": ("Office Bob", None)},

    "items": [item_vault_key, item_mainframe_key],

    "NPCs": []
}

room_stairs3 = {
    "name": "Stairs (the Basement)",

    "description":
    """Stairs that connect the basement to the ground floor""",

    "inspection":
    """You'd think that the stairs to hell would be going down, but in this case they lead up. Down here no one can bother you or
tell you to work. """,

    "exits": {"up": ("Stairs2", None), "west": ("Hallway east", None)},

    "items": [],

    "NPCs": []
}

room_hallway_east = {
    "name": "East Hallway",

    "description":
    """The hallway of the basement connects the three important rooms to the stairs. The backup generator room can be accessed from
this part of the hallway""",

    "inspection":
    """Its a hallway. What else did you expect?""",

    "exits": {"east": ("Stairs3", None), "west": ("Hallway west", None), "north": ("Generator", None)},

    "items": [],

    "NPCs": []
}

room_generator = {
    "name": "Generator Room",

    "description":
    """The backup generator room is a large room riddled with Stephen's technology turning a medium sized generator into the backup
for the entire building.""",

    "inspection":
    """This room has seen better days. I liked it better when it was the interrogation room. There's still some blood where the stains won't
come off the floor. Good times... Wait. My pistol is in the corner of the room. Someone tried to tuck it away behind the generator. How did
it get here? """,

    "exits": {"south": ("Hallway east", None)},

    "items": [item_gun],

    "NPCs": []
}

room_computer = {
    "name": "Computer Mainframe",

    "description":
    """The mainframe is stored within a well air conditioned room.""",

    "inspection":
    """The special computer before me has direct access to the mainframe. The things I could do with this machine...
I have to login first though. There is a card here which has the vault passcode on it. Someone left the damm thing lying
around. Our security really is questionable. """,

    "exits": {"south": ("Hallway west", None)},

    "items": [item_vault_pass],

    "NPCs": []
}

room_hallway_west = {
    "name": "West Hallway",

    "description":
    """The hallway of the basement connects the three important rooms to the stairs. The mainframe and vault can be accessed from
this part of the hallway""",

    "inspection":
    """Its a hallway. What else did you expect?""",

    "exits": {"north": ("Computer", item_mainframe_key), "east": ("Hallway east", None), "south": ("Vault", item_vault_key)},

    "items": [],

    "NPCs": []
}

room_vault = {
    "name": "the Vault Room",

    "description":
    """The vault is a high security storage space with an electronic password requirment as well as several locks. This
is where all important items are kept.""",

    "inspection":
    """This place is where people keep their dirty secrets. You wouldn't think it but there are some interesting
stories to how some of these items got here. Including this interesting piece of tech. I have no idea what it is but
it's blinking so it's either a bomb or a communicator. But why is it here? I should probably
ask Stephen about it but then again Debra might want to know if something fishy is going on. More importantly my secret
stash of used panties is still here and it's box looks unopened so I think my secret is safe.""",

    "exits": {"north": ("Hallway west", None)},

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
