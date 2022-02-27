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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_Markdown2HTML(object):
    def setupUi(self, Markdown2HTML):
        if not Markdown2HTML.objectName():
            Markdown2HTML.setObjectName(u"Markdown2HTML")
        Markdown2HTML.resize(1080, 800)
        icon = QIcon()
        icon.addFile(u"../icons/markdown-icon-23.png", QSize(), QIcon.Normal, QIcon.Off)
        Markdown2HTML.setWindowIcon(icon)
        Markdown2HTML.setAnimated(True)
        self.centralwidget = QWidget(Markdown2HTML)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.newFileButton = QPushButton(self.centralwidget)
        self.newFileButton.setObjectName(u"newFileButton")
        icon1 = QIcon()
        icon1.addFile(u"../icons/new-file-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newFileButton.setIcon(icon1)
        self.newFileButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.newFileButton)

        self.openButton = QPushButton(self.centralwidget)
        self.openButton.setObjectName(u"openButton")
        icon2 = QIcon()
        icon2.addFile(u"../icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openButton.setIcon(icon2)
        self.openButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.openButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        icon3 = QIcon()
        icon3.addFile(u"../icons/Save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon3)
        self.saveButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.saveButton)

        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        icon4 = QIcon()
        icon4.addFile(u"../icons/md-to-html.png", QSize(), QIcon.Normal, QIcon.Off)
        self.convertButton.setIcon(icon4)
        self.convertButton.setIconSize(QSize(50, 25))

        self.horizontalLayout.addWidget(self.convertButton)

        self.languagePickerButton = QPushButton(self.centralwidget)
        self.languagePickerButton.setObjectName(u"languagePickerButton")

        self.horizontalLayout.addWidget(self.languagePickerButton)

        self.currentFile = QLabel(self.centralwidget)
        self.currentFile.setObjectName(u"currentFile")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentFile.sizePolicy().hasHeightForWidth())
        self.currentFile.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.currentFile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_2)

        self.textEditor = QPlainTextEdit(self.centralwidget)
        self.textEditor.setObjectName(u"textEditor")

        self.horizontalLayout_2.addWidget(self.textEditor)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.htmlDisplayer = QTextEdit(self.centralwidget)
        self.htmlDisplayer.setObjectName(u"htmlDisplayer")

        self.horizontalLayout_2.addWidget(self.htmlDisplayer)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        Markdown2HTML.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Markdown2HTML)
        self.statusbar.setObjectName(u"statusbar")
        Markdown2HTML.setStatusBar(self.statusbar)

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
    # retranslateUi

