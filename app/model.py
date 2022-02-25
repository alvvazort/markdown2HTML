
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui
import markdown


class Markdown2HTML(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app\mainInterface.ui', self) #Carga la interfaz (Hecha en Qt designer)
        
        self.currentFileName=""
        ## Conexión de botones con sus funciones
        self.openButton.clicked.connect(self.openTxtFile) 
        self.saveButton.clicked.connect(self.saveFunction)
        self.convertButton.clicked.connect(self.convertFunction)
        
    
    def openTxtFile(self):
        picker = txtPicker(self).get_widget()
        picker.fileSelected.connect(self.textFileSelected)
        picker.show()
        return picker

    def textFileSelected(self, file):
        self.currentFile.setText(file)
        self.currentFileName=file

        text=open(file).read()
        self.textEditor.setPlainText(text) #Escribir texto en el editor

    def saveFunction(self):
        print("Saving...")
        print(self.currentFileName)
        #Obtener el texto del editor y guardarlo en el archivo
        file = open("myfile.txt", "w")
        file.write(self.textEditor.toPlainText())
        file.close()

    def convertFunction(self):
        print("Converting...")

class txtPicker:
    def __init__(self, ui):
        self.ui = ui

    def get_widget(self):
        picker = QtWidgets.QFileDialog(self.ui)
        picker.setMimeTypeFilters(['text/plain'])
        return picker
