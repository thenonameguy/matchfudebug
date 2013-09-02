# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MatcherOfflineDebugDialog
                                 A QGIS plugin
 Query Matchfu data based on matchid
                             -------------------
        begin                : 2013-09-02
        copyright            : (C) 2013 by Szabó Krisztián
        email                : thenonameguy24@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_matcherofflinedebug import Ui_MatcherOfflineDebug
# create the dialog for zoom to point


class MatcherOfflineDebugDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_MatcherOfflineDebug()
        self.ui.setupUi(self)
