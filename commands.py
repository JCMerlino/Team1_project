from game import *
from map_new import rooms
from storyline import *
from Dialogue import *
from talk_to_npc import *


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
            if can_player_go_through_exit(current_room["exits"][direction]):
                return rooms[current_room["exits"][direction][0]]
            else:
                if not stage_1["Completion"]:
                    print(stage_1["Leaving"])
                    return current_room
                else:
                    print("You cannot go there at the moment. Please complete your task first.")
                    return current_room
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
                if item_mainframe_key in inventory:
                    stage_3_1["Completion"] = True
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
                print(item_id["picture"])
                print(item_id["description"])

            for pos in range(len(current_room["NPCs"])):
                if inspected_object.capitalize() in current_room["NPCs"][pos]["name"]:
                    character_id = current_room["NPCs"][pos]
                    print(character_id["description"])
                    found = True
            if found:
                pass
            else:
                print("The object is not in the room")

    def give(target_item, target_npc, current_room, story_progress):
        if (target_npc == "debra") or (target_npc == "stephen"):
            found_npc = False
            found_item = False
            pos_item = 0
            pos_npc = 0
            while not found_item and pos_item != len(inventory):
                if inventory[pos_item]["id"] == target_item:
                    found_item = True
                else:
                    pos_item += 1
            while not found_npc and pos_npc != len(current_room["NPCs"]):
                if current_room["NPCs"][pos_npc]["name"] == target_npc.capitalize():
                    found_npc = True
                    npc_inventory = current_room["NPCs"][pos_npc]
                else:
                    pos_npc += 1

            if found_item and found_npc:
                if (STORY_HAS_DIAGNOSTICS in story_progress) and (target_item == "vaultlog"):
                        npc_inventory["inventory"].append(inventory.pop(pos_item))
                        print("You gave {0} to {1}".format(target_item, target_npc))
                elif target_npc == "stephen":
                    if (STORY_HAS_TECH in story_progress) and (target_item == "tech"):
                        npc_inventory["inventory"].append(inventory.pop(pos_item))
                        print("You gave {0} to {1}".format(target_item, target_npc))
                    elif (STORY_COFFEE_COLLECTION_STARTED in story_progress) and ((target_item == "mugs") or (target_item == "lead") or (target_item == "plate")):
                        npc_inventory["inventory"].append(inventory.pop(pos_item))
                        print("You gave {0} to {1}".format(target_item, target_npc))
                    elif (STORY_COFFEE_MADE in story_progress) and (target_item == "usb"):
                        npc_inventory["inventory"].append(inventory.pop(pos_item))
                        print("You gave {0} to {1}".format(target_item, target_npc))
                    else:
                        print("{0}: Why would I want that?".format(target_npc.capitalize()))
                elif target_npc == "debra":
                    if (STORY_DOUBLE_STARTED in story_progress) and ((target_item == "camera") or (target_item == "recorder") or (target_item == "gun")):
                        npc_inventory["inventory"].append(inventory.pop(pos_item))
                        print("You gave {0} to {1}".format(target_item, target_npc))
                    else:
                        print("{0}: Why would I want that?".format(target_npc.capitalize()))
            elif found_item and not found_npc:
                print("Give to who?")
            elif not found_item:
                print("You do not have this.")
            else:
                print("You can not give this.")
        else:
            if target_npc in ["debra", "samantha", "bob", "alexa", "jenifer", "stephen"]:
                print("{0}: Why would I want that?".format(target_npc.capitalize()))
            else:
                print("Give to who?")

    def talk(target_npc, current_room):
        found_npc = False
        pos_npc = 0
        while not found_npc and pos_npc != len(current_room["NPCs"]):
            if current_room["NPCs"][pos_npc]["name"] == target_npc.capitalize():
                found_npc = True

            else:
                pos_npc += 1
        if found_npc:
            if target_npc == "samantha":
                samantha_talks(current_room)
            elif target_npc == "jenifer":
                jenifer_talks(current_room)
            elif target_npc == "debra":
                debra_talks(current_room)
            elif target_npc == "bob":
                bob_talks(current_room)
            elif target_npc == "stephen":
                stephen_talks(current_room)
            elif target_npc == "alexa":
                alexa_talks(current_room)
        #if found_npc:
            #if found_npc and not stage_2["Completion"]:
                #story_progress.append("talked to {0}".format(current_room["NPCs"][pos_npc]["name"]))
                #print(stage_2["SamanthaStart"])
            #elif not stage_3["Completion"] and (current_room["NPCs"][pos_npc]["name"] == "Stephen"):
                #story_progress.append("talked to {0}".format(current_room["NPCs"][pos_npc]["name"]))
                #print("after stage 3")
            #else:
                #if "talked to {0}".format(current_room["NPCs"][pos_npc]["name"]) not in story_progress:
                    #print("You are talking to " + current_room["NPCs"][pos_npc]["name"])
                #else:
                    #print("You already talked to this person")

        else:
            print("You cannot talk to this person.")

    def double(target_npc, current_room):
        if (STORY_EVIDENCE_FOUND in story_progress) and (current_room["name"] == "the Break Room"):
            if target_npc.capitalize() == "Jenifer":
                print("Double jenifer")
                story_progress.append(STORY_CORRECT_AGENT)
            else:
                print("wrong agent")
                story_progress.append(STORY_INCORRECT_AGENT)
                #skip to stage 9
        else:
            print("This makes no sense.")