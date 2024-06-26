# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cyber3330d/Downloads/es501/es501/profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_profile_screen(object):
    def setupUi(self, profile_screen):
        profile_screen.setObjectName("profile_screen")
        profile_screen.resize(1400, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/assets/compeng_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        profile_screen.setWindowIcon(icon)
        profile_screen.setStyleSheet("background-color: rgb(246, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(profile_screen)
        self.verticalLayout.setContentsMargins(80, 48, 32, 48)
        self.verticalLayout.setSpacing(48)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header_layout = QtWidgets.QVBoxLayout()
        self.header_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.header_layout.setSpacing(0)
        self.header_layout.setObjectName("header_layout")
        self.logo = QtWidgets.QLabel(profile_screen)
        self.logo.setMinimumSize(QtCore.QSize(0, 0))
        self.logo.setStyleSheet("image: url(:/assets/compeng_Logo.png);\n"
"padding:0;\n"
"margin:0;")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.header_layout.addWidget(self.logo)
        self.welcome_text = QtWidgets.QLabel(profile_screen)
        self.welcome_text.setStyleSheet("font-size:32px;\n"
"color:#002060;\n"
"font-weight:700;\n"
"text-align:center;")
        self.welcome_text.setTextFormat(QtCore.Qt.MarkdownText)
        self.welcome_text.setScaledContents(True)
        self.welcome_text.setWordWrap(True)
        self.welcome_text.setObjectName("welcome_text")
        self.header_layout.addWidget(self.welcome_text)
        self.header_layout.setStretch(0, 8)
        self.header_layout.setStretch(1, 2)
        self.verticalLayout.addLayout(self.header_layout)
        self.profile_layout = QtWidgets.QHBoxLayout()
        self.profile_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.profile_layout.setContentsMargins(-1, 0, -1, -1)
        self.profile_layout.setSpacing(48)
        self.profile_layout.setObjectName("profile_layout")
        self.image_layout = QtWidgets.QVBoxLayout()
        self.image_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.image_layout.setSpacing(0)
        self.image_layout.setObjectName("image_layout")
        self.image_h_layout = QtWidgets.QHBoxLayout()
        self.image_h_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.image_h_layout.setSpacing(0)
        self.image_h_layout.setObjectName("image_h_layout")
        self.image = QtWidgets.QLabel(profile_screen)
        self.image.setMinimumSize(QtCore.QSize(300, 300))
        self.image.setStyleSheet("image:url(:/assets/me_1.png);\n"
"margin:0;\n"
"padding:0;\n"
"width:100%;\n"
"height:100%")
        self.image.setLineWidth(1)
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setWordWrap(True)
        self.image.setObjectName("image")
        self.image_h_layout.addWidget(self.image)
        self.image_layout.addLayout(self.image_h_layout)
        self.profile_layout.addLayout(self.image_layout)
        self.info_layout = QtWidgets.QVBoxLayout()
        self.info_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.info_layout.setSpacing(24)
        self.info_layout.setObjectName("info_layout")
        self.about_layout = QtWidgets.QVBoxLayout()
        self.about_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.about_layout.setSpacing(10)
        self.about_layout.setObjectName("about_layout")
        self.about_label = QtWidgets.QLabel(profile_screen)
        self.about_label.setStyleSheet("font-size:16px;\n"
"font-weight:600;\n"
"color:#002060;\n"
"")
        self.about_label.setObjectName("about_label")
        self.about_layout.addWidget(self.about_label, 0, QtCore.Qt.AlignBottom)
        self.about = QtWidgets.QLabel(profile_screen)
        self.about.setStyleSheet("text-align: justified;\n"
"color:#002060;\n"
"")
        self.about.setWordWrap(True)
        self.about.setObjectName("about")
        self.about_layout.addWidget(self.about, 0, QtCore.Qt.AlignTop)
        self.about_layout.setStretch(0, 1)
        self.about_layout.setStretch(1, 1)
        self.info_layout.addLayout(self.about_layout)
        self.position_specialization_layout = QtWidgets.QHBoxLayout()
        self.position_specialization_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.position_specialization_layout.setSpacing(64)
        self.position_specialization_layout.setObjectName("position_specialization_layout")
        self.position_layout = QtWidgets.QVBoxLayout()
        self.position_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.position_layout.setSpacing(10)
        self.position_layout.setObjectName("position_layout")
        self.position_label = QtWidgets.QLabel(profile_screen)
        self.position_label.setStyleSheet("font-size:16px;\n"
"font-weight:600;\n"
"color:#002060;\n"
"")
        self.position_label.setObjectName("position_label")
        self.position_layout.addWidget(self.position_label, 0, QtCore.Qt.AlignBottom)
        self.position = QtWidgets.QLabel(profile_screen)
        self.position.setStyleSheet("text-align: justified;\n"
"color:#002060;\n"
"")
        self.position.setScaledContents(True)
        self.position.setWordWrap(True)
        self.position.setObjectName("position")
        self.position_layout.addWidget(self.position, 0, QtCore.Qt.AlignTop)
        self.position_layout.setStretch(0, 1)
        self.position_layout.setStretch(1, 1)
        self.position_specialization_layout.addLayout(self.position_layout)
        self.specialization_layout = QtWidgets.QVBoxLayout()
        self.specialization_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.specialization_layout.setSpacing(10)
        self.specialization_layout.setObjectName("specialization_layout")
        self.specialization_label = QtWidgets.QLabel(profile_screen)
        self.specialization_label.setStyleSheet("font-size:16px;\n"
"font-weight:600;\n"
"color:#002060;\n"
"")
        self.specialization_label.setObjectName("specialization_label")
        self.specialization_layout.addWidget(self.specialization_label, 0, QtCore.Qt.AlignBottom)
        self.specialization = QtWidgets.QLabel(profile_screen)
        self.specialization.setStyleSheet("text-align: justified;\n"
"color:#002060;\n"
"")
        self.specialization.setWordWrap(True)
        self.specialization.setObjectName("specialization")
        self.specialization_layout.addWidget(self.specialization, 0, QtCore.Qt.AlignTop)
        self.specialization_layout.setStretch(0, 1)
        self.specialization_layout.setStretch(1, 1)
        self.position_specialization_layout.addLayout(self.specialization_layout)
        self.position_specialization_layout.setStretch(0, 1)
        self.position_specialization_layout.setStretch(1, 1)
        self.info_layout.addLayout(self.position_specialization_layout)
        self.contact_layout = QtWidgets.QVBoxLayout()
        self.contact_layout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.contact_layout.setSpacing(10)
        self.contact_layout.setObjectName("contact_layout")
        self.contact_label = QtWidgets.QLabel(profile_screen)
        self.contact_label.setStyleSheet("font-size:16px;\n"
"font-weight:600;\n"
"color:#002060;\n"
"")
        self.contact_label.setObjectName("contact_label")
        self.contact_layout.addWidget(self.contact_label, 0, QtCore.Qt.AlignBottom)
        self.contact = QtWidgets.QLabel(profile_screen)
        self.contact.setStyleSheet("text-align: left;\n"
"color: #0D6EB7;\n"
"")
        self.contact.setWordWrap(True)
        self.contact.setObjectName("contact")
        self.contact_layout.addWidget(self.contact, 0, QtCore.Qt.AlignTop)
        self.contact_layout.setStretch(0, 1)
        self.contact_layout.setStretch(1, 1)
        self.info_layout.addLayout(self.contact_layout)
        self.info_layout.setStretch(0, 1)
        self.info_layout.setStretch(1, 1)
        self.info_layout.setStretch(2, 1)
        self.profile_layout.addLayout(self.info_layout)
        self.profile_layout.setStretch(0, 1)
        self.profile_layout.setStretch(1, 3)
        self.verticalLayout.addLayout(self.profile_layout)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 6)

        self.retranslateUi(profile_screen)
        QtCore.QMetaObject.connectSlotsByName(profile_screen)

    def retranslateUi(self, profile_screen):
        _translate = QtCore.QCoreApplication.translate
        profile_screen.setWindowTitle(_translate("profile_screen", "Recognized Profile"))
        self.welcome_text.setText(_translate("profile_screen", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">WELCOME TO THE DEPARTMENT OF COMPUTER ENGINEERING</span></p></body></html>"))
        self.about_label.setText(_translate("profile_screen", "ABOUT"))
        self.about.setText(_translate("profile_screen", "<html><head/><body><p align=\"justify\">Professor Fauzan Alhassan, B. Eng (Computer Engineering ABU Zaria), </p><p align=\"justify\">MSc Human Computer Interaction and Design (Rochester Institute of Technology, USA), </p><p align=\"justify\">PhD Software Engineering (Carnegie Mellon University, Pittsburgh, PA), FNSE, COREN. </p></body></html>"))
        self.position_label.setText(_translate("profile_screen", "POSITION"))
        self.position.setText(_translate("profile_screen", "<html><head/><body><p align=\"justify\">Professor Department of Computer Engineering,</p><p align=\"justify\"> Ahmadu Bello University Zaria.</p></body></html>"))
        self.specialization_label.setText(_translate("profile_screen", "SPECIALIZATION"))
        self.specialization.setText(_translate("profile_screen", "<html><head/><body><p align=\"justify\">Human Computer Interaction (HCI) </p><p align=\"justify\">and Software Engineering.</p></body></html>"))
        self.contact_label.setText(_translate("profile_screen", "CONTACT"))
        self.contact.setText(_translate("profile_screen", "alhassanfauzan@abu.edu.ng"))
import assets_rc
