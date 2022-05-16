################################################################################
## Form generated from reading UI file 'ui_form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QTabWidget,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1239, 580)
        self.tabWidget = QTabWidget(Dialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(190, 50, 931, 461))
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget = QWidget(self.tab_2)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 90, 681, 61))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_SQL_Base_Name = QLabel(self.gridLayoutWidget)
        self.label_SQL_Base_Name.setObjectName(u"label_SQL_Base_Name")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_SQL_Base_Name.setFont(font)
        self.label_SQL_Base_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_SQL_Base_Name.setMargin(10)

        self.gridLayout.addWidget(self.label_SQL_Base_Name, 1, 0, 1, 1)

        self.label_Text_SQL_Base = QLabel(self.gridLayoutWidget)
        self.label_Text_SQL_Base.setObjectName(u"label_Text_SQL_Base")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_Text_SQL_Base.setFont(font1)
        self.label_Text_SQL_Base.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.label_Text_SQL_Base.setMargin(10)

        self.gridLayout.addWidget(self.label_Text_SQL_Base, 1, 1, 1, 1)

        self.btn_Connect_SQL_DB = QPushButton(self.gridLayoutWidget)
        self.btn_Connect_SQL_DB.setObjectName(u"btn_Connect_SQL_DB")

        self.gridLayout.addWidget(self.btn_Connect_SQL_DB, 1, 4, 1, 1)

        self.label_Text_SQL_Server_Name = QLabel(self.gridLayoutWidget)
        self.label_Text_SQL_Server_Name.setObjectName(u"label_Text_SQL_Server_Name")
        self.label_Text_SQL_Server_Name.setFont(font1)
        self.label_Text_SQL_Server_Name.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.label_Text_SQL_Server_Name.setMargin(10)

        self.gridLayout.addWidget(self.label_Text_SQL_Server_Name, 1, 3, 1, 1)

        self.label_SQL_Base_Name_2 = QLabel(self.gridLayoutWidget)
        self.label_SQL_Base_Name_2.setObjectName(u"label_SQL_Base_Name_2")
        self.label_SQL_Base_Name_2.setFont(font)
        self.label_SQL_Base_Name_2.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_SQL_Base_Name_2.setMargin(10)

        self.gridLayout.addWidget(self.label_SQL_Base_Name_2, 1, 2, 1, 1)

        self.comboBox = QComboBox(self.tab_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 220, 301, 31))
        self.comboBox_2 = QComboBox(self.tab_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(570, 200, 73, 22))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_Space_Name = QLabel(self.tab)
        self.label_Space_Name.setObjectName(u"label_Space_Name")
        self.label_Space_Name.setGeometry(QRect(10, 20, 150, 50))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_Space_Name.setFont(font2)
        self.label_Space_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_Space_Name.setMargin(10)
        self.label_Text_Space = QLabel(self.tab)
        self.label_Text_Space.setObjectName(u"label_Text_Space")
        self.label_Text_Space.setGeometry(QRect(140, 20, 300, 50))
        self.label_Text_Space.setFont(font1)
        self.label_Text_Space.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.label_Text_Space.setMargin(10)
        self.label_Table_Name = QLabel(self.tab)
        self.label_Table_Name.setObjectName(u"label_Table_Name")
        self.label_Table_Name.setGeometry(QRect(10, 90, 150, 50))
        self.label_Table_Name.setFont(font)
        self.label_Table_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_Table_Name.setMargin(10)
        self.label_Text_Table_Name = QLabel(self.tab)
        self.label_Text_Table_Name.setObjectName(u"label_Text_Table_Name")
        self.label_Text_Table_Name.setGeometry(QRect(180, 80, 300, 50))
        self.label_Text_Table_Name.setFont(font1)
        self.label_Text_Table_Name.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.label_Text_Table_Name.setMargin(10)
        self.label_Year = QLabel(self.tab)
        self.label_Year.setObjectName(u"label_Year")
        self.label_Year.setGeometry(QRect(50, 170, 151, 41))
        self.label_Year.setFont(font2)
        self.label_Year.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_Year.setMargin(10)
        self.label_Text_Year = QLabel(self.tab)
        self.label_Text_Year.setObjectName(u"label_Text_Year")
        self.label_Text_Year.setGeometry(QRect(230, 160, 100, 50))
        self.label_Text_Year.setFont(font1)
        self.label_Text_Year.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.label_Text_Year.setMargin(10)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437 \u0417\u0430\u043f\u0430\u0441\u0430", None))
        self.label_SQL_Base_Name.setText(QCoreApplication.translate("Dialog", u"SQL DB", None))
        self.label_Text_SQL_Base.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.btn_Connect_SQL_DB.setText(QCoreApplication.translate("Dialog", u"Connect", None))
        self.label_Text_SQL_Server_Name.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_SQL_Base_Name_2.setText(QCoreApplication.translate("Dialog", u"Server Name", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"12", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"23", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dialog", u"Tab 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Dialog", u"Page", None))
        self.label_Space_Name.setText(QCoreApplication.translate("Dialog", u"\u0412\u0418\u0414 \u0412\u0411\u0420", None))
        self.label_Text_Space.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_Table_Name.setText(QCoreApplication.translate("Dialog", u"Table Name", None))
        self.label_Text_Table_Name.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_Year.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0434", None))
        self.label_Text_Year.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dialog", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Dialog", u"Page", None))
    # retranslateUi

