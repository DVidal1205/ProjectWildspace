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
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QTextEdit, QToolButton, QVBoxLayout,
    QWidget, QMessageBox)
from pwEngine import pwEngine
from worldManager import world
import os


class Ui_MainWindow(object):

    def __init__(self):
        self.world = world(self)
        self.engine = pwEngine(self, world)

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Hello!")
        msgBox.setText("Welcome to Project Wildspace...")
        msgBox.setStandardButtons(QMessageBox.Ok)
                
        # Connect the button press to close the QMessageBox
        msgBox.buttonClicked.connect(msgBox.close)
                
        # Show the QMessageBox
        msgBox.exec()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QSize(960, 540))
        MainWindow.setMaximumSize(QSize(960, 540))
        icon = QIcon()
        icon.addFile(u"wildspace.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.topBarHLFrame = QFrame(self.horizontalLayoutWidget)
        self.topBarHLFrame.setObjectName(u"topBarHLFrame")
        self.topBarHLFrame.setStyleSheet(u".QFrame {background: rgba(30, 30, 38, 255)}")
        self.topBarHLFrame.setFrameShape(QFrame.StyledPanel)
        self.topBarHLFrame.setFrameShadow(QFrame.Raised)
        self.titleLabel = QLabel(self.topBarHLFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(350, 0, 281, 49))
        font = QFont()
        font.setFamilies([u"Bahnschrift Light"])
        font.setPointSize(26)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.label = QLabel(self.topBarHLFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(920, 10, 31, 31))
        self.label.setPixmap(QPixmap(u"wildspace.ico"))
        self.label.setScaledContents(True)

        self.topBarHL.addWidget(self.topBarHLFrame)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(100, 50, 861, 441))
        self.stackedWidget.setStyleSheet(u"")
        self.page1NPC = QWidget()
        self.page1NPC.setObjectName(u"page1NPC")
        self.gridLayoutWidget = QWidget(self.page1NPC)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 861, 491))
        self.npcGridContainer = QGridLayout(self.gridLayoutWidget)
        self.npcGridContainer.setObjectName(u"npcGridContainer")
        self.npcGridContainer.setContentsMargins(0, 0, 0, 0)
        self.npcFrame = QWidget(self.gridLayoutWidget)
        self.npcFrame.setObjectName(u"npcFrame")
        self.verticalLayoutWidget_2 = QWidget(self.npcFrame)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(430, 0, 421, 411))
        self.personalityVL = QVBoxLayout(self.verticalLayoutWidget_2)
        self.personalityVL.setObjectName(u"personalityVL")
        self.personalityVL.setContentsMargins(0, 0, 0, 0)
        self.npcFashionTxt = QLabel(self.verticalLayoutWidget_2)
        self.npcFashionTxt.setObjectName(u"npcFashionTxt")
        font1 = QFont()
        font1.setFamilies([u"Bahnschrift Light"])
        self.npcFashionTxt.setFont(font1)
        self.npcFashionTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcFashionTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.npcFashionTxt)

        self.npcFashionLabel = QLabel(self.verticalLayoutWidget_2)
        self.npcFashionLabel.setObjectName(u"npcFashionLabel")
        font2 = QFont()
        font2.setFamilies([u"Bahnschrift Light"])
        font2.setPointSize(8)
        self.npcFashionLabel.setFont(font2)
        self.npcFashionLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcFashionLabel.setAlignment(Qt.AlignCenter)
        self.npcFashionLabel.setWordWrap(True)
        self.npcFashionLabel.setMargin(5)

        self.personalityVL.addWidget(self.npcFashionLabel)

        self.npcQuirksTxt = QLabel(self.verticalLayoutWidget_2)
        self.npcQuirksTxt.setObjectName(u"npcQuirksTxt")
        self.npcQuirksTxt.setFont(font1)
        self.npcQuirksTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcQuirksTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.npcQuirksTxt)

        self.npcQuirksLabel = QLabel(self.verticalLayoutWidget_2)
        self.npcQuirksLabel.setObjectName(u"npcQuirksLabel")
        self.npcQuirksLabel.setFont(font2)
        self.npcQuirksLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcQuirksLabel.setAlignment(Qt.AlignCenter)
        self.npcQuirksLabel.setWordWrap(True)
        self.npcQuirksLabel.setMargin(5)

        self.personalityVL.addWidget(self.npcQuirksLabel)

        self.npcGoalsTxt = QLabel(self.verticalLayoutWidget_2)
        self.npcGoalsTxt.setObjectName(u"npcGoalsTxt")
        self.npcGoalsTxt.setFont(font1)
        self.npcGoalsTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcGoalsTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.npcGoalsTxt)

        self.npcGoalsLabel = QLabel(self.verticalLayoutWidget_2)
        self.npcGoalsLabel.setObjectName(u"npcGoalsLabel")
        self.npcGoalsLabel.setFont(font2)
        self.npcGoalsLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcGoalsLabel.setAlignment(Qt.AlignCenter)
        self.npcGoalsLabel.setWordWrap(True)
        self.npcGoalsLabel.setMargin(5)

        self.personalityVL.addWidget(self.npcGoalsLabel)

        self.npcBackgroundTxt = QLabel(self.verticalLayoutWidget_2)
        self.npcBackgroundTxt.setObjectName(u"npcBackgroundTxt")
        self.npcBackgroundTxt.setFont(font1)
        self.npcBackgroundTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcBackgroundTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.personalityVL.addWidget(self.npcBackgroundTxt)

        self.npcBackgroundLabel = QLabel(self.verticalLayoutWidget_2)
        self.npcBackgroundLabel.setObjectName(u"npcBackgroundLabel")
        font3 = QFont()
        font3.setPointSize(8)
        self.npcBackgroundLabel.setFont(font3)
        self.npcBackgroundLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcBackgroundLabel.setAlignment(Qt.AlignCenter)
        self.npcBackgroundLabel.setWordWrap(True)
        self.npcBackgroundLabel.setMargin(5)

        self.personalityVL.addWidget(self.npcBackgroundLabel)

        self.gridLayoutWidget_2 = QWidget(self.npcFrame)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 0, 381, 211))
        self.gridLayoutWidget_2.setFont(font1)
        self.npcCharacterGL = QGridLayout(self.gridLayoutWidget_2)
        self.npcCharacterGL.setObjectName(u"npcCharacterGL")
        self.npcCharacterGL.setHorizontalSpacing(12)
        self.npcCharacterGL.setContentsMargins(0, 0, 0, 0)
        self.npcFirstNameTxt = QLabel(self.gridLayoutWidget_2)
        self.npcFirstNameTxt.setObjectName(u"npcFirstNameTxt")
        self.npcFirstNameTxt.setFont(font1)
        self.npcFirstNameTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcFirstNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcCharacterGL.addWidget(self.npcFirstNameTxt, 0, 0, 1, 1)

        self.npcLastNameTxt = QLabel(self.gridLayoutWidget_2)
        self.npcLastNameTxt.setObjectName(u"npcLastNameTxt")
        self.npcLastNameTxt.setFont(font1)
        self.npcLastNameTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcLastNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcCharacterGL.addWidget(self.npcLastNameTxt, 0, 1, 1, 1)

        self.npcAlignmentTxt = QLabel(self.gridLayoutWidget_2)
        self.npcAlignmentTxt.setObjectName(u"npcAlignmentTxt")
        self.npcAlignmentTxt.setFont(font1)
        self.npcAlignmentTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcAlignmentTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcCharacterGL.addWidget(self.npcAlignmentTxt, 2, 1, 1, 1)

        self.npcFirstNameLabel = QLabel(self.gridLayoutWidget_2)
        self.npcFirstNameLabel.setObjectName(u"npcFirstNameLabel")
        font4 = QFont()
        font4.setFamilies([u"Bahnschrift Light"])
        font4.setPointSize(9)
        self.npcFirstNameLabel.setFont(font4)
        self.npcFirstNameLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcFirstNameLabel.setAlignment(Qt.AlignCenter)
        self.npcFirstNameLabel.setWordWrap(True)

        self.npcCharacterGL.addWidget(self.npcFirstNameLabel, 1, 0, 1, 1)

        self.npcAlignmentLabel = QLabel(self.gridLayoutWidget_2)
        self.npcAlignmentLabel.setObjectName(u"npcAlignmentLabel")
        self.npcAlignmentLabel.setFont(font4)
        self.npcAlignmentLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcAlignmentLabel.setAlignment(Qt.AlignCenter)
        self.npcAlignmentLabel.setWordWrap(True)

        self.npcCharacterGL.addWidget(self.npcAlignmentLabel, 3, 1, 1, 1)

        self.npcClassTxt = QLabel(self.gridLayoutWidget_2)
        self.npcClassTxt.setObjectName(u"npcClassTxt")
        self.npcClassTxt.setFont(font1)
        self.npcClassTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcClassTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcCharacterGL.addWidget(self.npcClassTxt, 4, 0, 1, 1)

        self.npcGenderTxt = QLabel(self.gridLayoutWidget_2)
        self.npcGenderTxt.setObjectName(u"npcGenderTxt")
        self.npcGenderTxt.setFont(font1)
        self.npcGenderTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcGenderTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcCharacterGL.addWidget(self.npcGenderTxt, 2, 0, 1, 1)

        self.npcLastNameLabel = QLabel(self.gridLayoutWidget_2)
        self.npcLastNameLabel.setObjectName(u"npcLastNameLabel")
        self.npcLastNameLabel.setFont(font4)
        self.npcLastNameLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcLastNameLabel.setAlignment(Qt.AlignCenter)
        self.npcLastNameLabel.setWordWrap(True)

        self.npcCharacterGL.addWidget(self.npcLastNameLabel, 1, 1, 1, 1)

        self.npcSubclassTxt = QLabel(self.gridLayoutWidget_2)
        self.npcSubclassTxt.setObjectName(u"npcSubclassTxt")
        self.npcSubclassTxt.setFont(font1)
        self.npcSubclassTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcSubclassTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcCharacterGL.addWidget(self.npcSubclassTxt, 4, 1, 1, 1)

        self.npcSubclassLabel = QLabel(self.gridLayoutWidget_2)
        self.npcSubclassLabel.setObjectName(u"npcSubclassLabel")
        self.npcSubclassLabel.setFont(font2)
        self.npcSubclassLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcSubclassLabel.setAlignment(Qt.AlignCenter)
        self.npcSubclassLabel.setWordWrap(True)

        self.npcCharacterGL.addWidget(self.npcSubclassLabel, 5, 1, 1, 1)

        self.genderLabel = QLabel(self.gridLayoutWidget_2)
        self.genderLabel.setObjectName(u"genderLabel")
        self.genderLabel.setFont(font4)
        self.genderLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.genderLabel.setAlignment(Qt.AlignCenter)
        self.genderLabel.setWordWrap(True)

        self.npcCharacterGL.addWidget(self.genderLabel, 3, 0, 1, 1)

        self.npcClassLabel = QLabel(self.gridLayoutWidget_2)
        self.npcClassLabel.setObjectName(u"npcClassLabel")
        self.npcClassLabel.setFont(font2)
        self.npcClassLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcClassLabel.setAlignment(Qt.AlignCenter)
        self.npcClassLabel.setWordWrap(True)

        self.npcCharacterGL.addWidget(self.npcClassLabel, 5, 0, 1, 1)

        self.gridLayoutWidget_3 = QWidget(self.npcFrame)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(20, 220, 381, 191))
        self.npcPhysicalGL = QGridLayout(self.gridLayoutWidget_3)
        self.npcPhysicalGL.setObjectName(u"npcPhysicalGL")
        self.npcPhysicalGL.setHorizontalSpacing(12)
        self.npcPhysicalGL.setContentsMargins(0, 0, 0, 0)
        self.npcHeightTxt = QLabel(self.gridLayoutWidget_3)
        self.npcHeightTxt.setObjectName(u"npcHeightTxt")
        self.npcHeightTxt.setFont(font1)
        self.npcHeightTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcHeightTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcPhysicalGL.addWidget(self.npcHeightTxt, 0, 1, 1, 1)

        self.npcHeightLabel = QLabel(self.gridLayoutWidget_3)
        self.npcHeightLabel.setObjectName(u"npcHeightLabel")
        self.npcHeightLabel.setFont(font2)
        self.npcHeightLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcHeightLabel.setAlignment(Qt.AlignCenter)
        self.npcHeightLabel.setWordWrap(True)

        self.npcPhysicalGL.addWidget(self.npcHeightLabel, 1, 1, 1, 1)

        self.npcRaceTxt = QLabel(self.gridLayoutWidget_3)
        self.npcRaceTxt.setObjectName(u"npcRaceTxt")
        self.npcRaceTxt.setFont(font1)
        self.npcRaceTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcRaceTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcPhysicalGL.addWidget(self.npcRaceTxt, 0, 0, 1, 1)

        self.npcBuildLabel = QLabel(self.gridLayoutWidget_3)
        self.npcBuildLabel.setObjectName(u"npcBuildLabel")
        self.npcBuildLabel.setFont(font2)
        self.npcBuildLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcBuildLabel.setAlignment(Qt.AlignCenter)
        self.npcBuildLabel.setWordWrap(True)

        self.npcPhysicalGL.addWidget(self.npcBuildLabel, 3, 1, 1, 1)

        self.npcRraceLabel = QLabel(self.gridLayoutWidget_3)
        self.npcRraceLabel.setObjectName(u"npcRraceLabel")
        self.npcRraceLabel.setFont(font2)
        self.npcRraceLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcRraceLabel.setAlignment(Qt.AlignCenter)
        self.npcRraceLabel.setWordWrap(True)

        self.npcPhysicalGL.addWidget(self.npcRraceLabel, 1, 0, 1, 1)

        self.npcEyesTxt = QLabel(self.gridLayoutWidget_3)
        self.npcEyesTxt.setObjectName(u"npcEyesTxt")
        self.npcEyesTxt.setFont(font1)
        self.npcEyesTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcEyesTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcPhysicalGL.addWidget(self.npcEyesTxt, 4, 0, 1, 1)

        self.npcAgeTxt = QLabel(self.gridLayoutWidget_3)
        self.npcAgeTxt.setObjectName(u"npcAgeTxt")
        self.npcAgeTxt.setFont(font1)
        self.npcAgeTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcAgeTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcPhysicalGL.addWidget(self.npcAgeTxt, 2, 0, 1, 1)

        self.npcBuildTxt = QLabel(self.gridLayoutWidget_3)
        self.npcBuildTxt.setObjectName(u"npcBuildTxt")
        self.npcBuildTxt.setFont(font1)
        self.npcBuildTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcBuildTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcPhysicalGL.addWidget(self.npcBuildTxt, 2, 1, 1, 1)

        self.npcAgeLabel = QLabel(self.gridLayoutWidget_3)
        self.npcAgeLabel.setObjectName(u"npcAgeLabel")
        self.npcAgeLabel.setFont(font2)
        self.npcAgeLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcAgeLabel.setAlignment(Qt.AlignCenter)
        self.npcAgeLabel.setWordWrap(True)

        self.npcPhysicalGL.addWidget(self.npcAgeLabel, 3, 0, 1, 1)

        self.npcHairTxt = QLabel(self.gridLayoutWidget_3)
        self.npcHairTxt.setObjectName(u"npcHairTxt")
        self.npcHairTxt.setFont(font1)
        self.npcHairTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.npcHairTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.npcPhysicalGL.addWidget(self.npcHairTxt, 4, 1, 1, 1)

        self.npcEyesLabel = QLabel(self.gridLayoutWidget_3)
        self.npcEyesLabel.setObjectName(u"npcEyesLabel")
        self.npcEyesLabel.setFont(font3)
        self.npcEyesLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcEyesLabel.setAlignment(Qt.AlignCenter)
        self.npcEyesLabel.setWordWrap(True)

        self.npcPhysicalGL.addWidget(self.npcEyesLabel, 5, 0, 1, 1)

        self.npcHairLabel = QLabel(self.gridLayoutWidget_3)
        self.npcHairLabel.setObjectName(u"npcHairLabel")
        self.npcHairLabel.setFont(font3)
        self.npcHairLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.npcHairLabel.setAlignment(Qt.AlignCenter)
        self.npcHairLabel.setWordWrap(True)

        self.npcPhysicalGL.addWidget(self.npcHairLabel, 5, 1, 1, 1)


        self.npcGridContainer.addWidget(self.npcFrame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page1NPC)
        self.page2Bldg = QWidget()
        self.page2Bldg.setObjectName(u"page2Bldg")
        self.page2Bldg.setFont(font1)
        self.gridLayoutWidget_4 = QWidget(self.page2Bldg)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 10, 841, 421))
        self.bldgGridContainer = QGridLayout(self.gridLayoutWidget_4)
        self.bldgGridContainer.setObjectName(u"bldgGridContainer")
        self.bldgGridContainer.setContentsMargins(0, 0, 0, 0)
        self.bldgFrame = QFrame(self.gridLayoutWidget_4)
        self.bldgFrame.setObjectName(u"bldgFrame")
        self.bldgFrame.setFrameShape(QFrame.StyledPanel)
        self.bldgFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_8 = QWidget(self.bldgFrame)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(370, -30, 461, 431))
        self.bldgBigVL = QVBoxLayout(self.verticalLayoutWidget_8)
        self.bldgBigVL.setObjectName(u"bldgBigVL")
        self.bldgBigVL.setContentsMargins(0, 0, 0, 0)
        self.bldgDesTxt = QLabel(self.verticalLayoutWidget_8)
        self.bldgDesTxt.setObjectName(u"bldgDesTxt")
        self.bldgDesTxt.setFont(font1)
        self.bldgDesTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.bldgDesTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bldgDesTxt.setWordWrap(True)

        self.bldgBigVL.addWidget(self.bldgDesTxt)

        self.bldgDesLabel = QLabel(self.verticalLayoutWidget_8)
        self.bldgDesLabel.setObjectName(u"bldgDesLabel")
        self.bldgDesLabel.setFont(font1)
        self.bldgDesLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.bldgDesLabel.setAlignment(Qt.AlignCenter)
        self.bldgDesLabel.setWordWrap(True)
        self.bldgDesLabel.setMargin(5)

        self.bldgBigVL.addWidget(self.bldgDesLabel)

        self.bldgVendorTxt = QLabel(self.verticalLayoutWidget_8)
        self.bldgVendorTxt.setObjectName(u"bldgVendorTxt")
        self.bldgVendorTxt.setFont(font1)
        self.bldgVendorTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.bldgVendorTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bldgVendorTxt.setWordWrap(True)

        self.bldgBigVL.addWidget(self.bldgVendorTxt)

        self.bldgVendorLabel = QLabel(self.verticalLayoutWidget_8)
        self.bldgVendorLabel.setObjectName(u"bldgVendorLabel")
        self.bldgVendorLabel.setFont(font1)
        self.bldgVendorLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.bldgVendorLabel.setAlignment(Qt.AlignCenter)
        self.bldgVendorLabel.setWordWrap(True)
        self.bldgVendorLabel.setMargin(5)

        self.bldgBigVL.addWidget(self.bldgVendorLabel)

        self.bldgGoodsTxt = QLabel(self.verticalLayoutWidget_8)
        self.bldgGoodsTxt.setObjectName(u"bldgGoodsTxt")
        self.bldgGoodsTxt.setFont(font1)
        self.bldgGoodsTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.bldgGoodsTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bldgGoodsTxt.setWordWrap(True)

        self.bldgBigVL.addWidget(self.bldgGoodsTxt)

        self.bldgGoodsLabel = QLabel(self.verticalLayoutWidget_8)
        self.bldgGoodsLabel.setObjectName(u"bldgGoodsLabel")
        self.bldgGoodsLabel.setFont(font1)
        self.bldgGoodsLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.bldgGoodsLabel.setAlignment(Qt.AlignCenter)
        self.bldgGoodsLabel.setWordWrap(True)
        self.bldgGoodsLabel.setMargin(5)

        self.bldgBigVL.addWidget(self.bldgGoodsLabel)

        self.verticalLayoutWidget_7 = QWidget(self.bldgFrame)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(9, 9, 321, 391))
        self.bldgSmallVL = QVBoxLayout(self.verticalLayoutWidget_7)
        self.bldgSmallVL.setObjectName(u"bldgSmallVL")
        self.bldgSmallVL.setContentsMargins(0, 0, 0, 0)
        self.bldgNameTxT = QLabel(self.verticalLayoutWidget_7)
        self.bldgNameTxT.setObjectName(u"bldgNameTxT")
        self.bldgNameTxT.setFont(font1)
        self.bldgNameTxT.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.bldgNameTxT.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bldgNameTxT.setWordWrap(True)

        self.bldgSmallVL.addWidget(self.bldgNameTxT)

        self.bldgNameLabel = QLabel(self.verticalLayoutWidget_7)
        self.bldgNameLabel.setObjectName(u"bldgNameLabel")
        self.bldgNameLabel.setFont(font1)
        self.bldgNameLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.bldgNameLabel.setAlignment(Qt.AlignCenter)
        self.bldgNameLabel.setWordWrap(True)
        self.bldgNameLabel.setMargin(5)

        self.bldgSmallVL.addWidget(self.bldgNameLabel)

        self.bldgTypeTxt = QLabel(self.verticalLayoutWidget_7)
        self.bldgTypeTxt.setObjectName(u"bldgTypeTxt")
        self.bldgTypeTxt.setFont(font1)
        self.bldgTypeTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.bldgTypeTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bldgTypeTxt.setWordWrap(True)

        self.bldgSmallVL.addWidget(self.bldgTypeTxt)

        self.bldgTypeLabel = QLabel(self.verticalLayoutWidget_7)
        self.bldgTypeLabel.setObjectName(u"bldgTypeLabel")
        self.bldgTypeLabel.setFont(font1)
        self.bldgTypeLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.bldgTypeLabel.setAlignment(Qt.AlignCenter)
        self.bldgTypeLabel.setWordWrap(True)
        self.bldgTypeLabel.setMargin(5)

        self.bldgSmallVL.addWidget(self.bldgTypeLabel)

        self.bldgSizeTxt = QLabel(self.verticalLayoutWidget_7)
        self.bldgSizeTxt.setObjectName(u"bldgSizeTxt")
        self.bldgSizeTxt.setFont(font1)
        self.bldgSizeTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.bldgSizeTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bldgSizeTxt.setWordWrap(True)

        self.bldgSmallVL.addWidget(self.bldgSizeTxt)

        self.bldgSizeLabel = QLabel(self.verticalLayoutWidget_7)
        self.bldgSizeLabel.setObjectName(u"bldgSizeLabel")
        self.bldgSizeLabel.setFont(font1)
        self.bldgSizeLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.bldgSizeLabel.setAlignment(Qt.AlignCenter)
        self.bldgSizeLabel.setWordWrap(True)
        self.bldgSizeLabel.setMargin(5)

        self.bldgSmallVL.addWidget(self.bldgSizeLabel)

        self.bldgArcTxt = QLabel(self.verticalLayoutWidget_7)
        self.bldgArcTxt.setObjectName(u"bldgArcTxt")
        self.bldgArcTxt.setFont(font1)
        self.bldgArcTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.bldgArcTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bldgArcTxt.setWordWrap(True)

        self.bldgSmallVL.addWidget(self.bldgArcTxt)

        self.bldgArcLabel = QLabel(self.verticalLayoutWidget_7)
        self.bldgArcLabel.setObjectName(u"bldgArcLabel")
        self.bldgArcLabel.setFont(font1)
        self.bldgArcLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.bldgArcLabel.setAlignment(Qt.AlignCenter)
        self.bldgArcLabel.setWordWrap(True)
        self.bldgArcLabel.setMargin(5)

        self.bldgSmallVL.addWidget(self.bldgArcLabel)

        self.bldgAmbTxt = QLabel(self.verticalLayoutWidget_7)
        self.bldgAmbTxt.setObjectName(u"bldgAmbTxt")
        self.bldgAmbTxt.setFont(font1)
        self.bldgAmbTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.bldgAmbTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bldgAmbTxt.setWordWrap(True)

        self.bldgSmallVL.addWidget(self.bldgAmbTxt)

        self.bldgAmbLabel = QLabel(self.verticalLayoutWidget_7)
        self.bldgAmbLabel.setObjectName(u"bldgAmbLabel")
        self.bldgAmbLabel.setFont(font1)
        self.bldgAmbLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.bldgAmbLabel.setAlignment(Qt.AlignCenter)
        self.bldgAmbLabel.setWordWrap(True)
        self.bldgAmbLabel.setMargin(5)

        self.bldgSmallVL.addWidget(self.bldgAmbLabel)

        self.bldgTrafficTxt = QLabel(self.verticalLayoutWidget_7)
        self.bldgTrafficTxt.setObjectName(u"bldgTrafficTxt")
        self.bldgTrafficTxt.setFont(font1)
        self.bldgTrafficTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.bldgTrafficTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bldgTrafficTxt.setWordWrap(True)

        self.bldgSmallVL.addWidget(self.bldgTrafficTxt)

        self.bldgTrafficLabel = QLabel(self.verticalLayoutWidget_7)
        self.bldgTrafficLabel.setObjectName(u"bldgTrafficLabel")
        self.bldgTrafficLabel.setFont(font1)
        self.bldgTrafficLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.bldgTrafficLabel.setAlignment(Qt.AlignCenter)
        self.bldgTrafficLabel.setWordWrap(True)
        self.bldgTrafficLabel.setMargin(5)

        self.bldgSmallVL.addWidget(self.bldgTrafficLabel)


        self.bldgGridContainer.addWidget(self.bldgFrame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page2Bldg)
        self.page3Twn = QWidget()
        self.page3Twn.setObjectName(u"page3Twn")
        self.gridLayoutWidget_5 = QWidget(self.page3Twn)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(-1, -1, 861, 441))
        self.twnGridContainer = QGridLayout(self.gridLayoutWidget_5)
        self.twnGridContainer.setObjectName(u"twnGridContainer")
        self.twnGridContainer.setContentsMargins(0, 0, 0, 0)
        self.twnFrame = QFrame(self.gridLayoutWidget_5)
        self.twnFrame.setObjectName(u"twnFrame")
        self.twnFrame.setFrameShape(QFrame.StyledPanel)
        self.twnFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_3 = QWidget(self.twnFrame)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(19, 9, 261, 421))
        self.twnSmallVL = QVBoxLayout(self.verticalLayoutWidget_3)
        self.twnSmallVL.setObjectName(u"twnSmallVL")
        self.twnSmallVL.setContentsMargins(0, 0, 0, 0)
        self.twnNameTxt = QLabel(self.verticalLayoutWidget_3)
        self.twnNameTxt.setObjectName(u"twnNameTxt")
        self.twnNameTxt.setFont(font1)
        self.twnNameTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.twnNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.twnNameTxt.setWordWrap(True)

        self.twnSmallVL.addWidget(self.twnNameTxt)

        self.twnNameLabel = QLabel(self.verticalLayoutWidget_3)
        self.twnNameLabel.setObjectName(u"twnNameLabel")
        self.twnNameLabel.setFont(font1)
        self.twnNameLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.twnNameLabel.setAlignment(Qt.AlignCenter)
        self.twnNameLabel.setWordWrap(True)
        self.twnNameLabel.setMargin(5)

        self.twnSmallVL.addWidget(self.twnNameLabel)

        self.twnPopTxt = QLabel(self.verticalLayoutWidget_3)
        self.twnPopTxt.setObjectName(u"twnPopTxt")
        self.twnPopTxt.setFont(font1)
        self.twnPopTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.twnPopTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.twnPopTxt.setWordWrap(True)

        self.twnSmallVL.addWidget(self.twnPopTxt)

        self.twnPopLabel = QLabel(self.verticalLayoutWidget_3)
        self.twnPopLabel.setObjectName(u"twnPopLabel")
        self.twnPopLabel.setFont(font1)
        self.twnPopLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.twnPopLabel.setAlignment(Qt.AlignCenter)
        self.twnPopLabel.setWordWrap(True)
        self.twnPopLabel.setMargin(5)

        self.twnSmallVL.addWidget(self.twnPopLabel)

        self.twnSprawlTxt = QLabel(self.verticalLayoutWidget_3)
        self.twnSprawlTxt.setObjectName(u"twnSprawlTxt")
        self.twnSprawlTxt.setFont(font1)
        self.twnSprawlTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.twnSprawlTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.twnSprawlTxt.setWordWrap(True)

        self.twnSmallVL.addWidget(self.twnSprawlTxt)

        self.twnSprawlLabel = QLabel(self.verticalLayoutWidget_3)
        self.twnSprawlLabel.setObjectName(u"twnSprawlLabel")
        self.twnSprawlLabel.setFont(font1)
        self.twnSprawlLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.twnSprawlLabel.setAlignment(Qt.AlignCenter)
        self.twnSprawlLabel.setWordWrap(True)
        self.twnSprawlLabel.setMargin(5)

        self.twnSmallVL.addWidget(self.twnSprawlLabel)

        self.twnArcTxt = QLabel(self.verticalLayoutWidget_3)
        self.twnArcTxt.setObjectName(u"twnArcTxt")
        self.twnArcTxt.setFont(font1)
        self.twnArcTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.twnArcTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.twnArcTxt.setWordWrap(True)

        self.twnSmallVL.addWidget(self.twnArcTxt)

        self.twnArcLabel = QLabel(self.verticalLayoutWidget_3)
        self.twnArcLabel.setObjectName(u"twnArcLabel")
        self.twnArcLabel.setFont(font1)
        self.twnArcLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.twnArcLabel.setAlignment(Qt.AlignCenter)
        self.twnArcLabel.setWordWrap(True)
        self.twnArcLabel.setMargin(5)

        self.twnSmallVL.addWidget(self.twnArcLabel)

        self.twnIndTxt = QLabel(self.verticalLayoutWidget_3)
        self.twnIndTxt.setObjectName(u"twnIndTxt")
        self.twnIndTxt.setFont(font1)
        self.twnIndTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.twnIndTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.twnIndTxt.setWordWrap(True)

        self.twnSmallVL.addWidget(self.twnIndTxt)

        self.twnIndLabel = QLabel(self.verticalLayoutWidget_3)
        self.twnIndLabel.setObjectName(u"twnIndLabel")
        self.twnIndLabel.setFont(font1)
        self.twnIndLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.twnIndLabel.setAlignment(Qt.AlignCenter)
        self.twnIndLabel.setWordWrap(True)
        self.twnIndLabel.setMargin(5)

        self.twnSmallVL.addWidget(self.twnIndLabel)

        self.twnClimTxt = QLabel(self.verticalLayoutWidget_3)
        self.twnClimTxt.setObjectName(u"twnClimTxt")
        self.twnClimTxt.setFont(font1)
        self.twnClimTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.twnClimTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.twnClimTxt.setWordWrap(True)

        self.twnSmallVL.addWidget(self.twnClimTxt)

        self.twnClimLabel = QLabel(self.verticalLayoutWidget_3)
        self.twnClimLabel.setObjectName(u"twnClimLabel")
        self.twnClimLabel.setFont(font1)
        self.twnClimLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.twnClimLabel.setAlignment(Qt.AlignCenter)
        self.twnClimLabel.setWordWrap(True)
        self.twnClimLabel.setMargin(5)

        self.twnSmallVL.addWidget(self.twnClimLabel)

        self.verticalLayoutWidget_4 = QWidget(self.twnFrame)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(310, -30, 521, 451))
        self.twnBigVL = QVBoxLayout(self.verticalLayoutWidget_4)
        self.twnBigVL.setObjectName(u"twnBigVL")
        self.twnBigVL.setContentsMargins(0, 0, 0, 0)
        self.twnGovTypeTxt = QLabel(self.verticalLayoutWidget_4)
        self.twnGovTypeTxt.setObjectName(u"twnGovTypeTxt")
        self.twnGovTypeTxt.setFont(font1)
        self.twnGovTypeTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.twnGovTypeTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.twnGovTypeTxt.setWordWrap(True)

        self.twnBigVL.addWidget(self.twnGovTypeTxt)

        self.twnGovTypeLabel = QLabel(self.verticalLayoutWidget_4)
        self.twnGovTypeLabel.setObjectName(u"twnGovTypeLabel")
        self.twnGovTypeLabel.setFont(font1)
        self.twnGovTypeLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.twnGovTypeLabel.setAlignment(Qt.AlignCenter)
        self.twnGovTypeLabel.setWordWrap(True)
        self.twnGovTypeLabel.setMargin(5)

        self.twnBigVL.addWidget(self.twnGovTypeLabel)

        self.twnLoreTxt = QLabel(self.verticalLayoutWidget_4)
        self.twnLoreTxt.setObjectName(u"twnLoreTxt")
        self.twnLoreTxt.setFont(font1)
        self.twnLoreTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.twnLoreTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.twnLoreTxt.setWordWrap(True)

        self.twnBigVL.addWidget(self.twnLoreTxt)

        self.twnLoreLabel = QLabel(self.verticalLayoutWidget_4)
        self.twnLoreLabel.setObjectName(u"twnLoreLabel")
        self.twnLoreLabel.setFont(font1)
        self.twnLoreLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.twnLoreLabel.setAlignment(Qt.AlignCenter)
        self.twnLoreLabel.setWordWrap(True)
        self.twnLoreLabel.setMargin(5)

        self.twnBigVL.addWidget(self.twnLoreLabel)

        self.twnQuestsTxt = QLabel(self.verticalLayoutWidget_4)
        self.twnQuestsTxt.setObjectName(u"twnQuestsTxt")
        self.twnQuestsTxt.setFont(font1)
        self.twnQuestsTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.twnQuestsTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.twnQuestsTxt.setWordWrap(True)

        self.twnBigVL.addWidget(self.twnQuestsTxt)

        self.twnQuestLabel = QLabel(self.verticalLayoutWidget_4)
        self.twnQuestLabel.setObjectName(u"twnQuestLabel")
        self.twnQuestLabel.setFont(font1)
        self.twnQuestLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.twnQuestLabel.setAlignment(Qt.AlignCenter)
        self.twnQuestLabel.setWordWrap(True)
        self.twnQuestLabel.setMargin(5)

        self.twnBigVL.addWidget(self.twnQuestLabel)


        self.twnGridContainer.addWidget(self.twnFrame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page3Twn)
        self.page4Enc = QWidget()
        self.page4Enc.setObjectName(u"page4Enc")
        self.gridLayoutWidget_6 = QWidget(self.page4Enc)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 0, 861, 441))
        self.encGridContainer = QGridLayout(self.gridLayoutWidget_6)
        self.encGridContainer.setObjectName(u"encGridContainer")
        self.encGridContainer.setContentsMargins(0, 0, 0, 0)
        self.encFrame = QFrame(self.gridLayoutWidget_6)
        self.encFrame.setObjectName(u"encFrame")
        self.encFrame.setFrameShape(QFrame.StyledPanel)
        self.encFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_5 = QWidget(self.encFrame)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 841, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.encNameTxt = QLabel(self.verticalLayoutWidget_5)
        self.encNameTxt.setObjectName(u"encNameTxt")
        self.encNameTxt.setFont(font1)
        self.encNameTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.encNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.encNameTxt.setWordWrap(True)
        self.encNameTxt.setMargin(5)

        self.verticalLayout.addWidget(self.encNameTxt)

        self.encNameLabel = QLabel(self.verticalLayoutWidget_5)
        self.encNameLabel.setObjectName(u"encNameLabel")
        self.encNameLabel.setFont(font1)
        self.encNameLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.encNameLabel.setAlignment(Qt.AlignCenter)
        self.encNameLabel.setWordWrap(True)
        self.encNameLabel.setMargin(5)

        self.verticalLayout.addWidget(self.encNameLabel)

        self.label_2 = QLabel(self.verticalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.encCRSlider = QSlider(self.verticalLayoutWidget_5)
        self.encCRSlider.setObjectName(u"encCRSlider")
        self.encCRSlider.setMinimum(1)
        self.encCRSlider.setMaximum(30)
        self.encCRSlider.setSingleStep(1)
        self.encCRSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.encCRSlider)

        self.label_3 = QLabel(self.verticalLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.encNumCreatures = QSlider(self.verticalLayoutWidget_5)
        self.encNumCreatures.setObjectName(u"encNumCreatures")
        self.encNumCreatures.setMinimum(1)
        self.encNumCreatures.setMaximum(10)
        self.encNumCreatures.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.encNumCreatures)

        self.encCreaturesTxt = QLabel(self.verticalLayoutWidget_5)
        self.encCreaturesTxt.setObjectName(u"encCreaturesTxt")
        self.encCreaturesTxt.setFont(font1)
        self.encCreaturesTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.encCreaturesTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.encCreaturesTxt.setWordWrap(True)
        self.encCreaturesTxt.setMargin(5)

        self.verticalLayout.addWidget(self.encCreaturesTxt)

        self.encCreaturesLabel = QLabel(self.verticalLayoutWidget_5)
        self.encCreaturesLabel.setObjectName(u"encCreaturesLabel")
        self.encCreaturesLabel.setFont(font1)
        self.encCreaturesLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.encCreaturesLabel.setAlignment(Qt.AlignCenter)
        self.encCreaturesLabel.setWordWrap(True)
        self.encCreaturesLabel.setMargin(5)

        self.verticalLayout.addWidget(self.encCreaturesLabel)

        self.encDesTxt = QLabel(self.verticalLayoutWidget_5)
        self.encDesTxt.setObjectName(u"encDesTxt")
        self.encDesTxt.setFont(font1)
        self.encDesTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.encDesTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.encDesTxt.setWordWrap(True)
        self.encDesTxt.setMargin(5)

        self.verticalLayout.addWidget(self.encDesTxt)

        self.encDesLabel = QLabel(self.verticalLayoutWidget_5)
        self.encDesLabel.setObjectName(u"encDesLabel")
        self.encDesLabel.setFont(font1)
        self.encDesLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.encDesLabel.setAlignment(Qt.AlignCenter)
        self.encDesLabel.setWordWrap(True)
        self.encDesLabel.setMargin(5)

        self.verticalLayout.addWidget(self.encDesLabel)


        self.encGridContainer.addWidget(self.encFrame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page4Enc)
        self.page5Grp = QWidget()
        self.page5Grp.setObjectName(u"page5Grp")
        self.gridLayoutWidget_7 = QWidget(self.page5Grp)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(-1, -1, 861, 441))
        self.grpGridContainer = QGridLayout(self.gridLayoutWidget_7)
        self.grpGridContainer.setObjectName(u"grpGridContainer")
        self.grpGridContainer.setContentsMargins(0, 0, 0, 0)
        self.grpFrame = QFrame(self.gridLayoutWidget_7)
        self.grpFrame.setObjectName(u"grpFrame")
        self.grpFrame.setFrameShape(QFrame.StyledPanel)
        self.grpFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_6 = QWidget(self.grpFrame)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 0, 261, 411))
        self.grpSmallVL = QVBoxLayout(self.verticalLayoutWidget_6)
        self.grpSmallVL.setObjectName(u"grpSmallVL")
        self.grpSmallVL.setContentsMargins(0, 0, 0, 0)
        self.grpNameTxt = QLabel(self.verticalLayoutWidget_6)
        self.grpNameTxt.setObjectName(u"grpNameTxt")
        self.grpNameTxt.setFont(font1)
        self.grpNameTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.grpNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.grpNameTxt.setWordWrap(True)

        self.grpSmallVL.addWidget(self.grpNameTxt)

        self.grpNameLabel = QLabel(self.verticalLayoutWidget_6)
        self.grpNameLabel.setObjectName(u"grpNameLabel")
        self.grpNameLabel.setFont(font1)
        self.grpNameLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.grpNameLabel.setAlignment(Qt.AlignCenter)
        self.grpNameLabel.setWordWrap(True)
        self.grpNameLabel.setMargin(5)

        self.grpSmallVL.addWidget(self.grpNameLabel)

        self.grpPopTxt = QLabel(self.verticalLayoutWidget_6)
        self.grpPopTxt.setObjectName(u"grpPopTxt")
        self.grpPopTxt.setFont(font1)
        self.grpPopTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.grpPopTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.grpPopTxt.setWordWrap(True)

        self.grpSmallVL.addWidget(self.grpPopTxt)

        self.grpPopTxt_2 = QLabel(self.verticalLayoutWidget_6)
        self.grpPopTxt_2.setObjectName(u"grpPopTxt_2")
        self.grpPopTxt_2.setFont(font1)
        self.grpPopTxt_2.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.grpPopTxt_2.setAlignment(Qt.AlignCenter)
        self.grpPopTxt_2.setWordWrap(True)
        self.grpPopTxt_2.setMargin(5)

        self.grpSmallVL.addWidget(self.grpPopTxt_2)

        self.grpMoralityTxt = QLabel(self.verticalLayoutWidget_6)
        self.grpMoralityTxt.setObjectName(u"grpMoralityTxt")
        self.grpMoralityTxt.setFont(font1)
        self.grpMoralityTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.grpMoralityTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.grpMoralityTxt.setWordWrap(True)

        self.grpSmallVL.addWidget(self.grpMoralityTxt)

        self.grpMoralityLabel = QLabel(self.verticalLayoutWidget_6)
        self.grpMoralityLabel.setObjectName(u"grpMoralityLabel")
        self.grpMoralityLabel.setFont(font1)
        self.grpMoralityLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.grpMoralityLabel.setAlignment(Qt.AlignCenter)
        self.grpMoralityLabel.setWordWrap(True)
        self.grpMoralityLabel.setMargin(5)

        self.grpSmallVL.addWidget(self.grpMoralityLabel)

        self.grpDevotionTxt = QLabel(self.verticalLayoutWidget_6)
        self.grpDevotionTxt.setObjectName(u"grpDevotionTxt")
        self.grpDevotionTxt.setFont(font1)
        self.grpDevotionTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.grpDevotionTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.grpDevotionTxt.setWordWrap(True)

        self.grpSmallVL.addWidget(self.grpDevotionTxt)

        self.grpDevotionTxt_2 = QLabel(self.verticalLayoutWidget_6)
        self.grpDevotionTxt_2.setObjectName(u"grpDevotionTxt_2")
        self.grpDevotionTxt_2.setFont(font1)
        self.grpDevotionTxt_2.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.grpDevotionTxt_2.setAlignment(Qt.AlignCenter)
        self.grpDevotionTxt_2.setWordWrap(True)
        self.grpDevotionTxt_2.setMargin(5)

        self.grpSmallVL.addWidget(self.grpDevotionTxt_2)

        self.verticalLayoutWidget_9 = QWidget(self.grpFrame)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(319, -31, 521, 451))
        self.grpBigVL = QVBoxLayout(self.verticalLayoutWidget_9)
        self.grpBigVL.setObjectName(u"grpBigVL")
        self.grpBigVL.setContentsMargins(0, 0, 0, 0)
        self.grpCauseTxt = QLabel(self.verticalLayoutWidget_9)
        self.grpCauseTxt.setObjectName(u"grpCauseTxt")
        self.grpCauseTxt.setFont(font1)
        self.grpCauseTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.grpCauseTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.grpCauseTxt.setWordWrap(True)

        self.grpBigVL.addWidget(self.grpCauseTxt)

        self.grpCauseLabel = QLabel(self.verticalLayoutWidget_9)
        self.grpCauseLabel.setObjectName(u"grpCauseLabel")
        self.grpCauseLabel.setFont(font1)
        self.grpCauseLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.grpCauseLabel.setAlignment(Qt.AlignCenter)
        self.grpCauseLabel.setWordWrap(True)
        self.grpCauseLabel.setMargin(5)

        self.grpBigVL.addWidget(self.grpCauseLabel)

        self.grpTraitsTxt = QLabel(self.verticalLayoutWidget_9)
        self.grpTraitsTxt.setObjectName(u"grpTraitsTxt")
        self.grpTraitsTxt.setFont(font1)
        self.grpTraitsTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.grpTraitsTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.grpTraitsTxt.setWordWrap(True)

        self.grpBigVL.addWidget(self.grpTraitsTxt)

        self.grpTraitsLabel = QLabel(self.verticalLayoutWidget_9)
        self.grpTraitsLabel.setObjectName(u"grpTraitsLabel")
        self.grpTraitsLabel.setFont(font1)
        self.grpTraitsLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.grpTraitsLabel.setAlignment(Qt.AlignCenter)
        self.grpTraitsLabel.setWordWrap(True)
        self.grpTraitsLabel.setMargin(5)

        self.grpBigVL.addWidget(self.grpTraitsLabel)

        self.grpPresenceTxt = QLabel(self.verticalLayoutWidget_9)
        self.grpPresenceTxt.setObjectName(u"grpPresenceTxt")
        self.grpPresenceTxt.setFont(font1)
        self.grpPresenceTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.grpPresenceTxt.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.grpPresenceTxt.setWordWrap(True)

        self.grpBigVL.addWidget(self.grpPresenceTxt)

        self.grpPresenceLabel = QLabel(self.verticalLayoutWidget_9)
        self.grpPresenceLabel.setObjectName(u"grpPresenceLabel")
        self.grpPresenceLabel.setFont(font1)
        self.grpPresenceLabel.setStyleSheet(u".QLabel {border: 1px solid rgba(177,147,242,255); color: rgba(119,244,136,255)}")
        self.grpPresenceLabel.setAlignment(Qt.AlignCenter)
        self.grpPresenceLabel.setWordWrap(True)
        self.grpPresenceLabel.setMargin(5)

        self.grpBigVL.addWidget(self.grpPresenceLabel)


        self.grpGridContainer.addWidget(self.grpFrame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page5Grp)
        self.page6Dungeon = QWidget()
        self.page6Dungeon.setObjectName(u"page6Dungeon")
        self.gridLayoutWidget_9 = QWidget(self.page6Dungeon)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(-1, -1, 861, 441))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.betaLabel = QLabel(self.gridLayoutWidget_9)
        self.betaLabel.setObjectName(u"betaLabel")
        font5 = QFont()
        font5.setFamilies([u"Bahnschrift SemiBold"])
        font5.setPointSize(24)
        font5.setBold(True)
        self.betaLabel.setFont(font5)
        self.betaLabel.setStyleSheet(u".QLabel {color: rgba(119,244,136,255)}")
        self.betaLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.betaLabel, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page6Dungeon)
        self.page7World = QWidget()
        self.page7World.setObjectName(u"page7World")
        self.gridLayoutWidget_8 = QWidget(self.page7World)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(0, 0, 861, 441))
        self.worldGridContainer = QGridLayout(self.gridLayoutWidget_8)
        self.worldGridContainer.setObjectName(u"worldGridContainer")
        self.worldGridContainer.setContentsMargins(0, 0, 0, 0)
        self.worldFrame = QFrame(self.gridLayoutWidget_8)
        self.worldFrame.setObjectName(u"worldFrame")
        self.worldFrame.setFrameShape(QFrame.StyledPanel)
        self.worldFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_10 = QWidget(self.worldFrame)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(19, 19, 441, 401))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.worldNameTxt = QLabel(self.verticalLayoutWidget_10)
        self.worldNameTxt.setObjectName(u"worldNameTxt")
        self.worldNameTxt.setFont(font1)
        self.worldNameTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.worldNameTxt.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.worldNameTxt)

        self.worldNameEdit = QLineEdit(self.verticalLayoutWidget_10)
        self.worldNameEdit.setObjectName(u"worldNameEdit")
        self.worldNameEdit.setMaxLength(25)

        self.verticalLayout_2.addWidget(self.worldNameEdit)

        self.worldTimeTxt = QLabel(self.verticalLayoutWidget_10)
        self.worldTimeTxt.setObjectName(u"worldTimeTxt")
        self.worldTimeTxt.setFont(font1)
        self.worldTimeTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.worldTimeTxt.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.worldTimeTxt)

        self.worldTimeEdit = QLineEdit(self.verticalLayoutWidget_10)
        self.worldTimeEdit.setObjectName(u"worldTimeEdit")
        self.worldTimeEdit.setMaxLength(25)

        self.verticalLayout_2.addWidget(self.worldTimeEdit)

        self.worldClimateTxt = QLabel(self.verticalLayoutWidget_10)
        self.worldClimateTxt.setObjectName(u"worldClimateTxt")
        self.worldClimateTxt.setFont(font1)
        self.worldClimateTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.worldClimateTxt.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.worldClimateTxt)

        self.worldClimateEdit = QLineEdit(self.verticalLayoutWidget_10)
        self.worldClimateEdit.setObjectName(u"worldClimateEdit")
        self.worldClimateEdit.setMaxLength(50)

        self.verticalLayout_2.addWidget(self.worldClimateEdit)

        self.worldGeoTxt = QLabel(self.verticalLayoutWidget_10)
        self.worldGeoTxt.setObjectName(u"worldGeoTxt")
        self.worldGeoTxt.setFont(font1)
        self.worldGeoTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.worldGeoTxt.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.worldGeoTxt)

        self.worldGeoEdit = QLineEdit(self.verticalLayoutWidget_10)
        self.worldGeoEdit.setObjectName(u"worldGeoEdit")
        self.worldGeoEdit.setMaxLength(50)

        self.verticalLayout_2.addWidget(self.worldGeoEdit)

        self.worldStabilityTxt = QLabel(self.verticalLayoutWidget_10)
        self.worldStabilityTxt.setObjectName(u"worldStabilityTxt")
        self.worldStabilityTxt.setFont(font1)
        self.worldStabilityTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.worldStabilityTxt.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.worldStabilityTxt)

        self.worldStabilityEdit = QLineEdit(self.verticalLayoutWidget_10)
        self.worldStabilityEdit.setObjectName(u"worldStabilityEdit")
        self.worldStabilityEdit.setMaxLength(100)

        self.verticalLayout_2.addWidget(self.worldStabilityEdit)

        self.worldMagicTxt = QLabel(self.verticalLayoutWidget_10)
        self.worldMagicTxt.setObjectName(u"worldMagicTxt")
        self.worldMagicTxt.setFont(font1)
        self.worldMagicTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.worldMagicTxt.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.worldMagicTxt)

        self.worldMagicEdit = QLineEdit(self.verticalLayoutWidget_10)
        self.worldMagicEdit.setObjectName(u"worldMagicEdit")
        self.worldMagicEdit.setMaxLength(100)

        self.verticalLayout_2.addWidget(self.worldMagicEdit)

        self.worldThemeTxt = QLabel(self.verticalLayoutWidget_10)
        self.worldThemeTxt.setObjectName(u"worldThemeTxt")
        self.worldThemeTxt.setFont(font1)
        self.worldThemeTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.worldThemeTxt.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.verticalLayout_2.addWidget(self.worldThemeTxt)

        self.worldThemeEdit = QLineEdit(self.verticalLayoutWidget_10)
        self.worldThemeEdit.setObjectName(u"worldThemeEdit")
        self.worldThemeEdit.setMaxLength(100)

        self.verticalLayout_2.addWidget(self.worldThemeEdit)

        self.worldDesEdit = QTextEdit(self.worldFrame)
        self.worldDesEdit.setObjectName(u"worldDesEdit")
        self.worldDesEdit.setGeometry(QRect(493, 39, 341, 381))
        font6 = QFont()
        font6.setFamilies([u"Bahnschrift Light"])
        font6.setPointSize(12)
        self.worldDesEdit.setFont(font6)
        self.worldDesTxt = QLabel(self.worldFrame)
        self.worldDesTxt.setObjectName(u"worldDesTxt")
        self.worldDesTxt.setGeometry(QRect(498, 17, 331, 20))
        self.worldDesTxt.setFont(font1)
        self.worldDesTxt.setStyleSheet(u".QLabel {color: rgba(119,244,136,255);}")
        self.worldDesTxt.setAlignment(Qt.AlignCenter)

        self.worldGridContainer.addWidget(self.worldFrame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page7World)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 50, 100, 501))
        self.sideBarVL = QVBoxLayout(self.verticalLayoutWidget)
        self.sideBarVL.setSpacing(0)
        self.sideBarVL.setObjectName(u"sideBarVL")
        self.sideBarVL.setContentsMargins(0, 0, 0, 0)
        self.sideBarVLFrame = QFrame(self.verticalLayoutWidget)
        self.sideBarVLFrame.setObjectName(u"sideBarVLFrame")
        self.sideBarVLFrame.setStyleSheet(u".QFrame {background: rgba(30, 30, 38, 255)}")
        self.sideBarVLFrame.setFrameShape(QFrame.StyledPanel)
        self.sideBarVLFrame.setFrameShadow(QFrame.Raised)
        self.groupBtn = QPushButton(self.sideBarVLFrame)
        self.groupBtn.setObjectName(u"groupBtn")
        self.groupBtn.setGeometry(QRect(10, 134, 80, 22))
        font7 = QFont()
        font7.setFamilies([u"Bahnschrift"])
        self.groupBtn.setFont(font7)
        self.groupBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.encounterBtn = QPushButton(self.sideBarVLFrame)
        self.encounterBtn.setObjectName(u"encounterBtn")
        self.encounterBtn.setGeometry(QRect(10, 102, 80, 22))
        self.encounterBtn.setFont(font7)
        self.encounterBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.npcBtn = QPushButton(self.sideBarVLFrame)
        self.npcBtn.setObjectName(u"npcBtn")
        self.npcBtn.setGeometry(QRect(10, 6, 80, 22))
        self.npcBtn.setFont(font7)
        self.npcBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.helpBtn = QToolButton(self.sideBarVLFrame)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setGeometry(QRect(37, 439, 26, 26))
        font8 = QFont()
        font8.setFamilies([u"Bahnschrift SemiBold"])
        font8.setPointSize(13)
        font8.setBold(True)
        self.helpBtn.setFont(font8)
        self.helpBtn.setStyleSheet(u".QToolButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.buildingBtn = QPushButton(self.sideBarVLFrame)
        self.buildingBtn.setObjectName(u"buildingBtn")
        self.buildingBtn.setGeometry(QRect(10, 38, 80, 22))
        self.buildingBtn.setFont(font7)
        self.buildingBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.dungeonBtn = QPushButton(self.sideBarVLFrame)
        self.dungeonBtn.setObjectName(u"dungeonBtn")
        self.dungeonBtn.setGeometry(QRect(10, 166, 80, 22))
        self.dungeonBtn.setFont(font7)
        self.dungeonBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.townBtn = QPushButton(self.sideBarVLFrame)
        self.townBtn.setObjectName(u"townBtn")
        self.townBtn.setGeometry(QRect(10, 70, 80, 22))
        self.townBtn.setFont(font7)
        self.townBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.warningBtn = QToolButton(self.sideBarVLFrame)
        self.warningBtn.setObjectName(u"warningBtn")
        self.warningBtn.setGeometry(QRect(37, 403, 26, 26))
        self.warningBtn.setStyleSheet(u".QToolButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.worldBtn = QPushButton(self.sideBarVLFrame)
        self.worldBtn.setObjectName(u"worldBtn")
        self.worldBtn.setGeometry(QRect(10, 200, 80, 22))
        self.worldBtn.setFont(font7)
        self.worldBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        self.sideBarVL.addWidget(self.sideBarVLFrame)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 490, 861, 51))
        self.bottomBarHL = QHBoxLayout(self.layoutWidget)
        self.bottomBarHL.setObjectName(u"bottomBarHL")
        self.bottomBarHL.setContentsMargins(10, 0, 10, 0)
        self.leftBottomBarHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomBarHL.addItem(self.leftBottomBarHLSpacer)

        self.dropDown = QComboBox(self.layoutWidget)
        self.dropDown.setObjectName(u"dropDown")
        self.dropDown.setFont(font7)
        self.dropDown.setStyleSheet(u".QComboBox {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        self.bottomBarHL.addWidget(self.dropDown)

        self.middleBottomBarHLSpacer_2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.bottomBarHL.addItem(self.middleBottomBarHLSpacer_2)

        self.generateBtn = QPushButton(self.layoutWidget)
        self.generateBtn.setObjectName(u"generateBtn")
        self.generateBtn.setFont(font7)
        self.generateBtn.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        self.bottomBarHL.addWidget(self.generateBtn)

        self.middleBottomBarHLSpacer = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.bottomBarHL.addItem(self.middleBottomBarHLSpacer)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font7)
        self.pushButton.setStyleSheet(u".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        self.bottomBarHL.addWidget(self.pushButton)

        self.rightBottomBarHLSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomBarHL.addItem(self.rightBottomBarHLSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.world.load()

        # Start at NPC
        self.stackedWidget.setCurrentIndex(0)

        # Slot Connects
        self.generateBtn.clicked.connect(self.generate)
        self.pushButton.clicked.connect(self.save)
        self.npcBtn.clicked.connect(self.npcClicked)
        self.buildingBtn.clicked.connect(self.bldgClicked)
        self.townBtn.clicked.connect(self.twnClicked)
        self.encounterBtn.clicked.connect(self.encClicked)
        self.groupBtn.clicked.connect(self.grpClicked)
        self.dungeonBtn.clicked.connect(self.dungeonClicked)
        self.worldBtn.clicked.connect(self.worldClicked)
        self.encCRSlider.valueChanged.connect(self.updateCR)
        self.encNumCreatures.valueChanged.connect(self.updateNum)
        self.helpBtn.pressed.connect(self.helpMessage)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    # Slot Functions
    def npcClicked(self):
        self.stackedWidget.setCurrentIndex(0)

        # Reset the other labels to the original purple value
        self.buildingBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.townBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.encounterBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.groupBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.groupBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.dungeonBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.worldBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        # Set the label to a dark purple
        self.npcBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgb(139, 61, 209)}")

    def bldgClicked(self):
        self.stackedWidget.setCurrentIndex(1)

        # Reset the other labels to the original purple value
        self.npcBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.townBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.encounterBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.groupBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.dungeonBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.worldBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        # Set the label to a dark purple
        self.buildingBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgb(139, 61, 209)}")

    def twnClicked(self):
        self.stackedWidget.setCurrentIndex(2)

        # Reset the other labels to the original purple value
        self.buildingBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.npcBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.encounterBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.groupBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.dungeonBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.worldBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        # Set the label to a dark purple
        self.townBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgb(139, 61, 209)}")

    def encClicked(self):
        self.stackedWidget.setCurrentIndex(3)

        # Reset the other labels to the original purple value
        self.buildingBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.townBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.npcBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.groupBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.dungeonBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.worldBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        # Set the label to a dark purple
        self.encounterBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgb(139, 61, 209)}")

    def grpClicked(self):
        self.stackedWidget.setCurrentIndex(4)

        # Reset the other labels to the original purple value
        self.buildingBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.townBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.encounterBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.npcBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.dungeonBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.worldBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        # Set the label to a dark purple
        self.groupBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgb(139, 61, 209)}")

    def dungeonClicked(self):
        self.stackedWidget.setCurrentIndex(5)

        # Reset the other labels to the original purple value
        self.buildingBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.townBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.encounterBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.groupBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.npcBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.worldBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        # Set the label to a dark purple
        self.dungeonBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgb(139, 61, 209)}")

    def worldClicked(self):
        self.stackedWidget.setCurrentIndex(6)

        # Reset the other labels to the original purple value
        self.buildingBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.townBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.encounterBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.groupBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.dungeonBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")
        self.npcBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgba(177,147,242,255)}")

        # Set the label to a dark purple
        self.worldBtn.setStyleSheet(".QPushButton {color: rgba(40,42,53,255); background: rgb(139, 61, 209)}")

    def helpMessage(self):
        # Create a QMessageBox
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle("Information")
        msgBox.setText("For more information, visit the project site at https://www.projectwildspace.tech, or submit an issue to the github repository.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        
        # Connect the button press to close the QMessageBox
        msgBox.buttonClicked.connect(msgBox.close)
        
        # Show the QMessageBox
        msgBox.exec()

    def generate(self):

        if os.path.getsize("api.txt") == 0:
            # Create a QMessageBox
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Warning")
            msgBox.setText("You do not have a valid API Key in api.txt. Please set one to use Project Wildspace. Be sure to restart the program after it is updated")
            msgBox.setStandardButtons(QMessageBox.Ok)
            
            # Connect the button press to close the QMessageBox
            msgBox.buttonClicked.connect(msgBox.close)
            
            # Show the QMessageBox
            msgBox.exec()
            
            self.warningBtn.setStyleSheet(".QToolButton {background: rgb(255,0,0); }")
            self.warningBtn.set
    
        index = self.stackedWidget.currentIndex()
        worldIndex = self.dropDown.currentIndex()
        if index == 0:
            self.engine.genNPC()
        elif index == 1:
            self.engine.genBLDG()
        elif index == 2:
            self.engine.genTWN()
        elif index == 3:
            self.engine.genENC()
        elif index == 4:
            self.engine.genGRP()
        self.world.load()
        self.dropDown.setCurrentIndex(worldIndex)

    def save(self):
        index = self.stackedWidget.currentIndex()
        worldIndex = self.dropDown.currentIndex()
        if index == 0:
            self.engine.saveNPC()
        elif index == 1:
            self.engine.saveBLDG()
        elif index == 2:
            self.engine.saveTWN()
        elif index == 3:
            self.engine.saveENC()
        elif index == 4:
            self.engine.saveGRP()
        elif index == 6:
            self.world.save()
        self.world.load()
        self.dropDown.setCurrentIndex(worldIndex)

    def updateCR(self):
        slider_value = self.encCRSlider.value()
        self.label_2.setText(f"Challenge Rating: {slider_value}")

    def updateNum(self):
        slider_value = self.encNumCreatures.value()
        self.label_3.setText(f"Number of Creatures: {slider_value}")
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Project Wildspace 0.0.1", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"Project Wildspace", None))
        self.label.setText("")
        self.npcFashionTxt.setText(QCoreApplication.translate("MainWindow", u"Fashion", None))
        self.npcFashionLabel.setText("")
        self.npcQuirksTxt.setText(QCoreApplication.translate("MainWindow", u"Quirks", None))
        self.npcQuirksLabel.setText("")
        self.npcGoalsTxt.setText(QCoreApplication.translate("MainWindow", u"Goals", None))
        self.npcGoalsLabel.setText("")
        self.npcBackgroundTxt.setText(QCoreApplication.translate("MainWindow", u"Background", None))
        self.npcBackgroundLabel.setText("")
        self.npcFirstNameTxt.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.npcLastNameTxt.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.npcAlignmentTxt.setText(QCoreApplication.translate("MainWindow", u"Alignment", None))
        self.npcFirstNameLabel.setText("")
        self.npcAlignmentLabel.setText("")
        self.npcClassTxt.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.npcGenderTxt.setText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.npcLastNameLabel.setText("")
        self.npcSubclassTxt.setText(QCoreApplication.translate("MainWindow", u"Subclass", None))
        self.npcSubclassLabel.setText("")
        self.genderLabel.setText("")
        self.npcClassLabel.setText("")
        self.npcHeightTxt.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.npcHeightLabel.setText("")
        self.npcRaceTxt.setText(QCoreApplication.translate("MainWindow", u"Race", None))
        self.npcBuildLabel.setText("")
        self.npcRraceLabel.setText("")
        self.npcEyesTxt.setText(QCoreApplication.translate("MainWindow", u"Eyes", None))
        self.npcAgeTxt.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.npcBuildTxt.setText(QCoreApplication.translate("MainWindow", u"Build", None))
        self.npcAgeLabel.setText("")
        self.npcHairTxt.setText(QCoreApplication.translate("MainWindow", u"Hair", None))
        self.npcEyesLabel.setText("")
        self.npcHairLabel.setText("")
        self.bldgDesTxt.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.bldgDesLabel.setText("")
        self.bldgVendorTxt.setText(QCoreApplication.translate("MainWindow", u"Vendor", None))
        self.bldgVendorLabel.setText("")
        self.bldgGoodsTxt.setText(QCoreApplication.translate("MainWindow", u"Goods", None))
        self.bldgGoodsLabel.setText("")
        self.bldgNameTxT.setText(QCoreApplication.translate("MainWindow", u"Building Name", None))
        self.bldgNameLabel.setText("")
        self.bldgTypeTxt.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.bldgTypeLabel.setText("")
        self.bldgSizeTxt.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.bldgSizeLabel.setText("")
        self.bldgArcTxt.setText(QCoreApplication.translate("MainWindow", u"Architecture", None))
        self.bldgArcLabel.setText("")
        self.bldgAmbTxt.setText(QCoreApplication.translate("MainWindow", u"Ambience", None))
        self.bldgAmbLabel.setText("")
        self.bldgTrafficTxt.setText(QCoreApplication.translate("MainWindow", u"Traffic", None))
        self.bldgTrafficLabel.setText("")
        self.twnNameTxt.setText(QCoreApplication.translate("MainWindow", u"Town Name", None))
        self.twnNameLabel.setText("")
        self.twnPopTxt.setText(QCoreApplication.translate("MainWindow", u"Population", None))
        self.twnPopLabel.setText("")
        self.twnSprawlTxt.setText(QCoreApplication.translate("MainWindow", u"Sprawl", None))
        self.twnSprawlLabel.setText("")
        self.twnArcTxt.setText(QCoreApplication.translate("MainWindow", u"Architecture", None))
        self.twnArcLabel.setText("")
        self.twnIndTxt.setText(QCoreApplication.translate("MainWindow", u"Industries", None))
        self.twnIndLabel.setText("")
        self.twnClimTxt.setText(QCoreApplication.translate("MainWindow", u"Climate", None))
        self.twnClimLabel.setText("")
        self.twnGovTypeTxt.setText(QCoreApplication.translate("MainWindow", u"Governing Type", None))
        self.twnGovTypeLabel.setText("")
        self.twnLoreTxt.setText(QCoreApplication.translate("MainWindow", u"Lore", None))
        self.twnLoreLabel.setText("")
        self.twnQuestsTxt.setText(QCoreApplication.translate("MainWindow", u"Quests", None))
        self.twnQuestLabel.setText("")
        self.encNameTxt.setText(QCoreApplication.translate("MainWindow", u"Encounter Name", None))
        self.encNameLabel.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Challenge Rating", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of Creatures", None))
        self.encCreaturesTxt.setText(QCoreApplication.translate("MainWindow", u"Creatures", None))
        self.encCreaturesLabel.setText("")
        self.encDesTxt.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.encDesLabel.setText("")
        self.grpNameTxt.setText(QCoreApplication.translate("MainWindow", u"Group Name", None))
        self.grpNameLabel.setText("")
        self.grpPopTxt.setText(QCoreApplication.translate("MainWindow", u"Population", None))
        self.grpPopTxt_2.setText("")
        self.grpMoralityTxt.setText(QCoreApplication.translate("MainWindow", u"Morality", None))
        self.grpMoralityLabel.setText("")
        self.grpDevotionTxt.setText(QCoreApplication.translate("MainWindow", u"Devotion", None))
        self.grpDevotionTxt_2.setText("")
        self.grpCauseTxt.setText(QCoreApplication.translate("MainWindow", u"Cause", None))
        self.grpCauseLabel.setText("")
        self.grpTraitsTxt.setText(QCoreApplication.translate("MainWindow", u"Distinctive Traits", None))
        self.grpTraitsLabel.setText("")
        self.grpPresenceTxt.setText(QCoreApplication.translate("MainWindow", u"Presence", None))
        self.grpPresenceLabel.setText("")
        self.betaLabel.setText(QCoreApplication.translate("MainWindow", u"DUNGEON GENERATION BETA COMING SOON...", None))
        self.worldNameTxt.setText(QCoreApplication.translate("MainWindow", u"World Name", None))
        self.worldTimeTxt.setText(QCoreApplication.translate("MainWindow", u"Time Period", None))
        self.worldClimateTxt.setText(QCoreApplication.translate("MainWindow", u"Climate", None))
        self.worldGeoTxt.setText(QCoreApplication.translate("MainWindow", u"Geography", None))
        self.worldStabilityTxt.setText(QCoreApplication.translate("MainWindow", u"Stability", None))
        self.worldMagicTxt.setText(QCoreApplication.translate("MainWindow", u"Presence of Magic", None))
        self.worldThemeTxt.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.worldDesTxt.setText(QCoreApplication.translate("MainWindow", u"World Description", None))
        self.groupBtn.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.encounterBtn.setText(QCoreApplication.translate("MainWindow", u"Encounter", None))
        self.npcBtn.setText(QCoreApplication.translate("MainWindow", u"NPC", None))
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.buildingBtn.setText(QCoreApplication.translate("MainWindow", u"Building", None))
        self.dungeonBtn.setText(QCoreApplication.translate("MainWindow", u"Dungeon", None))
        self.townBtn.setText(QCoreApplication.translate("MainWindow", u"Town", None))
        self.warningBtn.setText("")
        self.worldBtn.setText(QCoreApplication.translate("MainWindow", u"World", None))
        self.generateBtn.setText(QCoreApplication.translate("MainWindow", u"Generate!", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

