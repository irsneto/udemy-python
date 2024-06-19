class Player:
    def __init__(self):
        self.hp: int = 100
        self.treasure: int = 0
        self.monster_defeated: int = 0
        self.xp: int = 0
        self.turns: int = 0
        self.inventory: list = []
        self.max_itens: int = 5
        

    def add_item(self, item: dict) -> bool:
        if not self.is_inventory_full():
            self.inventory.append(item)
            return True


    def is_inventory_full(self):
        return len(self.inventory) == self.max_itens