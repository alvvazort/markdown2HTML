
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTranslator, QCoreApplication
import markdown


class Markdown2HTML(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app\mainInterface.ui', self) #Carga la interfaz (Hecha en Qt designer)
        
        self.currentFileName="new_file.txt"

        self.translator=QTranslator()
    
        ## Conexión de botones con sus funciones
        self.newFileButton.clicked.connect(self.newFile)
        self.openButton.clicked.connect(self.openTxtFile) 
        self.saveButton.clicked.connect(self.saveFunction)
        self.convertButton.clicked.connect(self.convertFunction)
        self.languagePickerButton.clicked.connect(self.pickLanguage)
        
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

    def pickLanguage(self): # Se abre un seleccionador de idioma y con lo que se devuelva traducimos.
        picker = languajePicker(self).get_widget(self)
        [idiomaSeleccionado, confirmacion] =picker
        if confirmacion: # Cambiamos idioma
            if idiomaSeleccionado=="English":
                self.translator.load("app/locale/english.qm")
                QCoreApplication.installTranslator(self.translator)
            elif idiomaSeleccionado=="Português":
                self.translator.load("app/locale/português.qm")
                QCoreApplication.installTranslator(self.translator)
            else:
                QCoreApplication.removeTranslator(self.translator)

        self.translateUi(self)

        return picker

    def translateUi(self, Markdown2HTML):
        Markdown2HTML.setWindowTitle(QCoreApplication.translate("Markdown2HTML", u"Markdown2HTML", None))
        self.newFileButton.setText("")
        self.openButton.setText("")
        self.saveButton.setText("")
        self.convertButton.setText("")
        self.languagePickerButton.setText(QCoreApplication.translate("Markdown2HTML", u"Language", None))
        self.currentFile.setText(QCoreApplication.translate("Markdown2HTML", u"Ning\u00fan archivo seleccionado", None))
    # retranslateUi

    

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

class languajePicker: #Ventana para escoger el idioma
    def __init__(self, ui):
        self.ui = ui

    def get_widget(self,mainWindow):
        picker = QtWidgets.QInputDialog(self.ui).getItem(None,"Language","Select a language", ["Español","English","Português"])
        
        #picker.addAction("Español")
        #picker.addAction("English")
        #picker.addAction("Português")

        return picker

    
