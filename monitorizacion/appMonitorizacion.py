# -*- coding: utf-8 -*-
"""
Created on Thu May 19 18:56:17 2016

@author: David Sanchez

@desc: Lanzador de la aplicacion de monitorizacion

"""
import sys
from PyQt4 import QtGui
import MonVista as vts

app = QtGui.QApplication(sys.argv) #Crea una aplicación
form = vts.MonitorizacionDlg()   #Crea una instancia del formulario
sys.exit(app.exec_())   #Se inicia la aplicación y se espera eventos
