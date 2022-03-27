
from turtle import width
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTranslator, QCoreApplication
from PyQt5.QtGui import QKeySequence,  QBrush, QColor

import markdown
from pymysql import NULL

import commands


class Markdown2HTML(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('app\mainInterface.ui', self) #Carga la interfaz (Hecha en Qt designer)

        self.formLayout.addRow(self.tr("&Nombre"), self.nameEdit)
        self.formLayout.addRow(self.tr("&Dirección"), self.addressEdit)

        ## 
        
        self.currentFileName="new_file.txt"

        self.fileSelected=False

        self.translator=QTranslator()
        self.graphicScene= QtWidgets.QGraphicsScene(backgroundBrush=QBrush(QColor(111,111,111)))
        self.graphicScene.width=self.graphicsView.width()
        self.graphicScene.height=self.graphicsView.height()
        
        self.graphicsView.setScene(self.graphicScene)

        self.undoView=NULL

        self.createActions()
        self.createMenus()

        

    def createActions(self):
        ## Undo & Redo

        self.undoStack = QtWidgets.QUndoStack(self)
        self.undoAction = self.undoStack.createUndoAction(self, self.tr("&Undo"))
        self.undoAction.setShortcuts(QKeySequence.Undo)
        self.redoAction = self.undoStack.createRedoAction(self, self.tr("&Redo"))
        self.redoAction.setShortcuts(QKeySequence.Redo)

        #GraphicViewer

        self.addBoxAction = QtWidgets.QAction(self.tr("Add &Box"))
        self.addBoxAction.setShortcut(QKeySequence("Ctrl+O"))
        self.addBoxAction.triggered.connect(self.addBoxFunction)
        

        self.addTriangleAction = QtWidgets.QAction(self.tr("Add &Triangle"))
        self.addTriangleAction.setShortcut(QKeySequence("Ctrl+T"))
        self.addTriangleAction.triggered.connect(self.addTriangleFunction)


    def addBoxFunction(self):
        addCommand = commands.AddCommand("Box",self.graphicScene)  
        self.undoStack.push(addCommand)
        self.graphicsView.update()

    def addTriangleFunction(self):
        addCommand = commands.AddCommand("Triangle",self.graphicScene)  
        self.undoStack.push(addCommand)
        self.graphicsView.update()


    def createMenus(self):
        ## Undo & Redo
        self.undoButton.setDefaultAction(self.undoAction)
        self.redoButton.setDefaultAction(self.redoAction)
        self.undoListButton.clicked.connect(self.showUndoList)

        self.nameEdit.editingFinished.connect(self.storeFieldText)
        self.addressEdit.editingFinished.connect(self.storeFieldText)
    

        ## Conexión de botones con sus funciones
        self.newFileButton.clicked.connect(self.newFile)
        self.openButton.clicked.connect(self.openTxtFile) 
        self.saveButton.clicked.connect(self.saveFunction)
        self.convertButton.clicked.connect(self.convertFunction)
        self.languagePickerButton.clicked.connect(self.pickLanguage)

        ## GraficViewer
        self.itemMenu= QtWidgets.QMenuBar()
        self.horizontalLayout_11.addWidget(self.itemMenu)
        self.itemMenu.addAction(self.addBoxAction)
        self.itemMenu.addAction(self.addTriangleAction)
        

    def storeFieldText(self):   
        textCommand = commands.TextCommand(self.sender())  
        self.undoStack.push(textCommand)

    def showUndoList(self):
        if (self.undoView==NULL):
            self.undoView = QtWidgets.QUndoView(self.undoStack,self.centralwidget)
            self.undoView.setObjectName(u"undoView")
            self.horizontalLayout.addWidget(self.undoView)
        
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
        self.fileSelected=True

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
        self.languagePickerButton.setText(QCoreApplication.translate("Markdown2HTML", u"Idioma", None))
        if(not self.fileSelected):
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

    
