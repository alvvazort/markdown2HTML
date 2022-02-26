
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui
import markdown


class Markdown2HTML(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app\mainInterface.ui', self) #Carga la interfaz (Hecha en Qt designer)
        
        self.currentFileName="new_file.txt"

        ## Conexión de botones con sus funciones
        self.newFileButton.clicked.connect(self.newFile)
        self.openButton.clicked.connect(self.openTxtFile) 
        self.saveButton.clicked.connect(self.saveFunction)
        self.convertButton.clicked.connect(self.convertFunction)
        
    def newFile(self):
        picker = txtCreator(self).get_widget()
        picker.fileSelected.connect(self.textFileCreate)
        picker.show()
        return picker

    def openTxtFile(self):
        picker = txtPicker(self).get_widget()
        picker.fileSelected.connect(self.textFileSelected)
        picker.show()
        return picker

    def textFileCreate(self, file):
        self.currentFile.setText(file)
        self.currentFileName=file
        file = open(self.currentFileName, "w")
        file.write(self.textEditor.toPlainText())
        file.close()



    def textFileSelected(self, file):
        self.currentFile.setText(file)
        self.currentFileName=file

        text=open(file).read()
        self.textEditor.setPlainText(text) #Escribir texto en el editor

    def saveFunction(self): #Guarda el archivo (txt o markdown)
        print("Saving...")
        print(self.currentFileName)
        #Obtener el texto del editor y guardarlo en el archivo
        file = open(self.currentFileName, "w")
        file.write(self.textEditor.toPlainText())
        file.close()

    def convertFunction(self): #Convierte el texto en markdown a html, lo guarda en html/markdown.html y lo muestra en pantalla
        print("Converting...")
        self.saveFunction()

        file = open(self.currentFileName, "r")

        textInHtml= markdown.markdown(file.read())
        
        self.htmlDisplayer.setHtml(textInHtml)
        file = open("html\markdown.html","w")
        file.write(textInHtml)
        file.close()
        

class txtPicker: #Ventana de dialogo para abrir txt
    def __init__(self, ui):
        self.ui = ui

    def get_widget(self):
        picker = QtWidgets.QFileDialog(self.ui)
        picker.setMimeTypeFilters(['text/markdown','text/plain'])
        return picker

class txtCreator: #Ventana de dialogo para crear txt
    def __init__(self, ui):
        self.ui = ui

    def get_widget(self):
        picker = QtWidgets.QFileDialog(self.ui)
        picker.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
        picker.setMimeTypeFilters(['text/markdown','text/plain'])
        return picker
