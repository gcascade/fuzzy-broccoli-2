class Stats:
    """
    A class to represent the stats of a character.
    """

    stat_descriptions = {
        "hp": "Health points.",
        "mp": "Mana points.",
        "strength": "Physical power.",
        "dexterity": "Agility and precision.",
        "intelligence": "Mental acuity.",
        "physical_defense": "Resistance to physical attacks.",
        "magical_resistance": "Resistance to magical attacks.",
        "accuracy": "Hit precision.",
        "evasion": "Dodge ability.",
        "luck": "Fortune affecting hits and dodges.",
        "wisdom": "Knowledge and insight.",
        "bravery": "Courage boosting attacks and defense.",
        "faith": "Spiritual strength enhancing magic and healing.",
        "charisma": "Charm and influence.",
    }

    def __init__(
        self,
        hp,
        mp,
        strength,
        dexterity,
        intelligence,
        physical_defense,
        magical_resistance,
        accuracy,
        evasion,
        luck,
        wisdom,
        bravery,
        faith,
        charisma,
    ):
        self.hp = hp
        self.mp = mp
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.physical_defense = physical_defense
        self.magical_resistance = magical_resistance
        self.accuracy = accuracy
        self.evasion = evasion
        self.luck = luck
        self.wisdom = wisdom
        self.bravery = bravery
        self.faith = faith
        self.charisma = charisma

    @staticmethod
    def get_stat_description(stat_name):
        """
        Get the description of a stat.
        :param stat_name: The name of the stat.
        :return: The description of the stat.
        """
        return Stats.stat_descriptions.get(stat_name, "Description not available")

    @classmethod
    def from_dict(cls, data):
        """
        Create a new Stats instance from a dictionary.
        :param data: A dictionary containing stats data.
        :return: Z new Stats instance created from the dictionary.
        """
        return cls(
            hp=data["hp"],
            mp=data["mp"],
            strength=data["strength"],
            dexterity=data["dexterity"],
            intelligence=data["intelligence"],
            physical_defense=data["physical_defense"],
            magical_resistance=data["magical_resistance"],
            accuracy=data["accuracy"],
            evasion=data["evasion"],
            luck=data["luck"],
            wisdom=data["wisdom"],
            bravery=data["bravery"],
            faith=data["faith"],
            charisma=data["charisma"],
        )

    def to_dict(self):
        """
        Return a dictionary representation of the stats.
        :return:
        """
        return {
            "hp": self.hp,
            "mp": self.mp,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "intelligence": self.intelligence,
            "physical_defense": self.physical_defense,
            "magical_resistance": self.magical_resistance,
            "accuracy": self.accuracy,
            "evasion": self.evasion,
            "luck": self.luck,
            "wisdom": self.wisdom,
            "bravery": self.bravery,
            "faith": self.faith,
            "charisma": self.charisma,
        }
