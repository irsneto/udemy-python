from colorama import Fore
from player import Player
from room import Room
from macro import Game
from prettytable import PrettyTable

import bestiary
import armory
import random

def welcome():
    print("                                                 ")
    print(Fore.RED + "                                                                 D U N G E O N")
    print(Fore.GREEN + """
            The village of Honeywood has been terrorized by strange, deadly creatures for months now. Unable to endure any 
            longer, the villagers pooled their wealth and hired the most skilled adventurer they could find: you. After
            listening to their tale of woe, you agree to enter the labyrinth where most of the creatures seem to originate,
            and destroy the foul beasts. Armed with a longsword and a bundle of torches, you descend into the labyrinth, 
            ready to do battle....
          
          """)
    

def play_game():

    adventurer = Player()
    current_game = Game(adventurer)


    welcome()
    input("Press ENTER to continue")
    explore_lab(current_game)
    

def generate_room() -> Room:
    items = []
    monster = {}

    if random.randint(0, 100) < 99:
        items.append(random.choice(list(armory.items.values())))

    if random.randint(0, 100) < 99:
        monster = random.choice(bestiary.monsters)

    return Room(items, monster)



def explore_lab(current_game: Game):
    while True:
        player_input = get_input()

        if player_input.startswith("get"):
            get_item(current_game, player_input)

        elif player_input == "inventory" or player_input == "inv":
            show_inventory(current_game)
            continue

        elif player_input == "help":
            show_help()
            continue

        elif player_input in ["n", "s", "e", "w"]:
            print(f"{Fore.CYAN}You move deeper into the dungeon")
            current_game.room = generate_room()
            current_game.room.print_description()

            for i in current_game.room.items:
                print(f"{Fore.LIGHTGREEN_EX}You found a new Item: {i['name']}" )

            if current_game.room.monster:
                print(f"{Fore.RED}D A N G E R ")
                print(f"{Fore.LIGHTRED_EX}{current_game.room.monster['name']}")

            continue

        elif player_input == "quit":
            print ("Is that your best?")

            # Print final score
            
            # quit or play again
            play_again()

        else:
            print("Can't get your thoughts")


def play_again():
    yn = get_yn("Play again? ")
    if yn == "yes":
        play_game()
    else:
        print("See u next time")
        exit(0)


def show_help():
    print(Fore.YELLOW + """Enter a command
        - n/s/e/w: move in a direction
        - map - show a map of the laby
        - look around and describe env
        - equip <item> - use an item from your inventory
        - unequip - stop using an item
        - fight - attack a foe
        - examine <object> - examine an object
        - use <item>
        - drop <item> 
        - rest - restore some health by resting
        - inventory
        - status
        - quit
          
          """)
    

def get_input():
    pl_input = input(Fore.YELLOW + "→ ").lower().strip()
    return pl_input

def get_yn(question):
    while True:
        answer = input(question + "(yes/no) \n→ ").lower().strip()
        if answer not in ["yes", "no", "y", "n"]:
            print("please enter a correct option")
        else:
            if answer == "y":
                answer = "yes"
            elif answer == "n":
                answer = "no"
            return answer


def show_inventory(current_game: Game):

    if len(current_game.player.inventory) > 0:
        table = PrettyTable(['Item', 'Type'])
        for i in current_game.player.inventory:
            for x, obj in i.items():
                table.add_row([obj["name"], obj["type"]])
    
        print(f"{Fore.BLUE}{table.get_string()}")
    
    else:
         print(f"{Fore.BLUE}There are valuable things out there, go find some")


def get_item(current_game: Game, item_name: str):
    if current_game.room.items:
        item = current_game.room.items.pop()
        item_dict = {item['name']: item}
        if current_game.player.add_item(item_dict):
            print(f"{Fore.CYAN}{item['name']} added to your inventory adventurer")
        else:
            print(f"{Fore.RED}My bag is full")
    else: 
        print("You can't get what does not exist")