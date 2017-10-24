from items import *
from characters import *
from Dialogue import *
import time
from gameparser import *

STORY_TALKED_TO_SAMANTHA = "talked to Samantha"
STORY_TALKED_TO_STEPHEN = "talked to Stephen"
STORY_ENTER_MAINFRAME = "entered mainframe"
STORY_USB_IN_MAINFRAME = "usb entered"
STORY_HAS_DIAGNOSTICS = "printed diagnostics"
STORY_COFFEE_STARTED = "gave stephen logs"
STORY_DOUBLE_STARTED = "gave debra logs"
STORY_ENTER_VAULT = "entered vault"
STORY_HAS_TECH = "recovered tech"
STORY_COFFEE_COLLECTION_STARTED = "gave tech to stephen"
STORY_COFFEE_MADE = "made coffee"
STORY_EVIDENCE_FOUND = "found evidence"
STORY_CORRECT_AGENT = "Correct agent"
STORY_INCORRECT_AGENT = "Incorrect agent"
STORY_CHEST_SHOT = "chest shot"
STORY_LEG_SHOT = "leg shot"


def checkProgress(current_room):
    from player import inventory, story_progress

    if current_room["name"] == "Samantha's Office" and (STORY_TALKED_TO_SAMANTHA in story_progress) and not stage_2["Completion"]:
        stage_2["Completion"] = True
    elif (STORY_TALKED_TO_STEPHEN in story_progress) and not stage_3["Completion"]:
        Stephen["inventory"].remove(item_usb)
        inventory.append(item_usb)
        stage_3["Completion"] = True
    elif current_room["name"] == "Computer Mainframe" and not stage_3_3["Completion"]:
        if not stage_3_2["Completion"]:
            story_progress.append(STORY_ENTER_MAINFRAME)
            if (item_usb in inventory) and (item_login in inventory):
                story_progress.append(STORY_USB_IN_MAINFRAME)
                inventory.remove(item_usb)
                print("login and usb inputted")
                stage_3_2["Completion"] = True
                if item_ink in inventory:
                    print("printing diagnostics")
                    inventory.append(item_vault_log)
                    inventory.remove(item_ink)
                    stage_3_3["Completion"] = True
                    story_progress.append(STORY_HAS_DIAGNOSTICS)
                else:
                    print("printer out of ink, please refill")
            elif (item_usb in inventory) or (item_login in inventory):
                if item_usb in inventory:
                    print("Need login details")
                elif item_login in inventory:
                    print("Please input usb")
            else:
                print("usb and login required")
        elif stage_3_2["Completion"] and not stage_3_3["Completion"]:
            if item_ink in inventory:
                print("printing diagnostics")
                inventory.append(item_vault_log)
                inventory.remove(item_ink)
                stage_3_3["Completion"] = True
                story_progress.append(STORY_HAS_DIAGNOSTICS)
            else:
                print("printer out of ink, please refill")
    elif (STORY_HAS_DIAGNOSTICS in story_progress) and not stage_3_4["Completion"]:
        if item_vault_log in Stephen["inventory"]:
            story_progress.append(STORY_COFFEE_STARTED)
            stage_3_4["Completion"] = True
            print("Start coffee ending")
        elif item_vault_log in Debra["inventory"]:
            print("start double agent ending")
            story_progress.append(STORY_DOUBLE_STARTED)
            stage_3_4["Completion"] = True
    elif (STORY_COFFEE_STARTED in story_progress):
        if current_room["name"] == "the Vault Room":
            if not stage_4_1C["Completion"]:
                story_progress.append(STORY_ENTER_VAULT)
                if (item_vault_pass in inventory):
                    inventory.append(item_tech)
                    story_progress.append(STORY_HAS_TECH)
                    print("Password accepted. Tech acquired")
                    stage_4_1C["Completion"] = True
                else:
                    print("Vault Password required.")
        elif (STORY_HAS_TECH in story_progress) and not stage_4_2C["Completion"]:
            if item_tech in Stephen["inventory"]:
                story_progress.append(STORY_COFFEE_COLLECTION_STARTED)
                stage_4_2C["Completion"] = True
        elif (STORY_COFFEE_COLLECTION_STARTED in story_progress) and not stage_5Coffee["Completion"]:
            if (item_mugs in Stephen["inventory"]) and (item_power_lead in Stephen["inventory"]) and (item_heat_plate in Stephen["inventory"]):
                story_progress.append(STORY_COFFEE_MADE)
                stage_5Coffee["Completion"] = True
    elif (STORY_DOUBLE_STARTED in story_progress):
        if not stage_4Agent:
            if (item_camera in Debra["inventory"]) and (item_recorder in Debra["inventory"]) and (item_gun in Debra["inventory"]):
                story_progress.append(STORY_EVIDENCE_FOUND)
                stage_4Agent["Completion"] = True
                Debra["inventory"].remove(item_gun)
                inventory.append(item_gun)
                print("Evidence given")
        elif not stage_5Agent and STORY_EVIDENCE_FOUND in story_progress:
            if current_room["name"] == "Computer Mainframe" and item_gun in inventory:
                print("Running fingerprints...")
                time.sleep(2)
                print("Match found!")
                print("Fingerprints match Jenifer's data.")
            elif current_room["name"] == "the Break Room":
                if STORY_CORRECT_AGENT in story_progress:
                    stage_5Agent["Completion"] = True
                elif STORY_INCORRECT_AGENT in story_progress:
                    stage5_Agent["Completion"] = True
                    #run dialogue for stage 9
        elif not stage_6Agent and STORY_CORRECT_AGENT in story_progress:
            #run dialog stage 6
            choice = ""
            while choice != "chest" or choice != "leg":
                shoot = input("Shoot Jenifer in the CHEST or LEG)")
                choice = normalise_input(shoot)

            if choice == "chest":
                #run dialog stage 7
                story_progress.append(STORY_CHEST_SHOT)
            elif choice == "leg":
                #run dialog stage 8
                story_progress.append(STORY_LEG_SHOT)