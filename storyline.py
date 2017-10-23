from items import *
from characters import *

STORY_TALKED_TO_SAMANTHA = "talked to Samantha"
STORY_TALKED_TO_STEPHEN = "talked to Stephen"
STORY_ENTER_MAINFRAME = "entered mainframe"
STORY_USB_IN_MAINFRAME = "usb entered"
STORY_HAS_DIAGNOSTICS = "printed diagnostics"
STORY_COFFEE_STARTED = "gave stephen logs"
STORY_DOUBLE_STARTED = "gave debra logs"

stage2 = False
stage3 = False
stage32 = False
stage33 = False


def checkProgress(current_room):
	global stage2, stage3, stage32, stage33
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
	elif (STORY_HAS_DIAGNOSTICS in story_progress):
		if item_vault_log in Stephen["inventory"]:
			story_progress.append(STORY_COFFEE_STARTED)
			print("Start coffee ending")
		elif item_vault_log in Debra["inventory"]:
			print("start double agent ending")
			story_progress.append(STORY_DOUBLE_STARTED)