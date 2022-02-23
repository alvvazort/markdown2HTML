import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Markdown2HTML(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainInterface.ui', self) #Carga la interfaz (Hecha en Qt designer)

    

def main():
    app = QApplication(sys.argv)
    form = Markdown2HTML() #Crea la ventana de la aplicación
    form.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window')


if __name__ == '__main__':
    main()
