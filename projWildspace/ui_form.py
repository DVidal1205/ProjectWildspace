# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)
from pwEngine import pwEngine

class Ui_MainWindow(object):

    def __init__(self):
        self.engine = pwEngine(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(QSize(960, 540))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 961, 51))
        self.topBarHL = QHBoxLayout(self.horizontalLayoutWidget)
        self.topBarHL.setObjectName(u"topBarHL")
        self.topBarHL.setContentsMargins(10, 0, 10, 0)
        self.horizontalSpacer = QSpacerItem(31, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.topBarHL.addItem(self.horizontalSpacer)

        self.hamburgerBtn = QToolButton(self.horizontalLayoutWidget)
        self.hamburgerBtn.setObjectName(u"hamburgerBtn")
        self.hamburgerBtn.setPopupMode(QToolButton.DelayedPopup)

        self.topBarHL.addWidget(self.hamburgerBtn)

        self.leftTopBarHLSpacer = QSpacerItem(365, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.topBarHL.addItem(self.leftTopBarHLSpacer)

        self.titleLabel = QLabel(self.horizontalLayoutWidget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.topBarHL.addWidget(self.titleLabel)

        self.rightTopBarHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topBarHL.addItem(self.rightTopBarHLSpacer)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(100, 50, 861, 491))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page1NPC = QWidget()
        self.page1NPC.setObjectName(u"page1NPC")
        self.gridLayoutWidget = QWidget(self.page1NPC)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 861, 491))
        self.npcGridContainer = QGridLayout(self.gridLayoutWidget)
        self.npcGridContainer.setObjectName(u"npcGridContainer")
        self.npcGridContainer.setContentsMargins(0, 0, 0, 0)
        self.npcWidgetContainer = QWidget(self.gridLayoutWidget)
        self.npcWidgetContainer.setObjectName(u"npcWidgetContainer")
        self.verticalLayoutWidget_2 = QWidget(self.npcWidgetContainer)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(419, 20, 421, 411))
        self.personalityVL = QVBoxLayout(self.verticalLayoutWidget_2)
        self.personalityVL.setObjectName(u"personalityVL")
        self.personalityVL.setContentsMargins(0, 0, 0, 0)
        self.personalityTxy = QLabel(self.verticalLayoutWidget_2)
        self.personalityTxy.setObjectName(u"personalityTxy")
        self.personalityTxy.setAlignment(Qt.AlignCenter)

        self.personalityVL.addWidget(self.personalityTxy)

        self.fashionTxt = QLabel(self.verticalLayoutWidget_2)
        self.fashionTxt.setObjectName(u"fashionTxt")
        self.fashionTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.fashionTxt)

        self.fashionLabel = QLabel(self.verticalLayoutWidget_2)
        self.fashionLabel.setObjectName(u"fashionLabel")
        self.fashionLabel.setAlignment(Qt.AlignCenter)

        self.personalityVL.addWidget(self.fashionLabel)

        self.quirksTxt = QLabel(self.verticalLayoutWidget_2)
        self.quirksTxt.setObjectName(u"quirksTxt")
        self.quirksTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.quirksTxt)

        self.quirksLabel = QLabel(self.verticalLayoutWidget_2)
        self.quirksLabel.setObjectName(u"quirksLabel")
        self.quirksLabel.setAlignment(Qt.AlignCenter)

        self.personalityVL.addWidget(self.quirksLabel)

        self.goalsTxt = QLabel(self.verticalLayoutWidget_2)
        self.goalsTxt.setObjectName(u"goalsTxt")
        self.goalsTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.goalsTxt)

        self.goalsLabel = QLabel(self.verticalLayoutWidget_2)
        self.goalsLabel.setObjectName(u"goalsLabel")
        self.goalsLabel.setAlignment(Qt.AlignCenter)

        self.personalityVL.addWidget(self.goalsLabel)

        self.backgroundTxt = QLabel(self.verticalLayoutWidget_2)
        self.backgroundTxt.setObjectName(u"backgroundTxt")
        self.backgroundTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.backgroundTxt)

        self.backgroundLabel = QLabel(self.verticalLayoutWidget_2)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setAlignment(Qt.AlignCenter)

        self.personalityVL.addWidget(self.backgroundLabel)

        self.gridLayoutWidget_2 = QWidget(self.npcWidgetContainer)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(19, 19, 381, 201))
        self.characterGL = QGridLayout(self.gridLayoutWidget_2)
        self.characterGL.setObjectName(u"characterGL")
        self.characterGL.setContentsMargins(0, 0, 0, 0)
        self.lastNameTxt = QLabel(self.gridLayoutWidget_2)
        self.lastNameTxt.setObjectName(u"lastNameTxt")
        self.lastNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.lastNameTxt, 1, 1, 1, 1)

        self.lastNameLabel = QLabel(self.gridLayoutWidget_2)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.lastNameLabel, 2, 1, 1, 1)

        self.subclassTxt = QLabel(self.gridLayoutWidget_2)
        self.subclassTxt.setObjectName(u"subclassTxt")
        self.subclassTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.subclassTxt, 5, 1, 1, 1)

        self.affiliationLabel = QLabel(self.gridLayoutWidget_2)
        self.affiliationLabel.setObjectName(u"affiliationLabel")
        self.affiliationLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.affiliationLabel, 4, 1, 1, 1)

        self.genderTxt = QLabel(self.gridLayoutWidget_2)
        self.genderTxt.setObjectName(u"genderTxt")
        self.genderTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.genderTxt, 3, 0, 1, 1)

        self.subclassLabel = QLabel(self.gridLayoutWidget_2)
        self.subclassLabel.setObjectName(u"subclassLabel")
        self.subclassLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.subclassLabel, 6, 1, 1, 1)

        self.firstNameLabel = QLabel(self.gridLayoutWidget_2)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.firstNameLabel, 2, 0, 1, 1)

        self.firstNameTxt = QLabel(self.gridLayoutWidget_2)
        self.firstNameTxt.setObjectName(u"firstNameTxt")
        self.firstNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.firstNameTxt, 1, 0, 1, 1)

        self.genderLabel = QLabel(self.gridLayoutWidget_2)
        self.genderLabel.setObjectName(u"genderLabel")
        self.genderLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.genderLabel, 4, 0, 1, 1)

        self.affilicationTxt = QLabel(self.gridLayoutWidget_2)
        self.affilicationTxt.setObjectName(u"affilicationTxt")
        self.affilicationTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.affilicationTxt, 3, 1, 1, 1)

        self.classTxt = QLabel(self.gridLayoutWidget_2)
        self.classTxt.setObjectName(u"classTxt")
        self.classTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.classTxt, 5, 0, 1, 1)

        self.classLabel = QLabel(self.gridLayoutWidget_2)
        self.classLabel.setObjectName(u"classLabel")
        self.classLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.classLabel, 6, 0, 1, 1)

        self.characterTxt = QLabel(self.gridLayoutWidget_2)
        self.characterTxt.setObjectName(u"characterTxt")
        self.characterTxt.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.characterTxt, 0, 0, 1, 2)

        self.gridLayoutWidget_3 = QWidget(self.npcWidgetContainer)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 240, 381, 191))
        self.physicalGL = QGridLayout(self.gridLayoutWidget_3)
        self.physicalGL.setObjectName(u"physicalGL")
        self.physicalGL.setContentsMargins(0, 0, 0, 0)
        self.raceLabel = QLabel(self.gridLayoutWidget_3)
        self.raceLabel.setObjectName(u"raceLabel")
        self.raceLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.raceLabel, 2, 0, 1, 1)

        self.buildLabel = QLabel(self.gridLayoutWidget_3)
        self.buildLabel.setObjectName(u"buildLabel")
        self.buildLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.buildLabel, 6, 0, 1, 2)

        self.ageTxt = QLabel(self.gridLayoutWidget_3)
        self.ageTxt.setObjectName(u"ageTxt")
        self.ageTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.ageTxt, 3, 0, 1, 1)

        self.eyesLabel = QLabel(self.gridLayoutWidget_3)
        self.eyesLabel.setObjectName(u"eyesLabel")
        self.eyesLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.eyesLabel, 4, 1, 1, 1)

        self.physicalTxt = QLabel(self.gridLayoutWidget_3)
        self.physicalTxt.setObjectName(u"physicalTxt")
        self.physicalTxt.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.physicalTxt, 0, 0, 1, 2)

        self.ageLabel = QLabel(self.gridLayoutWidget_3)
        self.ageLabel.setObjectName(u"ageLabel")
        self.ageLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.ageLabel, 4, 0, 1, 1)

        self.heightTxt = QLabel(self.gridLayoutWidget_3)
        self.heightTxt.setObjectName(u"heightTxt")
        self.heightTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.heightTxt, 1, 1, 1, 1)

        self.eyesTxt = QLabel(self.gridLayoutWidget_3)
        self.eyesTxt.setObjectName(u"eyesTxt")
        self.eyesTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.eyesTxt, 3, 1, 1, 1)

        self.buildTxt = QLabel(self.gridLayoutWidget_3)
        self.buildTxt.setObjectName(u"buildTxt")
        self.buildTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.buildTxt, 5, 0, 1, 2)

        self.raceTxt = QLabel(self.gridLayoutWidget_3)
        self.raceTxt.setObjectName(u"raceTxt")
        self.raceTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.raceTxt, 1, 0, 1, 1)

        self.heightLabel = QLabel(self.gridLayoutWidget_3)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.heightLabel, 2, 1, 1, 1)

        self.verticalLayoutWidget_3 = QWidget(self.npcWidgetContainer)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(-100, 430, 961, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.npcGridContainer.addWidget(self.npcWidgetContainer, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page1NPC)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(-10, 470, 971, 51))
        self.bottomBarHL = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.bottomBarHL.setObjectName(u"bottomBarHL")
        self.bottomBarHL.setContentsMargins(10, 0, 10, 0)
        self.leftTopBarHLSpacer_2 = QSpacerItem(420, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.bottomBarHL.addItem(self.leftTopBarHLSpacer_2)

        self.generateBtn = QPushButton(self.horizontalLayoutWidget_2)
        self.generateBtn.setObjectName(u"generateBtn")

        self.bottomBarHL.addWidget(self.generateBtn)

        self.horizontalSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.bottomBarHL.addItem(self.horizontalSpacer_2)

        self.dropDown = QComboBox(self.horizontalLayoutWidget_2)
        self.dropDown.setObjectName(u"dropDown")

        self.bottomBarHL.addWidget(self.dropDown)

        self.rightTopBarHLSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomBarHL.addItem(self.rightTopBarHLSpacer_2)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 50, 100, 461))
        self.sideBarVL = QVBoxLayout(self.verticalLayoutWidget)
        self.sideBarVL.setSpacing(10)
        self.sideBarVL.setObjectName(u"sideBarVL")
        self.sideBarVL.setContentsMargins(10, 0, 10, 0)
        self.npcBtn = QPushButton(self.verticalLayoutWidget)
        self.npcBtn.setObjectName(u"npcBtn")

        self.sideBarVL.addWidget(self.npcBtn)

        self.buildingBtn = QPushButton(self.verticalLayoutWidget)
        self.buildingBtn.setObjectName(u"buildingBtn")

        self.sideBarVL.addWidget(self.buildingBtn)

        self.townBtn = QPushButton(self.verticalLayoutWidget)
        self.townBtn.setObjectName(u"townBtn")

        self.sideBarVL.addWidget(self.townBtn)

        self.encounterBtn = QPushButton(self.verticalLayoutWidget)
        self.encounterBtn.setObjectName(u"encounterBtn")

        self.sideBarVL.addWidget(self.encounterBtn)

        self.groupBtn = QPushButton(self.verticalLayoutWidget)
        self.groupBtn.setObjectName(u"groupBtn")

        self.sideBarVL.addWidget(self.groupBtn)

        self.worldBtn = QPushButton(self.verticalLayoutWidget)
        self.worldBtn.setObjectName(u"worldBtn")

        self.sideBarVL.addWidget(self.worldBtn)

        self.sideBarVLVSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.sideBarVL.addItem(self.sideBarVLVSpacer)

        self.warningBtn = QToolButton(self.verticalLayoutWidget)
        self.warningBtn.setObjectName(u"warningBtn")

        self.sideBarVL.addWidget(self.warningBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.helpBtn = QToolButton(self.verticalLayoutWidget)
        self.helpBtn.setObjectName(u"helpBtn")

        self.sideBarVL.addWidget(self.helpBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.npcBtn.raise_()
        self.townBtn.raise_()
        self.encounterBtn.raise_()
        self.groupBtn.raise_()
        self.buildingBtn.raise_()
        self.warningBtn.raise_()
        self.worldBtn.raise_()
        self.helpBtn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)

    # Slots
        self.generateBtn.clicked.connect(self.generate)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def generate(self):
        self.engine.genNPC()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.hamburgerBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Project Wildspace", None))
        self.personalityTxy.setText(QCoreApplication.translate("MainWindow", u"Personality", None))
        self.fashionTxt.setText(QCoreApplication.translate("MainWindow", u"Fashion", None))
        self.fashionLabel.setText("")
        self.quirksTxt.setText(QCoreApplication.translate("MainWindow", u"Quirks", None))
        self.quirksLabel.setText("")
        self.goalsTxt.setText(QCoreApplication.translate("MainWindow", u"Goals", None))
        self.goalsLabel.setText("")
        self.backgroundTxt.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self.backgroundLabel.setText("")
        self.lastNameTxt.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.lastNameLabel.setText("")
        self.subclassTxt.setText(QCoreApplication.translate("MainWindow", u"Subclass", None))
        self.affiliationLabel.setText("")
        self.genderTxt.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.subclassLabel.setText("")
        self.firstNameLabel.setText("")
        self.firstNameTxt.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.genderLabel.setText("")
        self.affilicationTxt.setText(QCoreApplication.translate("MainWindow", u"Affiliation", None))
        self.classTxt.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.classLabel.setText("")
        self.characterTxt.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.raceLabel.setText("")
        self.buildLabel.setText("")
        self.ageTxt.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.eyesLabel.setText("")
        self.physicalTxt.setText(QCoreApplication.translate("MainWindow", u"Physical", None))
        self.ageLabel.setText("")
        self.heightTxt.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.eyesTxt.setText(QCoreApplication.translate("MainWindow", u"Eyes", None))
        self.buildTxt.setText(QCoreApplication.translate("MainWindow", u"Build", None))
        self.raceTxt.setText(QCoreApplication.translate("MainWindow", u"Race", None))
        self.heightLabel.setText("")
        self.generateBtn.setText(QCoreApplication.translate("MainWindow", u"Generate!", None))
        self.npcBtn.setText(QCoreApplication.translate("MainWindow", u"NPC", None))
        self.buildingBtn.setText(QCoreApplication.translate("MainWindow", u"Building", None))
        self.townBtn.setText(QCoreApplication.translate("MainWindow", u"Town", None))
        self.encounterBtn.setText(QCoreApplication.translate("MainWindow", u"Encounter", None))
        self.groupBtn.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.worldBtn.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.warningBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

