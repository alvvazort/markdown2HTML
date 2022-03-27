

from PyQt5 import QtWidgets
from PyQt5.QtCore import QPointF
from numpy import delete
import diagramItem
import datetime
class TextCommand(QtWidgets.QUndoCommand):

    def __init__(self, field):
    
        QtWidgets.QUndoCommand.__init__(self)
        
        # Record the field that has changed.
        self.field = field
        # Record the text at the time the command was created.
        self.text = field.text()
        self.setText(self.text) # Show in undoView this text

    def undo(self):
     
        # Remove the text from the file and set it in the field.
        # ...
        self.field.setText(self.text)
     
    def redo(self):
     
        # Store the text in the file and set it in the field.
        # ...
        self.field.setText(self.text)

class AddCommand(QtWidgets.QUndoCommand):

    def __init__(self,diagramType,diagramScene):
        super().__init__()
        self.diagramItem= diagramItem.DiagramItem(diagramType)
        self.diagramScene= diagramScene

        self.initialPosition = QPointF((datetime.datetime.now().second * 15) % diagramScene.width, (datetime.datetime.now().second * 15) % diagramScene.height)
        self.diagramItem.setPos(self.initialPosition)


        self.diagramScene.update()
        
        self.setText(""+diagramType+" added")

    def AddCommand(self):
        if not self.diagramItem.scene():
            del self.diagramItem

    def undo(self):
        self.diagramScene.removeItem(self.diagramItem)
        self.diagramScene.update()
        print("undo")

    def redo(self):
        self.diagramScene.addItem(self.diagramItem)
        self.diagramItem.setPos(self.initialPosition)
        self.diagramScene.update()
        print("redo")