import random

class Character():
    # character types: warrior, mage, wizard, knight
    #x and y are cordinates where the character is on the map

    def __init__(self, char_type, x, y, life_points, level):
        self.char_type = char_type
        self.x = x
        self.y = y
        self.life_points = life_points
        self.level = level

    def moveRight(self, x):
        return x + 1

    def moveLeft(self, x):
        return x - 1

    def moveUp(self, y):
        return y + 1

    def moveDown(self, y):
        return y - 1

    def attack(self):
        damage = random.randint(0, 1000)

        return damage

    def calculateLife(self, life_points, damage):
        return life_points - damage

class Hero(Character):
    collected_items = []

    def __init__(self, hero_class, hero_race, hero_abilities):
        self.hero_class = hero_class
        self.hero_race = hero_race
        self.hero_abilities = hero_abilities

    def defend(self, damage):
        return damage - random.randint(0, damage)

    def collectItem(self, items: list, new_item: str):
        items.append(new_item)

class Monster(Character):
    def __init__(self, sub_type):
        self.sub_type = sub_type

    def move_random(self, x, y):
        x = x + random.randint(0,100 - x)
        y = y + random.randint(0, 100 - y)

        return x, y

    def dropItem(self):
        items = ["sword", "staff", "ring", "helm", "chest"]

        return random.choice(items)

class Spawn(Monster):

    def random_type(self):
        monster_types = ["Orc", "Goblin", "Beast"]

        return random.choice(monster_types)

    def random_cordinates(self):
        x = random.randint(0, 100)
        y = random.randint(0, 100)

        return x, y

class Level(Hero):
    def __init__(self, current_level, experience):
        self.current_level = current_level
        self.experience = experience

    def gainExp(self, experience):
        return experience + random.randint(0, 1000)

    def levelUp(self, experience, current_level):
        if experience > 10000:
            return current_level + 1

class Item():
    # item types ex: weapon, armor, special items

    def __init__(self, item_type):
        self.item_type = item_type

class Map:
    width = 100
    height = 100

class MapLevel(Map):
    def __init__(self, current_level, last_level):
        self.current_level = current_level
        self.last_level = last_level

    def levelStart(self):
        print("Level start")

    def levelEnd(self):
        print("Level end")
