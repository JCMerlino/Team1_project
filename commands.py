from game import *
from map_new import rooms


class execute:

    def __init__(self):
        pass

    def go(direction, current_room):
        """This function, given the direction (e.g. "south") updates the current room
        to reflect the movement of the player if the direction is a valid exit
        (and prints the name of the room into which the player is
        moving). Otherwise, it prints "You cannot go there."
        """
        if is_valid_exit(current_room["exits"], direction):
            return rooms[current_room["exits"][direction]]
        else:
            print("You cannot go there")
            return current_room

    def take(item_id, current_room):
        """This function takes an item_id as an argument and moves this item from the
        list of items in the current room to the player's inventory. However, if
        there is no such item in the room, this function prints
        "You cannot take that."
        """
        found = False
        pos = 0
        while not found and pos != len(current_room["items"]):
            if current_room["items"][pos]["id"] == item_id:
                found = True
            else:
                pos += 1

        if found and check_player_mass(pos, current_room):
                inventory.append(current_room["items"].pop(pos))
        elif not found:
            print("You cannot take that.")
        else:
            print("Total mass of objects over 3kg, drop something before picking object up.")

    def drop(item_id, current_room):
        """This function takes an item_id as an argument and moves this item from the
        player's inventory to list of items in the current room. However, if there is
        no such item in the inventory, this function prints "You cannot drop that."
        """
        found = False
        pos = 0
        while not found and pos != len(inventory):
            if inventory[pos]["id"] == item_id:
                found = True
            else:
                pos += 1

        if found:
            current_room["items"].append(inventory.pop(pos))
        else:
            print("You cannot drop that.")
            
    def inspect(inspected_object, current_room):
        """ this function gives a different description of the room"""
        if inspected_object == "room":
            print(current_room["inspection"])
        else:
            found = False
            for pos in range(len(current_room["items"])):
                if inspected_object in current_room["items"][pos]["id"]:
                    item_id = current_room["items"][pos]
                    found = True
            
            for pos in range(len(inventory)):
                if inspected_object in inventory[pos]["id"]:
                    item_id = inventory[pos]
                    found = True
            if found:    
                item_id["picture"]
                print(item_id["description"])
            else:
                print("The object is not in the room")