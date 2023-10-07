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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QSize(960, 540))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u".MainWindow {background: rgba(40,42,53,255);}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 961, 51))
        self.topBarHL = QHBoxLayout(self.horizontalLayoutWidget)
        self.topBarHL.setSpacing(0)
        self.topBarHL.setObjectName(u"topBarHL")
        self.topBarHL.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.horizontalLayoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u".QFrame {background: rgba(30, 30, 38, 255)}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.titleLabel = QLabel(self.frame_2)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(340, 0, 281, 49))
        font = QFont()
        font.setFamilies([u"Bahnschrift Light"])
        font.setPointSize(26)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.hamburgerBtn = QToolButton(self.frame_2)
        self.hamburgerBtn.setObjectName(u"hamburgerBtn")
        self.hamburgerBtn.setGeometry(QRect(37, 11, 26, 26))
        self.hamburgerBtn.setStyleSheet(u".QToolButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.hamburgerBtn.setPopupMode(QToolButton.DelayedPopup)

        self.topBarHL.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(100, 50, 861, 441))
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
        self.verticalLayoutWidget_2.setGeometry(QRect(430, 0, 421, 411))
        self.personalityVL = QVBoxLayout(self.verticalLayoutWidget_2)
        self.personalityVL.setObjectName(u"personalityVL")
        self.personalityVL.setContentsMargins(0, 0, 0, 0)
        self.personalityTxy = QLabel(self.verticalLayoutWidget_2)
        self.personalityTxy.setObjectName(u"personalityTxy")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift Light"])
        self.personalityTxy.setFont(font1)
        self.personalityTxy.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.personalityTxy.setAlignment(Qt.AlignCenter)

        self.personalityVL.addWidget(self.personalityTxy)

        self.fashionTxt = QLabel(self.verticalLayoutWidget_2)
        self.fashionTxt.setObjectName(u"fashionTxt")
        self.fashionTxt.setFont(font1)
        self.fashionTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.fashionTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.fashionTxt)

        self.fashionLabel = QLabel(self.verticalLayoutWidget_2)
        self.fashionLabel.setObjectName(u"fashionLabel")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift Light"])
        font2.setPointSize(8)
        self.fashionLabel.setFont(font2)
        self.fashionLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.fashionLabel.setAlignment(Qt.AlignCenter)
        self.fashionLabel.setWordWrap(True)

        self.personalityVL.addWidget(self.fashionLabel)

        self.quirksTxt = QLabel(self.verticalLayoutWidget_2)
        self.quirksTxt.setObjectName(u"quirksTxt")
        self.quirksTxt.setFont(font1)
        self.quirksTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.quirksTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.quirksTxt)

        self.quirksLabel = QLabel(self.verticalLayoutWidget_2)
        self.quirksLabel.setObjectName(u"quirksLabel")
        self.quirksLabel.setFont(font2)
        self.quirksLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.quirksLabel.setAlignment(Qt.AlignCenter)
        self.quirksLabel.setWordWrap(True)

        self.personalityVL.addWidget(self.quirksLabel)

        self.goalsTxt = QLabel(self.verticalLayoutWidget_2)
        self.goalsTxt.setObjectName(u"goalsTxt")
        self.goalsTxt.setFont(font1)
        self.goalsTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.goalsTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.goalsTxt)

        self.goalsLabel = QLabel(self.verticalLayoutWidget_2)
        self.goalsLabel.setObjectName(u"goalsLabel")
        self.goalsLabel.setFont(font2)
        self.goalsLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.goalsLabel.setAlignment(Qt.AlignCenter)
        self.goalsLabel.setWordWrap(True)

        self.personalityVL.addWidget(self.goalsLabel)

        self.backgroundTxt = QLabel(self.verticalLayoutWidget_2)
        self.backgroundTxt.setObjectName(u"backgroundTxt")
        self.backgroundTxt.setFont(font1)
        self.backgroundTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.backgroundTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.backgroundTxt)

        self.backgroundLabel = QLabel(self.verticalLayoutWidget_2)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        font3 = QFont()
        font3.setPointSize(8)
        self.backgroundLabel.setFont(font3)
        self.backgroundLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.backgroundLabel.setAlignment(Qt.AlignCenter)
        self.backgroundLabel.setWordWrap(True)

        self.personalityVL.addWidget(self.backgroundLabel)

        self.gridLayoutWidget_2 = QWidget(self.npcWidgetContainer)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 0, 381, 211))
        self.gridLayoutWidget_2.setFont(font1)
        self.characterGL = QGridLayout(self.gridLayoutWidget_2)
        self.characterGL.setObjectName(u"characterGL")
        self.characterGL.setContentsMargins(0, 0, 0, 0)
        self.genderLabel = QLabel(self.gridLayoutWidget_2)
        self.genderLabel.setObjectName(u"genderLabel")
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift Light"])
        font4.setPointSize(9)
        self.genderLabel.setFont(font4)
        self.genderLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.genderLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.genderLabel, 4, 0, 1, 1)

        self.subclassLabel = QLabel(self.gridLayoutWidget_2)
        self.subclassLabel.setObjectName(u"subclassLabel")
        self.subclassLabel.setFont(font2)
        self.subclassLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.subclassLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.subclassLabel, 6, 1, 1, 1)

        self.alignmentTxt = QLabel(self.gridLayoutWidget_2)
        self.alignmentTxt.setObjectName(u"alignmentTxt")
        self.alignmentTxt.setFont(font1)
        self.alignmentTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.alignmentTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.alignmentTxt, 3, 1, 1, 1)

        self.firstNameTxt = QLabel(self.gridLayoutWidget_2)
        self.firstNameTxt.setObjectName(u"firstNameTxt")
        self.firstNameTxt.setFont(font1)
        self.firstNameTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.firstNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.firstNameTxt, 1, 0, 1, 1)

        self.firstNameLabel = QLabel(self.gridLayoutWidget_2)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setFont(font4)
        self.firstNameLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.firstNameLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.firstNameLabel, 2, 0, 1, 1)

        self.classLabel = QLabel(self.gridLayoutWidget_2)
        self.classLabel.setObjectName(u"classLabel")
        self.classLabel.setFont(font2)
        self.classLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.classLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.classLabel, 6, 0, 1, 1)

        self.lastNameTxt = QLabel(self.gridLayoutWidget_2)
        self.lastNameTxt.setObjectName(u"lastNameTxt")
        self.lastNameTxt.setFont(font1)
        self.lastNameTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.lastNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.lastNameTxt, 1, 1, 1, 1)

        self.genderTxt = QLabel(self.gridLayoutWidget_2)
        self.genderTxt.setObjectName(u"genderTxt")
        self.genderTxt.setFont(font1)
        self.genderTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.genderTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.genderTxt, 3, 0, 1, 1)

        self.lastNameLabel = QLabel(self.gridLayoutWidget_2)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setFont(font4)
        self.lastNameLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.lastNameLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.lastNameLabel, 2, 1, 1, 1)

        self.alignmentLabel = QLabel(self.gridLayoutWidget_2)
        self.alignmentLabel.setObjectName(u"alignmentLabel")
        self.alignmentLabel.setFont(font4)
        self.alignmentLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.alignmentLabel.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.alignmentLabel, 4, 1, 1, 1)

        self.characterTxt = QLabel(self.gridLayoutWidget_2)
        self.characterTxt.setObjectName(u"characterTxt")
        self.characterTxt.setFont(font1)
        self.characterTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.characterTxt.setAlignment(Qt.AlignCenter)

        self.characterGL.addWidget(self.characterTxt, 0, 0, 1, 2)

        self.classTxt = QLabel(self.gridLayoutWidget_2)
        self.classTxt.setObjectName(u"classTxt")
        self.classTxt.setFont(font1)
        self.classTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.classTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.classTxt, 5, 0, 1, 1)

        self.subclassTxt = QLabel(self.gridLayoutWidget_2)
        self.subclassTxt.setObjectName(u"subclassTxt")
        self.subclassTxt.setFont(font1)
        self.subclassTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.subclassTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.characterGL.addWidget(self.subclassTxt, 5, 1, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.npcWidgetContainer)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 220, 381, 191))
        self.physicalGL = QGridLayout(self.gridLayoutWidget_3)
        self.physicalGL.setObjectName(u"physicalGL")
        self.physicalGL.setContentsMargins(0, 0, 0, 0)
        self.heightTxt = QLabel(self.gridLayoutWidget_3)
        self.heightTxt.setObjectName(u"heightTxt")
        self.heightTxt.setFont(font1)
        self.heightTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.heightTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.heightTxt, 1, 1, 1, 1)

        self.ageTxt = QLabel(self.gridLayoutWidget_3)
        self.ageTxt.setObjectName(u"ageTxt")
        self.ageTxt.setFont(font1)
        self.ageTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.ageTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.ageTxt, 3, 0, 1, 1)

        self.buildLabel = QLabel(self.gridLayoutWidget_3)
        self.buildLabel.setObjectName(u"buildLabel")
        self.buildLabel.setFont(font2)
        self.buildLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.buildLabel, 4, 1, 1, 1)

        self.buildTxt = QLabel(self.gridLayoutWidget_3)
        self.buildTxt.setObjectName(u"buildTxt")
        self.buildTxt.setFont(font1)
        self.buildTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.buildTxt, 3, 1, 1, 1)

        self.physicalTxt = QLabel(self.gridLayoutWidget_3)
        self.physicalTxt.setObjectName(u"physicalTxt")
        self.physicalTxt.setFont(font1)
        self.physicalTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.physicalTxt.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.physicalTxt, 0, 0, 1, 2)

        self.raceTxt = QLabel(self.gridLayoutWidget_3)
        self.raceTxt.setObjectName(u"raceTxt")
        self.raceTxt.setFont(font1)
        self.raceTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.raceTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.raceTxt, 1, 0, 1, 1)

        self.eyesTxt = QLabel(self.gridLayoutWidget_3)
        self.eyesTxt.setObjectName(u"eyesTxt")
        self.eyesTxt.setFont(font1)
        self.eyesTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.eyesTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.eyesTxt, 5, 0, 1, 1)

        self.hairLabel = QLabel(self.gridLayoutWidget_3)
        self.hairLabel.setObjectName(u"hairLabel")
        self.hairLabel.setFont(font3)
        self.hairLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.hairLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.hairLabel, 6, 1, 1, 1)

        self.hairTxt = QLabel(self.gridLayoutWidget_3)
        self.hairTxt.setObjectName(u"hairTxt")
        self.hairTxt.setFont(font1)
        self.hairTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.hairTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.physicalGL.addWidget(self.hairTxt, 5, 1, 1, 1)

        self.raceLabel = QLabel(self.gridLayoutWidget_3)
        self.raceLabel.setObjectName(u"raceLabel")
        self.raceLabel.setFont(font2)
        self.raceLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.raceLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.raceLabel, 2, 0, 1, 1)

        self.heightLabel = QLabel(self.gridLayoutWidget_3)
        self.heightLabel.setObjectName(u"heightLabel")
        self.heightLabel.setFont(font2)
        self.heightLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.heightLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.heightLabel, 2, 1, 1, 1)

        self.eyesLabel = QLabel(self.gridLayoutWidget_3)
        self.eyesLabel.setObjectName(u"eyesLabel")
        self.eyesLabel.setFont(font3)
        self.eyesLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.eyesLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.eyesLabel, 6, 0, 1, 1)

        self.ageLabel = QLabel(self.gridLayoutWidget_3)
        self.ageLabel.setObjectName(u"ageLabel")
        self.ageLabel.setFont(font2)
        self.ageLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.ageLabel.setAlignment(Qt.AlignCenter)

        self.physicalGL.addWidget(self.ageLabel, 4, 0, 1, 1)

        self.verticalLayoutWidget_3 = QWidget(self.npcWidgetContainer)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(-100, 430, 961, 16))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.npcGridContainer.addWidget(self.npcWidgetContainer, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page1NPC)
        self.page2Building = QWidget()
        self.page2Building.setObjectName(u"page2Building")
        self.gridLayoutWidget_4 = QWidget(self.page2Building)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 841, 421))
        self.buildingGridContainer = QGridLayout(self.gridLayoutWidget_4)
        self.buildingGridContainer.setObjectName(u"buildingGridContainer")
        self.buildingGridContainer.setContentsMargins(0, 0, 0, 0)
        self.buildingTypeTxt = QLabel(self.gridLayoutWidget_4)
        self.buildingTypeTxt.setObjectName(u"buildingTypeTxt")
        self.buildingTypeTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildingTypeTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.buildingGridContainer.addWidget(self.buildingTypeTxt, 0, 1, 1, 1)

        self.buildingGoodsLabel = QLabel(self.gridLayoutWidget_4)
        self.buildingGoodsLabel.setObjectName(u"buildingGoodsLabel")
        self.buildingGoodsLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildingGoodsLabel.setAlignment(Qt.AlignCenter)

        self.buildingGridContainer.addWidget(self.buildingGoodsLabel, 11, 0, 1, 2)

        self.buildingTrafficLabel = QLabel(self.gridLayoutWidget_4)
        self.buildingTrafficLabel.setObjectName(u"buildingTrafficLabel")
        self.buildingTrafficLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildingTrafficLabel.setAlignment(Qt.AlignCenter)

        self.buildingGridContainer.addWidget(self.buildingTrafficLabel, 5, 1, 1, 1)

        self.buildingArcLabel = QLabel(self.gridLayoutWidget_4)
        self.buildingArcLabel.setObjectName(u"buildingArcLabel")
        self.buildingArcLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildingArcLabel.setAlignment(Qt.AlignCenter)

        self.buildingGridContainer.addWidget(self.buildingArcLabel, 3, 0, 1, 1)

        self.buildingSizeLabel = QLabel(self.gridLayoutWidget_4)
        self.buildingSizeLabel.setObjectName(u"buildingSizeLabel")
        self.buildingSizeLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildingSizeLabel.setAlignment(Qt.AlignCenter)

        self.buildingGridContainer.addWidget(self.buildingSizeLabel, 5, 0, 1, 1)

        self.buildingNameTxt = QLabel(self.gridLayoutWidget_4)
        self.buildingNameTxt.setObjectName(u"buildingNameTxt")
        self.buildingNameTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildingNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.buildingGridContainer.addWidget(self.buildingNameTxt, 0, 0, 1, 1)

        self.buildingGoodsTxt = QLabel(self.gridLayoutWidget_4)
        self.buildingGoodsTxt.setObjectName(u"buildingGoodsTxt")
        self.buildingGoodsTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildingGoodsTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.buildingGridContainer.addWidget(self.buildingGoodsTxt, 10, 0, 1, 2)

        self.buildingDesLabel = QLabel(self.gridLayoutWidget_4)
        self.buildingDesLabel.setObjectName(u"buildingDesLabel")
        self.buildingDesLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildingDesLabel.setAlignment(Qt.AlignCenter)

        self.buildingGridContainer.addWidget(self.buildingDesLabel, 7, 0, 1, 2)

        self.buildingTrafficTxt = QLabel(self.gridLayoutWidget_4)
        self.buildingTrafficTxt.setObjectName(u"buildingTrafficTxt")
        self.buildingTrafficTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildingTrafficTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.buildingGridContainer.addWidget(self.buildingTrafficTxt, 4, 1, 1, 1)

        self.buildingAmbLabel = QLabel(self.gridLayoutWidget_4)
        self.buildingAmbLabel.setObjectName(u"buildingAmbLabel")
        self.buildingAmbLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildingAmbLabel.setAlignment(Qt.AlignCenter)

        self.buildingGridContainer.addWidget(self.buildingAmbLabel, 3, 1, 1, 1)

        self.buildingAmbTxt = QLabel(self.gridLayoutWidget_4)
        self.buildingAmbTxt.setObjectName(u"buildingAmbTxt")
        self.buildingAmbTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildingAmbTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.buildingGridContainer.addWidget(self.buildingAmbTxt, 2, 1, 1, 1)

        self.buildingDesTxt = QLabel(self.gridLayoutWidget_4)
        self.buildingDesTxt.setObjectName(u"buildingDesTxt")
        self.buildingDesTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildingDesTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.buildingGridContainer.addWidget(self.buildingDesTxt, 6, 0, 1, 2)

        self.buildingTenderLabel = QLabel(self.gridLayoutWidget_4)
        self.buildingTenderLabel.setObjectName(u"buildingTenderLabel")
        self.buildingTenderLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildingTenderLabel.setAlignment(Qt.AlignCenter)

        self.buildingGridContainer.addWidget(self.buildingTenderLabel, 9, 0, 1, 2)

        self.buildingTenderTxt = QLabel(self.gridLayoutWidget_4)
        self.buildingTenderTxt.setObjectName(u"buildingTenderTxt")
        self.buildingTenderTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildingTenderTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.buildingGridContainer.addWidget(self.buildingTenderTxt, 8, 0, 1, 2)

        self.buildingTypeLabel = QLabel(self.gridLayoutWidget_4)
        self.buildingTypeLabel.setObjectName(u"buildingTypeLabel")
        self.buildingTypeLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildingTypeLabel.setAlignment(Qt.AlignCenter)

        self.buildingGridContainer.addWidget(self.buildingTypeLabel, 1, 1, 1, 1)

        self.buildingSizeTxt = QLabel(self.gridLayoutWidget_4)
        self.buildingSizeTxt.setObjectName(u"buildingSizeTxt")
        self.buildingSizeTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildingSizeTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.buildingGridContainer.addWidget(self.buildingSizeTxt, 4, 0, 1, 1)

        self.buildingArcTxt = QLabel(self.gridLayoutWidget_4)
        self.buildingArcTxt.setObjectName(u"buildingArcTxt")
        self.buildingArcTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.buildingArcTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.buildingGridContainer.addWidget(self.buildingArcTxt, 2, 0, 1, 1)

        self.buildingNameLabel = QLabel(self.gridLayoutWidget_4)
        self.buildingNameLabel.setObjectName(u"buildingNameLabel")
        self.buildingNameLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.buildingNameLabel.setAlignment(Qt.AlignCenter)

        self.buildingGridContainer.addWidget(self.buildingNameLabel, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page2Building)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 50, 100, 501))
        self.sideBarVL = QVBoxLayout(self.verticalLayoutWidget)
        self.sideBarVL.setSpacing(0)
        self.sideBarVL.setObjectName(u"sideBarVL")
        self.sideBarVL.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.verticalLayoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u".QFrame {background: rgba(30, 30, 38, 255)}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.groupBtn = QPushButton(self.frame)
        self.groupBtn.setObjectName(u"groupBtn")
        self.groupBtn.setGeometry(QRect(10, 134, 80, 22))
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift"])
        self.groupBtn.setFont(font5)
        self.groupBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.encounterBtn = QPushButton(self.frame)
        self.encounterBtn.setObjectName(u"encounterBtn")
        self.encounterBtn.setGeometry(QRect(10, 102, 80, 22))
        self.encounterBtn.setFont(font5)
        self.encounterBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.npcBtn = QPushButton(self.frame)
        self.npcBtn.setObjectName(u"npcBtn")
        self.npcBtn.setGeometry(QRect(10, 6, 80, 22))
        self.npcBtn.setFont(font5)
        self.npcBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.helpBtn = QToolButton(self.frame)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setGeometry(QRect(37, 439, 26, 26))
        self.helpBtn.setStyleSheet(u".QToolButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.buildingBtn = QPushButton(self.frame)
        self.buildingBtn.setObjectName(u"buildingBtn")
        self.buildingBtn.setGeometry(QRect(10, 38, 80, 22))
        self.buildingBtn.setFont(font5)
        self.buildingBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.worldBtn = QPushButton(self.frame)
        self.worldBtn.setObjectName(u"worldBtn")
        self.worldBtn.setGeometry(QRect(10, 166, 80, 22))
        self.worldBtn.setFont(font5)
        self.worldBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.townBtn = QPushButton(self.frame)
        self.townBtn.setObjectName(u"townBtn")
        self.townBtn.setGeometry(QRect(10, 70, 80, 22))
        self.townBtn.setFont(font5)
        self.townBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.warningBtn = QToolButton(self.frame)
        self.warningBtn.setObjectName(u"warningBtn")
        self.warningBtn.setGeometry(QRect(37, 403, 26, 26))
        self.warningBtn.setStyleSheet(u".QToolButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        self.sideBarVL.addWidget(self.frame)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 490, 861, 51))
        self.bottomBarHL_2 = QHBoxLayout(self.layoutWidget)
        self.bottomBarHL_2.setObjectName(u"bottomBarHL_2")
        self.bottomBarHL_2.setContentsMargins(10, 0, 10, 0)
        self.leftBottomBarHLSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomBarHL_2.addItem(self.leftBottomBarHLSpacer_2)

        self.generateBtn_2 = QPushButton(self.layoutWidget)
        self.generateBtn_2.setObjectName(u"generateBtn_2")
        self.generateBtn_2.setFont(font5)
        self.generateBtn_2.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        self.bottomBarHL_2.addWidget(self.generateBtn_2)

        self.middleBottomBarHLSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.bottomBarHL_2.addItem(self.middleBottomBarHLSpacer_2)

        self.dropDown_2 = QComboBox(self.layoutWidget)
        self.dropDown_2.setObjectName(u"dropDown_2")
        self.dropDown_2.setFont(font5)
        self.dropDown_2.setStyleSheet(u".QComboBox {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        self.bottomBarHL_2.addWidget(self.dropDown_2)

        self.rightBottomBarHLSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomBarHL_2.addItem(self.rightBottomBarHLSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Project Wildspace", None))
        self.hamburgerBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.personalityTxy.setText(QCoreApplication.translate("MainWindow", u"Personality", None))
        self.fashionTxt.setText(QCoreApplication.translate("MainWindow", u"Fashion", None))
        self.fashionLabel.setText("")
        self.quirksTxt.setText(QCoreApplication.translate("MainWindow", u"Quirks", None))
        self.quirksLabel.setText("")
        self.goalsTxt.setText(QCoreApplication.translate("MainWindow", u"Goals", None))
        self.goalsLabel.setText("")
        self.backgroundTxt.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self.backgroundLabel.setText("")
        self.genderLabel.setText("")
        self.subclassLabel.setText("")
        self.alignmentTxt.setText(QCoreApplication.translate("MainWindow", u"Alignment", None))
        self.firstNameTxt.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.firstNameLabel.setText("")
        self.classLabel.setText("")
        self.lastNameTxt.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.genderTxt.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.lastNameLabel.setText("")
        self.alignmentLabel.setText("")
        self.characterTxt.setText(QCoreApplication.translate("MainWindow", u"Character", None))
        self.classTxt.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.subclassTxt.setText(QCoreApplication.translate("MainWindow", u"Subclass", None))
        self.heightTxt.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.ageTxt.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.buildLabel.setText("")
        self.buildTxt.setText(QCoreApplication.translate("MainWindow", u"Build", None))
        self.physicalTxt.setText(QCoreApplication.translate("MainWindow", u"Physical", None))
        self.raceTxt.setText(QCoreApplication.translate("MainWindow", u"Race", None))
        self.eyesTxt.setText(QCoreApplication.translate("MainWindow", u"Eyes", None))
        self.hairLabel.setText("")
        self.hairTxt.setText(QCoreApplication.translate("MainWindow", u"Hair", None))
        self.raceLabel.setText("")
        self.heightLabel.setText("")
        self.eyesLabel.setText("")
        self.ageLabel.setText("")
        self.buildingTypeTxt.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.buildingGoodsLabel.setText("")
        self.buildingTrafficLabel.setText("")
        self.buildingArcLabel.setText("")
        self.buildingSizeLabel.setText("")
        self.buildingNameTxt.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.buildingGoodsTxt.setText(QCoreApplication.translate("MainWindow", u"Goods", None))
        self.buildingDesLabel.setText("")
        self.buildingTrafficTxt.setText(QCoreApplication.translate("MainWindow", u"Traffic", None))
        self.buildingAmbLabel.setText("")
        self.buildingAmbTxt.setText(QCoreApplication.translate("MainWindow", u"Ambience", None))
        self.buildingDesTxt.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.buildingTenderLabel.setText("")
        self.buildingTenderTxt.setText(QCoreApplication.translate("MainWindow", u"Tender", None))
        self.buildingTypeLabel.setText("")
        self.buildingSizeTxt.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.buildingArcTxt.setText(QCoreApplication.translate("MainWindow", u"Architecture", None))
        self.buildingNameLabel.setText("")
        self.groupBtn.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.encounterBtn.setText(QCoreApplication.translate("MainWindow", u"Encounter", None))
        self.npcBtn.setText(QCoreApplication.translate("MainWindow", u"NPC", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.buildingBtn.setText(QCoreApplication.translate("MainWindow", u"Building", None))
        self.worldBtn.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.townBtn.setText(QCoreApplication.translate("MainWindow", u"Town", None))
        self.warningBtn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.generateBtn_2.setText(QCoreApplication.translate("MainWindow", u"Generate!", None))
    # retranslateUi

