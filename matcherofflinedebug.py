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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from matcherofflinedebugdialog import MatcherOfflineDebugDialog


class MatcherOfflineDebug:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.canvas=iface.mapCanvas()

        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/matcherofflinedebug"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/matcherofflinedebug_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = MatcherOfflineDebugDialog()
    def getMatchIds(self):
        matchidIndex=1
        provider=self.find_layer_by_name("prior_statuses").dataProvider()
        provider.select([matchidIndex])
        feat=QgsFeature()
        li=[]
        while provider.nextFeature(feat):
            li.append(feat.attributeMap())
        ids=[]
        for i in range(len(li)):
            ids.append(li[i][matchidIndex].toInt()[0])
        return sorted(set(ids)) 

    def getTimeStamps(self):
        timestampindex=5
        provider=self.find_layer_by_name("prior_statuses").dataProvider()
        provider.select([timestampindex])
        feat=QgsFeature()
        li=[]
        while provider.nextFeature(feat):
            li.append(feat.attributeMap())
        timestamps=[]
        for i in range(len(li)):
            timestamps.append(li[i][timestampindex].toString())
        return sorted(set(timestamps)) 

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/matcherofflinedebug/icon.png"),
            u"Query Matchfu data", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&MatcherOfflineDebug", self.action)
        QObject.connect(self.dlg.ui.btn_nextID,SIGNAL("clicked()"),self.nextID)
        QObject.connect(self.dlg.ui.btn_prevID,SIGNAL("clicked()"),self.prevID)
        QObject.connect(self.dlg.ui.btn_jump,SIGNAL("clicked()"),self.jump)
    
    def jump(self):
        self.addToCurrentID(self.dlg.ui.inp_jump.text().toInt()[0]-self.currentid)

    def nextID(self):
        self.addToCurrentID(1)

    def addToCurrentID(self,change):
        if self.currentid+change<=len(self.matchids) and self.currentid+change>0:
            self.currentid+=change
            print "Current ID:",self.currentid
            self.dlg.ui.label.setText(str(self.currentid)+'/'+str(len(self.matchids)))
            self.showByID()

    def getWantedLayers(self):
        matchid_layer_names=["prior_statuses","prior_teleports","prior_candidates_0","last_nodes_to","last_nodes_from","last_statuses","matched_candidates"]
        self.wanted_layers={}
        self.orig_subsets={}
        self.concat_helper={}
        for name in matchid_layer_names:
            self.wanted_layers[name]=self.find_layer_by_name(name)
            self.orig_subsets[name]=self.wanted_layers[name].subsetString()
            if self.orig_subsets[name]=="":
                self.concat_helper[name]=" "
            else:
                self.concat_helper[name]=" and "

    def showByID(self):
        #TODO: this is where the magic will happen
        for name in self.wanted_layers:
            if name[:5]=="prior":
                self.wanted_layers[name].setSubsetString(self.orig_subsets[name]+self.concat_helper[name]+"matchid < "+str(self.currentid))
            else:
                self.wanted_layers[name].setSubsetString(self.orig_subsets[name]+self.concat_helper[name]+"matchid = "+str(self.currentid))
        self.dlg.ui.label.setText(str(self.currentid)+'/'+str(len(self.matchids)))
        self.dlg.ui.biglabel.setText(str(self.timestamps[self.currentid]))
        self.canvas.refresh()

    def prevID(self):
        self.addToCurrentID(-1)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&MatcherOfflineDebug", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def find_layer_by_name(self,name):
        for layer in self.layers:
            if layer.name()==name:
                return layer
        return "404"

    def run(self):
        # show the dialog
        self.layers=self.canvas.layers()
        self.matchids=self.getMatchIds()
        self.timestamps=self.getTimeStamps()
        self.currentid=self.matchids[0]
        self.getWantedLayers()
        self.showByID()
        self.dlg.ui.label.setText(str(self.currentid)+'/'+str(len(self.matchids)))
        self.dlg.show()
