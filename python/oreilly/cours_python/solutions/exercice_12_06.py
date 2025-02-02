#! /usr/bin/env python
# -*- coding: Latin-1 -*-

# Classes d�riv�es - polymorphisme

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        return 3.1416 * self.rayon**2
        
class Cylindre(Cercle):
    def __init__(self, rayon, hauteur):
        Cercle.__init__(self, rayon)
        self.hauteur = hauteur
        
    def volume(self):
        return self.surface()*self.hauteur
        
        # la m�thode surface() est h�rit�e de la classe parente
        
class Cone(Cylindre):
    def __init__(self, rayon, hauteur):
        Cylindre.__init__(self, rayon, hauteur)
                
    def volume(self):
        return Cylindre.volume(self)/3
        
        # cette nouvelle m�thode volume() remplace celle que
        # l'on a h�rit�e de la classe parente (exemple de polymorphisme)

# Programme test :

cyl = Cylindre(5, 7)
print "Surf. de section du cylindre =", cyl.surface()
print "Volume du cylindre =", cyl.volume()

co = Cone(5,7)
print "Surf. de base du c�ne =", co.surface()
print "Volume du c�ne =", co.volume()
