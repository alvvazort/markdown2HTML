# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainInterface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ImageViewerWindow(object):
    def setupUi(self, ImageViewerWindow):
        if not ImageViewerWindow.objectName():
            ImageViewerWindow.setObjectName(u"ImageViewerWindow")
        ImageViewerWindow.resize(1080, 800)
        self.centralwidget = QWidget(ImageViewerWindow)
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

        self.openButton = QPushButton(self.centralwidget)
        self.openButton.setObjectName(u"openButton")
        icon = QIcon()
        icon.addFile(u"../icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openButton.setIcon(icon)
        self.openButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.openButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        icon1 = QIcon()
        icon1.addFile(u"../icons/Save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.saveButton)

        self.convertButton = QPushButton(self.centralwidget)
        self.convertButton.setObjectName(u"convertButton")
        icon2 = QIcon()
        icon2.addFile(u"../icons/md-to-html.png", QSize(), QIcon.Normal, QIcon.Off)
        self.convertButton.setIcon(icon2)
        self.convertButton.setIconSize(QSize(50, 25))

        self.horizontalLayout.addWidget(self.convertButton)

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

        self.htmlDisplayer = QPlainTextEdit(self.centralwidget)
        self.htmlDisplayer.setObjectName(u"htmlDisplayer")

        self.horizontalLayout_2.addWidget(self.htmlDisplayer)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        ImageViewerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ImageViewerWindow)
        self.statusbar.setObjectName(u"statusbar")
        ImageViewerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImageViewerWindow)

        QMetaObject.connectSlotsByName(ImageViewerWindow)
    # setupUi

    def retranslateUi(self, ImageViewerWindow):
        ImageViewerWindow.setWindowTitle(QCoreApplication.translate("ImageViewerWindow", u"Example Image Viewer", None))
        self.openButton.setText("")
        self.saveButton.setText("")
        self.convertButton.setText("")
        self.currentFile.setText(QCoreApplication.translate("ImageViewerWindow", u"No file selected", None))
        
    # retranslateUi

