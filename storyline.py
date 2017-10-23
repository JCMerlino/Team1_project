from items import *
from characters import *

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

stage2 = False
stage3 = False
stage32 = False
stage33 = False
stage34 = False
stage41 = False
stage42 = False
stage5 = False


def checkProgress(current_room):
	global stage2, stage3, stage32, stage33, stage34, stage41, stage42, stage5
	from player import inventory, story_progress
	
	if current_room["name"] == "Samantha's Office" and (STORY_TALKED_TO_SAMANTHA in story_progress) and not stage2:
		stage2 = True
		print("Stage2 is" + str(stage2))
	elif (STORY_TALKED_TO_STEPHEN in story_progress) and not stage3:
		Stephen["inventory"].remove(item_usb)
		inventory.append(item_usb)
		stage3 = True
		story_progress.remove(STORY_TALKED_TO_STEPHEN)
	elif current_room["name"] == "Computer Mainframe":
		if not stage32:
			story_progress.append(STORY_ENTER_MAINFRAME)
			if (item_usb in inventory) and (item_login in inventory):
				story_progress.append(STORY_USB_IN_MAINFRAME)
				inventory.remove(item_usb)
				print("login and usb inputted")
				stage32 = True
				if item_ink in inventory:
					print("printing diagnostics")
					inventory.append(item_vault_log)
					inventory.remove(item_ink)
					stage33 = True
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
		elif stage32 and not stage33:
			if item_ink in inventory:
				print("printing diagnostics")
				inventory.append(item_vault_log)
				inventory.remove(item_ink)
				stage33 = True
				story_progress.append(STORY_HAS_DIAGNOSTICS)
			else:
				print("printer out of ink, please refill")
	elif (STORY_HAS_DIAGNOSTICS in story_progress) and not stage34:
		if item_vault_log in Stephen["inventory"]:
			story_progress.append(STORY_COFFEE_STARTED)
			stage34 = True
			print("Start coffee ending")
		elif item_vault_log in Debra["inventory"]:
			print("start double agent ending")
			story_progress.append(STORY_DOUBLE_STARTED)
			stage34 = True
	elif (STORY_COFFEE_STARTED in story_progress):
		if current_room["name"] == "the Vault Room":
			if not stage41:
				story_progress.append(STORY_ENTER_VAULT)
				if (item_vault_pass in inventory):
					inventory.append(item_tech)
					story_progress.append(STORY_HAS_TECH)
					print("Password accepted. Tech acquired")
					stage41 = True
				else:
					print("Vault Password required.")
		elif (STORY_HAS_TECH in story_progress) and not stage42:
			if item_tech in Stephen["inventory"]:
				story_progress.append(STORY_COFFEE_COLLECTION_STARTED)
				stage42 = True
		elif (STORY_COFFEE_COLLECTION_STARTED in story_progress) and not stage5:
			if (item_mugs in Stephen["inventory"]) and (item_power_lead in Stephen["inventory"]) and (item_heat_plate in Stephen["inventory"]):
				story_progress.append(STORY_COFFEE_MADE)
				stage5 = True