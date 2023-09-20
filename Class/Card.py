class Card:
    """Class permettant de créer une carte avec IP, Nom, Coût, Type, Vie, Attaque, Raretée"""

    def __init__(self, ID : int, Name : str, Type : str, Cost  : int, Health : int, Attack : int, Rarity : str, Class : list) :

        self.IP = ID

        self.Name = Name

        self.Type = Type

        self.Cost = Cost

        self.Health = Health

        self.Attack = Attack

        self.Rarity = Rarity

        self.Class = Class