# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:06:35 2016

@author: David Sanchez

@link: https://github.com/i22safed/monitorizacion

@desc: Controlador de la tarea de monitorizacion ISSBC

"""

__docformat__ = "restructuredtext"

from PyQt4 import QtGui
import MonMod as ma

def eventoMonitorizar(dominio):
	"""
	Metodo encargado de ejecutar el metodo para monitorizar
	indicando el dominio

	:param dominio: Dominio en el que se va a monitorizar

	:author: Michael Castillo Polo y Luis Miguel López Coleto
	:date: 10/06/2015
	"""

	mp = ma.MonitorizacionDlg()
	return mp.execute()
