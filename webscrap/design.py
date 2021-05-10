# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ACSWebScrapper(object):
    def setupUi(self, ACSWebScrapper):
        ACSWebScrapper.setObjectName("ACSWebScrapper")
        ACSWebScrapper.resize(421, 217)
        self.centralwidget = QtWidgets.QWidget(ACSWebScrapper)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.KwLine = QtWidgets.QLineEdit(self.groupBox)
        self.KwLine.setStyleSheet("")
        self.KwLine.setText("")
        self.KwLine.setObjectName("KwLine")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.KwLine)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.NumEdit = QtWidgets.QComboBox(self.groupBox)
        self.NumEdit.setObjectName("NumEdit")
        self.NumEdit.addItem("")
        self.NumEdit.addItem("")
        self.NumEdit.addItem("")
        self.NumEdit.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.NumEdit)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.EarlDateLine = QtWidgets.QLineEdit(self.groupBox_2)
        self.EarlDateLine.setObjectName("EarlDateLine")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.EarlDateLine)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.LateDateLine = QtWidgets.QLineEdit(self.groupBox_2)
        self.LateDateLine.setObjectName("LateDateLine")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.LateDateLine)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        ACSWebScrapper.setCentralWidget(self.centralwidget)

        self.retranslateUi(ACSWebScrapper)
        QtCore.QMetaObject.connectSlotsByName(ACSWebScrapper)

    def retranslateUi(self, ACSWebScrapper):
        _translate = QtCore.QCoreApplication.translate
        ACSWebScrapper.setWindowTitle(_translate("ACSWebScrapper", "ACS Web Scrapper"))
        self.groupBox.setTitle(_translate("ACSWebScrapper", "Obligatory"))
        self.label.setText(_translate("ACSWebScrapper", "Key Words:"))
        self.label_2.setText(_translate("ACSWebScrapper", "Number of articles:"))
        self.NumEdit.setToolTip(_translate("ACSWebScrapper", "<html><head/><body><p>Choose number of articles</p></body></html>"))
        self.NumEdit.setItemText(0, _translate("ACSWebScrapper", "----Choose number of articles----"))
        self.NumEdit.setItemText(1, _translate("ACSWebScrapper", "20"))
        self.NumEdit.setItemText(2, _translate("ACSWebScrapper", "50"))
        self.NumEdit.setItemText(3, _translate("ACSWebScrapper", "100"))
        self.groupBox_2.setTitle(_translate("ACSWebScrapper", "Optional"))
        self.label_3.setText(_translate("ACSWebScrapper", "Earliest article Date:"))
        self.label_4.setText(_translate("ACSWebScrapper", "Latest Article Date:"))
        self.pushButton.setText(_translate("ACSWebScrapper", "Export to Excel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ACSWebScrapper = QtWidgets.QMainWindow()
    ui = Ui_ACSWebScrapper()
    ui.setupUi(ACSWebScrapper)
    ACSWebScrapper.show()
    sys.exit(app.exec_())