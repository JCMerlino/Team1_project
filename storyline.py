from items import *
from characters import *

STORY_TALKED_TO_SAMANTHA = "talked to Samantha"
STORY_TALKED_TO_STEPHEN = "talked to Stephen"
STORY_ENTER_MAINFRAME = "entered mainframe"
STORY_USB_IN_MAINFRAME = "usb entered"

stage3 = False
stage32 = False


def checkProgress(current_room):
	global stage3, stage32
	from player import inventory, story_progress
	if (STORY_TALKED_TO_STEPHEN in story_progress) and not stage3:
		Stephen["inventory"].remove(item_usb)
		inventory.append(item_usb)
		stage3 = True
	elif current_room["name"] == "Computer Mainframe":
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
			else:
				print("printer out of ink, please refill")
		elif (item_usb in inventory) or (item_login in inventory):
			if item_usb in inventory:
				print("Need login details")
			elif item_login in inventory:
				print("Please input usb")
		else:
			print("usb and login required")