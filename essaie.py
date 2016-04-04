class Valeur_1:
    par1 = 'Bonjour'
    def __init__(self, ch):
        self.x = ch
    def __add__(self, autre): # addition vectorielle
        if self.x == "":
            return Valeur_1(autre.x + self.par2)
        else:
            return Valeur_1(autre.x + self.par1)
        
#    def __str__(self): # affichage d’un Vecteur2D
#        return "Vecteur(%s, %s)" % (self.x, self.y)
v1 = Valeur_1("titi")
v2 = Valeur_1("tata")

print(v1.par1 + v2.par2) # Vecteur(4.6, 6.8)