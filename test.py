# heritage  EXERCICE REUSSIR
# classe mere
class Player:
    # constructeur
    def __init__(self, pseudo, helth, attack):
        
        self.pseudo = pseudo
        self.helth = helth
        self.attack = attack
        
        print("Bienvenue au joueur", pseudo , "/Point de vie:", helth , "/attaque:", attack)
        
        # les getters
    def get_pseudo(self):
        return self.pseudo
    
    def get_helth(self):
        return self.helth
    
    def get_attack(self):
        return self.attack
    
    # methode
    def dommage(self, dommage):
        self.helth -= dommage
        #print("Aie.... vous venez de subir", dommage, "degats!!!!")
        
    def player_attack(self, player_attack):
        player_attack.dommage = self.attack
        
        
# classe fille
class Warrior(Player):
    # constructeur
    def __init__(self, pseudo, helth, attack):
        super().__init__(pseudo, helth, attack)
        self.armor = 3
    
    # methode
    def dommage(self, dommage):
        if self.armor > 0:
            self.armor -=1
            dommage = 0
            
        super().dommage(dommage)
            
       # recharge le point de vie supplementaire du guerrier
    def blade(self):
        self.armor = 3
        
        # retourne le point du point de vie supplementaire
    def get_armor_point(self):
        return self.armor
    
# objets
player = Player("Gutember", 20, 3)

player.dommage(2)

warrior = Warrior("GrandGuerrier", 40, 5)

warrior.dommage(4)

print("Point de Vie:", warrior.get_helth() , "Point de Vie Supplementaire:", warrior.get_armor_point())

warrior.dommage(4)

print("Point de Vie:", warrior.get_helth() , "Point de Vie Supplementaire:", warrior.get_armor_point())

warrior.dommage(4)

print("Point de Vie:", warrior.get_helth() , "Point de Vie Supplementaire:", warrior.get_armor_point())

warrior.dommage(4)

print("Point de Vie:", warrior.get_helth() , "Point de Vie Supplementaire:", warrior.get_armor_point())

# print("Bienvenue au joueur", player1.pseudo , "/Point de vie:", player1.helth , "/attaque:", player1.attack)

# print("Bienvenue au joueur", player2.pseudo , "/Point de vie:", player2.helth , "/attaque:", player2.attack)

# print("Apres l'attaque du joueur 1 son point de vie est:", player1.get_helth())
    