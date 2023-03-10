# Commente le code suivant

class AB:
    # Constructeur et setters
    def __init__(self, valeur=None, gauche=None, droite=None):
        self.racine = [valeur]
        self.gauche = gauche
        self.droite = droite

    def set_racine(self, valeur):
        self.racine = [valeur]

    def set_gauche(self, gauche):
        self.gauche = gauche

    def set_droite(self, droite):
        self.droite = droite

    # Méthodes
    # Méthode qui retourne True si l'arbre est vide, False sinon
    def estVide(self):
        return self.racine == [None]
    
    # Méthode qui retourne la taille de l'arbre
    def taille(self):
        # Vérifie si l'arbre est vide (s'il est vide, on retourne 0)
        if self.estVide():
            return 0
        # Vérifie si l'arbre est une feuille (s'il est une feuille, on retourne 1)
        elif self.gauche is None and self.droite is None:
            return 1
        # Vérifie si l'arbre a un seul sous-arbre (gauche ou droit) et si oui, on retourne la taille de ce sous-arbre + 1
        elif self.gauche is None:
            return 1 + self.droite.taille()
        elif self.droite is None:
            return 1 + self.gauche.taille()
        else:
            return 1 + self.gauche.taille() + self.droite.taille()
        
    # Méthode qui retourne la hauteur de l'arbre
    def hauteur(self):
        # Vérifie si l'arbre est vide (s'il est vide, on retourne -1)
        if self.estVide():
            return -1
        # Vérifie si l'arbre est une feuille (s'il est une feuille, on retourne 0)
        elif self.gauche is None and self.droite is None:
            return 0
        # Vérifie si l'arbre a un seul sous-arbre (gauche ou droit) et si oui, on retourne la hauteur de ce sous-arbre + 1
        elif self.gauche is None:
            return 1 + self.droite.hauteur()
        elif self.droite is None:
            return 1 + self.gauche.hauteur()
        else:
            return 1 + max(self.gauche.hauteur(), self.droite.hauteur())
    
    # Méthode qui retourne la liste des valeurs de l'arbre en parcours préfixe
    def prefixe(self):
        # Vérifie si l'arbre est vide (s'il est vide, on retourne une liste vide)
        if self.estVide():
            return []
        else:
            # Vérifie si l'arbre est une feuille (s'il est une feuille, on retourne une liste contenant la valeur de la racine)
            result = [self.racine[0]]
            # Vérifie si l'arbre a un sous-arbre gauche et si oui, on ajoute les valeurs de ce sous-arbre à la liste result
            if self.gauche is not None:
                result += self.gauche.prefixe()
            # Vérifie si l'arbre a un sous-arbre droit et si oui, on ajoute les valeurs de ce sous-arbre à la liste result
            if self.droite is not None:
                result += self.droite.prefixe()
            return result
    
    # Méthode qui retourne la liste des valeurs de l'arbre en parcours infixe
    def infixe(self):
        if self.estVide():
            return []
        else:
            result = []
            if self.gauche is not None:
                result += self.gauche.infixe()
            result += [self.racine[0]]
            if self.droite is not None:
                result += self.droite.infixe()
            return result
    
    # Méthode qui retourne la liste des valeurs de l'arbre en parcours suffixe
    def suffixe(self):
        if self.estVide():
            return []
        else:
            result = []
            if self.gauche is not None:
                result += self.gauche.suffixe()
            if self.droite is not None:
                result += self.droite.suffixe()
            result += [self.racine[0]]
            return result
    
    # Méthode qui retourne True si l'arbre est un ABR, False sinon
    def estABR(self,):
        # Vérifie si l'arbre est vide
        if self.estVide():
            return True
        # Vérifie si l'arbre est une feuille
        elif self.gauche is None and self.droite is None:
            return True
        # Vérifie si l'arbre a un seul sous-arbre (gauche ou droit) et si les valeurs de l'arbre sont respectivement plus petites ou plus grandes que la valeur de la racine
        elif self.gauche is None:
            return self.racine[0] < self.droite.racine[0] and self.droite.estABR()
        elif self.droite is None:
            return self.racine[0] > self.gauche.racine[0] and self.gauche.estABR()
        else:
            # Vérifie si les valeurs de l'arbre sont respectivement plus petites ou plus grandes que la valeur de la racine et si les sous-arbres gauche et droit sont des ABR
            return self.racine[0] > self.gauche.racine[0] and self.racine[0] < self.droite.racine[0] and self.gauche.estABR() and self.droite.estABR()
    
    # Méthode qui retourne True si l'arbre est équilibré, False sinon (un arbre est équilibré si la différence de hauteur entre ses sous-arbres gauche et droit est au plus égale à 1)
    def estEquilibre(self):
        # Vérifie si l'arbre est vide
        if self.estVide():
            return True
        # Vérifie si l'arbre est une feuille
        elif self.gauche is None and self.droite is None:
            return True
        # Vérifie si l'arbre a un seul sous-arbre (gauche ou droit) et si la hauteur de ce sous-arbre est au plus égale à 0
        elif self.gauche is None:
            return self.droite.hauteur() <= 0 and self.droite.estEquilibre()
        elif self.droite is None:
            return self.gauche.hauteur() <= 0 and self.gauche.estEquilibre()
        # Vérifie si la différence de hauteur entre les sous-arbres gauche et droit est au plus égale à 1
        else:
            return abs(self.gauche.hauteur() - self.droite.hauteur()) <= 1 and self.gauche.estEquilibre() and self.droite.estEquilibre()


    # Créé un nouvel arbre avec la valeur de la racine de l'arbre actuel comme valeur de la racine, le sous-arbre gauche de l'arbre actuel comme sous-arbre gauche du nouveau arbre et le sous-arbre gauche du sous-arbre droit de l'arbre actuel comme sous-arbre droit du nouveau arbre
    # C'est pas très clair désolé
    def rotationGauche(self):
        # Vérifie si l'arbre a un sous-arbre droit
        if self.droite is None:
            return None
        newRacine = self.droite.racine
        newGauche = AB(self.racine[0], self.gauche, self.droite.gauche)
        self.racine = newRacine
        self.gauche = newGauche
        self.droite = self.droite.droite
        return self

    def rotationDroite(self):
        if self.gauche is None:
            return None
        newRacine = self.gauche.racine
        newDroite = AB(self.racine[0], self.gauche.droite, self.droite)
        self.racine = newRacine
        self.gauche = self.gauche.gauche
        self.droite = newDroite
        return self