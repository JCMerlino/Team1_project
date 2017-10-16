from map import rooms
from player import *
from game import *


class execute():

	def __init__(self):
		super(execute, self).__init__()

	def go(direction):
		"""This function, given the direction (e.g. "south") updates the current room
		to reflect the movement of the player if the direction is a valid exit
		(and prints the name of the room into which the player is
		moving). Otherwise, it prints "You cannot go there."
		"""
		global current_room
		if is_valid_exit(current_room["exits"], direction):
			current_room = rooms[current_room["exits"][direction]]
		else:
			print("You cannot go there")

	def take(item_id):
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

		if found:
			if check_mass(pos):
				inventory.append(current_room["items"].pop(pos))
			else:
				print("Total mass of objects over 3kg, drop something before picking object up.")
		else:
			print("You cannot take that.")

	def drop(item_id):
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

	def talk():
		pass

	def inspect():
		pass

	def give():
		pass