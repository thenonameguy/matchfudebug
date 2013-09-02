# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_matcherofflinedebug.ui'
#
# Created: Mon Sep  2 11:44:31 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MatcherOfflineDebug(object):
    def setupUi(self, MatcherOfflineDebug):
        MatcherOfflineDebug.setObjectName(_fromUtf8("MatcherOfflineDebug"))
        MatcherOfflineDebug.resize(258, 218)
        self.btn_nextID = QtGui.QPushButton(MatcherOfflineDebug)
        self.btn_nextID.setGeometry(QtCore.QRect(170, 190, 87, 27))
        self.btn_nextID.setObjectName(_fromUtf8("btn_nextID"))
        self.btn_prevID = QtGui.QPushButton(MatcherOfflineDebug)
        self.btn_prevID.setGeometry(QtCore.QRect(0, 190, 87, 27))
        self.btn_prevID.setObjectName(_fromUtf8("btn_prevID"))
        self.listWidget = QtGui.QListWidget(MatcherOfflineDebug)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 256, 192))
        self.listWidget.setMaximumSize(QtCore.QSize(256, 16777215))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        self.retranslateUi(MatcherOfflineDebug)
        QtCore.QMetaObject.connectSlotsByName(MatcherOfflineDebug)

    def retranslateUi(self, MatcherOfflineDebug):
        MatcherOfflineDebug.setWindowTitle(QtGui.QApplication.translate("MatcherOfflineDebug", "Matcher Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nextID.setText(QtGui.QApplication.translate("MatcherOfflineDebug", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_prevID.setText(QtGui.QApplication.translate("MatcherOfflineDebug", "Previous", None, QtGui.QApplication.UnicodeUTF8))

