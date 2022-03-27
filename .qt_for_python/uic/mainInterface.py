# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainInterface.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QTextEdit,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Markdown2HTML(object):
    def setupUi(self, Markdown2HTML):
        if not Markdown2HTML.objectName():
            Markdown2HTML.setObjectName(u"Markdown2HTML")
        Markdown2HTML.resize(1089, 864)
        icon = QIcon()
        icon.addFile(u"../icons/markdown-icon-23.png", QSize(), QIcon.Normal, QIcon.Off)
        Markdown2HTML.setWindowIcon(icon)
        Markdown2HTML.setAnimated(True)
        self.centralwidget = QWidget(Markdown2HTML)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 1071, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line_9 = QFrame(self.verticalLayoutWidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        
        self.horizontalLayout_7.addWidget(self.line_9)

        self.newFileButton = QPushButton(self.verticalLayoutWidget)
        self.newFileButton.setObjectName(u"newFileButton")
        icon1 = QIcon()
        icon1.addFile(u"../icons/new-file-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newFileButton.setIcon(icon1)
        self.newFileButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.newFileButton)

        self.openButton = QPushButton(self.verticalLayoutWidget)
        self.openButton.setObjectName(u"openButton")
        icon2 = QIcon()
        icon2.addFile(u"../icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openButton.setIcon(icon2)
        self.openButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.openButton)

        self.saveButton = QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName(u"saveButton")
        icon3 = QIcon()
        icon3.addFile(u"../icons/Save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon3)
        self.saveButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_7.addWidget(self.saveButton)

        self.convertButton = QPushButton(self.verticalLayoutWidget)
        self.convertButton.setObjectName(u"convertButton")
        icon4 = QIcon()
        icon4.addFile(u"../icons/md-to-html.png", QSize(), QIcon.Normal, QIcon.Off)
        self.convertButton.setIcon(icon4)
        self.convertButton.setIconSize(QSize(50, 25))

        self.horizontalLayout_7.addWidget(self.convertButton)

        self.languagePickerButton = QPushButton(self.verticalLayoutWidget)
        self.languagePickerButton.setObjectName(u"languagePickerButton")

        self.horizontalLayout_7.addWidget(self.languagePickerButton)

        self.currentFile = QLabel(self.verticalLayoutWidget)
        self.currentFile.setObjectName(u"currentFile")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentFile.sizePolicy().hasHeightForWidth())
        self.currentFile.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.currentFile)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.line_10 = QFrame(self.verticalLayoutWidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_10)

        self.textEditor = QPlainTextEdit(self.verticalLayoutWidget)
        self.textEditor.setObjectName(u"textEditor")

        self.horizontalLayout_8.addWidget(self.textEditor)

        self.line_11 = QFrame(self.verticalLayoutWidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_11)

        self.htmlDisplayer = QTextEdit(self.verticalLayoutWidget)
        self.htmlDisplayer.setObjectName(u"htmlDisplayer")

        self.horizontalLayout_8.addWidget(self.htmlDisplayer)

        self.line_12 = QFrame(self.verticalLayoutWidget)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.VLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_12)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(470, 430, 151, 20))
        self.label.setTextFormat(Qt.MarkdownText)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 450, 531, 31))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.undoButton = QToolButton(self.horizontalLayoutWidget_2)
        self.undoButton.setObjectName(u"undoButton")
        icon5 = QIcon()
        icon5.addFile(u"../icons/undo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.undoButton.setIcon(icon5)
        self.undoButton.setPopupMode(QToolButton.InstantPopup)

        self.horizontalLayout_11.addWidget(self.undoButton)

        self.undoListButton = QPushButton(self.horizontalLayoutWidget_2)
        self.undoListButton.setObjectName(u"undoListButton")
        icon6 = QIcon()
        icon6.addFile(u"../icons/Arrow-down.svg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.undoListButton.setIcon(icon6)
        self.undoListButton.setIconSize(QSize(15, 15))

        self.horizontalLayout_11.addWidget(self.undoListButton)

        self.redoButton = QToolButton(self.horizontalLayoutWidget_2)
        self.redoButton.setObjectName(u"redoButton")
        icon7 = QIcon()
        icon7.addFile(u"../icons/redo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.redoButton.setIcon(icon7)
        self.redoButton.setPopupMode(QToolButton.DelayedPopup)
        self.redoButton.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.horizontalLayout_11.addWidget(self.redoButton)

        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(560, 770, 501, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.addressEdit = QLineEdit(self.formLayoutWidget)
        self.addressEdit.setObjectName(u"addressEdit")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.addressEdit)

        self.nameEdit = QLineEdit(self.formLayoutWidget)
        self.nameEdit.setObjectName(u"nameEdit")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameEdit)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(560, 490, 501, 261))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 490, 531, 341))
        Markdown2HTML.setCentralWidget(self.centralwidget)
        self.retranslateUi(Markdown2HTML)

        QMetaObject.connectSlotsByName(Markdown2HTML)
    # setupUi

    def retranslateUi(self, Markdown2HTML):
        Markdown2HTML.setWindowTitle(QCoreApplication.translate("Markdown2HTML", u"Markdown2HTML", None))
        self.newFileButton.setText("")
        self.openButton.setText("")
        self.saveButton.setText("")
        self.convertButton.setText("")
        self.languagePickerButton.setText(QCoreApplication.translate("Markdown2HTML", u"Idioma", None))
        self.currentFile.setText(QCoreApplication.translate("Markdown2HTML", u"Ning\u00fan archivo seleccionado", None))
        self.label.setText(QCoreApplication.translate("Markdown2HTML", u"**Prueba de Undo y Redo**", None))
        self.undoButton.setText("")
        self.undoListButton.setText("")
        self.redoButton.setText("")
    # retranslateUi

