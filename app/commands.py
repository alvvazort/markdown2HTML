

from PyQt5 import QtWidgets

class TextCommand(QtWidgets.QUndoCommand):

    def __init__(self, field):
    
        QtWidgets.QUndoCommand.__init__(self)
        
        # Record the field that has changed.
        self.field = field
        
        # Record the text at the time the command was created.
        self.text = field.text()

    def undo(self):
     
        # Remove the text from the file and set it in the field.
        # ...
        self.field.setText(self.text)
     
    def redo(self):
     
        # Store the text in the file and set it in the field.
        # ...
        self.field.setText(self.text)