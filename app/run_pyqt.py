import sys

from PyQt5.QtWidgets import QApplication

import model


def main():
    app = QApplication(sys.argv)
    form = model.Markdown2HTML() #Crea la interfaz y el modelo de la aplicación
    
    form.show()
    
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window')


if __name__ == '__main__':
    main()
