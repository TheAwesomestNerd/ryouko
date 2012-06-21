# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(832, 480)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Ryouko", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setStyleSheet(_fromUtf8("QListWidget {\n"
"border: 0;\n"
"}"))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mainLayout = QtGui.QGridLayout(self.centralWidget)
        self.mainLayout.setMargin(0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.mainToolBar = QtGui.QWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainToolBar.sizePolicy().hasHeightForWidth())
        self.mainToolBar.setSizePolicy(sizePolicy)
        self.mainToolBar.setStyleSheet(_fromUtf8("#mainToolBar {\n"
"border-bottom: 1px solid palette(shadow);\n"
"}"))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.mainToolBarContents = QtGui.QGridLayout(self.mainToolBar)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setSpacing(0)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setObjectName(_fromUtf8("mainToolBarContents"))
        self.mainToolBarLayout = QtGui.QHBoxLayout()
        self.mainToolBarLayout.setSpacing(0)
        self.mainToolBarLayout.setContentsMargins(-1, -1, -1, 0)
        self.mainToolBarLayout.setObjectName(_fromUtf8("mainToolBarLayout"))
        self.subToolBar = QtGui.QWidget(self.mainToolBar)
        self.subToolBar.setStyleSheet(_fromUtf8("#subToolBar {\n"
"min-width: 24px;\n"
"}\n"
"\n"
"QListWidget {\n"
"border: 0;\n"
"}\n"
"        \n"
"QToolButton, QPushButton {\n"
"min-width: 24px;\n"
"border: 1px solid transparent;\n"
"padding: 4px;\n"
"border-radius: 4px;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QToolButton:hover, QPushButton:hover {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.subToolBar.setObjectName(_fromUtf8("subToolBar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.subToolBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backButton = QtGui.QPushButton(self.subToolBar)
        self.backButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.backButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Back</b><br>Alt+Left Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setStyleSheet(_fromUtf8(""))
        self.backButton.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        self.nextButton = QtGui.QPushButton(self.subToolBar)
        self.nextButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.nextButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Next</b><br>Alt+Right Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setStyleSheet(_fromUtf8(""))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.stopButton = QtGui.QPushButton(self.subToolBar)
        self.stopButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stopButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Stop</b><br>Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.reloadButton = QtGui.QPushButton(self.subToolBar)
        self.reloadButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.reloadButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Reload</b><br>F5", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.horizontalLayout.addWidget(self.reloadButton)
        self.findButton = QtGui.QPushButton(self.subToolBar)
        self.findButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.findButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Find</b><br>Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.horizontalLayout.addWidget(self.findButton)
        self.urlBar = QtGui.QLineEdit(self.subToolBar)
        self.urlBar.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Location Bar</b><br>Ctrl+L; Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.urlBar.setObjectName(_fromUtf8("urlBar"))
        self.horizontalLayout.addWidget(self.urlBar)
        self.goButton = QtGui.QPushButton(self.subToolBar)
        self.goButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.goButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Go</b><br>Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setStyleSheet(_fromUtf8(""))
        self.goButton.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.horizontalLayout.addWidget(self.goButton)
        self.mainToolBarLayout.addWidget(self.subToolBar)
        self.focusURLBarButton = QtGui.QPushButton(self.mainToolBar)
        self.focusURLBarButton.setStyleSheet(_fromUtf8("max-width: 0;\n"
"min-width: 0;\n"
"width: 0;\n"
"background: transparent;"))
        self.focusURLBarButton.setText(_fromUtf8(""))
        self.focusURLBarButton.setIconSize(QtCore.QSize(0, 0))
        self.focusURLBarButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.focusURLBarButton.setFlat(True)
        self.focusURLBarButton.setObjectName(_fromUtf8("focusURLBarButton"))
        self.mainToolBarLayout.addWidget(self.focusURLBarButton)
        self.searchButton = QtGui.QPushButton(self.mainToolBar)
        self.searchButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.searchButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Search</b><br>Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.mainToolBarLayout.addWidget(self.searchButton)
        self.searchEditButton = QtGui.QToolButton(self.mainToolBar)
        self.searchEditButton.setStyleSheet(_fromUtf8("max-width: 16px;"))
        self.searchEditButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.searchEditButton.setArrowType(QtCore.Qt.DownArrow)
        self.searchEditButton.setObjectName(_fromUtf8("searchEditButton"))
        self.mainToolBarLayout.addWidget(self.searchEditButton)
        self.mainToolBarContents.addLayout(self.mainToolBarLayout, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.mainToolBar, 1, 0, 1, 1)
        self.statusBar = QtGui.QWidget(self.centralWidget)
        self.statusBar.setStyleSheet(_fromUtf8("#statusBar {\n"
"border-top: 1px solid palette(shadow);\n"
"}"))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.statusBarLayout = QtGui.QHBoxLayout(self.statusBar)
        self.statusBarLayout.setSpacing(6)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setObjectName(_fromUtf8("statusBarLayout"))
        self.statusMessage = QtGui.QLineEdit(self.statusBar)
        self.statusMessage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.statusMessage.setStyleSheet(_fromUtf8("QLineEdit {\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"border: 0;\n"
"background: transparent;\n"
"}"))
        self.statusMessage.setText(_fromUtf8(""))
        self.statusMessage.setReadOnly(True)
        self.statusMessage.setObjectName(_fromUtf8("statusMessage"))
        self.statusBarLayout.addWidget(self.statusMessage)
        self.progressBar = QtGui.QProgressBar(self.statusBar)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(_fromUtf8("min-height: 1em;\n"
"max-height: 1em;\n"
"min-width: 200px;\n"
"max-width: 200px;"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.statusBarLayout.addWidget(self.progressBar)
        self.zoomBar = QtGui.QWidget(self.statusBar)
        self.zoomBar.setStyleSheet(_fromUtf8("QToolButton, QPushButton {\n"
"min-width: 16px;\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"padding-left: 4px;\n"
"padding-right: 4px;\n"
"border-radius: 4px;\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.zoomBar.setObjectName(_fromUtf8("zoomBar"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.zoomBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.zoomOutButton = QtGui.QPushButton(self.zoomBar)
        self.zoomOutButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomOutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom Out</b><br>Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setObjectName(_fromUtf8("zoomOutButton"))
        self.horizontalLayout_3.addWidget(self.zoomOutButton)
        self.zoomSlider = QtGui.QSlider(self.zoomBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomSlider.sizePolicy().hasHeightForWidth())
        self.zoomSlider.setSizePolicy(sizePolicy)
        self.zoomSlider.setMinimumSize(QtCore.QSize(128, 0))
        self.zoomSlider.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomSlider.setStyleSheet(_fromUtf8("max-height: 1em;"))
        self.zoomSlider.setMinimum(1)
        self.zoomSlider.setMaximum(12)
        self.zoomSlider.setSliderPosition(4)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setInvertedAppearance(False)
        self.zoomSlider.setInvertedControls(False)
        self.zoomSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.zoomSlider.setTickInterval(1)
        self.zoomSlider.setObjectName(_fromUtf8("zoomSlider"))
        self.horizontalLayout_3.addWidget(self.zoomSlider)
        self.zoomInButton = QtGui.QPushButton(self.zoomBar)
        self.zoomInButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomInButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom In</b><br>Ctrl++; Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setObjectName(_fromUtf8("zoomInButton"))
        self.horizontalLayout_3.addWidget(self.zoomInButton)
        self.zoomLabel = QtGui.QLabel(self.zoomBar)
        self.zoomLabel.setStyleSheet(_fromUtf8("margin-left: 2px;"))
        self.zoomLabel.setText(QtGui.QApplication.translate("MainWindow", "1.00x", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.horizontalLayout_3.addWidget(self.zoomLabel)
        self.statusBarLayout.addWidget(self.zoomBar)
        self.mainLayout.addWidget(self.statusBar, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.backButton, self.nextButton)
        MainWindow.setTabOrder(self.nextButton, self.stopButton)
        MainWindow.setTabOrder(self.stopButton, self.reloadButton)
        MainWindow.setTabOrder(self.reloadButton, self.findButton)
        MainWindow.setTabOrder(self.findButton, self.urlBar)
        MainWindow.setTabOrder(self.urlBar, self.goButton)
        MainWindow.setTabOrder(self.goButton, self.focusURLBarButton)
        MainWindow.setTabOrder(self.focusURLBarButton, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.searchEditButton)
        MainWindow.setTabOrder(self.searchEditButton, self.statusMessage)
        MainWindow.setTabOrder(self.statusMessage, self.zoomOutButton)
        MainWindow.setTabOrder(self.zoomOutButton, self.zoomSlider)
        MainWindow.setTabOrder(self.zoomSlider, self.zoomInButton)

    def retranslateUi(self, MainWindow):
        pass

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/foxhead128/ryouko/ryouko_lib/mainwindow.ui'
#
# Created: Mon Mar 26 21:40:48 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(832, 480)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Ryouko", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setStyleSheet(_fromUtf8("QListWidget {\n"
"border: 0;\n"
"}"))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mainLayout = QtGui.QGridLayout(self.centralWidget)
        self.mainLayout.setMargin(0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.mainToolBar = QtGui.QWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainToolBar.sizePolicy().hasHeightForWidth())
        self.mainToolBar.setSizePolicy(sizePolicy)
        self.mainToolBar.setStyleSheet(_fromUtf8("#mainToolBar {\n"
"border-bottom: 1px solid palette(shadow);\n"
"}"))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.mainToolBarContents = QtGui.QGridLayout(self.mainToolBar)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setSpacing(0)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setObjectName(_fromUtf8("mainToolBarContents"))
        self.mainToolBarLayout = QtGui.QHBoxLayout()
        self.mainToolBarLayout.setSpacing(0)
        self.mainToolBarLayout.setContentsMargins(-1, -1, -1, 0)
        self.mainToolBarLayout.setObjectName(_fromUtf8("mainToolBarLayout"))
        self.subToolBar = QtGui.QWidget(self.mainToolBar)
        self.subToolBar.setStyleSheet(_fromUtf8("#subToolBar {\n"
"min-width: 24px;\n"
"}\n"
"\n"
"QListWidget {\n"
"border: 0;\n"
"}\n"
"        \n"
"QToolButton, QPushButton {\n"
"min-width: 24px;\n"
"border: 1px solid transparent;\n"
"padding: 4px;\n"
"border-radius: 4px;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QToolButton:hover, QPushButton:hover {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.subToolBar.setObjectName(_fromUtf8("subToolBar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.subToolBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backButton = QtGui.QPushButton(self.subToolBar)
        self.backButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.backButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Back</b><br>Alt+Left Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setStyleSheet(_fromUtf8(""))
        self.backButton.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        self.nextButton = QtGui.QPushButton(self.subToolBar)
        self.nextButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.nextButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Next</b><br>Alt+Right Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setStyleSheet(_fromUtf8(""))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.stopButton = QtGui.QPushButton(self.subToolBar)
        self.stopButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stopButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Stop</b><br>Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.reloadButton = QtGui.QPushButton(self.subToolBar)
        self.reloadButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.reloadButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Reload</b><br>F5", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.horizontalLayout.addWidget(self.reloadButton)
        self.findButton = QtGui.QPushButton(self.subToolBar)
        self.findButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.findButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Find</b><br>Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.horizontalLayout.addWidget(self.findButton)
        self.urlBar = QtGui.QLineEdit(self.subToolBar)
        self.urlBar.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Location Bar</b><br>Ctrl+L; Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.urlBar.setObjectName(_fromUtf8("urlBar"))
        self.horizontalLayout.addWidget(self.urlBar)
        self.goButton = QtGui.QPushButton(self.subToolBar)
        self.goButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.goButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Go</b><br>Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setStyleSheet(_fromUtf8(""))
        self.goButton.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.horizontalLayout.addWidget(self.goButton)
        self.mainToolBarLayout.addWidget(self.subToolBar)
        self.focusURLBarButton = QtGui.QPushButton(self.mainToolBar)
        self.focusURLBarButton.setStyleSheet(_fromUtf8("max-width: 0;\n"
"min-width: 0;\n"
"width: 0;\n"
"background: transparent;"))
        self.focusURLBarButton.setText(_fromUtf8(""))
        self.focusURLBarButton.setIconSize(QtCore.QSize(0, 0))
        self.focusURLBarButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.focusURLBarButton.setFlat(True)
        self.focusURLBarButton.setObjectName(_fromUtf8("focusURLBarButton"))
        self.mainToolBarLayout.addWidget(self.focusURLBarButton)
        self.searchButton = QtGui.QPushButton(self.mainToolBar)
        self.searchButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.searchButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Search</b><br>Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.mainToolBarLayout.addWidget(self.searchButton)
        self.searchEditButton = QtGui.QToolButton(self.mainToolBar)
        self.searchEditButton.setStyleSheet(_fromUtf8("QToolButton { max-width: 16px; }"))
        self.searchEditButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.searchEditButton.setArrowType(QtCore.Qt.DownArrow)
        self.searchEditButton.setObjectName(_fromUtf8("searchEditButton"))
        self.mainToolBarLayout.addWidget(self.searchEditButton)
        self.mainToolBarContents.addLayout(self.mainToolBarLayout, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.mainToolBar, 1, 0, 1, 1)
        self.statusBar = QtGui.QWidget(self.centralWidget)
        self.statusBar.setStyleSheet(_fromUtf8("#statusBar {\n"
"border-top: 1px solid palette(shadow);\n"
"}"))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.statusBarLayout = QtGui.QHBoxLayout(self.statusBar)
        self.statusBarLayout.setSpacing(6)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setObjectName(_fromUtf8("statusBarLayout"))
        self.statusMessage = QtGui.QLineEdit(self.statusBar)
        self.statusMessage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.statusMessage.setStyleSheet(_fromUtf8("QLineEdit {\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"border: 0;\n"
"background: transparent;\n"
"}"))
        self.statusMessage.setText(_fromUtf8(""))
        self.statusMessage.setReadOnly(True)
        self.statusMessage.setObjectName(_fromUtf8("statusMessage"))
        self.statusBarLayout.addWidget(self.statusMessage)
        self.progressBar = QtGui.QProgressBar(self.statusBar)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(_fromUtf8("min-height: 1em;\n"
"max-height: 1em;\n"
"min-width: 200px;\n"
"max-width: 200px;"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.statusBarLayout.addWidget(self.progressBar)
        self.zoomBar = QtGui.QWidget(self.statusBar)
        self.zoomBar.setStyleSheet(_fromUtf8("QToolButton, QPushButton {\n"
"min-width: 16px;\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"padding-left: 4px;\n"
"padding-right: 4px;\n"
"border-radius: 4px;\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.zoomBar.setObjectName(_fromUtf8("zoomBar"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.zoomBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.zoomOutButton = QtGui.QPushButton(self.zoomBar)
        self.zoomOutButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomOutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom Out</b><br>Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setObjectName(_fromUtf8("zoomOutButton"))
        self.horizontalLayout_3.addWidget(self.zoomOutButton)
        self.zoomSlider = QtGui.QSlider(self.zoomBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomSlider.sizePolicy().hasHeightForWidth())
        self.zoomSlider.setSizePolicy(sizePolicy)
        self.zoomSlider.setMinimumSize(QtCore.QSize(128, 0))
        self.zoomSlider.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomSlider.setStyleSheet(_fromUtf8("max-height: 1em;"))
        self.zoomSlider.setMinimum(1)
        self.zoomSlider.setMaximum(12)
        self.zoomSlider.setSliderPosition(4)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setInvertedAppearance(False)
        self.zoomSlider.setInvertedControls(False)
        self.zoomSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.zoomSlider.setTickInterval(1)
        self.zoomSlider.setObjectName(_fromUtf8("zoomSlider"))
        self.horizontalLayout_3.addWidget(self.zoomSlider)
        self.zoomInButton = QtGui.QPushButton(self.zoomBar)
        self.zoomInButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomInButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom In</b><br>Ctrl++; Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setObjectName(_fromUtf8("zoomInButton"))
        self.horizontalLayout_3.addWidget(self.zoomInButton)
        self.zoomLabel = QtGui.QLabel(self.zoomBar)
        self.zoomLabel.setStyleSheet(_fromUtf8("margin-left: 2px;"))
        self.zoomLabel.setText(QtGui.QApplication.translate("MainWindow", "1.00x", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.horizontalLayout_3.addWidget(self.zoomLabel)
        self.statusBarLayout.addWidget(self.zoomBar)
        self.mainLayout.addWidget(self.statusBar, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.backButton, self.nextButton)
        MainWindow.setTabOrder(self.nextButton, self.stopButton)
        MainWindow.setTabOrder(self.stopButton, self.reloadButton)
        MainWindow.setTabOrder(self.reloadButton, self.findButton)
        MainWindow.setTabOrder(self.findButton, self.urlBar)
        MainWindow.setTabOrder(self.urlBar, self.goButton)
        MainWindow.setTabOrder(self.goButton, self.focusURLBarButton)
        MainWindow.setTabOrder(self.focusURLBarButton, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.searchEditButton)
        MainWindow.setTabOrder(self.searchEditButton, self.statusMessage)
        MainWindow.setTabOrder(self.statusMessage, self.zoomOutButton)
        MainWindow.setTabOrder(self.zoomOutButton, self.zoomSlider)
        MainWindow.setTabOrder(self.zoomSlider, self.zoomInButton)

    def retranslateUi(self, MainWindow):
        pass

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './mainwindow.ui'
#
# Created: Tue May  1 15:21:45 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(832, 480)
        MainWindow.setStyleSheet(_fromUtf8("QListWidget {\n"
"border: 0;\n"
"}"))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mainLayout = QtGui.QGridLayout(self.centralWidget)
        self.mainLayout.setMargin(0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.mainToolBar = QtGui.QWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainToolBar.sizePolicy().hasHeightForWidth())
        self.mainToolBar.setSizePolicy(sizePolicy)
        self.mainToolBar.setStyleSheet(_fromUtf8("#mainToolBar {\n"
"border-bottom: 1px solid palette(shadow);\n"
"}"))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.mainToolBarContents = QtGui.QGridLayout(self.mainToolBar)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setSpacing(0)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setObjectName(_fromUtf8("mainToolBarContents"))
        self.mainToolBarLayout = QtGui.QHBoxLayout()
        self.mainToolBarLayout.setSpacing(0)
        self.mainToolBarLayout.setContentsMargins(-1, -1, -1, 0)
        self.mainToolBarLayout.setObjectName(_fromUtf8("mainToolBarLayout"))
        self.subToolBar = QtGui.QWidget(self.mainToolBar)
        self.subToolBar.setStyleSheet(_fromUtf8("#subToolBar {\n"
"min-width: 24px;\n"
"}\n"
"\n"
"QListWidget {\n"
"border: 0;\n"
"}\n"
"        \n"
"QToolButton, QPushButton {\n"
"min-width: 24px;\n"
"border: 1px solid transparent;\n"
"padding: 4px;\n"
"border-radius: 4px;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QToolButton:hover, QPushButton:hover {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.subToolBar.setObjectName(_fromUtf8("subToolBar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.subToolBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backButton = QtGui.QPushButton(self.subToolBar)
        self.backButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.backButton.setStyleSheet(_fromUtf8(""))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        self.nextButton = QtGui.QPushButton(self.subToolBar)
        self.nextButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.nextButton.setStyleSheet(_fromUtf8(""))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.stopButton = QtGui.QPushButton(self.subToolBar)
        self.stopButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.reloadButton = QtGui.QPushButton(self.subToolBar)
        self.reloadButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.horizontalLayout.addWidget(self.reloadButton)
        self.findButton = QtGui.QPushButton(self.subToolBar)
        self.findButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.horizontalLayout.addWidget(self.findButton)
        self.findNextButton = QtGui.QPushButton(self.subToolBar)
        self.findNextButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.findNextButton.setObjectName(_fromUtf8("findNextButton"))
        self.horizontalLayout.addWidget(self.findNextButton)
        self.urlBar = QtGui.QLineEdit(self.subToolBar)
        self.urlBar.setObjectName(_fromUtf8("urlBar"))
        self.horizontalLayout.addWidget(self.urlBar)
        self.goButton = QtGui.QPushButton(self.subToolBar)
        self.goButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.goButton.setStyleSheet(_fromUtf8(""))
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.horizontalLayout.addWidget(self.goButton)
        self.mainToolBarLayout.addWidget(self.subToolBar)
        self.focusURLBarButton = QtGui.QPushButton(self.mainToolBar)
        self.focusURLBarButton.setStyleSheet(_fromUtf8("max-width: 0;\n"
"min-width: 0;\n"
"width: 0;\n"
"background: transparent;"))
        self.focusURLBarButton.setText(_fromUtf8(""))
        self.focusURLBarButton.setIconSize(QtCore.QSize(0, 0))
        self.focusURLBarButton.setFlat(True)
        self.focusURLBarButton.setObjectName(_fromUtf8("focusURLBarButton"))
        self.mainToolBarLayout.addWidget(self.focusURLBarButton)
        self.searchButton = QtGui.QPushButton(self.mainToolBar)
        self.searchButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.mainToolBarLayout.addWidget(self.searchButton)
        self.searchEditButton = QtGui.QToolButton(self.mainToolBar)
        self.searchEditButton.setStyleSheet(_fromUtf8("QToolButton { max-width: 16px; }"))
        self.searchEditButton.setArrowType(QtCore.Qt.DownArrow)
        self.searchEditButton.setObjectName(_fromUtf8("searchEditButton"))
        self.mainToolBarLayout.addWidget(self.searchEditButton)
        self.mainToolBarContents.addLayout(self.mainToolBarLayout, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.mainToolBar, 1, 0, 1, 1)
        self.statusBar = QtGui.QWidget(self.centralWidget)
        self.statusBar.setStyleSheet(_fromUtf8("#statusBar {\n"
"border-top: 1px solid palette(shadow);\n"
"}"))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.statusBarLayout = QtGui.QHBoxLayout(self.statusBar)
        self.statusBarLayout.setSpacing(6)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setObjectName(_fromUtf8("statusBarLayout"))
        self.statusMessage = QtGui.QLineEdit(self.statusBar)
        self.statusMessage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.statusMessage.setStyleSheet(_fromUtf8("QLineEdit {\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"border: 0;\n"
"background: transparent;\n"
"}"))
        self.statusMessage.setText(_fromUtf8(""))
        self.statusMessage.setReadOnly(True)
        self.statusMessage.setObjectName(_fromUtf8("statusMessage"))
        self.statusBarLayout.addWidget(self.statusMessage)
        self.progressBar = QtGui.QProgressBar(self.statusBar)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(_fromUtf8("min-height: 1em;\n"
"max-height: 1em;\n"
"min-width: 200px;\n"
"max-width: 200px;"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.statusBarLayout.addWidget(self.progressBar)
        self.zoomBar = QtGui.QWidget(self.statusBar)
        self.zoomBar.setStyleSheet(_fromUtf8("QToolButton, QPushButton {\n"
"min-width: 16px;\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"padding-left: 4px;\n"
"padding-right: 4px;\n"
"border-radius: 4px;\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.zoomBar.setObjectName(_fromUtf8("zoomBar"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.zoomBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.zoomOutButton = QtGui.QPushButton(self.zoomBar)
        self.zoomOutButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomOutButton.setObjectName(_fromUtf8("zoomOutButton"))
        self.horizontalLayout_3.addWidget(self.zoomOutButton)
        self.zoomSlider = QtGui.QSlider(self.zoomBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomSlider.sizePolicy().hasHeightForWidth())
        self.zoomSlider.setSizePolicy(sizePolicy)
        self.zoomSlider.setMinimumSize(QtCore.QSize(128, 0))
        self.zoomSlider.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomSlider.setStyleSheet(_fromUtf8("max-height: 1em;"))
        self.zoomSlider.setMinimum(1)
        self.zoomSlider.setMaximum(12)
        self.zoomSlider.setSliderPosition(4)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setInvertedAppearance(False)
        self.zoomSlider.setInvertedControls(False)
        self.zoomSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.zoomSlider.setTickInterval(1)
        self.zoomSlider.setObjectName(_fromUtf8("zoomSlider"))
        self.horizontalLayout_3.addWidget(self.zoomSlider)
        self.zoomInButton = QtGui.QPushButton(self.zoomBar)
        self.zoomInButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomInButton.setObjectName(_fromUtf8("zoomInButton"))
        self.horizontalLayout_3.addWidget(self.zoomInButton)
        self.zoomLabel = QtGui.QLabel(self.zoomBar)
        self.zoomLabel.setStyleSheet(_fromUtf8("margin-left: 2px;"))
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.horizontalLayout_3.addWidget(self.zoomLabel)
        self.statusBarLayout.addWidget(self.zoomBar)
        self.mainLayout.addWidget(self.statusBar, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.backButton, self.nextButton)
        MainWindow.setTabOrder(self.nextButton, self.stopButton)
        MainWindow.setTabOrder(self.stopButton, self.reloadButton)
        MainWindow.setTabOrder(self.reloadButton, self.findButton)
        MainWindow.setTabOrder(self.findButton, self.urlBar)
        MainWindow.setTabOrder(self.urlBar, self.goButton)
        MainWindow.setTabOrder(self.goButton, self.focusURLBarButton)
        MainWindow.setTabOrder(self.focusURLBarButton, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.searchEditButton)
        MainWindow.setTabOrder(self.searchEditButton, self.statusMessage)
        MainWindow.setTabOrder(self.statusMessage, self.zoomOutButton)
        MainWindow.setTabOrder(self.zoomOutButton, self.zoomSlider)
        MainWindow.setTabOrder(self.zoomSlider, self.zoomInButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Ryouko", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Back</b><br>Alt+Left Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Next</b><br>Alt+Right Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Stop</b><br>Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Reload</b><br>F5", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Find</b><br>Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.findNextButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Find Next</b><br>Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.findNextButton.setText(QtGui.QApplication.translate("MainWindow", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.urlBar.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Location Bar</b><br>Ctrl+L; Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Go</b><br>Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.focusURLBarButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Search</b><br>Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchEditButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom Out</b><br>Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom In</b><br>Ctrl++; Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomLabel.setText(QtGui.QApplication.translate("MainWindow", "1.00x", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/foxhead128/Applications/ryouko/ryouko_lib/mainwindow.ui'
#
# Created: Sat Jun  9 16:42:52 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(832, 480)
        MainWindow.setStyleSheet(_fromUtf8("QListWidget {\n"
"border: 0;\n"
"}"))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mainLayout = QtGui.QGridLayout(self.centralWidget)
        self.mainLayout.setMargin(0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.mainToolBar = QtGui.QWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainToolBar.sizePolicy().hasHeightForWidth())
        self.mainToolBar.setSizePolicy(sizePolicy)
        self.mainToolBar.setStyleSheet(_fromUtf8("#mainToolBar {\n"
"border-bottom: 1px solid palette(shadow);\n"
"}"))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.mainToolBarContents = QtGui.QGridLayout(self.mainToolBar)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setSpacing(0)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setObjectName(_fromUtf8("mainToolBarContents"))
        self.mainToolBarLayout = QtGui.QHBoxLayout()
        self.mainToolBarLayout.setSpacing(0)
        self.mainToolBarLayout.setContentsMargins(-1, -1, -1, 0)
        self.mainToolBarLayout.setObjectName(_fromUtf8("mainToolBarLayout"))
        self.subToolBar = QtGui.QWidget(self.mainToolBar)
        self.subToolBar.setStyleSheet(_fromUtf8("#subToolBar {\n"
"min-width: 24px;\n"
"}\n"
"\n"
"QListWidget {\n"
"border: 0;\n"
"}\n"
"        \n"
"QToolButton, QPushButton {\n"
"min-width: 24px;\n"
"border: 1px solid transparent;\n"
"padding: 4px;\n"
"border-radius: 4px;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QToolButton:hover, QPushButton:hover {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.subToolBar.setObjectName(_fromUtf8("subToolBar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.subToolBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backButton = QtGui.QPushButton(self.subToolBar)
        self.backButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.backButton.setStyleSheet(_fromUtf8(""))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        self.nextButton = QtGui.QPushButton(self.subToolBar)
        self.nextButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.nextButton.setStyleSheet(_fromUtf8(""))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.stopButton = QtGui.QPushButton(self.subToolBar)
        self.stopButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.reloadButton = QtGui.QPushButton(self.subToolBar)
        self.reloadButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.horizontalLayout.addWidget(self.reloadButton)
        self.findButton = QtGui.QPushButton(self.subToolBar)
        self.findButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.horizontalLayout.addWidget(self.findButton)
        self.findNextButton = QtGui.QPushButton(self.subToolBar)
        self.findNextButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.findNextButton.setObjectName(_fromUtf8("findNextButton"))
        self.horizontalLayout.addWidget(self.findNextButton)
        self.urlBar = QtGui.QLineEdit(self.subToolBar)
        self.urlBar.setObjectName(_fromUtf8("urlBar"))
        self.horizontalLayout.addWidget(self.urlBar)
        self.addBookmarkButton = QtGui.QPushButton(self.subToolBar)
        self.addBookmarkButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.addBookmarkButton.setStyleSheet(_fromUtf8(""))
        self.addBookmarkButton.setObjectName(_fromUtf8("addBookmarkButton"))
        self.horizontalLayout.addWidget(self.addBookmarkButton)
        self.goButton = QtGui.QPushButton(self.subToolBar)
        self.goButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.goButton.setStyleSheet(_fromUtf8(""))
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.horizontalLayout.addWidget(self.goButton)
        self.mainToolBarLayout.addWidget(self.subToolBar)
        self.focusURLBarButton = QtGui.QPushButton(self.mainToolBar)
        self.focusURLBarButton.setStyleSheet(_fromUtf8("max-width: 0;\n"
"min-width: 0;\n"
"width: 0;\n"
"background: transparent;"))
        self.focusURLBarButton.setText(_fromUtf8(""))
        self.focusURLBarButton.setIconSize(QtCore.QSize(0, 0))
        self.focusURLBarButton.setFlat(True)
        self.focusURLBarButton.setObjectName(_fromUtf8("focusURLBarButton"))
        self.mainToolBarLayout.addWidget(self.focusURLBarButton)
        self.searchButton = QtGui.QPushButton(self.mainToolBar)
        self.searchButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.mainToolBarLayout.addWidget(self.searchButton)
        self.searchEditButton = QtGui.QToolButton(self.mainToolBar)
        self.searchEditButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.searchEditButton.setStyleSheet(_fromUtf8("QToolButton { max-width: 16px; }"))
        self.searchEditButton.setArrowType(QtCore.Qt.DownArrow)
        self.searchEditButton.setObjectName(_fromUtf8("searchEditButton"))
        self.mainToolBarLayout.addWidget(self.searchEditButton)
        self.mainToolBarContents.addLayout(self.mainToolBarLayout, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.mainToolBar, 1, 0, 1, 1)
        self.statusBar = QtGui.QWidget(self.centralWidget)
        self.statusBar.setStyleSheet(_fromUtf8("#statusBar {\n"
"border-top: 1px solid palette(shadow);\n"
"}"))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.statusBarLayout = QtGui.QHBoxLayout(self.statusBar)
        self.statusBarLayout.setSpacing(6)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setObjectName(_fromUtf8("statusBarLayout"))
        self.statusMessage = QtGui.QLineEdit(self.statusBar)
        self.statusMessage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.statusMessage.setStyleSheet(_fromUtf8("QLineEdit {\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"border: 0;\n"
"background: transparent;\n"
"}"))
        self.statusMessage.setText(_fromUtf8(""))
        self.statusMessage.setReadOnly(True)
        self.statusMessage.setObjectName(_fromUtf8("statusMessage"))
        self.statusBarLayout.addWidget(self.statusMessage)
        self.progressBar = QtGui.QProgressBar(self.statusBar)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(_fromUtf8("min-height: 1em;\n"
"max-height: 1em;\n"
"min-width: 200px;\n"
"max-width: 200px;"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.statusBarLayout.addWidget(self.progressBar)
        self.zoomBar = QtGui.QWidget(self.statusBar)
        self.zoomBar.setStyleSheet(_fromUtf8("QToolButton, QPushButton {\n"
"min-width: 16px;\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"padding-left: 4px;\n"
"padding-right: 4px;\n"
"border-radius: 4px;\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.zoomBar.setObjectName(_fromUtf8("zoomBar"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.zoomBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.zoomOutButton = QtGui.QPushButton(self.zoomBar)
        self.zoomOutButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomOutButton.setObjectName(_fromUtf8("zoomOutButton"))
        self.horizontalLayout_3.addWidget(self.zoomOutButton)
        self.zoomSlider = QtGui.QSlider(self.zoomBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomSlider.sizePolicy().hasHeightForWidth())
        self.zoomSlider.setSizePolicy(sizePolicy)
        self.zoomSlider.setMinimumSize(QtCore.QSize(128, 0))
        self.zoomSlider.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomSlider.setStyleSheet(_fromUtf8("max-height: 1em;"))
        self.zoomSlider.setMinimum(1)
        self.zoomSlider.setMaximum(12)
        self.zoomSlider.setSliderPosition(4)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setInvertedAppearance(False)
        self.zoomSlider.setInvertedControls(False)
        self.zoomSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.zoomSlider.setTickInterval(1)
        self.zoomSlider.setObjectName(_fromUtf8("zoomSlider"))
        self.horizontalLayout_3.addWidget(self.zoomSlider)
        self.zoomInButton = QtGui.QPushButton(self.zoomBar)
        self.zoomInButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomInButton.setObjectName(_fromUtf8("zoomInButton"))
        self.horizontalLayout_3.addWidget(self.zoomInButton)
        self.zoomLabel = QtGui.QLabel(self.zoomBar)
        self.zoomLabel.setStyleSheet(_fromUtf8("margin-left: 2px;"))
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.horizontalLayout_3.addWidget(self.zoomLabel)
        self.statusBarLayout.addWidget(self.zoomBar)
        self.mainLayout.addWidget(self.statusBar, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.backButton, self.nextButton)
        MainWindow.setTabOrder(self.nextButton, self.stopButton)
        MainWindow.setTabOrder(self.stopButton, self.reloadButton)
        MainWindow.setTabOrder(self.reloadButton, self.findButton)
        MainWindow.setTabOrder(self.findButton, self.findNextButton)
        MainWindow.setTabOrder(self.findNextButton, self.urlBar)
        MainWindow.setTabOrder(self.urlBar, self.addBookmarkButton)
        MainWindow.setTabOrder(self.addBookmarkButton, self.goButton)
        MainWindow.setTabOrder(self.goButton, self.focusURLBarButton)
        MainWindow.setTabOrder(self.focusURLBarButton, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.searchEditButton)
        MainWindow.setTabOrder(self.searchEditButton, self.statusMessage)
        MainWindow.setTabOrder(self.statusMessage, self.zoomOutButton)
        MainWindow.setTabOrder(self.zoomOutButton, self.zoomSlider)
        MainWindow.setTabOrder(self.zoomSlider, self.zoomInButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Ryouko", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Back</b><br>Alt+Left Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Next</b><br>Alt+Right Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Stop</b><br>Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Reload</b><br>F5", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Find</b><br>Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.findNextButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Find Next</b><br>Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.findNextButton.setText(QtGui.QApplication.translate("MainWindow", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.urlBar.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Location Bar</b><br>Ctrl+L; Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.addBookmarkButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Add Bookmark</b><br>Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.addBookmarkButton.setText(QtGui.QApplication.translate("MainWindow", "Add Bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Go</b><br>Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.focusURLBarButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Search</b><br>Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchEditButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom Out</b><br>Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom In</b><br>Ctrl++; Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomLabel.setText(QtGui.QApplication.translate("MainWindow", "1.00x", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/foxhead128/Applications/ryouko/ryouko_lib/mainwindow.ui'
#
# Created: Wed Jun 20 22:23:56 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(832, 480)
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mainLayout = QtGui.QGridLayout(self.centralWidget)
        self.mainLayout.setMargin(0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.statusBar = QtGui.QWidget(self.centralWidget)
        self.statusBar.setStyleSheet(_fromUtf8("#statusBar {\n"
"border-top: 1px solid palette(shadow);\n"
"}"))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.statusBarLayout = QtGui.QHBoxLayout(self.statusBar)
        self.statusBarLayout.setSpacing(6)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setObjectName(_fromUtf8("statusBarLayout"))
        self.statusMessage = QtGui.QLineEdit(self.statusBar)
        self.statusMessage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.statusMessage.setStyleSheet(_fromUtf8("QLineEdit {\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"border: 0;\n"
"background: transparent;\n"
"}"))
        self.statusMessage.setText(_fromUtf8(""))
        self.statusMessage.setReadOnly(True)
        self.statusMessage.setObjectName(_fromUtf8("statusMessage"))
        self.statusBarLayout.addWidget(self.statusMessage)
        self.progressBar = QtGui.QProgressBar(self.statusBar)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(_fromUtf8("min-height: 1em;\n"
"max-height: 1em;\n"
"min-width: 200px;\n"
"max-width: 200px;"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.statusBarLayout.addWidget(self.progressBar)
        self.zoomBar = QtGui.QWidget(self.statusBar)
        self.zoomBar.setStyleSheet(_fromUtf8("QToolButton, QPushButton {\n"
"min-width: 16px;\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"padding-left: 4px;\n"
"padding-right: 4px;\n"
"border-radius: 4px;\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.zoomBar.setObjectName(_fromUtf8("zoomBar"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.zoomBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.zoomOutButton = QtGui.QPushButton(self.zoomBar)
        self.zoomOutButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomOutButton.setObjectName(_fromUtf8("zoomOutButton"))
        self.horizontalLayout_3.addWidget(self.zoomOutButton)
        self.zoomSlider = QtGui.QSlider(self.zoomBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomSlider.sizePolicy().hasHeightForWidth())
        self.zoomSlider.setSizePolicy(sizePolicy)
        self.zoomSlider.setMinimumSize(QtCore.QSize(128, 0))
        self.zoomSlider.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomSlider.setStyleSheet(_fromUtf8("max-height: 1em;"))
        self.zoomSlider.setMinimum(1)
        self.zoomSlider.setMaximum(12)
        self.zoomSlider.setSliderPosition(4)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setInvertedAppearance(False)
        self.zoomSlider.setInvertedControls(False)
        self.zoomSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.zoomSlider.setTickInterval(1)
        self.zoomSlider.setObjectName(_fromUtf8("zoomSlider"))
        self.horizontalLayout_3.addWidget(self.zoomSlider)
        self.zoomInButton = QtGui.QPushButton(self.zoomBar)
        self.zoomInButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomInButton.setObjectName(_fromUtf8("zoomInButton"))
        self.horizontalLayout_3.addWidget(self.zoomInButton)
        self.zoomLabel = QtGui.QLabel(self.zoomBar)
        self.zoomLabel.setStyleSheet(_fromUtf8("margin-left: 2px;"))
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.horizontalLayout_3.addWidget(self.zoomLabel)
        self.statusBarLayout.addWidget(self.zoomBar)
        self.mainLayout.addWidget(self.statusBar, 4, 0, 1, 1)
        self.mainToolBarContainer = QtGui.QWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainToolBarContainer.sizePolicy().hasHeightForWidth())
        self.mainToolBarContainer.setSizePolicy(sizePolicy)
        self.mainToolBarContainer.setStyleSheet(_fromUtf8(""))
        self.mainToolBarContainer.setObjectName(_fromUtf8("mainToolBarContainer"))
        self.mainToolBarContents = QtGui.QGridLayout(self.mainToolBarContainer)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setSpacing(0)
        self.mainToolBarContents.setMargin(0)
        self.mainToolBarContents.setObjectName(_fromUtf8("mainToolBarContents"))
        self.mainToolBarLayout = QtGui.QHBoxLayout()
        self.mainToolBarLayout.setSpacing(0)
        self.mainToolBarLayout.setContentsMargins(-1, -1, -1, 0)
        self.mainToolBarLayout.setObjectName(_fromUtf8("mainToolBarLayout"))
        self.subToolBar = QtGui.QWidget(self.mainToolBarContainer)
        self.subToolBar.setStyleSheet(_fromUtf8("#subToolBar {\n"
"min-width: 24px;\n"
"}\n"
"\n"
"QPushButton:default {\n"
"border: 0;\n"
"}"))
        self.subToolBar.setObjectName(_fromUtf8("subToolBar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.subToolBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.backButton = QtGui.QPushButton(self.subToolBar)
        self.backButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.backButton.setStyleSheet(_fromUtf8(""))
        self.backButton.setObjectName(_fromUtf8("backButton"))
        self.horizontalLayout.addWidget(self.backButton)
        self.nextButton = QtGui.QPushButton(self.subToolBar)
        self.nextButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.nextButton.setStyleSheet(_fromUtf8(""))
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.stopButton = QtGui.QPushButton(self.subToolBar)
        self.stopButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.horizontalLayout.addWidget(self.stopButton)
        self.reloadButton = QtGui.QPushButton(self.subToolBar)
        self.reloadButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.reloadButton.setObjectName(_fromUtf8("reloadButton"))
        self.horizontalLayout.addWidget(self.reloadButton)
        self.findButton = QtGui.QPushButton(self.subToolBar)
        self.findButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.horizontalLayout.addWidget(self.findButton)
        self.findNextButton = QtGui.QPushButton(self.subToolBar)
        self.findNextButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.findNextButton.setObjectName(_fromUtf8("findNextButton"))
        self.horizontalLayout.addWidget(self.findNextButton)
        self.urlBar = QtGui.QLineEdit(self.subToolBar)
        self.urlBar.setObjectName(_fromUtf8("urlBar"))
        self.horizontalLayout.addWidget(self.urlBar)
        self.addBookmarkButton = QtGui.QPushButton(self.subToolBar)
        self.addBookmarkButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.addBookmarkButton.setStyleSheet(_fromUtf8(""))
        self.addBookmarkButton.setObjectName(_fromUtf8("addBookmarkButton"))
        self.horizontalLayout.addWidget(self.addBookmarkButton)
        self.goButton = QtGui.QPushButton(self.subToolBar)
        self.goButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.goButton.setStyleSheet(_fromUtf8(""))
        self.goButton.setObjectName(_fromUtf8("goButton"))
        self.horizontalLayout.addWidget(self.goButton)
        self.mainToolBarLayout.addWidget(self.subToolBar)
        self.focusURLBarButton = QtGui.QPushButton(self.mainToolBarContainer)
        self.focusURLBarButton.setStyleSheet(_fromUtf8("max-width: 0;\n"
"min-width: 0;\n"
"width: 0;\n"
"background: transparent;"))
        self.focusURLBarButton.setText(_fromUtf8(""))
        self.focusURLBarButton.setIconSize(QtCore.QSize(0, 0))
        self.focusURLBarButton.setFlat(True)
        self.focusURLBarButton.setObjectName(_fromUtf8("focusURLBarButton"))
        self.mainToolBarLayout.addWidget(self.focusURLBarButton)
        self.searchButton = QtGui.QPushButton(self.mainToolBarContainer)
        self.searchButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.mainToolBarLayout.addWidget(self.searchButton)
        self.searchEditButton = QtGui.QToolButton(self.mainToolBarContainer)
        self.searchEditButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.searchEditButton.setStyleSheet(_fromUtf8("QToolButton { max-width: 16px; }"))
        self.searchEditButton.setArrowType(QtCore.Qt.DownArrow)
        self.searchEditButton.setObjectName(_fromUtf8("searchEditButton"))
        self.mainToolBarLayout.addWidget(self.searchEditButton)
        self.mainToolBarContents.addLayout(self.mainToolBarLayout, 0, 0, 1, 1)
        self.mainLayout.addWidget(self.mainToolBarContainer, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.backButton, self.nextButton)
        MainWindow.setTabOrder(self.nextButton, self.stopButton)
        MainWindow.setTabOrder(self.stopButton, self.reloadButton)
        MainWindow.setTabOrder(self.reloadButton, self.findButton)
        MainWindow.setTabOrder(self.findButton, self.findNextButton)
        MainWindow.setTabOrder(self.findNextButton, self.urlBar)
        MainWindow.setTabOrder(self.urlBar, self.addBookmarkButton)
        MainWindow.setTabOrder(self.addBookmarkButton, self.goButton)
        MainWindow.setTabOrder(self.goButton, self.focusURLBarButton)
        MainWindow.setTabOrder(self.focusURLBarButton, self.searchButton)
        MainWindow.setTabOrder(self.searchButton, self.searchEditButton)
        MainWindow.setTabOrder(self.searchEditButton, self.statusMessage)
        MainWindow.setTabOrder(self.statusMessage, self.zoomOutButton)
        MainWindow.setTabOrder(self.zoomOutButton, self.zoomSlider)
        MainWindow.setTabOrder(self.zoomSlider, self.zoomInButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Ryouko", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom Out</b><br>Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom In</b><br>Ctrl++; Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomLabel.setText(QtGui.QApplication.translate("MainWindow", "1.00x", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Back</b><br>Alt+Left Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.backButton.setText(QtGui.QApplication.translate("MainWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Next</b><br>Alt+Right Arrow", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindow", "Next", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Stop</b><br>Esc", None, QtGui.QApplication.UnicodeUTF8))
        self.stopButton.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Reload</b><br>F5", None, QtGui.QApplication.UnicodeUTF8))
        self.reloadButton.setText(QtGui.QApplication.translate("MainWindow", "Reload", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Find</b><br>Ctrl+F", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(QtGui.QApplication.translate("MainWindow", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.findNextButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Find Next</b><br>Ctrl+G", None, QtGui.QApplication.UnicodeUTF8))
        self.findNextButton.setText(QtGui.QApplication.translate("MainWindow", "Find Next", None, QtGui.QApplication.UnicodeUTF8))
        self.urlBar.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Location Bar</b><br>Ctrl+L; Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.addBookmarkButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Add Bookmark</b><br>Ctrl+D", None, QtGui.QApplication.UnicodeUTF8))
        self.addBookmarkButton.setText(QtGui.QApplication.translate("MainWindow", "Add Bookmark", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Go</b><br>Enter", None, QtGui.QApplication.UnicodeUTF8))
        self.goButton.setText(QtGui.QApplication.translate("MainWindow", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.focusURLBarButton.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+D", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Search</b><br>Ctrl+K", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.searchEditButton.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.mainToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/foxhead128/Applications/ryouko/ryouko_lib/mainwindow.ui'
#
# Created: Wed Jun 20 22:55:16 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(832, 480)
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mainLayout = QtGui.QGridLayout(self.centralWidget)
        self.mainLayout.setMargin(0)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(_fromUtf8("mainLayout"))
        self.statusBar = QtGui.QWidget(self.centralWidget)
        self.statusBar.setStyleSheet(_fromUtf8("#statusBar {\n"
"border-top: 1px solid palette(shadow);\n"
"}"))
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        self.statusBarLayout = QtGui.QHBoxLayout(self.statusBar)
        self.statusBarLayout.setSpacing(6)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setMargin(0)
        self.statusBarLayout.setObjectName(_fromUtf8("statusBarLayout"))
        self.statusMessage = QtGui.QLineEdit(self.statusBar)
        self.statusMessage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.statusMessage.setStyleSheet(_fromUtf8("QLineEdit {\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"border: 0;\n"
"background: transparent;\n"
"}"))
        self.statusMessage.setText(_fromUtf8(""))
        self.statusMessage.setReadOnly(True)
        self.statusMessage.setObjectName(_fromUtf8("statusMessage"))
        self.statusBarLayout.addWidget(self.statusMessage)
        self.progressBar = QtGui.QProgressBar(self.statusBar)
        self.progressBar.setEnabled(True)
        self.progressBar.setStyleSheet(_fromUtf8("min-height: 1em;\n"
"max-height: 1em;\n"
"min-width: 200px;\n"
"max-width: 200px;"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.statusBarLayout.addWidget(self.progressBar)
        self.zoomBar = QtGui.QWidget(self.statusBar)
        self.zoomBar.setStyleSheet(_fromUtf8("QToolButton, QPushButton {\n"
"min-width: 16px;\n"
"min-height: 1em;\n"
"max-height: 1em;\n"
"padding-left: 4px;\n"
"padding-right: 4px;\n"
"border-radius: 4px;\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));\n"
"}\n"
"\n"
"QToolButton:pressed, QPushButton:pressed {\n"
"border: 1px solid palette(shadow);\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));\n"
"}"))
        self.zoomBar.setObjectName(_fromUtf8("zoomBar"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.zoomBar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.zoomOutButton = QtGui.QPushButton(self.zoomBar)
        self.zoomOutButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomOutButton.setObjectName(_fromUtf8("zoomOutButton"))
        self.horizontalLayout_3.addWidget(self.zoomOutButton)
        self.zoomSlider = QtGui.QSlider(self.zoomBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zoomSlider.sizePolicy().hasHeightForWidth())
        self.zoomSlider.setSizePolicy(sizePolicy)
        self.zoomSlider.setMinimumSize(QtCore.QSize(128, 0))
        self.zoomSlider.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomSlider.setStyleSheet(_fromUtf8("max-height: 1em;"))
        self.zoomSlider.setMinimum(1)
        self.zoomSlider.setMaximum(12)
        self.zoomSlider.setSliderPosition(4)
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setInvertedAppearance(False)
        self.zoomSlider.setInvertedControls(False)
        self.zoomSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.zoomSlider.setTickInterval(1)
        self.zoomSlider.setObjectName(_fromUtf8("zoomSlider"))
        self.horizontalLayout_3.addWidget(self.zoomSlider)
        self.zoomInButton = QtGui.QPushButton(self.zoomBar)
        self.zoomInButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomInButton.setObjectName(_fromUtf8("zoomInButton"))
        self.horizontalLayout_3.addWidget(self.zoomInButton)
        self.zoomLabel = QtGui.QLabel(self.zoomBar)
        self.zoomLabel.setStyleSheet(_fromUtf8("margin-left: 2px;"))
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.horizontalLayout_3.addWidget(self.zoomLabel)
        self.statusBarLayout.addWidget(self.zoomBar)
        self.mainLayout.addWidget(self.statusBar, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.statusMessage, self.zoomOutButton)
        MainWindow.setTabOrder(self.zoomOutButton, self.zoomSlider)
        MainWindow.setTabOrder(self.zoomSlider, self.zoomInButton)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Ryouko", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom Out</b><br>Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomOutButton.setText(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setToolTip(QtGui.QApplication.translate("MainWindow", "<b>Zoom In</b><br>Ctrl++; Ctrl+=", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomInButton.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomLabel.setText(QtGui.QApplication.translate("MainWindow", "1.00x", None, QtGui.QApplication.UnicodeUTF8))
        self.mainToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))

