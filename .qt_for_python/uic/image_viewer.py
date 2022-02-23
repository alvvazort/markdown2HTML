# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_viewer.ui'
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
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u"../icons/Save-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton)

        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        icon1 = QIcon()
        iconThemeName = u"icons\\md-to-html.png"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"../icons/md-to-html.png", QSize(), QIcon.Normal, QIcon.Off)
        
        self.saveButton.setIcon(icon1)
        self.saveButton.setIconSize(QSize(50, 25))

        self.horizontalLayout.addWidget(self.saveButton)

        self.currentFile = QLabel(self.centralwidget)
        self.currentFile.setObjectName(u"currentFile")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentFile.sizePolicy().hasHeightForWidth())
        self.currentFile.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.currentFile)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.imageLabel)

        ImageViewerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ImageViewerWindow)
        self.statusbar.setObjectName(u"statusbar")
        ImageViewerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ImageViewerWindow)

        QMetaObject.connectSlotsByName(ImageViewerWindow)
    # setupUi

    def retranslateUi(self, ImageViewerWindow):
        ImageViewerWindow.setWindowTitle(QCoreApplication.translate("ImageViewerWindow", u"Example Image Viewer", None))
        self.pushButton.setText("")
        self.saveButton.setText("")
        self.currentFile.setText(QCoreApplication.translate("ImageViewerWindow", u"No file selected", None))
        self.imageLabel.setText("")
    # retranslateUi

