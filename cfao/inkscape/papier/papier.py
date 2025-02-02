#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Copyright 2012 Sebastien Celles <s.celles@gmail.com>

This file is part of Papier Extension for Inkscape.

Papier Extension for Inkscape is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Papier Extension for Inkscape is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Papier Extension for Inkscape. If not, see http://www.gnu.org/licenses/.
'''

# Les deux lignes suivantes sont necessaires seulement si le script n'est pas 
#  directement dans le dossier d'installation
import sys
#sys.path.append('/usr/share/inkscape/extensions')

# Utilisation du module inkex avec des effets predefinis
import inkex 
# Le module simplestyle fournit des fonctions pour le parsing des styles
from simplestyle import *
from simpletransform import *

class CPapier( inkex.Effect ):
	"""
	Exemple Inkscape 
	Cree un nouveau calque et dessine des elements de base
	"""
	def __init__(self):
		"""
		Constructeur
		Definit l'option "--strTexte" du script
		"""
		# Appel du constructeur.
		inkex.Effect.__init__(self)

		# Definit la chaine d'option "--strTexte" avec le raccourci "-w" et 
		#  la valeur par defaut "Hello".
		self.OptionParser.add_option('-w', '--strTexte', action = 'store',
		                             type = 'string', 
		                             dest = 'strTexte', default = 'Hello',
		                             help = 'Message a ecrire ?')

	def get_xval(self, x):
		return(float(x)/self.scaleX+self.x0)

	def get_yval(self, y):
		return(float(y)/self.scaleX+self.y0)

	def drawtext(self, layer, x, y, msg, RGB, size):		
		texte = inkex.etree.Element(inkex.addNS('text', 'svg'))
		texte.text = msg
		texte.set('x', str( str(float(x)/self.scaleX+self.x0) + 'mm' ) )
		texte.set('y', str( str(float(y)/self.scaleY+self.y0) + 'mm' ) )
		style = {'text-align' : 'center', \
		         'text-anchor': 'center', \
		         'font-size': size,\
		         'fillstyle': 'rgb(255,255,0)',\
		         'fill': RGB}
		texte.set('style', formatStyle(style) )
		layer.append( texte ) # Ajoute le texte au calque


	def drawpoint(self, layer, x, y, rayon=1, RGB='rgb(0,0,255)'):
		cercle = inkex.etree.Element(inkex.addNS('circle','svg'))
		cercle.set('cx', str(float(x)/self.scaleX+self.x0) + 'mm')
		cercle.set('cy', str(float(y)/self.scaleY+self.y0) + 'mm')
		cercle.set('r', str(rayon) + 'mm')
		cercle.set('fill', RGB)
		cercle.set('stroke', RGB)
		cercle.set('stroke-width', '1px')
		layer.append(cercle)

	def drawline_extrapo(self, layer, x1, y1, x2, y2, x_ex1, x_ex2, RGB='rgb(10,10,10)', strokewidth='1px', show_point=False):
		a = float(y2 - y1) / float(x2 - x1)
		#a = a * (-self.scaleY)
		y_ex1 = a * (x_ex1 - x1) + y1
		y_ex2 = a * (x_ex2 - x1) + y1
		self.drawline(layer, x_ex1, y_ex1, x_ex2, y_ex2, RGB, strokewidth)
		self.drawpoint(layer, x1, y1, 1, RGB)
		self.drawpoint(layer, x2, y2, 1, RGB)
	
	def drawline(self, layer, x1, y1, x2, y2, RGB='rgb(10,10,10)', strokewidth='1px'):
		line = inkex.etree.Element(inkex.addNS('line', 'svg'))
		line.set('stroke', RGB);
		line.set('stroke-width', strokewidth );
		line.set('x1', str(float(x1)/self.scaleX+self.x0) + 'mm' )
		line.set('y1', str(float(y1)/self.scaleY+self.y0) + 'mm' )
		line.set('x2', str(float(x2)/self.scaleX+self.x0) + 'mm' )
		line.set('y2', str(float(y2)/self.scaleY+self.y0) + 'mm' );
		layer.append( line ) # Ajout de la ligne sur le calque
	
	def effect(self):
		"""
		Fonction principale
		Surchage la fonction de la classe de base
		Dessine quelques elements sur le document SVG
		"""
		# Recupere le document SVG principal
		svg = self.document.getroot()

		# Recuperation de la hauteur et de la largeur de la feuille
		width  = inkex.unittouu( svg.get('width') )
		height = inkex.unittouu( svg.attrib['height'] )
		
		# Reglage unite en mm
		# ToDo
		
		
		# Creation d'un nouveau calque
		layer = inkex.etree.SubElement(svg, 'g')
		layer.set(inkex.addNS( 'label', 'inkscape'), 'Layer texte' )
		layer.set(inkex.addNS( 'groupmode', 'inkscape'), 'layer' )
		
		# Creation d'un element texte
		#texte = inkex.etree.Element(inkex.addNS('text', 'svg'))
		# - Recuperation de la valeur de la variable "strTexte" saisie dans la 
		#    boite de dialogue
		#strVal = self.options.strTexte
		#strVal = "Oscillogramme"
		#texte.text = strVal
		
		# Reglages initiaux
		#x_org = 0
		#y_org = 50
		#pas_x = width / 6
		#pas_y = width / 10

		#texte = inkex.etree.Element(inkex.addNS('text', 'svg'))
		#texte.text = strVal
		
		# Set text position to center of document.
		#texte.set('x', str( x_org ) )
		#texte.set('y', str( y_org ) )
		
		# Center text horizontally with CSS style.
		#style = {'text-align' : 'left', \
		#         'text-anchor': 'top', \
		#         'font-size': '48pt',\
		#         'fill':'rgb(255, 0, 0)'}
		#texte.set('style', formatStyle(style) )
		
		# Ajoute le texte au calque
		#layer.append( texte )
		
		# origine (haut-gauche)
		self.x0 = 5 # mm
		self.y0 = 290 # mm

		self.x0 = self.x0 + 60 # mm
		self.y0 = self.y0 - 10 # mm

		#inkex.debug("x0 = %f" % (self.x0))
		#inkex.debug("y0 = %f" % (self.y0))

		#self.x0 = 205 # mm
		#self.y0 = 490 # mm
		
		self.scaleX = 1
		self.scaleY = -1		
		
		#papier_width = 200
		#papier_height = 250
		
		#papier_width = 150
		#papier_height = 120

		papier_width = 120
		papier_height = 260

		# 5 cm
		couleur0 = 'rgb(5,5,5)'
		strokewidth0 = '2px'

		# 1 cm
		couleur1 = 'rgb(5,5,5)'
		strokewidth1 = '1.2px'

		# 5 mm
		couleur2 = 'rgb(100,100,100)'
		strokewidth2 = '1.2px'

		# 1 mm
		couleur3 = 'rgb(127,127,127)'
		strokewidth3 = '1px'

		# Creation des lignes horizontales secondaires (1mm)
		for i in range(0,papier_height/10,1):
			for k in range(1,10):
				self.drawline(layer, 0, i*10+k, papier_width, i*10+k, couleur3, strokewidth3)

		# Creation des lignes verticales secondaires (1mm)
		for j in range(0,papier_width/10,1):
			for k in range(1,10):
				self.drawline(layer, j*10+k, 0, j*10+k, papier_height, couleur3, strokewidth3)

		# Creation des lignes horizontales secondaires (5mm)
                k = 5
		for i in range(0,papier_height/10,1):
                        self.drawline(layer, 0, i*10+k, papier_width, i*10+k, couleur2, strokewidth2)

		# Creation des lignes horizontales verticales (5mm)
                k = 5
		for j in range(0,papier_width/10,1):
			self.drawline(layer, j*10+k, 0, j*10+k, papier_height, couleur2, strokewidth2)

		Xorigin = 0
		Yorigin = 0
		
		for i in range(0,papier_height+10,10):
			if ((i-Yorigin)%50)<>0: # Creation des lignes horizontales primaires (1cm)
				self.drawline(layer, 0, i, papier_width, i, couleur1,strokewidth1)
			else: # Creation des lignes horizontales primaires (5cm)
				self.drawline(layer, 0, i, papier_width, i, couleur0,strokewidth0)

		for j in range(0,papier_width+10,10):
			if ((j-Xorigin)%50)<>0: # Creation des lignes verticales primaires (1cm)
				self.drawline(layer, j, 0, j, papier_height, couleur1, strokewidth1)
			else: # Creation des lignes verticales (5cm)
				self.drawline(layer, j, 0, j, papier_height, couleur0, strokewidth0)
		
		# Creation des axes
		colorCustom0 = 'rgb(0,0,0)' # axes
		
		colorAxes = colorCustom0
		self.drawline(layer, Xorigin, 0, Xorigin, papier_height, colorAxes, '3px') # axe ordonnees
		self.drawline(layer, 0, Yorigin, papier_width, Yorigin, colorAxes, '3px') # axe abscisses
		self.drawtext(layer, -5+Xorigin + 2.5, papier_height + 2.5, 'U (V)', colorAxes, '12pt')		# Etiquette nom axe Y
		self.drawtext(layer, papier_width + 2.5, -1.4+Yorigin, 'I (A)', colorAxes, '12pt')		# Etiquette nom axe X
		#self.drawtext(layer, papier_width-5, Yorigin+2.5, 'I (A)', colorAxes, '12pt')		# Etiquette nom axe X

		YmajorTick = 50
		YminorTickNb = 5
		colorTick = colorCustom0
		for i in range(0, (papier_height + YmajorTick)//YmajorTick):
			y = i*YmajorTick+Yorigin
			self.drawline(layer, -2.5+Xorigin, y, Xorigin, y, colorTick,'2px')
			if i<>0: # tofix
				for k in range(1, YminorTickNb):
					y = i*YmajorTick+Yorigin-k*YmajorTick/YminorTickNb
					#if y>=self.get_yval(0) and y<self.get_yval(papier_height):
					self.drawline(layer, -1.5+Xorigin, y, Xorigin, y, colorTick,'2px')

		XmajorTick = 50
		XminorTickNb = 5
		colorTick = colorCustom0
		for j in range(0, (papier_width + XmajorTick)//XmajorTick):
			x = j*XmajorTick+Xorigin
			self.drawline(layer, x, -2.5+Yorigin, x, Yorigin, colorTick,'2px')
			if j<>0: # tofix
				for k in range(1, YminorTickNb):
					x = j*XmajorTick+Xorigin-k*XmajorTick/XminorTickNb
					#if x>=self.get_xval(0) and x<=self.get_xval(papier_width):
					self.drawline(layer, x, -1.5+Yorigin, x, Yorigin, colorTick,'2px')

		colorWrite = colorCustom0
		#self.drawtext(layer, 0.5*papier_width, 0.85*papier_height, 'Titre du graphique', 'rgb(255, 0, 0)', '18pt')		# Etiquette titre graphique
		self.drawtext(layer, -0.30*papier_width, 1.12*papier_height, 'Nom : ........................', colorWrite, '18pt')		# Etiquette titre graphique
		self.drawtext(layer, 0.35*papier_width, 1.12*papier_height, 'Prenom : ........................', colorWrite, '18pt')		# Etiquette titre graphique
		
		matrix = parseTransform('rotate(45)')
		
		self.drawtext(layer, 0, 1.07*papier_height, 'Montage : ...........................................', colorWrite, '18pt')		# Etiquette titre graphique

		# Creation du texte sur axe ordonnees

		# Creation du texte sur axe abscisses
		
		# Nouvelle origine
		
		self.x0 = self.x0 + Xorigin # tjs en mm par rapport au Haut-Gauche
		self.y0 = self.y0 - Yorigin # tjs en mm par rapport au Haut-Gauche
		
		self.scaleX = 1  # 1 cm = scaleX UniteX
		self.scaleY = -0.1 # 1 cm = 10mm = scaleY UniteY

		#self.drawline(layer, 0, 0, 10, 20, 'rgb(0,255,0)', '3px')
		
		#self.drawline(layer, 0, 12, 100, 10, 'rgb(0,255,0)', '3px')
		#self.drawline_extrapo(layer, 0, 12, 100, 10, -1, 13, 'rgb(0,255,255)', '3px')
		
		# Trace des points experimentaux, de la modelisation lineaire, ...
		#self.drawpoint(layer, 0, 0, 1, 'rgb(0,0,255)')
		#self.drawpoint(layer, 10, 20, 1, 'rgb(0,255,255)')
		
		# Trace de courbe		

# Execute la fonction "effect" de la classe "CHello"
drawing = CPapier()
drawing.affect()