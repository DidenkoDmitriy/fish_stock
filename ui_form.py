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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(917, 526)
        self.label_Text_SQL_Base = QLabel(Dialog)
        self.label_Text_SQL_Base.setObjectName(u"label_Text_SQL_Base")
        self.label_Text_SQL_Base.setGeometry(QRect(170, 10, 300, 50))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_Text_SQL_Base.setFont(font)
        self.label_Text_SQL_Base.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.label_Text_SQL_Base.setMargin(10)
        self.label_Text_Table_Name = QLabel(Dialog)
        self.label_Text_Table_Name.setObjectName(u"label_Text_Table_Name")
        self.label_Text_Table_Name.setGeometry(QRect(170, 70, 300, 50))
        self.label_Text_Table_Name.setFont(font)
        self.label_Text_Table_Name.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.label_Text_Table_Name.setMargin(10)
        self.label_SQL_Base_Name = QLabel(Dialog)
        self.label_SQL_Base_Name.setObjectName(u"label_SQL_Base_Name")
        self.label_SQL_Base_Name.setGeometry(QRect(10, 10, 150, 50))
        self.label_SQL_Base_Name.setFont(font)
        self.label_SQL_Base_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_SQL_Base_Name.setMargin(10)
        self.label_Table_Name = QLabel(Dialog)
        self.label_Table_Name.setObjectName(u"label_Table_Name")
        self.label_Table_Name.setGeometry(QRect(10, 70, 150, 50))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_Table_Name.setFont(font1)
        self.label_Table_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_Table_Name.setMargin(10)
        self.label_Space_Name = QLabel(Dialog)
        self.label_Space_Name.setObjectName(u"label_Space_Name")
        self.label_Space_Name.setGeometry(QRect(10, 130, 150, 50))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_Space_Name.setFont(font2)
        self.label_Space_Name.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_Space_Name.setMargin(10)
        self.label_Text_Space = QLabel(Dialog)
        self.label_Text_Space.setObjectName(u"label_Text_Space")
        self.label_Text_Space.setGeometry(QRect(170, 130, 300, 50))
        self.label_Text_Space.setFont(font)
        self.label_Text_Space.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.label_Text_Space.setMargin(10)
        self.label_Year = QLabel(Dialog)
        self.label_Year.setObjectName(u"label_Year")
        self.label_Year.setGeometry(QRect(10, 190, 151, 41))
        self.label_Year.setFont(font2)
        self.label_Year.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.label_Year.setMargin(10)
        self.label_Text_Year = QLabel(Dialog)
        self.label_Text_Year.setObjectName(u"label_Text_Year")
        self.label_Text_Year.setGeometry(QRect(520, 60, 100, 50))
        self.label_Text_Year.setFont(font)
        self.label_Text_Year.setStyleSheet(u"background-color: rgb(247, 247, 247);")
        self.label_Text_Year.setMargin(10)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(520, 10, 121, 41))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 190, 301, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437 \u0417\u0430\u043f\u0430\u0441\u0430", None))
        self.label_Text_SQL_Base.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_Text_Table_Name.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_SQL_Base_Name.setText(QCoreApplication.translate("Dialog", u"SQL Base", None))
        self.label_Table_Name.setText(QCoreApplication.translate("Dialog", u"Table Name", None))
        self.label_Space_Name.setText(QCoreApplication.translate("Dialog", u"\u0412\u0418\u0414 \u0412\u0411\u0420", None))
        self.label_Text_Space.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_Year.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0434", None))
        self.label_Text_Year.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437", None))
    # retranslateUi

