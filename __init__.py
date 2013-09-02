# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MatcherOfflineDebug
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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "MatcherOfflineDebug"


def description():
    return "Query Matchfu data based on matchid"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Szabó Krisztián"

def email():
    return "thenonameguy24@gmail.com"

def classFactory(iface):
    # load MatcherOfflineDebug class from file MatcherOfflineDebug
    from matcherofflinedebug import MatcherOfflineDebug
    return MatcherOfflineDebug(iface)
