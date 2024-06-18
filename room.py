from colorama import Fore
import descriptions
import random

class Room:
    def __init__(self, items: list, monster: dict):
        self.description: str = descriptions.descriptions[random.randrange(0, len(descriptions.descriptions) - 1)]
        self.sound: str = descriptions.sounds[random.randrange(0, len(descriptions.sounds) - 1)]
        self.smell: str = descriptions.smells[random.randrange(0, len(descriptions.smells) - 1)]
        self.items: list = items
        self.monster: dict = monster

    def print_description(self):
        print(Fore.LIGHTYELLOW_EX + f"{self.description}  \n{self.sound}\n{self.smell}")