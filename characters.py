class Character:
	def __init__(self, name, type, character_class):
		self.name = name
		self.character_class = character_class
		base_stats = type[character_class]
		self.hp = base_stats["hp"]
		self.attack = base_stats["attack"]


def character_creation():
	name = input("What's your hero's name?:")
	hero_class = input(f"{list(heroes.keys())}/nChoose a class:")
	return [name, heroes ,hero_class]


heroes = {"knight":{"hp":100, "attack":30}}

player_choices = character_creation()

hero = Character(*player_choices)

print(hero.name,hero.character_class, hero.hp, hero.attack)
