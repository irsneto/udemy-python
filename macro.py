from room import Room
from player import Player

class Game:
    def __init__(self, player: Player):
        self.player = player
        self.room = None
        self.num_monsters: int = 0
        self.rooms: dict = {}
        self.x: int = 0
        self.y: int = 0

    
    def set_rooms(self, rooms: dict):
        self.rooms = rooms
    

    def set_current_room(self, room: Room):
        self.room - room