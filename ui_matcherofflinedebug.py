# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_matcherofflinedebug.ui'
#
# Created: Tue Sep  3 14:24:36 2013
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
        MatcherOfflineDebug.resize(250, 248)
        MatcherOfflineDebug.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MatcherOfflineDebug.setWindowOpacity(1.0)
        MatcherOfflineDebug.setAutoFillBackground(False)
        MatcherOfflineDebug.setModal(False)
        self.biglabel = QtGui.QLabel(MatcherOfflineDebug)
        self.biglabel.setGeometry(QtCore.QRect(0, 0, 251, 181))
        self.biglabel.setText(_fromUtf8(""))
        self.biglabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.biglabel.setWordWrap(True)
        self.biglabel.setObjectName(_fromUtf8("biglabel"))
        self.widget = QtGui.QWidget(MatcherOfflineDebug)
        self.widget.setGeometry(QtCore.QRect(0, 220, 251, 29))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inp_jump = QtGui.QLineEdit(self.widget)
        self.inp_jump.setObjectName(_fromUtf8("inp_jump"))
        self.horizontalLayout.addWidget(self.inp_jump)
        self.btn_jump = QtGui.QPushButton(self.widget)
        self.btn_jump.setObjectName(_fromUtf8("btn_jump"))
        self.horizontalLayout.addWidget(self.btn_jump)
        self.splitter = QtGui.QSplitter(MatcherOfflineDebug)
        self.splitter.setGeometry(QtCore.QRect(0, 190, 251, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.btn_prevID = QtGui.QPushButton(self.splitter)
        self.btn_prevID.setObjectName(_fromUtf8("btn_prevID"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName(_fromUtf8("label"))
        self.btn_nextID = QtGui.QPushButton(self.splitter)
        self.btn_nextID.setObjectName(_fromUtf8("btn_nextID"))

        self.retranslateUi(MatcherOfflineDebug)
        QtCore.QMetaObject.connectSlotsByName(MatcherOfflineDebug)

    def retranslateUi(self, MatcherOfflineDebug):
        MatcherOfflineDebug.setWindowTitle(QtGui.QApplication.translate("MatcherOfflineDebug", "Matcher Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_jump.setText(QtGui.QApplication.translate("MatcherOfflineDebug", "Jump to MatchID!", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_prevID.setText(QtGui.QApplication.translate("MatcherOfflineDebug", "Previous", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_nextID.setText(QtGui.QApplication.translate("MatcherOfflineDebug", "Next", None, QtGui.QApplication.UnicodeUTF8))

