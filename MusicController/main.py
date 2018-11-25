import os
import sys

import math

import RLPy

import PySide2
from PySide2.QtMultimedia import QSound
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QWidget, QAbstractItemView 
from PySide2.QtWidgets import QMenu, QAction, QPushButton
from PySide2.QtWidgets import QTreeWidgetItem, QTreeWidget, QTreeView, QTableWidget, QComboBox
from PySide2.shiboken2 import wrapInstance

class KeyControlButton(QPushButton):
    def __init__(self, text, wav, parent):
        super().__init__(text)
        self.text = text
        self.parent = parent
        self.parent.addWidget(self)
        self.clicked.connect(self.play)
        
        self.hot_key_address = RLPy.RUi.AddHotKey(self.text)
        self.hot_key_action = wrapInstance(int(self.hot_key_address), PySide2.QtWidgets.QAction)
        self.hot_key_action.triggered.connect(self.play)
        
        self.audio_path = os.path.dirname(os.path.abspath(__file__))+"\\wav\\"+ wav+".wav"

        #self.audio_object = RLPy.RAudio.CreateAudioObject()
        #------------- crash -------------#
        #self.audio_object.Load(self.audio_path)
        #---------------------------------#
        #self.selection_list = RLPy.RGlobal.GetAvatars()
        #self.avatar = self.selection_list[0]
        #RLPy.RAudio.LoadAudioToObject(self.avatar, self.audio_object, RLPy.RTime(0), 1000)
        
    def play(self):
        print (self.text)
        QSound.play(self.audio_path)
        
class MusicController(QWidget):
    global rl_py_timer
    global timer_callback

    def __init__(self):
        super().__init__()
        
        self.layout = QtWidgets.QHBoxLayout()
        
        self.button_a = KeyControlButton("A", "do", self.layout)
        self.button_s = KeyControlButton("S", "re", self.layout)
        self.button_d = KeyControlButton("D", "mi", self.layout)
        self.button_f = KeyControlButton("F", "fa", self.layout)
        self.button_g = KeyControlButton("G", "so", self.layout)
        
        self.setLayout(self.layout)

def run_script():
    music_control_widget = MusicController()
    music_control_widget.show()
    
    app.exec_()
    
    
    