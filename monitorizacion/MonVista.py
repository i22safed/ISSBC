# -*- coding: utf-8 -*-
"""
Created on Wed May 18 12:06:36 2016

@author: David Sanchez

@link: https://github.com/i22safed/monitorizacion

@desc: Vista de la tarea de monitorizacion ISSBC

"""

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import MonCtrl as ctrl

class MonitorizacionDlg(QtGui.QWidget):

    """
        @desc: Clase donde se codificara la interfaz de la aplicación

        @author: David Sanchez


    """

    def __init__(self):     # Constructor de la clase Vista

        super(MonitorizacionDlg, self).__init__()


        # Declaramos los elementos de la parrilla

        # Declaramos un elemento espaciador de 10 espacios

        self.labelEspacio = QtGui.QLabel(u"          ")

        # Declaramos los elementos de la zona de monitorizacion

        self.labelJustificacion = QtGui.QLabel(u"Justificación de la monitorización",self)
        self.cuadroJustificacion=QtGui.QPlainTextEdit()
        self.cuadroJustificacion.setReadOnly(True)

        # Descripcion del dominio

        self.labelDescripcionDominio = QtGui.QLabel(u"Descripcion del dominio",self)

        # Declaramos el selector de la semana

        self.labelComboBoxDominio=QtGui.QLabel("Dominio", self)
        self.comboBoxDominio = QtGui.QComboBox()
        self.comboBoxDominio.addItem("Invernadero")
        self.comboBoxDominio.addItem("Vivero")

        # Declaramos el selector de la semana

        self.labelComboBoxSemana=QtGui.QLabel("Semana", self)
        self.comboBoxSemana = QtGui.QComboBox()

        # Declaramos los botones de Monitorizar, Borrar y Salir y sus respectivas
        # señales

        self.monButtom = QtGui.QPushButton("Monitorizar")
        self.monButtom.clicked.connect(self.monitorizar)
        self.monButtom.setShortcut("Ctrl+M")

        self.delButtom = QtGui.QPushButton("Borrar")
        self.delButtom.clicked.connect()

        self.exitButtom = QtGui.QPushButton("Salir")
        self.exitButtom.clicked.connect(self.close)
        self.exitButtom.setShortcut('Ctrl+Q')

        # Declaramos 5 progress bar para los 5 parametros que poseemos

        self.labelTemp = QtGui.QLabel(u"Temperatura")
        self.progressBarTemp = QtGui.QProgressBar()
        self.progressBarTemp.setValue(25)

        self.labelHumTie = QtGui.QLabel(u"Humeddad del medio")
        self.progressBarHumTie = QtGui.QProgressBar()
        self.progressBarHumTie.setValue(33)

        self.labelPh = QtGui.QLabel(u"pH de la tierra")
        self.progressBarPh = QtGui.QProgressBar()
        self.progressBarPh.setValue(41)

        self.labelRiego = QtGui.QLabel(u"Frecuencia de riego")
        self.progressBarRiego = QtGui.QProgressBar()
        self.progressBarRiego.setValue(87)




        # Una vez declarada la etiqueta, declaramos a continuacion la tabla y su
        # respectiva estructura interna → CAMBIAR DEBERIA DE SER UNA FUNCION



        self.tablaWidgetDescripcionDominio= QtGui.QTableWidget(4,3)


        # Declaramos la parrilla y su respectivo espaciado

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(20)

        # Objetos que tendrá la parrilla


        # Espaciadores

        self.grid.addWidget(self.labelEspacio,1,1)
        self.grid.addWidget(self.labelEspacio,2,1)
        self.grid.addWidget(self.labelEspacio,1,2)
        self.grid.addWidget(self.labelEspacio,1,3)
        self.grid.addWidget(self.labelEspacio,1,4)
        self.grid.addWidget(self.labelEspacio,1,5)
        self.grid.addWidget(self.labelEspacio,1,4)
        self.grid.addWidget(self.labelEspacio,8,1)
        self.grid.addWidget(self.labelEspacio,8,2)
        self.grid.addWidget(self.labelEspacio,8,3)
        self.grid.addWidget(self.labelEspacio,8,4)
        self.grid.addWidget(self.labelEspacio,8,5)
        self.grid.addWidget(self.labelEspacio,1,8)
        self.grid.addWidget(self.labelEspacio,2,8)
        self.grid.addWidget(self.labelEspacio,3,8)
        self.grid.addWidget(self.labelEspacio,4,8)
        self.grid.addWidget(self.labelEspacio,6,8)
        self.grid.addWidget(self.labelEspacio,7,8)
        self.grid.addWidget(self.labelEspacio,8,9)
        self.grid.addWidget(self.labelEspacio,9,1)
        self.grid.addWidget(self.labelEspacio,9,2)
        self.grid.addWidget(self.labelEspacio,9,3)
        self.grid.addWidget(self.labelEspacio,9,4)
        self.grid.addWidget(self.labelEspacio,9,5)
        self.grid.addWidget(self.labelEspacio,9,6)
        self.grid.addWidget(self.labelEspacio,9,7)
        self.grid.addWidget(self.labelEspacio,9,8)
        self.grid.addWidget(self.labelEspacio,8,5)
        self.grid.addWidget(self.labelEspacio,10,1)
        self.grid.addWidget(self.labelEspacio,10,2)
        self.grid.addWidget(self.labelEspacio,10,3)
        self.grid.addWidget(self.labelEspacio,10,4)
        self.grid.addWidget(self.labelEspacio,10,5)
        self.grid.addWidget(self.labelEspacio,10,6)
        self.grid.addWidget(self.labelEspacio,10,7)
        self.grid.addWidget(self.labelEspacio,10,8)


        self.grid.addWidget(self.labelJustificacion,2,2)
        self.grid.addWidget(self.cuadroJustificacion,3,2,1,2)


        self.grid.addWidget(self.labelTemp,4,2)
        self.grid.addWidget(self.progressBarTemp,5,2)

        self.grid.addWidget(self.labelHumTie,4,3)
        self.grid.addWidget(self.progressBarHumTie,5,3)

        self.grid.addWidget(self.labelPh,6,2)
        self.grid.addWidget(self.progressBarPh,7,2)

        self.grid.addWidget(self.labelRiego,6,3)
        self.grid.addWidget(self.progressBarRiego,7,3)

        self.grid.addWidget(self.labelEspacio,1,3)

        self.grid.addWidget(self.labelDescripcionDominio,2,5)
        self.grid.addWidget(self.tablaWidgetDescripcionDominio,3,5,1,4)

        self.grid.addWidget(self.labelComboBoxDominio,4,5)
        self.grid.addWidget(self.comboBoxDominio,5,5,1,4)

        self.grid.addWidget(self.labelComboBoxSemana,6,5)
        self.grid.addWidget(self.comboBoxSemana,7,5,1,4)
        self.rellenaComboSemana()

        self.grid.addWidget(self.monButtom,9,6)
        self.grid.addWidget(self.delButtom,9,7)
        self.grid.addWidget(self.exitButtom,9,8)

        # La declaramos como principal

        self.setLayout(self.grid)

        # Para que se vea la ventana

        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle("Tarea de monitorizacion")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()

        """
        Temperatura, Humedad aire, Humedad Tierra , Veces de riego, y pH

        """

    def monitorizar(self):

            explicacion = "Esto funca"

            self.cuadroJustificacion.clear()
            self.cuadroJustificacion.appendPlainText(explicacion)
            self.cuadroJustificacion.moveCursor(QtGui.QTextCursor.Start)

    def rellenaComboSemana(self):

            nombreFichero = "invernadero/invernaderoPh.txt"

            nEleCombo=["1","2","3","4","5","6","7","8","9","10","11","12","13",
            "14","15","16","17","18","19","20"]

            fichero = open(nombreFichero, 'r')

            i=0

            for linea in fichero:
                self.comboBoxSemana.addItem(nEleCombo[i])
                i+=1

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    form = MonitorizacionDlg()
    sys.exit(app.exec_())
