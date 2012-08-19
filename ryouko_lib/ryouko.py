#! /usr/bin/env python

# This file is licensed under the terms of the following MIT License:

## START OF LICENSE ##
"""
Copyright (c) 2012 Daniel Sim (foxhead128)
Portions of the code are copyright (c) 2011 roberto.alsina

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
## END OF LICENSE ##

from __future__ import print_function
import locale

def do_nothing():
    return

try:
    from PyQt4 import QtCore, QtGui, QtWebKit, QtNetwork
except:
    from Tkinter import *
    root = Tk()
    root.title(tr('error'))
    w = Label(root, text=tr('noPyQtError'))
    w.pack()
    button = Button(root, text="OK", command=sys.exit)
    button.pack()
    root.mainloop()
    sys.exit()

use_unity_launcher = False
try:
    from gi.repository import Unity, Gio, GObject, Dbusmenu
except:
    do_nothing()
else:
    use_unity_launcher = True

use_linux_notifications = False
try:
    import pynotify
except:
    do_nothing()
else:
    pynotify.init("Ryouko")
    use_linux_notifications = True

import os, sys, json, time, datetime, string, shutil, traceback

app_vista = False
if sys.platform.startswith("win"):
    import platform
    if platform.release() == "7" or platform.release() == "Vista":
        app_vista = True

try: from urllib.request import urlretrieve
except ImportError:
    try: from urllib import urlretrieve
    except:
        print("", end="")
    else:
        import urllib
else:
    import urllib.request

try: __file__
except: __file__ = sys.executable
app_lib = os.path.dirname(os.path.realpath(__file__))
app_locale = locale.getdefaultlocale()[0]
sys.path.append(app_lib)
app_default_useragent = "Mozilla/5.0 (X11, Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) Qt/4.8.1 Safari/534.34"
app_webview_default_icon = QtGui.QIcon()
app_tabs_on_top = False

from ryouko_common import *
from RUrlBar import RUrlBar
from RSearchBar import RSearchBar
from Python23Compat import *
from QStringFunctions import *
from SettingsManager import SettingsManager
from RWebKit import RWebPage, RWebView, RAboutPageView, doNothing
from DownloaderThread import DownloaderThread
from DialogFunctions import inputDialog, centerWidget, message
from MovableTabWidget import MovableTabWidget
from BrowserHistory import BrowserHistory
from HistoryCompletionList import HistoryCompletionList
from BookmarksManager import BookmarksManager
from ContextMenu import ContextMenu
from MenuPopupWindow import MenuPopupWindowMenu, MenuPopupWindow
from RExpander import RExpander
from SearchManager import SearchManager, doNothing
from RHBoxLayout import RHBoxLayout
from NotificationManager import NotificationManager
from TranslationManager import *
from RExtensionButton import RExtensionButton
from DownloadManager import DownloadManagerGUI

app_gnome_unity_integration = False
"""if sys.platform.startswith("linux"):
    if "gnome-session" in commands.getoutput('ps -A'):
        app_gnome_unity_integration = True
#app_use_ambiance = False
if sys.platform.startswith("linux"):
    if get_key("/desktop/gnome/shell/windows/theme") == "Ambiance" and "gnome-session" in commands.getoutput('ps -A'):
        app_use_ambiance = True"""

app_windows = []
app_closed_windows = []
app_info = os.path.join(app_lib, "info.txt")
app_icons = os.path.join(app_lib, 'icons')

def ryouko_icon(name):
    return os.path.join(app_icons, name)

app_version = "N/A"
app_codename = "N/A"
if os.path.exists(app_info):
    readVersionFile = open(app_info)
    metadata = readVersionFile.readlines()
    readVersionFile.close()
    if len(metadata) > 0:
        app_version = metadata[0].rstrip("\n")
        if len(metadata) > 1:
            app_codename = metadata[1].rstrip("\n")
app_gui = os.path.join(app_lib, "mainwindow.ui")
app_home = os.path.expanduser(os.path.join("~", ".ryouko-data"))
app_profile_name = "default"
app_default_profile_file = os.path.join(app_home, "profiles.txt")
app_profile_folder = os.path.join(app_home, "profiles")
app_commandline = ""
app_profile_exists = False
app_kill_cookies = False
app_kill_temp_files = False
app_extensions = []
app_extensions_whitelist = []
app_extensions_path = []
app_extensions_path.append(os.path.join(app_lib, "extensions"))
for arg in sys.argv:
    app_commandline = "%s%s " % (app_commandline, arg)
if sys.platform.startswith("win"):
    app_logo = ryouko_icon('about-logo.png')
else:
    app_logo = ryouko_icon("logo.svg")
user_links = ""

def loadCookies():
    if os.path.exists(app_cookies):
        global app_cookiejar
        cookieFile = open(app_cookies, "r")
        try: c = json.load(cookieFile)
        except:
            print("Error! Cookies could not be loaded!")
            c = []
        cookieFile.close()
        cookies = []
        for cookie in c:
            try: cookies.append(QtNetwork.QNetworkCookie().parseCookies(QtCore.QByteArray(cookie))[0])
            except: do_nothing()
        app_cookiejar.setAllCookies(cookies)

def saveCookies():
    if app_kill_cookies == False:
        cookieFile = open(app_cookies, "w")
        cookies = []
        if sys.version_info[0] >= 3:
            for c in app_cookiejar.allCookies():
                cookies.append(unicode(qstring(c.toRawForm())).strip("b'").rstrip("'"))
        else:
            for c in app_cookiejar.allCookies():
                cookies.append(unicode(qstring(c.toRawForm())))
        json.dump(cookies, cookieFile)
        cookieFile.close()
    else:
        if sys.platform.startswith("linux"):
            os.system("shred -v \"%s\"" % (app_cookies))
        try: remove2(app_cookies)
        except:
            doNothing()

app_cookiejar = QtNetwork.QNetworkCookieJar(QtCore.QCoreApplication.instance())


class RSettingsManager(SettingsManager):
    def errorMessage(self, backend):
        notificationMessage("Error!", "Backend %s could not be found!" % (backend))

settings_manager = RSettingsManager()

def remove2(fname):
    os.remove(fname)
    try: u = os.path.join(os.path.expanduser("~"), settings_manager.settings['cloudService'], "ryouko-profiles", os.path.split(fname)[1])
    except: return
    else:
        if os.path.exists(u):
            os.remove(u)

def changeProfile(profile, init = False):
    global app_profile_name; global app_profile; global app_links;
    global app_lock; global app_cookies; global app_instance2;
    global app_tabs_on_top_conf; global app_menubar_conf;
    global app_extensions; global app_extensions_folder;
    global app_extensions_path; global app_extensions_whitelist;
    global app_extensions_wlfile
    app_profile_name = profile
    app_profile = os.path.join(app_profile_folder, profile)
    app_extensions_wlfile = os.path.join(app_profile, "extensions.conf")
    if os.path.exists(app_extensions_wlfile):
        f = open(app_extensions_wlfile, "r")
        try: a = f.read()
        except: do_nothing()
        f.close()
        app_extensions_whitelist = a.split("\n")
    else:
        app_extensions_whitelist = []
    app_extensions_path.append(os.path.join(app_profile, "extensions"))
    app_links = os.path.join(app_profile, "links")
    app_tabs_on_top_conf = os.path.join(app_profile, "tabsontop.conf")
    app_menubar_conf = os.path.join(app_profile, "menubar_visible.conf")
    app_lock = os.path.join(app_profile, ".lockfile")
    app_cookies = os.path.join(app_profile, "cookies.json")
    app_instance2 = os.path.join(app_profile, "instance2-says.txt")
    loadCookies()    
    if not os.path.isdir(app_home):
        os.makedirs(app_home)
    if not os.path.isdir(app_profile_folder):
        os.makedirs(app_profile_folder)
    if not os.path.isdir(app_profile):
        os.makedirs(app_profile)

    settings_manager.changeProfile(app_profile)

    try: bookmarksManager
    except: doNothing()
    else: bookmarksManager.setDirectory(app_links)

    global user_links
    try: user_links = bookmarksManager.reload_user_links(app_links)
    except: do_nothing()

    try: browserHistory
    except: doNothing()
    else:
        browserHistory.setAppProfile(app_profile)
        browserHistory.reload()

    try: searchManager
    except: doNothing()
    else: searchManager.changeProfile(app_profile)

app_default_profile_name = "default"
if os.path.exists(app_default_profile_file):
    f = open(app_default_profile_file)
    app_default_profile_name = f.read()
    f.close()
    app_default_profile_name = app_default_profile_name.replace("\n", "")
if not os.path.exists(os.path.join(app_profile_folder, app_default_profile_name)):
    app_default_profile_name = "default"
changeProfile(app_default_profile_name, True)

bookmarksManager = BookmarksManager(app_links)

def rebuild_bookmarks_toolbar():
    global user_links
    user_links = bookmarksManager.reload_user_links(app_links)

bookmarksManager.bookmarksChanged.connect(rebuild_bookmarks_toolbar)

bookmarksManager.setDirectory(app_links)
user_links = bookmarksManager.reload_user_links(bookmarksManager.app_links)

reset = False

blanktoolbarsheet = "QToolBar { border: 0; }"
tabsontopsheet =  "QToolBar{background:palette(window);border-bottom:1px solid palette(shadow);}"
tabsontopsheet2 = """QTabBar::tab {
padding: 4px;
border: 1px solid palette(shadow);
}

QTabBar::tab:top {
border-top-left-radius: 4px;
border-top-right-radius:4px;
border-bottom: 1px solid palette(shadow);
background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop:0 palette(window), stop:1 palette(midlight));
}

QTabBar::tab:top:selected {
border-bottom: 0;
padding-bottom: 5px;
background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop:0 palette(light), stop:1 palette(window));
}"""
windowtoolbarsheet = "QToolBar { border: 0; background: palette(window); }"
dw_stylesheet = ""

def hiddenNotificationMessage(message="This is a message."):
    if use_linux_notifications == False:
        notificationManager.newNotification(message)
    else:
        linux_notification(message)

def notificationMessage(message="This is a message."):
    if use_linux_notifications == False:
        notificationManager.show()
        notificationManager.newNotification(message)
    else:
        linux_notification(message)

def linux_notification(string="This is a message."):
    n = pynotify.Notification(tr("ryoukoSays"), string)
    n.show()

def confirmQuit():
    if len(app_windows) == 0:
        undoCloseWindow()
    q = QtGui.QMessageBox.question(None, tr("query"),
    tr("quitWarning"), QtGui.QMessageBox.Yes | 
    QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    if downloadManagerGUI.progress > 0.0:
        r = QtGui.QMessageBox.question(None, tr("warning"),
    tr("downloadsInProgress"), QtGui.QMessageBox.Yes | 
    QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    else:
        r = QtGui.QMessageBox.Yes
    if q == QtGui.QMessageBox.Yes and r == QtGui.QMessageBox.Yes:
        QtCore.QCoreApplication.instance().quit() 

def prepareQuit():
    if os.path.exists(app_lock) and not os.path.isdir(app_lock):
        remove2(app_lock)
    saveCookies()
    try: settings_manager.settings['cloudService']
    except: doNothing()
    else:
        sync_data()
    sys.exit()

def acopy(f1, f2):
    if os.path.isdir(f1):
        if os.path.exists(f2):
            shutil.rmtree(f2)
        shutil.copytree(f1, f2)
    elif os.path.exists(f1):
        shutil.copyfile(f1, f2)

def sync_data():
    sfile = os.path.join(app_profile, "app_sync.conf")

    # If syncing data has been enabled
    if settings_manager.settings['cloudService'] != "No" and settings_manager.settings['cloudService'] != "None" and os.path.exists(sfile):
        remote = os.path.join(os.path.expanduser("~"), settings_manager.settings['cloudService'], "ryouko-profiles")
        remote_profile = os.path.join(remote, app_profile_name)
        if not os.path.exists(remote_profile):
            os.makedirs(remote_profile)
        d = os.listdir(app_profile)
        for fname in d:
            r = os.path.join(remote_profile, fname)
            l = os.path.join(app_profile, fname)
            if not os.path.exists(r) and os.path.exists(l):
                acopy(l, r)
            elif not os.path.exists(l) and os.path.exists(r):
                acopy(r, l)
            if os.path.exists(r) and os.path.exists(l):
                rt = int(float(os.stat(r).st_mtime)*100)
                lt = int(float(os.stat(l).st_mtime)*100)
                if (lt >= rt) == False:
                    acopy(r, l)
                elif (rt >= lt) == False:
                    acopy(l, r)
            elif os.path.exists(l):         
                acopy(l, r)
            elif os.path.exists(r):
                acopy(r, l)

    elif settings_manager.settings['cloudService'] != "No" and settings_manager.settings['cloudService'] != "None" and not os.path.exists(sfile):
        remote = os.path.join(os.path.expanduser("~"), settings_manager.settings['cloudService'], "ryouko-profiles")
        remote_profile = os.path.join(remote, app_profile_name)
        if os.path.isdir(remote_profile):
            try: shutil.rmtree(app_profile)
            except:
                for win in app_windows:
                    for tab in range(win.tabs.count()):
                        win.tabs.widget(tab).webView.disablePersistentStorage()
                        #except: do_nothing()
                shutil.rmtree(app_profile)
            shutil.copytree(remote_profile, app_profile)
            f = open(sfile, "w")
            f.write("")
            f.close()

        else:
            if not os.path.exists(remote):
                os.makedirs(remote)
            shutil.copytree(app_profile, remote_profile)
            f = open(sfile, "w")
            f.write("")
            f.close()

    elif settings_manager.settings['cloudService'] == "No" or settings_manager.settings['cloudService'] == "None":
        if os.path.exists(sfile) and not os.path.isdir(sfile):
            remove2(sfile)

def touch(fname):
    f = open(fname, "w")
    f.write("")
    f.close()

searchManager = SearchManager(app_profile)

class ListMenu(MenuPopupWindow):
    currentRowChanged = QtCore.pyqtSignal(int)
    itemActivated = QtCore.pyqtSignal(QtGui.QListWidgetItem)
    itemClicked = QtCore.pyqtSignal(QtGui.QListWidgetItem)
    def __init__(self, parent=None):
        MenuPopupWindow.__init__(self, parent)
        self.setStyleSheet("ListMenu { border: 1px solid palette(shadow); } ")
        self.list = QtGui.QListWidget()
        self.list.setStyleSheet("QListWidget { border: 1px solid transparent; background: transparent; color: palette(window-text); } ")
        self.list.setWordWrap(True)
        self.list.currentRowChanged.connect(self.currentRowChanged.emit)
        self.list.itemActivated.connect(self.itemActivated.emit)
        self.list.itemClicked.connect(self.itemClicked.emit)
        self.list.itemActivated.connect(self.hide)
        self.list.itemClicked.connect(self.hide)
        self.setCentralWidget(self.list)
    def row(self, item):
        return self.list.row(item)
    def setCurrentRow(self, index):
        self.list.setCurrentRow(index)
    def append(self, text):
        self.list.addItem(text)
    def addItem(self, text):
        self.append(text)
    def clear(self):
        self.list.clear()

class SearchEditor(MenuPopupWindow):
    if sys.version_info[0] >= 3:
        searchChanged = QtCore.pyqtSignal(str)
    else:
        searchChanged = QtCore.pyqtSignal(QtCore.QString)
    def __init__(self, parent=None):
        super(SearchEditor, self).__init__(parent)
        self.parent = parent
        self.setWindowTitle(tr('searchEditor'))
        self.styleSheet = "QMainWindow { border: 1px solid palette(shadow);} QToolBar { border: 0; }"
        if os.path.exists(app_logo):
            self.setWindowIcon(QtGui.QIcon(app_logo))

        closeWindowAction = QtGui.QAction(self)
        closeWindowAction.setShortcuts(["Ctrl+W", "Ctrl+Shift+K"])
        closeWindowAction.triggered.connect(self.close)
        self.addAction(closeWindowAction)

        self.entryBar = QtGui.QToolBar()
        self.entryBar.setStyleSheet(blanktoolbarsheet)
        self.entryBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.entryBar.setMovable(False)
        self.addToolBar(self.entryBar)

        eLabel = QtGui.QLabel(" " + tr('newExpression'))
        self.entryBar.addWidget(eLabel)
        self.expEntry = QtGui.QLineEdit()
        self.expEntry.returnPressed.connect(self.addSearch)
        self.entryBar.addWidget(self.expEntry)
        self.addSearchButton = QtGui.QPushButton(tr("add"))
        self.addSearchButton.clicked.connect(self.addSearch)
        self.entryBar.addWidget(self.addSearchButton)

        self.engineList = QtGui.QListWidget()
        self.engineList.itemClicked.connect(self.applySearch)
        self.engineList.itemActivated.connect(self.applySearch)
        self.setCentralWidget(self.engineList)

        self.takeSearchAction = QtGui.QAction(self)
        self.takeSearchAction.triggered.connect(self.takeSearch)
        self.takeSearchAction.setShortcut("Del")
        self.addAction(self.takeSearchAction)

        self.hideAction = QtGui.QAction(self)
        self.hideAction.triggered.connect(self.hide)
        self.hideAction.setShortcut("Esc")
        self.addAction(self.hideAction)

    def primeDisplay(self):
        self.reload()
        self.expEntry.setFocus()

    def focusOutEvent(self, e):
        e.accept()
        self.hide()

    def reload(self):
        self.engineList.clear()
        for name in searchManager.searchEngines:
            keyword = "None"
            if searchManager.searchEngines[name]['keyword'] != "":
                keyword = searchManager.searchEngines[name]['keyword']
            self.engineList.addItem("%s\nKeyword: %s" % (name, keyword))
        for item in range(0, self.engineList.count()):
            if searchManager.searchEngines[unicode(self.engineList.item(item).text()).split("\n")[0]]['expression'] == searchManager.currentSearch:
                self.engineList.setCurrentItem(self.engineList.item(item))
                self.searchChanged.emit(qstring(unicode(self.engineList.item(item).text()).split("\n")[0]))
                break

    def addSearch(self):
        if "%s" in self.expEntry.text():
            name = inputDialog(tr('query'), tr('enterName'))
            if name and name != "":
                keyword = inputDialog(tr('query'), tr('enterKeyword'))
                searchManager.add(name, self.expEntry.text(), keyword)
            self.reload()
        else:
            message(tr('error'), tr('newSearchError'), "warn")

    def applySearch(self, item=False, old=False):
        if item:
            try: unicode(item.text()).split("\n")[0]
            except:
                notificationMessage(tr('searchError'))
            else:
                searchManager.change(unicode(item.text()).split("\n")[0])
        if item != None:
            self.searchChanged.emit(qstring(unicode(item.text()).split("\n")[0]))

    def takeSearch(self):
        searchManager.remove(unicode(self.engineList.currentItem().text()).split("\n")[0])
        self.reload()

searchEditor = None

class BookmarksManagerGUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(BookmarksManagerGUI, self).__init__()
        self.parent = parent
        if os.path.exists(app_logo):
            self.setWindowIcon(QtGui.QIcon(app_logo))
        self.setWindowTitle(tr('bookmarks'))
        self.nameToolBar = QtGui.QToolBar("Add a bookmarky")
        if app_gnome_unity_integration:
            self.nameToolBar.setStyleSheet(windowtoolbarsheet)
        else:
            self.nameToolBar.setStyleSheet(blanktoolbarsheet)
        self.nameToolBar.setMovable(False)
        self.nameToolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        nameLabel = QtGui.QLabel(tr('name') + ": ")
        self.nameField = QtGui.QLineEdit()
        self.nameField.returnPressed.connect(self.addBookmark)
        self.nameToolBar.addWidget(nameLabel)
        self.nameToolBar.addWidget(self.nameField)
        self.urlToolBar = QtGui.QToolBar("Add a bookmarky")
        if app_gnome_unity_integration:
            self.urlToolBar.setStyleSheet(windowtoolbarsheet)
        else:
            self.urlToolBar.setStyleSheet(blanktoolbarsheet)
        self.urlToolBar.setMovable(False)
        self.urlToolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        uLabel = QtGui.QLabel(tr('url') + ": ")
        self.urlField = QtGui.QLineEdit()
        self.urlField.returnPressed.connect(self.addBookmark)
        self.urlToolBar.addWidget(uLabel)
        self.urlToolBar.addWidget(self.urlField)
        self.finishToolBar = QtGui.QToolBar()
        if app_gnome_unity_integration:
            self.finishToolBar.setStyleSheet(windowtoolbarsheet)
        else:
            self.finishToolBar.setStyleSheet(blanktoolbarsheet)
        self.finishToolBar.setMovable(False)
        self.finishToolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.addButton = QtGui.QPushButton(tr('add'))
        self.addButton.clicked.connect(self.addBookmark)
        self.finishToolBar.addWidget(self.addButton)
        self.removeButton = QtGui.QPushButton(tr('remove'))
        self.removeButton.clicked.connect(self.removeBookmark)
        self.finishToolBar.addWidget(self.removeButton)
        self.bookmarksList = QtGui.QListWidget()
        self.bookmarksList.currentRowChanged.connect(self.setText)
        self.bookmarksList.itemActivated.connect(self.openBookmark)
        removeBookmarkAction = QtGui.QAction(self)
        removeBookmarkAction.setShortcut("Del")
        removeBookmarkAction.triggered.connect(self.removeBookmark)
        self.addAction(removeBookmarkAction)
        closeWindowAction = QtGui.QAction(self)
        closeWindowAction.setShortcuts(["Ctrl+W", "Ctrl+Shift+O"])
        if self.parent:
            closeWindowAction.triggered.connect(self.parent.close)
        else:
            closeWindowAction.triggered.connect(self.close)
        self.addAction(closeWindowAction)

        otherTabAction = QtGui.QAction(self)
        otherTabAction.setShortcut("Ctrl+Shift+H")
        otherTabAction.triggered.connect(self.switchTabs)
        self.addAction(otherTabAction)

        bookmarksManager.bookmarksChanged.connect(self.reload_)
        self.addToolBar(self.nameToolBar)
        self.addToolBarBreak()
        self.addToolBar(self.urlToolBar)
        self.addToolBarBreak()
        self.addToolBar(self.finishToolBar)
        self.setCentralWidget(self.bookmarksList)
        self.reload_()

    def setText(self):
        if self.bookmarksList.currentItem():
            self.nameField.setText(self.bookmarksList.currentItem().text())
            for bookmark in bookmarksManager.bookmarks:
                if bookmark["name"] == unicode(self.bookmarksList.currentItem().text()):
                    self.urlField.setText(bookmark["url"])

    def switchTabs(self):
        if self.parent.tabs:
            self.parent.tabs.setCurrentIndex(1)

    def display(self):
        if self.parent.display and self.parent.tabs:
            self.parent.display()
            self.parent.tabs.setCurrentIndex(0)
            self.show()
            self.nameField.setFocus()
            self.nameField.selectAll()
            self.activateWindow()
        else:
            self.show()
            self.resize(640, 480)
            self.nameField.setFocus()
            self.nameField.selectAll()
            self.activateWindow()
    def reload_(self):
        self.bookmarksList.clear()
        for bookmark in bookmarksManager.bookmarks:
            self.bookmarksList.addItem(bookmark["name"])
    def openBookmark(self):
        if win.closed:
            win.show()
            win.closed = False
            win.resize(800, 480)
        for bookmark in bookmarksManager.bookmarks:
            if bookmark["name"] == unicode(self.bookmarksList.currentItem().text()):
                win.newTab(None, bookmark["url"])
                break
    def addBookmark(self):
        if unicode(self.nameField.text()) != "" and unicode(self.urlField.text()) != "":
            bookmarksManager.add(unicode(self.urlField.text()), unicode(self.nameField.text()))
        else:
            notificationMessage(tr('bookmarkError'))
    def removeBookmarkIfFocused(self):
        if self.bookmarksList.hasFocus():
            removeBookmark()
    def removeBookmark(self):
        bookmarksManager.removeByName(unicode(self.bookmarksList.currentItem().text()))
    def closeEvent(self, ev):
        try:
            self.parent.close()
        except:
            doNothing()
        return QtGui.QMainWindow.closeEvent(self, ev)

class ClearHistoryDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(ClearHistoryDialog, self).__init__()
        self.parent = parent

        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.setWindowTitle(tr('clearHistory'))
        if os.path.exists(app_logo):
            self.setWindowIcon(QtGui.QIcon(app_logo))

        closeWindowAction = QtGui.QAction(self)
        closeWindowAction.setShortcuts(["Esc", "Ctrl+W", "Ctrl+Shift+Del"])
        closeWindowAction.triggered.connect(self.close)
        self.addAction(closeWindowAction)

        self.contents = QtGui.QWidget()
        self.layout = QtGui.QVBoxLayout()
        self.contents.setLayout(self.layout)
        self.setCentralWidget(self.contents)
        self.createClearHistoryToolBar()

    def show(self):
        self.setVisible(True)
        centerWidget(self)

    def display(self):
        self.show()
        self.activateWindow()

    def createClearHistoryToolBar(self):
        label = QtGui.QLabel(tr("clearHistoryDesc") + ":")
        self.layout.addWidget(label)
        self.selectRange = QtGui.QComboBox()
        self.selectRange.addItem(tr('lastMin'))
        self.selectRange.addItem(tr('last2Min'))
        self.selectRange.addItem(tr('last5Min'))
        self.selectRange.addItem(tr('last10Min'))
        self.selectRange.addItem(tr('last15Min'))
        self.selectRange.addItem(tr('last30Min'))
        self.selectRange.addItem(tr('lastHr'))
        self.selectRange.addItem(tr('last2Hr'))
        self.selectRange.addItem(tr('last4Hr'))
        self.selectRange.addItem(tr('last8Hr'))
        self.selectRange.addItem(tr('last24Hr'))
        self.selectRange.addItem(tr('today'))
        self.selectRange.addItem(tr('everything'))
        self.selectRange.addItem("----------------")
        self.selectRange.addItem(tr('cookies'))
        self.selectRange.addItem(tr('persistentStorage'))
        self.layout.addWidget(self.selectRange)
        self.toolBar = QtGui.QToolBar("")
        self.toolBar.setStyleSheet(blanktoolbarsheet)
        self.toolBar.setMovable(False)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.clearHistoryButton = QtGui.QPushButton(tr('clear'))
        self.clearHistoryButton.clicked.connect(self.clearHistory)
        self.toolBar.addWidget(self.clearHistoryButton)
        self.closeButton = QtGui.QPushButton(tr('close'))
        self.closeButton.clicked.connect(self.close)
        self.toolBar.addWidget(self.closeButton)

    def clearHistoryRange(self, timeRange=0.0):
        question = QtGui.QMessageBox.question(None, tr("warning"),
        tr("clearHistoryWarn"), QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if question == QtGui.QMessageBox.Yes:
            if sys.platform.startswith("linux"):
                os.system("shred -v \"%s\"" % (os.path.join(app_profile, "WebpageIcons.db")))
            try: remove2(os.path.join(app_profile, "WebpageIcons.db"))
            except:
                doNothing()
            saveTime = time.time()
            browserHistory.reload()
            newHistory = []
            for item in browserHistory.history:
                try:
                    difference = saveTime - int(item['time'])
                except:
                    print("Error!")
                else:
#                    print(int(round(difference*100)), int(timeRange*100))
                    if int(round(difference*100)) > int(timeRange*100):
                        newHistory.append(item)
            browserHistory.history = newHistory
            browserHistory.save()
            for win in app_windows:
                try:
                    win.reloadHistory()
                except:
                    doNothing()
            if library.advancedHistoryViewGUI.reload_:
                library.advancedHistoryViewGUI.reload_()

    def clearHistory(self):
        if self.selectRange.currentIndex() == 0:
            self.clearHistoryRange(60.0)
        elif self.selectRange.currentIndex() == 1:
            self.clearHistoryRange(120.0)
        elif self.selectRange.currentIndex() == 2:
            self.clearHistoryRange(300.0)
        elif self.selectRange.currentIndex() == 3:
            self.clearHistoryRange(600.0)
        elif self.selectRange.currentIndex() == 4:
            self.clearHistoryRange(900.0)
        elif self.selectRange.currentIndex() == 5:
            self.clearHistoryRange(1800.0)
        elif self.selectRange.currentIndex() == 6:
            self.clearHistoryRange(3600.0)
        elif self.selectRange.currentIndex() == 7:
            self.clearHistoryRange(7200.0)
        elif self.selectRange.currentIndex() == 8:
            self.clearHistoryRange(14400.0)
        elif self.selectRange.currentIndex() == 9:
            self.clearHistoryRange(28800.0)
        elif self.selectRange.currentIndex() == 10:
            self.clearHistoryRange(86400.0)
        elif self.selectRange.currentIndex() == 11:
            question = QtGui.QMessageBox.question(None, tr("warning"),
            tr("clearHistoryWarn"), QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if question == QtGui.QMessageBox.Yes:
                if sys.platform.startswith("linux"):
                    os.system("shred -v \"%s\"" % (os.path.join(app_profile, "WebpageIcons.db")))
                try: remove2(os.path.join(app_profile, "WebpageIcons.db"))
                except:
                    doNothing()
                saveMonth = time.strftime("%m")
                saveDay = time.strftime("%d")
                now = datetime.datetime.now()
                saveYear = "%d" % now.year
                newHistory = []
                for item in browserHistory.history:
                    if item['month'] != saveMonth and item['monthday'] != saveDay and item['year'] != saveYear:
                        newHistory.append(item)
                browserHistory.history = newHistory
                browserHistory.save()
                for win in app_windows:
                    try:
                        win.reloadHistory()
                    except:
                        doNothing()
                if library.advancedHistoryViewGUI.reload_:
                    library.advancedHistoryViewGUI.reload_()
        elif self.selectRange.currentIndex() == 12:
            question = QtGui.QMessageBox.question(None, tr("warning"),
            tr("clearHistoryWarn"), QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if question == QtGui.QMessageBox.Yes:
                if sys.platform.startswith("linux"):
                    os.system("shred -v \"%s\"" % (os.path.join(app_profile, "WebpageIcons.db")))
                try: remove2(os.path.join(app_profile, "WebpageIcons.db"))
                except:
                    doNothing()
                browserHistory.history = []
                browserHistory.save()
                for win in app_windows:
                    try:
                        win.reloadHistory()
                    except:
                        doNothing()
                if library.advancedHistoryViewGUI.reload_:
                    library.advancedHistoryViewGUI.reload_()
        elif self.selectRange.currentIndex() == 14:
            question = QtGui.QMessageBox.question(None, tr("warning"),
        tr("clearHistoryWarn"), QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if question == QtGui.QMessageBox.Yes:
                global app_kill_cookies
                app_kill_cookies = True
                notificationMessage(tr('clearCookiesMsg'))
        elif self.selectRange.currentIndex() == 15:
            question = QtGui.QMessageBox.question(None, tr("warning"),
        tr("clearHistoryWarn"), QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if question == QtGui.QMessageBox.Yes:
                d = os.path.join(app_profile, "LocalStorage")
                if sys.platform.startswith("linux"):
                    os.chdir(d)
                    os.system("find \"" + d + "\" -type f -exec shred {} \;")
                try: shutil.rmtree(d)
                except:
                    doNothing()

clearHistoryDialog = None

class AdvancedHistoryViewGUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(AdvancedHistoryViewGUI, self).__init__()
        self.parent = parent

        self.historyToolBar = QtGui.QToolBar("")
        if app_gnome_unity_integration:
            self.historyToolBar.setStyleSheet(windowtoolbarsheet)
        else:
            self.historyToolBar.setStyleSheet(blanktoolbarsheet)
        self.historyToolBar.setMovable(False)
        self.historyToolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.addToolBar(self.historyToolBar)

        clearHistoryAction = QtGui.QAction(QtGui.QIcon.fromTheme("edit-clear", QtGui.QIcon(ryouko_icon("clear.png"))), tr('clearHistoryHKey'), self)
        clearHistoryAction.setToolTip(tr('clearHistoryTT'))
        clearHistoryAction.setShortcut("Ctrl+Shift+Del")
        clearHistoryAction.triggered.connect(clearHistoryDialog.show)
        self.historyToolBar.addAction(clearHistoryAction)

        self.historyToolBar.addSeparator()

        searchLabel = QtGui.QLabel(tr("searchLabel") + ": ")
        self.historyToolBar.addWidget(searchLabel)

        self.searchBox = QtGui.QLineEdit()
        self.searchBox.textChanged.connect(self.searchHistoryFromBox)
        self.historyToolBar.addWidget(self.searchBox)

        findAction = QtGui.QAction(self)
        findAction.setShortcuts(["Ctrl+F", "Ctrl+K"])
        findAction.triggered.connect(self.searchBox.setFocus)
        findAction.triggered.connect(self.searchBox.selectAll)
        self.addAction(findAction)

        self.historyView = QtGui.QTreeWidget()
        self.historyView.setHeaderLabels([tr("title"), tr("count"), tr("weekday"), tr("date"), tr("time"), tr('url')])
        self.historyView.itemActivated.connect(self.loadHistoryItem)
        self.historyView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setCentralWidget(self.historyView)

        deleteHistoryItemAction = QtGui.QAction(tr("delete"), self)
        deleteHistoryItemAction.setShortcut("Del")
        deleteHistoryItemAction.triggered.connect(self.deleteHistoryItem)
        self.addAction(deleteHistoryItemAction)

        self.historyViewMenu = ContextMenu()
        self.historyView.customContextMenuRequested.connect(self.historyViewMenu.show2)
        self.historyViewMenu.addAction(deleteHistoryItemAction)

        otherTabAction = QtGui.QAction(self)
        otherTabAction.setShortcut("Ctrl+Shift+O")
        otherTabAction.triggered.connect(self.switchTabs)
        self.addAction(otherTabAction)

        closeWindowAction = QtGui.QAction(self)
        closeWindowAction.setShortcuts(["Ctrl+W", "Ctrl+Shift+H"])
        if self.parent:
            closeWindowAction.triggered.connect(self.parent.close)
        else:
            closeWindowAction.triggered.connect(self.close)
        self.addAction(closeWindowAction)

        browserHistory.historyChanged.connect(self.reload_)

        self.reload_()

    def deleteHistoryItem(self):
        if self.historyView.hasFocus():
            u = ""
            item = self.historyView.currentItem()
            if sys.version_info[0] <= 2:
                u = unicode(item.data(5, 0).toString())
            else:
                u = unicode(item.data(5, 0))
            browserHistory.removeByUrl(u)

    def searchHistoryFromBox(self):
        if self.searchBox.text() != "":
            self.searchHistory(self.searchBox.text())
        else:
            self.reload_()

    def searchHistory(self, string=""):
        string = unicode(string)
        if string != "":
            self.searchOn = True
            self.historyView.clear()
            history = []
            string = unicode(string)
            for item in browserHistory.history:
                add = False
                for subitem in item:
                    if string.lower() in unicode(item[subitem]).lower():
                        add = True
                        break
                if add == True:
                    history.append(item)
            for item in history:
                t = self.buildItem(item)
                self.historyView.addTopLevelItem(t)
        else:
            self.searchOn = False
            self.reloadHistory()

    def loadHistoryItem(self, item):
        u = ""
        if sys.version_info[0] <= 2:
            u = unicode(item.data(5, 0).toString())
        else:
            u = unicode(item.data(5, 0))
        if win.closed:
            win.show()
            win.closed = False
            win.resize(800, 480)
        win.newTab(None, u)

    def switchTabs(self):
        if self.parent.tabs:
            self.parent.tabs.setCurrentIndex(0)

    def clear(self):
        self.historyView.clear()

    def closeEvent(self, ev):
        try:
            self.parent.close()
        except:
            doNothing()
        return QtGui.QMainWindow.closeEvent(self, ev)
    
    def display(self):
        if self.parent.display and self.parent.tabs:
            self.parent.display()
            self.parent.tabs.setCurrentIndex(1)
            self.show()
            self.searchBox.setFocus()
            self.searchBox.selectAll()
            self.activateWindow()
        else:
            self.show()
            self.resize(640, 480)
            self.searchBox.setFocus()
            self.searchBox.selectAll()
            self.activateWindow()

    def buildItem(self, item):
        t = QtGui.QTreeWidgetItem(qstringlist([item['name'], str(item['count']), item['weekday'], str(item['year']) + "/" + str(item['month']) + "/" + str(item['monthday']), item['timestamp'], item['url']]))
        return t

    def reload_(self):
        self.historyView.clear()
        for item in browserHistory.history:
            t = self.buildItem(item)
            self.historyView.addTopLevelItem(t)

class Library(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Library, self).__init__()
        self.parent = parent
        if os.path.exists(app_logo):
            self.setWindowIcon(QtGui.QIcon(app_logo))

        self.setWindowTitle(tr('library'))
        self.tabs = MovableTabWidget(self, True)
        self.tabs.setDocumentMode(False)
        self.setCentralWidget(self.tabs)
        self.bookmarksManagerGUI = BookmarksManagerGUI(self)
        self.tabs.addTab(self.bookmarksManagerGUI, tr('bookmarks'))
        self.advancedHistoryViewGUI = AdvancedHistoryViewGUI(self)
        self.tabs.addTab(self.advancedHistoryViewGUI, tr('historyHKey'))
    def display(self):
        self.show()
        self.resize(640, 480)
        self.activateWindow()

library = ""

browserHistory = BrowserHistory(app_profile)

def showAboutPage(webView):
    webView.load(QtCore.QUrl("about:blank"))
    webView.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
        <html style='padding-bottom: 19.25pt;'>
        <head>
        <title>""" + tr('aboutRyouko') + """</title>
        <script type='text/javascript'>
        window.onload = function() {
            document.getElementById(\"userAgent\").innerHTML = navigator.userAgent;
        }
        </script>
        <style type="text/css">
        b, h1, h2 {
        font-family: sans-serif;
        }

        *:not(b):not(h1):not(h2) {
        font-family: monospace;
        }

        #toolbar {
        overflow-y: auto;
        height: 19.25pt;
        width: 100%;
        left: 0;
        bottom: 0;
        padding: 2px;
        padding-left: 0;
        padding-right:0;
        background: ThreeDFace;
        position: fixed;
        visibility: visible;
        z-index: 9001;
        border-top: 1px solid ThreeDShadow;
        }

        #toolbar * {
        font-family: sans-serif;
        font-size: 11pt;
        background: transparent;
        padding: 0;
        border: 0;
        color: ButtonText;
        text-decoration: none;
        -webkit-appearance: none;
        }

        #toolbar a:hover,
        #ryouko-toolbar input:hover {
        text-decoration: underline;
        }
        </style>
        </head>
        <body style='font-family: sans-serif; font-size: 11pt;'>
        <center>
        <div style=\"max-width: 640px;\">
        <a name='about'></a>
        <h1 style='margin-bottom: 0;'>""" + tr('aboutRyouko') + """</h1>
        <img src='file://%""" + ryouko_icon("about-logo.png") + """'></img><br/>
        <div style=\"text-align: left;\">
        <b>Ryouko:</b> """ + app_version + """<br/>
        <b>""" + tr('codename') + """:</b> \"""" + app_codename + """\"<br/>
        <b>OS:</b> """ + sys.platform + """<br/>
        <b>Qt:</b> """ + str(QtCore.qVersion()) + """<br/>
        <b>Python:</b> """ + str(sys.version_info[0])+"."+str(sys.version_info[1])+"."+str(sys.version_info[2]) + """<br/>
        <b>""" + tr("userAgent") + """:</b> <span id="userAgent">JavaScript must be enabled to display the user agent!</span><br/>
        <b>""" + tr("commandLine") + """:</b> """ + app_commandline + "<br/>\
        <b>" + tr('executablePath') + ":</b> " + os.path.realpath(__file__) + "<br/><center>\
        </center></div></div></center></body></html>")

class RAboutDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(RAboutDialog, self).__init__()
        self.parent = parent

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.tabs = QtGui.QTabWidget()
        self.tabs.setDocumentMode(True)
        self.setCentralWidget(self.tabs)

        if os.path.exists(app_logo):
            self.setWindowIcon(QtGui.QIcon(app_logo))
        self.setWindowTitle(tr('aboutRyouko'))

        self.closeWindowAction = QtGui.QAction(self)
        self.closeWindowAction.setShortcuts(["Ctrl+W", "Esc", "Enter"])
        self.closeWindowAction.triggered.connect(self.close)
        self.addAction(self.closeWindowAction)

        self.aboutPage = RAboutPageView()

        showAboutPage(self.aboutPage)

        self.tabs.addTab(self.aboutPage, tr("aboutRyoukoHKey"))

        self.licensePage = RAboutPageView()

        self.tabs.addTab(self.licensePage, tr("licenseHKey"))

    def updateUserAgent(self):
        try: settings_manager.settings['customUserAgent']
        except:
            doNothing()
        else:
            if settings_manager.settings['customUserAgent'].replace(" ", "") != "":
                self.aboutPage.page().userAgent = settings_manager.settings['customUserAgent']
            else:
                self.aboutPage.page().userAgent = app_default_useragent
        showAboutPage(self.aboutPage)

    def show(self):
        self.setVisible(True)
        centerWidget(self)
        h = self.licensePage.history()
        for item in h.backItems(h.count()):
            self.licensePage.back()
        h = os.path.join(app_lib, "LICENSE.html").replace("\\", "/")
        if sys.platform.startswith("win"):
            h = h.replace(h[0:2], "")
        self.licensePage.load(QtCore.QUrl("file://" + h))


aboutDialog = None

downloadManagerGUI = None

def downloadStarted():
    global downloadStartTimer
    notificationMessage(tr('downloadStarted'))
    downloadStartTimer.stop()

downloadStartTimer = QtCore.QTimer()
downloadStartTimer.timeout.connect(downloadStarted)

def downloadFinished():
    notificationMessage(tr('downloadFinished'))

notificationManager = None

def firstRun():
    if sys.platform.startswith("linux"):
        c = app_menubar_conf
    elif sys.platform.startswith("win"):
        c = app_tabs_on_top_conf
    else:
        return
    f = open(c, "w")
    f.write("")
    f.close()

def undoCloseWindow():
    try:
        global app_windows
        global app_closed_windows
        app_windows.append(app_closed_windows[len(app_closed_windows) - 1])
        del app_closed_windows[len(app_closed_windows) - 1]
    except:
        print("No more windows left!")
    else:
        if type(app_windows[len(app_windows) - 1]) == TabBrowser:
            if app_windows[len(app_windows) - 1].tabs.count() < 1:
                app_windows[len(app_windows) - 1].newTab()
                app_windows[len(app_windows) - 1].tabs.widget(app_windows[len(app_windows) - 1].tabs.currentIndex()).webView.buildNewTabPage()
        app_windows[len(app_windows) - 1].show()

class Browser(QtGui.QMainWindow):
    def __init__(self, parent=None, url=False, pb=False):
        super(Browser, self).__init__()
        self.parent = parent
        self.pb = pb
        self.findText = ""
        self.initUI(url)

    def swapWebView(self, webView):
        try: self.webView
        except: do_nothing()
        else:
            if self.webView != None:
                self.webView.deleteLater()
                del self.webView
        self.webView = webView
        if self.pb != True and self.webView.pb != True:
            self.webView.setCookieJar(app_cookiejar)
        self.webView.setSettingsManager(settings_manager)
        self.webView.saveCookies.connect(saveCookies)
        self.webView.downloadStarted.connect(self.downloadStarted)
        self.updateSettings()
        self.webView.setParent(self)
        self.mainLayout.addWidget(self.webView, 1, 0)
        self.webView.urlChanged.connect(browserHistory.reload)
        self.webView.titleChanged.connect(browserHistory.reload)
        if not self.pb and not self.webView.pb:
            self.webView.urlChanged.connect(browserHistory.append)
            self.webView.titleChanged.connect(browserHistory.updateTitles)
        self.webInspector.setPage(self.webView.page())
        self.webView.settings().setIconDatabasePath(qstring(app_profile))
        self.webView.page().linkHovered.connect(self.updateStatusMessage)
        self.webView.loadFinished.connect(self.progressBar.hide)
        self.webView.loadProgress.connect(self.progressBar.setValue)
        self.webView.loadProgress.connect(self.progressBar.show)
        self.webView.undoCloseWindowRequest.connect(undoCloseWindow)
        self.webView.page().alertToolBar.connect(self.addToolBarBreak)
        self.webView.page().alertToolBar.connect(self.addToolBar)
        bookmarksManager.userLinksChanged.connect(self.webView.setUserLinks)

    def downloadStarted(self):
        downloadStartTimer.start(250)

    def initUI(self, url):

        self.centralWidget = QtGui.QWidget()
        self.mainLayout = QtGui.QGridLayout()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

        self.webInspector = QtWebKit.QWebInspector(self)
        self.webInspectorDock = QtGui.QDockWidget(tr('webInspector'))
        self.webInspectorDock.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.webInspectorDock.setWidget(self.webInspector)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.webInspectorDock)
        self.webInspectorDock.hide()

        self.progressBar = QtGui.QProgressBar(self)

        webView = RWebView(self, settings_manager, self.pb, app_profile, searchManager, user_links, downloadManagerGUI)
        self.swapWebView(webView)

        self.mainLayout.setSpacing(0);
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        historySearchAction = QtGui.QAction(self)
        historySearchAction.triggered.connect(self.parent.focusHistorySearch)
        #historySearchAction.setShortcuts(["Alt+H"])
        self.addAction(historySearchAction)

        self.mainLayout.addWidget(self.webView, 1, 0)

        # Status bar
        self.statusBarBorder = QtGui.QWidget(self)
        self.statusBarBorder.setStyleSheet("""
        background: palette(shadow);
        """)
        self.statusBarBorder.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed))
        self.statusBarBorder.setMinimumHeight(1)
        self.mainLayout.addWidget(self.statusBarBorder, 2, 0)
        self.statusBar = QtGui.QFrame(self)
        self.statusBar.setStyleSheet("""
        QFrame {
        background: palette(window);
        border: 0;
        }
        """)
        self.mainLayout.addWidget(self.statusBar, 3, 0)
        self.statusBarLayout = QtGui.QHBoxLayout(self.statusBar)
        self.statusBarLayout.setContentsMargins(0,0,0,0)        
        self.statusBar.setLayout(self.statusBarLayout)
        self.statusMessage = QtGui.QLineEdit(self)
        self.statusMessage.setReadOnly(True)
        self.statusMessage.setFocusPolicy(QtCore.Qt.TabFocus)
        self.parent.historyCompletion.statusMessage.connect(self.statusMessage.setText)
        self.statusMessage.setStyleSheet("""
        QLineEdit {
        min-height: 1em;
        max-height: 1em;
        border: 0;
        background: transparent;
        }
        """)
        self.statusBarLayout.addWidget(self.statusMessage)
        self.progressBar.hide()
        self.progressBar.setStyleSheet("""
        min-height: 1em;
        max-height: 1em;
        min-width: 200px;
        max-width: 200px;
        """)
        self.statusBarLayout.addWidget(self.progressBar)
        self.zoomBar = QtGui.QWidget(self)
        self.zoomBar.setStyleSheet("""
        QToolButton, QPushButton {
        min-width: 16px;
        min-height: 1em;
        max-height: 1em;
        padding-left: 4px;
        padding-right: 4px;
        border-radius: 4px;
        border: 1px solid palette(shadow);
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(light), stop:1 palette(button));
        }

        QToolButton:pressed, QPushButton:pressed {
        border: 1px solid palette(shadow);
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,     stop:0 palette(shadow), stop:1 palette(button));
        }
        """)
        self.statusBarLayout.addWidget(self.zoomBar)
        self.zoomBarLayout = QtGui.QHBoxLayout(self.zoomBar)
        self.zoomBarLayout.setContentsMargins(0,2,0,0)
        self.zoomBarLayout.setSpacing(0)
        self.zoomBar.setLayout(self.zoomBarLayout)
        
        self.zoomOutButton = QtGui.QPushButton("-", self)
        self.zoomOutButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomSlider = QtGui.QSlider(self)
        self.zoomSlider.setStyleSheet("max-height: 1em;")
        self.zoomSlider.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomSlider.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed))
        self.zoomSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomSlider.setMinimum(1)
        self.zoomSlider.setMaximum(12)
        self.zoomSlider.setSliderPosition(4)
        self.zoomSlider.setTickInterval(1)
        self.zoomSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.zoomSlider.setMinimumWidth(128)
        self.zoomInButton = QtGui.QPushButton("+", self)
        self.zoomInButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.zoomLabel = QtGui.QLabel("1.00x")
        self.zoomLabel.setStyleSheet("margin-left: 2px;")
        self.zoomBarLayout.addWidget(self.zoomOutButton)
        self.zoomBarLayout.addWidget(self.zoomSlider)
        self.zoomBarLayout.addWidget(self.zoomInButton)
        self.zoomBarLayout.addWidget(self.zoomLabel)

        self.webView.statusBarMessage.connect(self.statusMessage.setText)

        self.zoomOutAction = QtGui.QAction(self)
        self.zoomOutAction.setShortcut("Ctrl+-")
        self.zoomOutAction.triggered.connect(self.zoomOut)
        self.addAction(self.zoomOutAction)
        self.zoomInAction = QtGui.QAction(self)
        self.zoomInAction.setShortcuts(["Ctrl+Shift+=", "Ctrl+="])
        self.zoomInAction.triggered.connect(self.zoomIn)
        self.addAction(self.zoomInAction)
        self.zoomResetAction = QtGui.QAction(self)
        self.zoomResetAction.setShortcut("Ctrl+0")
        self.zoomResetAction.triggered.connect(self.zoomReset)
        self.addAction(self.zoomResetAction)
        self.zoomOutButton.clicked.connect(self.zoomOut)
        self.zoomInButton.clicked.connect(self.zoomIn)
        self.zoomSlider.valueChanged.connect(self.zoom)
        self.webView.show()
        #self.enableDisableBF()

    def zoomIn(self):
        self.zoomSlider.setValue(self.zoomSlider.value() + 1)

    def zoomOut(self):
        self.zoomSlider.setValue(self.zoomSlider.value() - 1)

    def zoomReset(self):
        self.zoomSlider.setValue(4)
        
    def zoom(self, value):
        self.webView.setZoomFactor(float(value) * 0.25)
        self.zoomLabel.setText(qstring("%.2fx" % (float(value) * 0.25)))

    def updateStatusMessage(self, link="", title="", content=""):
        self.statusMessage.setText(qstring(link))

    def updateSettings(self):
        self.webView.updateSettings()

downloaderThread = DownloaderThread()

class ExtensionManagerGUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle(tr('pluginsBlacklist'))
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.initUI()
    def initUI(self):
        pluginsWindow = QtGui.QWidget()
        pluginsLayout = QtGui.QVBoxLayout()
        self.editPluginsButton = QtGui.QPushButton(tr('togglePlugin'))
        self.editPluginsButton.setFocusPolicy(QtCore.Qt.TabFocus)
        pluginsSubLayout = QtGui.QGridLayout()
        eplabel = QtGui.QLabel("<b>" + tr('enabledExtensions') + "</b>")
        dplabel = QtGui.QLabel("<b>" + tr('disabledExtensions') + "</b>")
        self.enabledExtensionsList = QtGui.QListWidget()
        self.disabledExtensionsList = QtGui.QListWidget()
        self.editPluginsButton.clicked.connect(self.enableDisableExtension)
        self.enabledExtensionsList.itemActivated.connect(self.enableDisableExtension)
        self.disabledExtensionsList.itemActivated.connect(self.enableDisableExtension)
        self.setCentralWidget(pluginsWindow)
        pluginsWindow.setLayout(pluginsLayout)
        pluginsLayout.addWidget(self.editPluginsButton)
        pluginsLayout.addLayout(pluginsSubLayout)
        pluginsSubLayout.addWidget(eplabel, 0, 0)
        pluginsSubLayout.addWidget(dplabel, 0, 1)
        pluginsSubLayout.addWidget(self.enabledExtensionsList, 1, 0)
        pluginsSubLayout.addWidget(self.disabledExtensionsList, 1, 1)
        self.loadExtensions()

    def loadExtensions(self):
        self.enabledExtensionsList.clear()
        self.disabledExtensionsList.clear()
        for e in app_extensions:
            if e["name"] in app_extensions_whitelist:
                self.enabledExtensionsList.addItem(e["name"])
            else:
                self.disabledExtensionsList.addItem(e["name"])
        self.disabledExtensionsList.sortItems(QtCore.Qt.AscendingOrder)
        self.enabledExtensionsList.sortItems(QtCore.Qt.AscendingOrder)

    def saveExtensions(self):
        l = ""
        for i in range(self.enabledExtensionsList.count()):
            l = l + self.enabledExtensionsList.item(i).text() + "\n"
        f = open(app_extensions_wlfile, "w")
        f.write(l)
        f.close()
                
    def enableDisableExtension(self):
        if self.enabledExtensionsList.hasFocus():
            plugin = self.enabledExtensionsList.currentItem().text()
            self.enabledExtensionsList.takeItem(self.enabledExtensionsList.row(self.enabledExtensionsList.currentItem()))
            self.disabledExtensionsList.addItem(plugin)
            self.disabledExtensionsList.sortItems(QtCore.Qt.AscendingOrder)
        elif self.disabledExtensionsList.hasFocus():
            plugin = self.disabledExtensionsList.currentItem().text()
            self.disabledExtensionsList.takeItem(self.disabledExtensionsList.row(self.disabledExtensionsList.currentItem()))
            self.enabledExtensionsList.addItem(plugin)
            self.enabledExtensionsList.sortItems(QtCore.Qt.AscendingOrder)

class CDialog(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(CDialog, self).__init__()
        self.parent = parent
        self.settings = {}
        self.setWindowFlags(QtCore.Qt.Dialog)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.initUI()
        self.filterListCount = 0
        self.resize(400, 400)

    def initUI(self):
        closeWindowAction = QtGui.QAction(self)
        closeWindowAction.setShortcuts(["Ctrl+W", "Ctrl+,", "Ctrl+Alt+P", "Esc"])
        closeWindowAction.triggered.connect(self.close)
        self.addAction(closeWindowAction)

        self.setWindowTitle(tr('preferences'))
        self.setWindowIcon(QtGui.QIcon(app_logo))
        self.tabs = QtGui.QTabWidget()
        self.setCentralWidget(self.tabs)

        # General settings page
        self.generalWidget = QtGui.QWidget()
        self.gLayout = QtGui.QVBoxLayout()
        self.generalWidget.setLayout(self.gLayout)
        self.tabs.addTab(self.generalWidget, tr('general'))

        # Content settings page
        self.cWidget = QtGui.QWidget()
        self.cLayout = QtGui.QVBoxLayout()
        self.cWidget.setLayout(self.cLayout)
        self.tabs.addTab(self.cWidget, tr('content'))

        # Data settings page
        self.aWidget = QtGui.QWidget()
        self.aLayout = QtGui.QVBoxLayout()
        self.aWidget.setLayout(self.aLayout)
        self.tabs.addTab(self.aWidget, tr('data'))

        # Browsing settings page
        self.pWidget = QtGui.QWidget()
        self.pLayout = QtGui.QVBoxLayout()
        self.pWidget.setLayout(self.pLayout)
        self.tabs.addTab(self.pWidget, tr('browsing'))

        # Advanced settings page
        self.nWidget = QtGui.QWidget()
        self.nLayout = QtGui.QVBoxLayout()
        self.nWidget.setLayout(self.nLayout)
        self.tabs.addTab(self.nWidget, tr('advanced'))

        homePagesLabel = QtGui.QLabel(tr('homePages') + ":")
        self.gLayout.addWidget(homePagesLabel)
        self.homePagesField = QtGui.QTextEdit()
        self.gLayout.addWidget(self.homePagesField)
        self.showBTBox = QtGui.QCheckBox(tr('bookmarksToolBarShow'))
        self.gLayout.addWidget(self.showBTBox)
        self.rTabsBox = QtGui.QCheckBox(tr('openTabsRelative'))
        self.gLayout.addWidget(self.rTabsBox)
        newWindowBox = QtGui.QLabel(tr('newWindowOption0'))
        self.gLayout.addWidget(newWindowBox)
        self.openTabsBox = QtGui.QCheckBox(tr('newWindowOption'))
        self.gLayout.addWidget(self.openTabsBox)
        uCloseLabel = QtGui.QLabel(tr('maxUndoCloseTab') + ":")
        self.gLayout.addWidget(uCloseLabel)
        self.undoCloseTabCount = QtGui.QLineEdit()
        self.undoCloseTabCount.setInputMask(qstring("#90"))
        self.gLayout.addWidget(self.undoCloseTabCount)
        uCloseNoteLabel = QtGui.QLabel(tr('maxUndoCloseTabNote'))
        self.gLayout.addWidget(uCloseNoteLabel)
        self.imagesBox = QtGui.QCheckBox(tr('autoLoadImages'))
        self.cLayout.addWidget(self.imagesBox)
        self.jsBox = QtGui.QCheckBox(tr('enableJS'))
        self.cLayout.addWidget(self.jsBox)
        self.javaBox = QtGui.QCheckBox(tr('enableJava'))
        self.cLayout.addWidget(self.javaBox)
        self.storageBox = QtGui.QCheckBox(tr('enableStorage'))
        self.cLayout.addWidget(self.storageBox)
        self.pluginsBox = QtGui.QCheckBox(tr('enablePlugins'))
        self.cLayout.addWidget(self.pluginsBox)

        self.gDocsBox = QtGui.QCheckBox(tr('enableGDViewer'))
        self.cLayout.addWidget(self.gDocsBox)

        self.zohoBox = QtGui.QCheckBox(tr('enableZohoViewer'))
        self.cLayout.addWidget(self.zohoBox)

        self.pbBox = QtGui.QCheckBox(tr('enablePB'))
        self.pLayout.addWidget(self.pbBox)

        self.aBBox = QtGui.QCheckBox(tr('enableAB'))
        self.aBBox.stateChanged.connect(self.tryDownload)
        downloaderThread.fileDownloaded.connect(self.applyFilters)
        self.cLayout.addWidget(self.aBBox)
        self.uALabel1 = QtGui.QLabel(tr("userAgent") + ":")
        self.cLayout.addWidget(self.uALabel1)
        self.uABox = QtGui.QComboBox()
        self.uABox.setMaximumWidth(400)
        self.uABox.addItem("Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)")
        self.uABox.addItem("Mozilla/4.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)")
        self.uABox.addItem("Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))")
        self.uABox.addItem("----------------")
        self.uABox.addItem("Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.35 (KHTML, like Gecko) Ubuntu/10.10 Chromium/13.0.764.0 Chrome/13.0.764.0 Safari/534.35")
        self.uABox.addItem("Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1")
        self.uABox.addItem("----------------")
        self.uABox.addItem("BlackBerry8100/4.2.0")
        self.uABox.addItem("----------------")
        self.uABox.addItem("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1")
        self.uABox.addItem("----------------")
        self.uABox.addItem("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10")
        self.uABox.addItem("Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3")
        self.uABox.addItem("Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10")
        self.uABox.setEditable(True)
        self.cLayout.addWidget(self.uABox)
        self.uALabel2 = QtGui.QLabel(tr("customUserAgent"))
        self.cLayout.addWidget(self.uALabel2)
        self.cLayout.addWidget(RExpander())
        self.editSearchButton = QtGui.QPushButton(tr('manageSearchEngines'), self)
        try: self.editSearchButton.clicked.connect(searchEditor.display)
        except:
            doNothing()
        self.gLayout.addWidget(self.editSearchButton)
        self.gLayout.addWidget(RExpander())

        # Proxy configuration stuff
        proxyBox = QtGui.QLabel(tr('proxyConfig'))
        self.pLayout.addWidget(proxyBox)
        self.proxySel = QtGui.QComboBox()
        self.proxySel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self.proxySel.addItem("None")
        self.proxySel.addItem('Socks5')
        self.proxySel.addItem('Http')
        sLabel = QtGui.QLabel(tr('type') + ":")
        l0 = RHBoxLayout()
        l0.addWidget(sLabel)
        l0.addWidget(self.proxySel)
        l0l = QtGui.QWidget()
        l0l.setLayout(l0)
        self.pLayout.addWidget(l0l)
        hLabel = QtGui.QLabel(tr('hostname') + ":")
        self.hostnameBox = QtGui.QLineEdit()
        l1 = RHBoxLayout()
        l1.addWidget(hLabel)
        l1.addWidget(self.hostnameBox)
        l1l = QtGui.QWidget()
        l1l.setLayout(l1)
        self.pLayout.addWidget(l1l)
        p1Label = QtGui.QLabel(tr('port') + ":")
        self.portBox = QtGui.QLineEdit()
        l2 = RHBoxLayout()
        l2.addWidget(p1Label)
        l2.addWidget(self.portBox)
        l2l = QtGui.QWidget()
        l2l.setLayout(l2)
        self.pLayout.addWidget(l2l)
        uLabel = QtGui.QLabel(tr('user') + ":")
        self.userBox = QtGui.QLineEdit()
        l3 = RHBoxLayout()
        l3.addWidget(uLabel)
        l3.addWidget(self.userBox)
        l3l = QtGui.QWidget()
        l3l.setLayout(l3)
        self.pLayout.addWidget(l3l)
        p2Label = QtGui.QLabel(tr('password') + ":")
        self.passwordBox = QtGui.QLineEdit()
        l4 = RHBoxLayout()
        l4.addWidget(p2Label)
        l4.addWidget(self.passwordBox)
        l4l = QtGui.QWidget()
        l4l.setLayout(l4)
        self.pLayout.addWidget(l4l)

        self.pLayout.addWidget(RExpander())

        # Data Management
        self.clearHistoryButton = QtGui.QPushButton(tr('clearHistory'))
        self.clearHistoryButton.clicked.connect(self.showHistoryDialog)
        self.aLayout.addWidget(self.clearHistoryButton)

        sProfileLabel = QtGui.QLabel(tr('selectProfile') + ":")
        self.profileList = QtGui.QListWidget()
        self.addProfileButton = QtGui.QPushButton(tr("addProfile"))
        self.addProfileButton.clicked.connect(self.addProfile)
        self.aLayout.addWidget(sProfileLabel)
        self.aLayout.addWidget(self.profileList)
        self.aLayout.addWidget(self.addProfileButton)

        cloudLabel = QtGui.QLabel(tr("cloudService"))
        cloudLabel.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        #cloudLabel2 = QtGui.QLabel(tr("cloudService2"))
        #cloudLabel2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self.cloudBox = QtGui.QComboBox()
        self.cloudBox.addItem("No")
        self.cloudBox.addItem("Dropbox")
        self.cloudBox.addItem("Ubuntu One")
        self.aLayout.addWidget(cloudLabel)
        self.aLayout.addWidget(self.cloudBox)
        #self.aLayout.addWidget(cloudLabel2)

        self.aLayout.addWidget(RExpander())

        self.cToolBar = QtGui.QToolBar()
        self.cToolBar.setStyleSheet(blanktoolbarsheet)
        self.cToolBar.setMovable(False)
        self.cToolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        applyAction = QtGui.QPushButton(tr('apply'))
        applyAction.setShortcut("Ctrl+S")
        applyAction.clicked.connect(self.saveSettings)
        closeAction = QtGui.QPushButton(tr('close'))
        closeAction.clicked.connect(self.hide)
        self.cToolBar.addWidget(applyAction)
        self.cToolBar.addWidget(closeAction)
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.cToolBar)

        self.extensionManager = ExtensionManagerGUI()
        self.nLayout.addWidget(self.extensionManager)

        self.s1Box = QtGui.QCheckBox(tr("allowInjectAddons"))
        self.nLayout.addWidget(self.s1Box)

        fr = os.path.join(app_profile, "firstrun.conf")
        if not os.path.exists(fr):
            firstRun()
            f = open(fr, "w")
            f.write("")
            f.close()
        self.loadSettings()
        self.saveSettings()
        self.loadSettings()

    def showHistoryDialog(self):
        clearHistoryDialog.display()    

    def checkOSWBox(self):
        if self.openTabsBox.isChecked():
            self.oswBox.setCheckState(QtCore.Qt.Unchecked)
    def checkOTabsBox(self):
        if self.oswBox.isChecked():
            self.openTabsBox.setCheckState(QtCore.Qt.Unchecked)
    def applyFilters(self):
        l = os.listdir(os.path.join(app_profile, "adblock"))
        if len(l) != self.filterListCount:
            settings_manager.applyFilters()
            self.filterListCount = len(l)
    def tryDownload(self):
        if self.aBBox.isChecked():
            l = os.listdir(os.path.join(app_profile, "adblock"))
            if len(l) == 0:
                downloaderThread.setUrl("https://easylist-downloads.adblockplus.org/easylist.txt")
                downloaderThread.setDestination(os.path.join(app_profile, "adblock", "easylist.txt"))
                downloaderThread.start()
    def loadSettings(self):
        if not os.path.exists(app_profile):
            os.makedirs(app_profile)
        settings_manager.loadSettings()
        self.settings = settings_manager.settings
        try: self.settings['homePages']
        except: self.homePagesField.setText("http://www.sourceforge.net/projects/ryouko")
        else: self.homePagesField.setText(qstring(self.settings['homePages']))
        try: self.settings['openInTabs']
        except: self.openTabsBox.setChecked(True)
        else: self.openTabsBox.setChecked(self.settings['openInTabs'])
        try: self.settings['loadImages']
        except: self.imagesBox.setChecked(True)
        else: self.imagesBox.setChecked(self.settings['loadImages'])
        try: self.settings['jsEnabled']
        except: self.jsBox.setChecked(True)
        else: self.jsBox.setChecked(self.settings['jsEnabled'])
        try: self.settings['relativeTabs']
        except: self.rTabsBox.setChecked(False)
        else: self.rTabsBox.setChecked(self.settings['relativeTabs'])
        try: self.settings['showBookmarksToolBar']
        except: self.showBTBox.setChecked(True)
        else: self.showBTBox.setChecked(self.settings['showBookmarksToolBar'])
        try: self.settings['javaEnabled']
        except: self.javaBox.setChecked(True)
        else: self.javaBox.setChecked(self.settings['javaEnabled'])
        try: self.settings['storageEnabled']
        except: self.storageBox.setChecked(True)
        else: self.storageBox.setChecked(self.settings['storageEnabled'])
        try: self.settings['pluginsEnabled']
        except:
            if sys.platform.startswith("linux"):
                self.pluginsBox.setChecked(False)
            else:
                self.pluginsBox.setChecked(True)
        else: self.pluginsBox.setChecked(self.settings['pluginsEnabled'])
        try: self.settings['privateBrowsing']
        except: self.pbBox.setChecked(False)
        else: self.pbBox.setChecked(self.settings['privateBrowsing'])
        try: self.settings['googleDocsViewerEnabled']
        except: self.gDocsBox.setChecked(True)
        else: self.gDocsBox.setChecked(self.settings['googleDocsViewerEnabled'])
        try: self.settings['zohoViewerEnabled']
        except: self.zohoBox.setChecked(True)
        else: self.zohoBox.setChecked(self.settings['zohoViewerEnabled'])
        try: self.settings['adBlock']
        except: self.aBBox.setChecked(False)
        else: self.aBBox.setChecked(self.settings['adBlock'])
        try: self.settings['customUserAgent']
        except: doNothing()
        else: self.uABox.setEditText(self.settings['customUserAgent'])
        try: self.settings['maxUndoCloseTab']
        except: self.undoCloseTabCount.setText("-1")
        else:
            try:
                self.undoCloseTabCount.setText(str(self.settings['maxUndoCloseTab']))
            except:
                self.undoCloseTabCount.setText("-1")
        try: self.settings['proxy']
        except: doNothing()
        else:
            pr = self.settings['proxy']
            if pr['type']:
                for i in range(self.proxySel.count()):
                    u = self.proxySel.itemText(i)
                    if pr['type'] == u:
                        self.proxySel.setCurrentIndex(i)
                        break
            if pr['hostname']:
                self.hostnameBox.setText(pr['hostname'])
            if pr['port']:
                self.portBox.setText(pr['port'])
            if pr['user']:
                self.userBox.setText(pr['user'])
            if pr['password']:
                self.portBox.setText(pr['password'])
        try: self.settings["allowInjectAddons"]
        except: do_nothing()
        else:
            self.s1Box.setChecked(self.settings["allowInjectAddons"])
        try: self.settings['cloudService']
        except:
            doNothing()
        else:
            for i in range(self.cloudBox.count()):
                u = self.cloudBox.itemText(i)
                if self.settings['cloudService'] == u:
                    self.cloudBox.setCurrentIndex(i)
                    break
        self.reloadProfiles()
        if os.path.exists(app_default_profile_file):
            f = open(app_default_profile_file)
            d = f.read().replace("\n", "")
            f.close()
            for i in range(self.profileList.count()):
                u = self.profileList.item(i).text()
                if unicode(u) == d:
                    self.profileList.setCurrentRow(i)
                    break
        else:
            for i in range(self.profileList.count()):
                u = self.profileList.item(i).text()
                if unicode(u) == app_default_profile_name:
                    self.profileList.setCurrentRow(i)
                    break
        try: self.profileList.currentItem()
        except: self.profileList.setCurrentRow(0)
        try:
            global app_windows
            for window in app_windows:
                try:
                    window.updateSettings()
                except:
                    doNothing()
        except:
            doNothing()
    def addProfile(self):
        pname = inputDialog(tr('query'), tr('enterProfileName'))
        if pname:
            try: os.makedirs(os.path.join(app_profile_folder, unicode(pname)))
            except:
                message(tr("error"), tr("profileError2"), "warn")
        self.reloadProfiles()
        for i in range(self.profileList.count()):
            u = self.profileList.item(i).text()
            if unicode(u) == app_default_profile_name:
                self.profileList.setCurrentRow(i)
                break
    def reloadProfiles(self):
        self.profileList.clear()
        l = os.listdir(app_profile_folder)
        for profile in l:
            if os.path.isdir(os.path.join(app_profile_folder, profile)):
                self.profileList.addItem(profile)
    def saveSettings(self):
        self.extensionManager.saveExtensions()
        if unicode(self.undoCloseTabCount.text()) == "":
            self.undoCloseTabCount.setText("-1")
        self.settings = {'homePages': unicode(self.homePagesField.toPlainText()), 'openInTabs' : self.openTabsBox.isChecked(), 'loadImages' : self.imagesBox.isChecked(), 'jsEnabled' : self.jsBox.isChecked(), 'showBookmarksToolBar': self.showBTBox.isChecked(), 'javaEnabled' : self.javaBox.isChecked(), 'storageEnabled' : self.storageBox.isChecked(), 'pluginsEnabled' : self.pluginsBox.isChecked(), 'privateBrowsing' : self.pbBox.isChecked(), 'backend' : 'qt', 'loginToDownload' : False, 'adBlock' : self.aBBox.isChecked(), 'proxy' : {"type" : unicode(self.proxySel.currentText()), "hostname" : unicode(self.hostnameBox.text()), "port" : unicode(self.portBox.text()), "user" : unicode(self.userBox.text()), "password" : unicode(self.passwordBox.text())}, "cloudService" : unicode(self.cloudBox.currentText()), 'maxUndoCloseTab' : int(unicode(self.undoCloseTabCount.text())), 'googleDocsViewerEnabled' : self.gDocsBox.isChecked(), 'zohoViewerEnabled': self.zohoBox.isChecked(), 'customUserAgent' : unicode(self.uABox.currentText()), "relativeTabs" : self.rTabsBox.isChecked(), "allowInjectAddons" : self.s1Box.isChecked()}
        f = open(app_default_profile_file, "w")
        if self.profileList.currentItem() == None:
            self.profileList.setCurrentRow(0)
            if self.profileList.currentItem() == None:
                self.profileList.addItem("default")
                self.profileList.setCurrentRow(0)
        f.write(unicode(self.profileList.currentItem().text()))
        f.close()
        settings_manager.settings = self.settings
        aboutDialog.updateUserAgent()
        settings_manager.setBackend('qt')
        settings_manager.saveSettings()
        global app_windows
        for window in app_windows:
            try:
                window.updateSettings()
            except:
                doNothing()
        

cDialog = None

class TabBrowser(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(TabBrowser, self).__init__()
        self.parent = parent
        if os.path.exists(app_logo):
            if not sys.platform.startswith("win"):
                self.setWindowIcon(QtGui.QIcon(app_logo))
            else:
                if os.path.exists(ryouko_icon('about-logo.png')):
                    self.setWindowIcon(QtGui.QIcon(ryouko_icon('about-logo.png')))
        self.tabCount = 0
        self.closed = False
        self.extensions = []
        self.closedTabsList = []
        self.tempHistory = []
        self.searchOn = False
        self.tempHistory = []

        if app_vista == True:
            self.setStyleSheet("""
            TabBrowser {
            background-image: url(\"""" + os.path.join(app_lib, "images", "win-toolbar.png").replace("\\", "/") + """\");
            background-color: #e1e6f6;
            background-repeat: repeat-x;
            }

            QMenuBar, QToolBar {
            border: 0;
            background: transparent;
            }
            """)

        self.urlCheckTimer = QtCore.QTimer()
        self.urlCheckTimer.timeout.connect(self.checkForURLs)
        self.urlCheckTimer.start(250)

        global app_windows
        app_windows.append(self)

        self.rebuildLock()

        self.mouseX = False
        self.mouseY = False

        self.initUI()

    def mousePressEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.showTabsContextMenu()
        else:
            self.mouseX = ev.globalX()
            self.origX = self.x()
            self.mouseY = ev.globalY()
            self.origY = self.y()

    def mouseMoveEvent(self, ev):
        if self.mouseX and self.mouseY and not self.isMaximized():
            self.move(self.origX + ev.globalX() - self.mouseX,
self.origY + ev.globalY() - self.mouseY)

    def mouseReleaseEvent(self, ev):
        self.mouseX = False
        self.mouseY = False

    def checkForURLs(self):
        if os.path.exists(app_instance2) and not self.closed:
            f = open(app_instance2)
            i2contents = f.readlines()
            f.close()
            remove2(app_instance2)
            for item in i2contents:
                item = item.replace("\n", "")
                if not "://" in item and not "about:" in item and not item == "":
                    item = "http://%s" % (item)
                if not item == "":
                    self.newTab(None, item)
        if self.closed:
            self.urlCheckTimer.stop()

    def rebuildLock(self):
        if not os.path.exists(app_lock):
            f = open(app_lock, "w")
            f.write("")
            f.close()

    def checkTempFiles(self):
        if app_kill_temp_files == True:
            shred_directory(os.path.join(app_profile, "temp"))

    def quit(self):
        confirmQuit()

    def closeEvent(self, ev):
        if len(app_windows) <= 1:
            ev.ignore()
            q = QtGui.QMessageBox.Yes
#        elif self.tabs.count() > 1:
#            q = QtGui.QMessageBox.question(None, tr("warning"),
#        tr("multiWindowWarn"), QtGui.QMessageBox.Yes | 
#        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        else:
           q = QtGui.QMessageBox.Yes 
        if q == QtGui.QMessageBox.Yes:
            global app_windows
            if self in app_windows:
                del app_windows[app_windows.index(self)]
                global app_closed_windows
                if len(app_closed_windows) >= 10:
                    del app_closed_windows[0]
                app_closed_windows.append(self)
            self.closed = True
            m = os.path.join(app_profile, "maximized.conf")
            if self.windowState() == QtCore.Qt.WindowMaximized:
                f = open(m, "w")
                f.write("")
                f.close()
            else:
                if os.path.exists(m):
                    remove2(m)
            return QtGui.QMainWindow.closeEvent(self, ev)
        else:
            ev.ignore()
            return

    def aboutRyoukoHKey(self):
        aboutDialog.show()

    def currentWebView(self):
        return self.tabs.widget(self.tabs.currentIndex()).webView

    def back(self):
        self.currentWebView().back()
        self.setIcon()

    def showBackList(self, dummy=None):
        self.backList.clear()
        h = self.currentWebView().history()
        for item in h.backItems(h.count()):
            self.backList.addItem(item.title())
        self.backList.show()
        self.backList.display(True, self.mainToolBar.widgetForAction(self.backAction).mapToGlobal(QtCore.QPoint(0,0)).x(), self.mainToolBar.widgetForAction(self.backAction).mapToGlobal(QtCore.QPoint(0,0)).y(),
        self.backList.width(),
        self.mainToolBar.widgetForAction(self.backAction).height())
        self.backList.list.setFocus()

    def backFromList(self, item):
        h = self.currentWebView().history()
        h.goToItem(h.backItems(h.count())[self.backList.row(item)])

    def forward(self):
        self.currentWebView().forward()
        self.setIcon()

    def showNextList(self, dummy=None):
        self.nextList.clear()
        h = self.currentWebView().history()
        for item in h.forwardItems(h.count()):
            self.nextList.addItem(item.title())
        self.nextList.show()
        self.nextList.display(True, self.mainToolBar.widgetForAction(self.nextAction).mapToGlobal(QtCore.QPoint(0,0)).x(), self.mainToolBar.widgetForAction(self.nextAction).mapToGlobal(QtCore.QPoint(0,0)).y(),
        self.nextList.width(),
        self.mainToolBar.widgetForAction(self.nextAction).height())
        self.nextList.list.setFocus()

    def nextFromList(self, item):
        h = self.currentWebView().history()
        h.goToItem(h.forwardItems(h.count())[self.nextList.row(item)])

    def reload(self):
        self.currentWebView().reload()
        self.setIcon()

    def stop(self):
        if self.findBar.hasFocus() and self.findToolBar.isVisible():
            self.findToolBar.hide()
        else:
            self.currentWebView().stop()
            self.urlBar2.setText(self.currentWebView().url().toString())

    def stopReload(self):
        if self.currentWebView().isLoading():
            self.stop()
        else:
            self.reload()

    def toggleStopReload(self):
        if self.currentWebView().isLoading():
            self.historyCompletionBox.hide()
            self.mainToolBar.widgetForAction(self.stopReloadAction).setToolTip(tr("stopBtnTT"))
            self.mainToolBar.widgetForAction(self.stopReloadAction).setIcon(QtGui.QIcon().fromTheme("process-stop", QtGui.QIcon(ryouko_icon("stop.png"))))
        else:
            self.mainToolBar.widgetForAction(self.stopReloadAction).setToolTip(tr("reloadBtnTT"))
            self.mainToolBar.widgetForAction(self.stopReloadAction).setIcon(QtGui.QIcon().fromTheme("view-refresh", QtGui.QIcon(ryouko_icon('reload.png'))))

    def find(self):
        if self.findToolBar.isVisible() and self.findBar.hasFocus():
            self.findToolBar.hide()
        else:
            self.currentWebView().parent2.addToolBarBreak()
            self.currentWebView().parent2.addToolBar(self.findToolBar)
            self.findToolBar.show()
            self.findBar.setFocus()
            self.findBar.selectAll()
        #self.currentWebView().findText)(self.findBar.text())

    def findNext(self):
        self.currentWebView().findNextText(unicode(self.findBar.text()))

    def findPrevious(self):
        self.currentWebView().findPreviousText(unicode(self.findBar.text()))

    def translate(self):
        self.currentWebView().translate()

    def showHistoryBox(self):
        if not self.historyCompletionBox.isVisible():
            if not self.urlBar.text() == self.currentWebView().url().toString():
                self.urlBar2.setFocus(True)
                self.historyCompletionBox.move(self.urlBar.mapToGlobal(QtCore.QPoint(0,0)).x(), self.urlBar.mapToGlobal(QtCore.QPoint(0,0)).y())
                self.historyCompletionBox.show()
                self.historyCompletionBox.resize(self.urlBar.width(), self.historyCompletionBox.height())

    def historyUp(self):
        if self.historyCompletion.currentRow() == 0 and self.historyCompletion.hasFocus():
            self.historyCompletion.setFocus(False)
            self.urlBar2.setFocus(True)
        elif not self.urlBar2.hasFocus():
            self.historyCompletion.setCurrentRow(self.historyCompletion.currentRow() - 1)
        else:
            self.urlBar2.setFocus(False)
            self.historyCompletion.setFocus(True)
            self.historyCompletion.setCurrentRow(self.historyCompletion.count() - 1)

    def historyDown(self):
        if self.urlBar2.hasFocus():
            self.historyCompletion.setCurrentRow(0)
            self.urlBar2.setFocus(False)
            self.historyCompletion.setFocus(True)
        elif not self.historyCompletion.currentRow() == self.historyCompletion.count() - 1:
            self.historyCompletion.setCurrentRow(self.historyCompletion.currentRow() + 1)
        else:
            self.historyCompletion.setFocus(False)
            self.urlBar2.setFocus(True)

    def enableDisableBF(self):
        try: self.currentWebView()
        except: do_nothing()
        else:
            if self.currentWebView().page().history().canGoBack():
                self.mainToolBar.widgetForAction(self.backAction).setEnabled(True)
            else:
                self.mainToolBar.widgetForAction(self.backAction).setEnabled(False)
            if self.currentWebView().page().history().canGoForward():
                self.mainToolBar.widgetForAction(self.nextAction).setEnabled(True)
            else:
                self.mainToolBar.widgetForAction(self.nextAction).setEnabled(False)

    def setIcon(self):
        try: i = self.currentWebView().icon()
        except: do_nothing()
        else:
            if i.actualSize(QtCore.QSize(16, 16)).width() < 1 or    self.currentWebView().url() == QtCore.QUrl("about:blank"):
                self.urlBar.setIcon(app_webview_default_icon)
                self.urlBar2.setIcon(app_webview_default_icon)
            else:
                self.urlBar.setIcon(i)
                self.urlBar2.setIcon(i)
            self.urlBar.repaint()
            self.urlBar2.repaint()

    def focusSearch(self):
        self.searchBar.setFocus()
        self.searchBar.selectAll()

    def searchWeb(self):
        urlBar = self.searchBar.text()
        url = QtCore.QUrl(searchManager.currentSearch.replace("%s", urlBar))
        self.currentWebView().load(url)

    def focusURLBar(self):
        if not self.historyCompletionBox.isVisible():
            self.urlBar.setFocus()
            self.urlBar.selectAll()
        else:
            self.urlBar2.setFocus()
            self.urlBar2.selectAll()

    def loadExtensionURL(self, url):
        self.currentWebView().load(url)

    def loadExtensionJS(self, js):
        self.currentWebView().page().mainFrame().evaluateJavaScript(js)

    def loadExtensionPython(self, pie):
        try: exec(unicode(pie))
        except: notificationMessage("extensionError")

    def updateWeb(self):
        urlBar = self.urlBar.text()
        urlBar = unicode(urlBar)
        header = ""
        search = False
        for key in searchManager.searchEngines:
            if urlBar.startswith("%s " % (searchManager.searchEngines[key]['keyword'])):
                search = searchManager.searchEngines[key]
                break
        if search:
            urlBar = urlBar.replace("%s " % (search['keyword']), "")
            urlBar = QtCore.QUrl(search['expression'].replace("%s", urlBar))
            self.currentWebView().load(urlBar)
        else:
            if not unicode(urlBar).startswith("about:") and not "://" in unicode(urlBar) and " " in unicode(urlBar):
                self.searchBar.setText(self.urlBar.text())
                self.searchWeb()
            else:
                if os.path.exists(unicode(urlBar)):
                    header = "file://"
                elif not unicode(urlBar).startswith("about:") and not "://" in unicode(urlBar) and not "javascript:" in unicode(urlBar):
                    header = "http://"
                if unicode(urlBar) == "about:" or unicode(urlBar) == "about:version":
                    showAboutPage(self.currentWebView())
                else:
                    url = qstring(header + unicode(urlBar))
                    url = QtCore.QUrl(url)
                    self.currentWebView().load(url)

    def searchHistoryFromPopup(self, string):
        string = unicode(string)
        if string != "" and string != unicode(self.currentWebView().url().toString()) and string != "about:version":
            self.searchOn = True
            self.historyCompletion.clear()
            history = []
            string = unicode(string)
            for item in browserHistory.history:
                add = False
                for subitem in item:
                    if string.lower() in unicode(item[subitem]).lower():
                        add = True
                        break
                if add == True:
                    history.append(item)
                    self.historyCompletion.addItem(item['name'])
            self.tempHistory = history
        else:
            self.historyCompletionBox.hide()

    def updateText(self):        
        url = self.currentWebView().url()
        texturl = url.toString()
        #self.setText(texturl)

    def rSyncText(self):
        if self.urlBar2.text() != self.urlBar.text():
            self.urlBar2.setText(self.urlBar.text())

    def syncText(self):
        self.urlBar.setText(self.urlBar2.text())

    def openHistoryItemFromPopup(self, item):
        self.currentWebView().load(QtCore.QUrl(self.tempHistory[self.historyCompletion.row(item)]['url']))
        self.historyCompletionBox.hide()
        self.currentWebView().show()                    

    def bookmarkPage(self):
        name = inputDialog(tr('addBookmark'), tr('enterName'), unicode(self.currentWebView().title()))
        if name and name != "":
            bookmarksManager.add(unicode(self.currentWebView().url().toString()), unicode(name))

    def showClosedTabsMenu(self):
        self.closedTabsMenu.display(True, self.mainToolBar.widgetForAction(self.closedTabsMenuButton).mapToGlobal(QtCore.QPoint(0,0)).x(), self.mainToolBar.widgetForAction(self.closedTabsMenuButton).mapToGlobal(QtCore.QPoint(0,0)).y(),
        self.mainToolBar.widgetForAction(self.closedTabsMenuButton).width(),
        self.mainToolBar.widgetForAction(self.closedTabsMenuButton).height())
        self.closedTabsMenu.list.setFocus()

    def editSearch(self):
        searchEditor.display(True, self.searchMenuButton.mapToGlobal(QtCore.QPoint(0,0)).x(), self.searchMenuButton.mapToGlobal(QtCore.QPoint(0,0)).y(), self.searchMenuButton.width(), self.searchMenuButton.height())

    def initUI(self):

        # Quit action
        quitAction = QtGui.QAction(tr("quit"), self)
        quitAction.setShortcut("Ctrl+Shift+Q")
        quitAction.triggered.connect(self.quit)
        self.addAction(quitAction)

        # History sidebar
        self.historyDock = QtGui.QDockWidget(tr('history'))
#        if app_use_ambiance:
#            self.historyDock.setStyleSheet(dw_stylesheet)
        self.historyDock.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.historyDockWindow = QtGui.QMainWindow()
        self.historyToolBar = QtGui.QToolBar("History Toolbar")
        self.historyToolBar.setStyleSheet(blanktoolbarsheet)
        self.historyToolBar.setMovable(False)
        self.historyList = QtGui.QListWidget()
        self.historyList.itemActivated.connect(self.openHistoryItem)
        deleteHistoryItemAction = QtGui.QAction(self)
        deleteHistoryItemAction.setShortcut("Del")
        deleteHistoryItemAction.triggered.connect(self.deleteHistoryItem)
        self.addAction(deleteHistoryItemAction)
        self.searchHistoryField = QtGui.QLineEdit()
        self.searchHistoryField.textChanged.connect(self.searchHistory)
        clearHistoryAction = QtGui.QAction(QtGui.QIcon.fromTheme("edit-clear", QtGui.QIcon(ryouko_icon("clear.png"))), tr('clearHistoryHKey'), self)
        clearHistoryAction.setToolTip(tr('clearHistoryTT'))
        clearHistoryAction.setShortcut("Ctrl+Shift+Del")
        clearHistoryAction.triggered.connect(self.showClearHistoryDialog)
        self.addAction(clearHistoryAction)
        self.historyToolBar.addWidget(self.searchHistoryField)
        self.historyToolBar.addAction(clearHistoryAction)
        self.historyDockWindow.addToolBar(self.historyToolBar)
        self.historyDockWindow.setCentralWidget(self.historyList)
        self.historyDock.setWidget(self.historyDockWindow)
        browserHistory.historyChanged.connect(self.reloadHistory)
        self.reloadHistory()
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.historyDock)
        self.historyDock.hide()

        self.closedTabsMenu = ListMenu()
        self.closedTabsMenu.itemClicked.connect(self.undoCloseTab)
        self.closedTabsMenu.itemActivated.connect(self.undoCloseTab)
        
        manageBookmarksAction = QtGui.QAction(QtGui.QIcon(ryouko_icon("heart.png")), tr('viewBookmarks'), self)
        manageBookmarksAction.setShortcut("Ctrl+Shift+O")
        manageBookmarksAction.triggered.connect(library.bookmarksManagerGUI.display)
        self.addAction(manageBookmarksAction)

        viewNotificationsAction = QtGui.QAction(QtGui.QIcon().fromTheme("dialog-warning", QtGui.QIcon(ryouko_icon("alert.png"))), tr('viewNotifications'), self)
        viewNotificationsAction.setShortcut("Ctrl+Alt+N")
        viewNotificationsAction.triggered.connect(notificationManager.show)
        self.addAction(viewNotificationsAction)

        self.mainToolBar = QtGui.QToolBar("")
        self.mainToolBar.setMovable(False)
        self.mainToolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.addToolBar(self.mainToolBar)

        self.historyCompletionBox = QtGui.QWidget()

        self.downArrowAction = QtGui.QAction(self)
        self.downArrowAction.setShortcut("Down")
        self.downArrowAction.triggered.connect(self.historyDown)

        self.historyCompletionBox.addAction(self.downArrowAction)

        self.upArrowAction = QtGui.QAction(self)
        self.upArrowAction.setShortcut("Up")
        self.upArrowAction.triggered.connect(self.historyUp)

        self.historyCompletionBox.addAction(self.upArrowAction)

        self.historyCompletionBoxLayout = QtGui.QVBoxLayout()
        self.historyCompletionBoxLayout.setContentsMargins(0,0,0,0)
        self.historyCompletionBoxLayout.setSpacing(0)
        self.historyCompletionBox.setLayout(self.historyCompletionBoxLayout)
        self.historyCompletionBox.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Popup)
        self.historyCompletion = HistoryCompletionList(self)
        self.historyCompletion.setWordWrap(True)
        self.historyCompletion.itemActivated.connect(self.openHistoryItemFromPopup)       

        self.backAction = QtGui.QAction(self)
        self.backAction.setText(tr("back"))
        self.backAction.setToolTip(tr("backBtnTT"))
        self.backAction.triggered.connect(self.back)
        self.backAction.setIcon(QtGui.QIcon().fromTheme("go-previous", QtGui.QIcon(ryouko_icon('back.png'))))
        self.mainToolBar.addAction(self.backAction)
        self.mainToolBar.widgetForAction(self.backAction).setFocusPolicy(QtCore.Qt.TabFocus)
        self.mainToolBar.widgetForAction(self.backAction).setPopupMode(QtGui.QToolButton.MenuButtonPopup)

        self.backList = ListMenu()
        self.backList.itemClicked.connect(self.backFromList)
        self.backList.itemActivated.connect(self.backFromList)

        self.backListMenu = MenuPopupWindowMenu(self.showBackList)
        self.mainToolBar.widgetForAction(self.backAction).setMenu(self.backListMenu)

        self.nextAction = QtGui.QAction(self)
        self.nextAction.setToolTip(tr("nextBtnTT"))
        self.nextAction.triggered.connect(self.forward)
        self.nextAction.setText("")
        self.nextAction.setIcon(QtGui.QIcon().fromTheme("go-next", QtGui.QIcon(ryouko_icon('next.png'))))
        self.mainToolBar.addAction(self.nextAction)
        self.mainToolBar.widgetForAction(self.nextAction).setFocusPolicy(QtCore.Qt.TabFocus)
        self.mainToolBar.widgetForAction(self.nextAction).setPopupMode(QtGui.QToolButton.MenuButtonPopup)

        self.nextList = ListMenu()
        self.nextList.itemClicked.connect(self.nextFromList)
        self.nextList.itemActivated.connect(self.nextFromList)

        self.nextListMenu = MenuPopupWindowMenu(self.showNextList)
        self.mainToolBar.widgetForAction(self.nextAction).setMenu(self.nextListMenu)

        self.reloadAction = QtGui.QAction(self)
        self.reloadAction.triggered.connect(self.reload)
        self.addAction(self.reloadAction)

        self.stopAction = QtGui.QAction(self)
        self.stopAction.setShortcuts(["Esc"])
        self.stopAction.triggered.connect(self.stop)
        self.addAction(self.stopAction)

        self.stopReloadAction = QtGui.QAction(self)
        self.stopReloadAction.triggered.connect(self.stopReload)
        self.stopReloadAction.setText("")
        self.stopReloadAction.setToolTip(tr("reloadBtnTT"))
        self.stopReloadAction.setIcon(QtGui.QIcon().fromTheme("view-reload", QtGui.QIcon(ryouko_icon('reload.png'))))
        self.mainToolBar.addAction(self.stopReloadAction)
        self.addAction(self.stopReloadAction)
        self.mainToolBar.widgetForAction(self.stopReloadAction).setFocusPolicy(QtCore.Qt.TabFocus)

        self.findToolBar = QtGui.QToolBar()
        if sys.platform.startswith("win"):
            self.findToolBar.setStyleSheet("QToolBar{background-color:palette(window);border:0;border-bottom:1px solid palette(shadow);}")
        self.findToolBar.setMovable(False)
        self.findToolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.findToolBar)
        self.findToolBar.hide()

        self.findAction = QtGui.QAction(self)
        self.findAction.triggered.connect(self.find)
        self.findAction.setShortcut("Ctrl+F")
        self.findAction.setText(tr("findHKey"))
        self.findAction.setToolTip(tr("findBtnTT"))
        self.findAction.setIcon(QtGui.QIcon().fromTheme("edit-find", QtGui.QIcon(ryouko_icon('find.png'))))
        self.mainToolBar.addAction(self.findAction)
        self.mainToolBar.widgetForAction(self.findAction).setFocusPolicy(QtCore.Qt.TabFocus)

        self.findNextAction = QtGui.QAction(self)
        self.findNextAction.triggered.connect(self.findNext)
        self.findNextAction.setShortcuts(["Ctrl+G", "F3"])
        self.findNextAction.setText(tr("findNextHKey"))
        self.findNextAction.setToolTip(tr("findNextBtnTT"))
        self.findNextAction.setIcon(QtGui.QIcon().fromTheme("media-seek-forward", QtGui.QIcon(ryouko_icon('find-next.png'))))

        self.findPreviousAction = QtGui.QAction(self)
        self.findPreviousAction.triggered.connect(self.findPrevious)
        self.findPreviousAction.setShortcut("Ctrl+Shift+G")
        self.findPreviousAction.setText(tr("findPreviousHKey"))
        self.findPreviousAction.setToolTip(tr("findPreviousBtnTT"))
        self.findPreviousAction.setIcon(QtGui.QIcon().fromTheme("media-seek-backward", QtGui.QIcon(ryouko_icon('find-previous.png'))))

        self.findBar = QtGui.QLineEdit()
        self.findBar.returnPressed.connect(self.findNext)

        self.findToolBar.addWidget(self.findBar)
        self.findToolBar.addAction(self.findPreviousAction)
        self.findToolBar.addAction(self.findNextAction)

        self.closeFindToolBarAction = QtGui.QAction(self)
        self.closeFindToolBarAction.triggered.connect(self.findToolBar.hide)
        self.closeFindToolBarAction.setIcon(QtGui.QIcon().fromTheme("window-close", QtGui.QIcon(ryouko_icon("close.png"))))

        self.findToolBar.addAction(self.closeFindToolBarAction)

        self.addAction(self.findPreviousAction)
        self.addAction(self.findNextAction)

        self.translateAction = QtGui.QAction(self)
        self.translateAction.triggered.connect(self.translate)
        self.translateAction.setShortcut("Alt+Shift+T")
        self.translateAction.setIcon(QtGui.QIcon().fromTheme("preferences-desktop-locale", QtGui.QIcon(ryouko_icon('translate.png'))))
        self.translateAction.setToolTip(tr("translateBtnTT"))
        self.mainToolBar.addAction(self.translateAction)
        self.addAction(self.translateAction)
        self.mainToolBar.widgetForAction(self.translateAction).setFocusPolicy(QtCore.Qt.TabFocus)

        self.splitter = QtGui.QSplitter()
        self.splitter.setChildrenCollapsible(False)
        self.mainToolBar.addWidget(self.splitter)

        self.urlToolBar = QtGui.QToolBar()
        self.urlToolBar.setStyleSheet(blanktoolbarsheet + " QToolBar{padding:0;margin:0;}")
        self.splitter.addWidget(self.urlToolBar)

        self.searchToolBar = QtGui.QToolBar()
        self.searchToolBar.setStyleSheet(blanktoolbarsheet + " QToolBar{padding:0;margin:0;}")
        self.splitter.addWidget(self.searchToolBar)

        self.urlBar = RUrlBar(QtGui.QIcon(), self)
        self.urlToolBar.addWidget(self.urlBar)

        self.urlBar2 = RUrlBar()
        self.urlBar2.setIcon(QtGui.QIcon())
        self.historyCompletionBoxLayout.addWidget(self.urlBar2)
        self.historyCompletionBoxLayout.addWidget(self.historyCompletion)

        self.urlBar.setToolTip(tr("locationBarTT"))
        self.urlBar.textChanged.connect(self.rSyncText)
        self.urlBar.textChanged.connect(self.showHistoryBox)

        self.urlBar2.textChanged.connect(self.syncText)
        self.urlBar2.returnPressed.connect(self.updateWeb)
        self.urlBar.returnPressed.connect(self.updateWeb)
        self.urlBar2.textChanged.connect(self.searchHistoryFromPopup)
        searchAction = QtGui.QAction(self)
        searchAction.setShortcut("Ctrl+K")
        searchAction.triggered.connect(self.focusSearch)
        self.addAction(searchAction)
        self.historyCompletionBox.addAction(searchAction)

        self.addBookmarkButton = QtGui.QToolButton(self)
        self.addBookmarkButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.addBookmarkButton.clicked.connect(self.bookmarkPage)
        self.addBookmarkButton.setText("")
        self.addBookmarkButton.setToolTip(tr("addBookmarkTT"))
        self.addBookmarkButton.setShortcut("Ctrl+D")
        self.addBookmarkButton.setIcon(QtGui.QIcon().fromTheme("emblem-favorite", QtGui.QIcon(ryouko_icon('heart.png'))))
        self.addBookmarkButton.setIconSize(QtCore.QSize(16, 16))
        self.urlToolBar.addWidget(self.addBookmarkButton)

        self.searchBar = RSearchBar(self)
        self.searchBar.setStyleSheet("QLineEdit{min-width:200px;}")
        searchEditor.searchChanged.connect(self.searchBar.setLabel)
        self.searchBar.returnPressed.connect(self.searchWeb)
        self.searchToolBar.addWidget(self.searchBar)
        self.splitter.setSizes([1920, 200])
        searchEditor.reload()

        self.searchMenuButtonContainer = QtGui.QWidget(self)
        self.searchMenuButtonContainerLayout = QtGui.QVBoxLayout(self.searchMenuButtonContainer)
        self.searchMenuButtonContainerLayout.setSpacing(0);
        self.searchMenuButtonContainerLayout.setContentsMargins(0, 0, 0, 0)
        self.searchMenuButtonContainer.setLayout(self.searchMenuButtonContainerLayout)
        self.searchMenuButton = QtGui.QToolButton(self)
        self.searchMenuButton.setStyleSheet("QToolButton { max-width: 16px; }")
        self.searchMenuButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.searchMenuButton.setToolTip(tr("searchBtnTT"))
        self.searchMenuButton.clicked.connect(self.editSearch)
        self.searchMenuButton.setShortcut("Ctrl+Shift+K")
        self.searchMenuButton.setToolTip(tr("editSearchTT"))
        self.searchMenuButton.setArrowType(QtCore.Qt.DownArrow)
        self.searchMenuButtonContainerLayout.addWidget(self.searchMenuButton)
        self.mainToolBar.addWidget(self.searchMenuButtonContainer)

        self.focusURLBarAction = QtGui.QAction(self)
        self.historyCompletionBox.addAction(self.focusURLBarAction)
        self.focusURLBarAction.setShortcuts(["Alt+D", "Ctrl+L"])
        self.focusURLBarAction.triggered.connect(self.focusURLBar)
        self.addAction(self.focusURLBarAction)

        self.closedTabsMenuButton = QtGui.QAction(self)
        self.closedTabsMenuButton.setText(tr("closedTabs"))
        self.closedTabsMenuButton.setIcon(QtGui.QIcon.fromTheme("user-trash", QtGui.QIcon(ryouko_icon("trash.png"))))
        self.closedTabsMenuButton.triggered.connect(self.showClosedTabsMenu)

        self.mainMenuButton = QtGui.QAction(self)
        self.mainMenuButton.setText(tr("menu"))
        self.mainMenuButton.setIcon(QtGui.QIcon.fromTheme("document-properties", QtGui.QIcon(ryouko_icon("preferences.png"))))
        self.mainMenuButton.setShortcuts(["Alt+M"])
        self.mainMenuButton.triggered.connect(self.showCornerWidgetsMenu)
        self.mainMenu = QtGui.QMenu(self)
        self.mainMenu.setTitle(tr('menu'))

        self.mainToolBar.addAction(self.closedTabsMenuButton)
        self.mainToolBar.widgetForAction(self.closedTabsMenuButton).setFocusPolicy(QtCore.Qt.TabFocus)

        self.extensionToolBar = QtGui.QToolBar()
        self.extensionToolBar.setIconSize(QtCore.QSize(16, 16))
        self.extensionToolBar.setMovable(False)
        self.extensionToolBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.extensionToolBar.setStyleSheet("QToolBar{border:0;margin: 0;padding:0;background:palette(window);}")
        
        count = 0
        for e in app_extensions:
            try: e["name"]
            except: print("Error! Extension has no name!")
            else:
                if e["name"] in app_extensions_whitelist:
                    count = count + 1
                    try:
                        exec("ext" + str(count) + " = RExtensionButton(self)")
                        exec("ext" + str(count) + ".setText(e['name'])")
                        exec("ext" + str(count) + ".setToolTip(e['name'])")
                    except: do_nothing()
                    else:
                        nobutton = False
                        try: e["icon"]
                        except: do_nothing()
                        else:
                            if e["folder"] != None:
                                icon = os.path.join(unicode(e["folder"]), unicode(e["icon"]))
                                if os.path.exists(icon) and not os.path.isdir(icon):
                                    try: exec("ext" + str(count) + ".setIcon(QtGui.QIcon(icon))")
                                    except: do_nothing()
                        try: e["type"]
                        except: do_nothing()
                        else:
                            try: exec("ext" + str(count) + ".setType(unicode(e['type']))")
                            except: do_nothing()
                            else:
                                if unicode(e["type"]).lower() == "python-inject":
                                    nobutton = True
                        try: e["js"]
                        except: do_nothing()
                        else:
                            try: exec("ext" + str(count) + ".setJavaScript(unicode(e['js']))")
                            except: do_nothing()
                        try: e["javascript"]
                        except: do_nothing()
                        else:
                            try: exec("ext" + str(count) + ".setJavaScript(unicode(e['javascript']))")
                            except: do_nothing()
                        try: e["python"]
                        except: do_nothing()
                        else:
                            try: exec("ext" + str(count) + ".setPython(unicode(e['python']))")
                            except: do_nothing()
                        try: e["url"]
                        except: do_nothing()
                        else:
                            try: exec("ext" + str(count) + ".setLink(unicode(e['url']))")
                            except: do_nothing()
                        try: exec("ext" + str(count) + ".linkTriggered.connect(self.loadExtensionURL)")
                        except: do_nothing()
                        try: exec("ext" + str(count) + ".javaScriptTriggered.connect(self.loadExtensionJS)")
                        except: do_nothing()
                        try: exec("ext" + str(count) + ".pythonTriggered.connect(self.loadExtensionPython)")
                        except: do_nothing()
                        if nobutton == False:
                            try: exec("self.extensionToolBar.addWidget(ext" + str(count) + ")")
                            except: do_nothing()
                        else:
                            try: exec("ext" + str(count) + ".deleteLater()")
                            except: do_nothing()
                            try: cDialog.settings["allowInjectAddons"]
                            except: notificationMessage(tr("extensionWarn"))
                            else:
                                if cDialog.settings["allowInjectAddons"] != True:
                                    notificationMessage(tr("extensionWarn"))
                                else:
                                    exec(e["python"])

        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.extensionToolBar)
        if count == 0:
            self.extensionToolBar.hide()

        self.mainToolBar.addAction(self.mainMenuButton)
        self.mainToolBar.widgetForAction(self.mainMenuButton).setFocusPolicy(QtCore.Qt.TabFocus)
        self.mainToolBar.widgetForAction(self.mainMenuButton).setPopupMode(QtGui.QToolButton.InstantPopup)
        self.mainToolBar.widgetForAction(self.mainMenuButton).setMenu(self.mainMenu)

        # Tabs
        self.tabs = MovableTabWidget(self)
        self.tabs.currentChanged.connect(self.hideInspectors)
        self.tabs.currentChanged.connect(self.enableDisableBF)
        self.tabs.currentChanged.connect(self.setIcon)
        self.tabs.currentChanged.connect(self.correctURLText)
        self.tabs.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tabs.setMovable(True)
        self.nextTabAction = QtGui.QAction(self)
        self.nextTabAction.triggered.connect(self.nextTab)
        self.nextTabAction.setShortcut("Ctrl+Tab")
        self.addAction(self.nextTabAction)
        self.previousTabAction = QtGui.QAction(self)
        self.previousTabAction.triggered.connect(self.previousTab)
        self.previousTabAction.setShortcut("Ctrl+Shift+Tab")
        self.addAction(self.previousTabAction)
        self.tabs.setTabsClosable(True)
        self.tabs.currentChanged.connect(self.updateTitles)
        self.tabs.tabCloseRequested.connect(self.closeTab)

        self.fullScreenAction = QtGui.QAction(QtGui.QIcon().fromTheme("view-fullscreen", QtGui.QIcon(ryouko_icon("fullscreen.png"))), tr("toggleFullscreen"), self)
        self.fullScreenAction.setShortcut("F11")
        self.fullScreenAction.triggered.connect(self.toggleFullScreen)
        self.addAction(self.fullScreenAction)

        self.rMaxAction = QtGui.QAction(self)
        self.rMaxAction.setShortcut("Alt+F10")
        self.rMaxAction.triggered.connect(self.rMax)
        self.addAction(self.rMaxAction)

        # "Toolbar" for top right corner
        self.cornerWidgets = QtGui.QWidget()
        self.cornerWidgets.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        #self.cornerWidgets.setStyleSheet(cornerWidgetsSheet)
        self.tabs.setCornerWidget(self.cornerWidgets,QtCore.Qt.TopRightCorner)
        self.cornerWidgetsLayout = QtGui.QHBoxLayout()
        self.cornerWidgetsLayout.setContentsMargins(0,0,0,0)
        self.cornerWidgetsLayout.setSpacing(0)
        self.cornerWidgets.setLayout(self.cornerWidgetsLayout)
        self.cornerWidgetsToolBar = QtGui.QToolBar()
        self.cornerWidgetsToolBar.setStyleSheet("QToolBar { border: 0; background: transparent; padding: 0; margin: 0;}")# icon-size: 16px; }")
        self.cornerWidgetsLayout.addWidget(self.cornerWidgetsToolBar)

        """self.showCornerWidgetsMenuAction = QtGui.QAction(self)
        self.showCornerWidgetsMenuAction.setShortcut("Alt+M")
        self.showCornerWidgetsMenuAction.setToolTip(tr("cornerWidgetsMenuTT"))
        self.showCornerWidgetsMenuAction.triggered.connect(self.showCornerWidgetsMenu)"""

        closeTabForeverAction = QtGui.QAction(tr('closeTabForever'), self)
        closeTabForeverAction.setShortcut("Ctrl+Shift+W")
        self.addAction(closeTabForeverAction)
        closeTabForeverAction.triggered.connect(self.permanentCloseTab)

        # New tab button
        newTabAction = QtGui.QAction(QtGui.QIcon().fromTheme("tab-new", QtGui.QIcon(ryouko_icon('newtab.png'))), tr('newTabBtn'), self)
        newTabAction.setToolTip(tr('newTabBtnTT'))
        newTabAction.setShortcuts(['Ctrl+T'])
        newTabAction.triggered.connect(self.newTab)
        self.addAction(newTabAction)
        self.newTabButton = QtGui.QToolButton()
        self.newTabButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.newTabButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.newTabButton.setDefaultAction(newTabAction)
        self.cornerWidgetsToolBar.addWidget(self.newTabButton)

        self.tabsContextMenuMenu = MenuPopupWindowMenu(self.showTabsContextMenuAtCornerWidgets)
        self.newTabButton.setMenu(self.tabsContextMenuMenu)

        self.showTabsContextMenuAction = QtGui.QAction(self)
        self.showTabsContextMenuAction.setShortcuts(["Alt+W"])
        self.showTabsContextMenuAction.triggered.connect(self.showTabsContextMenuAtCornerWidgets)
        self.addAction(self.showTabsContextMenuAction)

        # New window button
        newWindowAction = QtGui.QAction(QtGui.QIcon().fromTheme("window-new", QtGui.QIcon(ryouko_icon('newwindow.png'))), tr("newWindowBtn"), self)
        newWindowAction.setShortcut('Ctrl+N')
        newWindowAction.triggered.connect(self.newWindow)
        self.addAction(newWindowAction)

        # Save page action
        savePageAction = QtGui.QAction(QtGui.QIcon().fromTheme("document-save-as", QtGui.QIcon(ryouko_icon('saveas.png'))), tr('saveAs'), self)
        savePageAction.setShortcut('Ctrl+S')
        savePageAction.triggered.connect(self.savePage)
        self.mainMenu.addAction(savePageAction)
        self.addAction(savePageAction)

        printAction = QtGui.QAction(QtGui.QIcon().fromTheme("document-print", QtGui.QIcon(ryouko_icon('print.png'))), tr('print'), self)
        printAction.setShortcut('Ctrl+P')
        printAction.triggered.connect(self.printPage)
        self.mainMenu.addAction(printAction)
        self.addAction(printAction)

        printPreviewAction = QtGui.QAction(QtGui.QIcon().fromTheme("document-print-preview", QtGui.QIcon(ryouko_icon('printpreview.png'))), tr('printPreviewHKey'), self)
        printPreviewAction.triggered.connect(self.printPreview)
        self.mainMenu.addAction(printPreviewAction)
        self.addAction(printPreviewAction)

        self.mainMenu.addSeparator()

        self.mainMenu.addAction(self.findAction)
        self.mainMenu.addAction(self.findNextAction)
        self.mainMenu.addAction(self.findPreviousAction)

        self.mainMenu.addSeparator()

        self.mainMenu.addAction(self.fullScreenAction)

        self.mainMenu.addSeparator()

        # Undo closed tab button
        undoCloseTabAction = QtGui.QAction(QtGui.QIcon().fromTheme("edit-undo", QtGui.QIcon(ryouko_icon('undo.png'))), tr('undoCloseTabBtn'), self)
        undoCloseTabAction.setToolTip(tr('undoCloseTabBtnTT'))
        undoCloseTabAction.setShortcuts(['Ctrl+Shift+T'])
        undoCloseTabAction.triggered.connect(self.undoCloseTab)
        self.addAction(undoCloseTabAction)

        undoCloseWindowAction = QtGui.QAction(tr('undoCloseWindow'), self)
        undoCloseWindowAction.setShortcut("Ctrl+Shift+N")
        undoCloseWindowAction.triggered.connect(undoCloseWindow)
        self.addAction(undoCloseWindowAction)

        # History sidebar button
        historyToggleAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-open-recent", QtGui.QIcon(ryouko_icon("history.png"))), tr('viewHistoryBtn'), self)
        historyToggleAction.setToolTip(tr('viewHistoryBtnTT'))
        historyToggleAction.triggered.connect(self.historyToggle)
        historyToggleAction.triggered.connect(self.historyToolBar.show)
        historyToggleAction.setShortcut("Ctrl+H")
        self.addAction(historyToggleAction)
        self.mainMenu.addAction(historyToggleAction)

        advHistoryAction = QtGui.QAction(QtGui.QIcon.fromTheme("x-office-calendar", QtGui.QIcon(ryouko_icon("adv-history.png"))), tr('viewAdvHistory'), self)
        advHistoryAction.setShortcut("Ctrl+Shift+H")
        advHistoryAction.triggered.connect(library.advancedHistoryViewGUI.display)
        self.addAction(advHistoryAction)
        self.mainMenu.addAction(advHistoryAction)

        # New private browsing tab button
        newpbTabAction = QtGui.QAction(QtGui.QIcon().fromTheme("face-devilish", QtGui.QIcon(ryouko_icon('pb.png'))), tr('newPBTabBtn'), self)
        newpbTabAction.setToolTip(tr('newPBTabBtnTT'))
        newpbTabAction.setShortcuts(['Ctrl+Shift+P'])
        newpbTabAction.triggered.connect(self.newpbTab)
        self.addAction(newpbTabAction)
#        self.mainMenu.addAction(closeTabForeverAction)
        self.mainMenu.addSeparator()

        self.tabsOnTopAction = QtGui.QAction(tr("tabsOnTop"), self)
        self.tabsOnTopAction.setCheckable(True)
        self.tabsOnTopAction.setShortcut("Ctrl+Shift+,")
        self.reverseToggleTabsOnTop()
        self.tabsOnTopAction.triggered.connect(self.toggleTabsOnTop)
        self.addAction(self.tabsOnTopAction)

        self.toggleMBAction = QtGui.QAction(tr("showMenuBar"), self)
        self.toggleMBAction.setCheckable(True)
        self.toggleMBAction.setShortcut("Ctrl+Shift+M")
        self.mainMenu.addAction(self.toggleMBAction)
        self.toggleMBAction.triggered.connect(self.toggleMenuBar)

        self.toggleBTAction = QtGui.QAction(tr("showBookmarksToolBar"), self)
        self.toggleBTAction.setCheckable(True)
        self.toggleBTAction.setShortcut("Ctrl+Shift+B")
        self.toggleBTAction.triggered.connect(self.toggleBookmarksToolBar)
        self.mainMenu.addAction(self.toggleBTAction)

        self.mainMenu.addSeparator()
        self.mainMenu.addAction(self.tabsOnTopAction)
        self.mainMenu.addSeparator()

        try: settings_manager.settings["showBookmarksToolBar"]
        except: do_nothing()
        else:
            if settings_manager.settings["showBookmarksToolBar"] == True:
                self.toggleBTAction.setChecked(True)

        self.mainMenu.addAction(manageBookmarksAction)
        self.mainMenu.addSeparator()

        closeTabAction = QtGui.QAction(QtGui.QIcon(ryouko_icon("close.png")), tr('closeTab'), self)
        closeTabAction.setShortcut("Ctrl+W")
        closeTabAction.triggered.connect(self.closeCurrentTab)
        self.addAction(closeTabAction)
        closeLeftTabsAction = QtGui.QAction(QtGui.QIcon(ryouko_icon('close-left.png')), tr('closeLeftTabs'), self)
        closeLeftTabsAction.setShortcut("Ctrl+Shift+L")
        closeLeftTabsAction.triggered.connect(self.closeLeftTabs)
        self.addAction(closeLeftTabsAction)
        closeRightTabsAction = QtGui.QAction(QtGui.QIcon(ryouko_icon('close-right.png')), tr('closeRighttTabs'), self)
        closeRightTabsAction.setShortcut("Ctrl+Shift+R")
        closeRightTabsAction.triggered.connect(self.closeRightTabs)
        self.addAction(closeRightTabsAction)

        self.tabsContextMenu = ContextMenu()
        self.tabsContextMenu.setTitle(tr("windowsHKey"))
        self.tabsContextMenu.addAction(newTabAction)
        self.tabsContextMenu.addAction(newWindowAction)
        self.tabsContextMenu.addAction(newpbTabAction)
        self.tabsContextMenu.addSeparator()
        self.tabsContextMenu.addAction(closeTabAction)
        self.tabsContextMenu.addAction(closeLeftTabsAction)
        self.tabsContextMenu.addAction(closeRightTabsAction)
        self.tabsContextMenu.addAction(closeTabForeverAction)
        self.tabsContextMenu.addSeparator()
        self.tabsContextMenu.addAction(undoCloseTabAction)
        self.tabsContextMenu.addAction(undoCloseWindowAction)

        self.menuBar = QtGui.QMenuBar()
        self.menuBar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.setMenuBar(self.menuBar)
        self.reverseToggleMenuBar()

        self.tabs.customContextMenuRequested.connect(self.tabsContextMenu.show2)

        activateTab1Action = QtGui.QAction(self)
        activateTab2Action = QtGui.QAction(self)
        activateTab3Action = QtGui.QAction(self)
        activateTab4Action = QtGui.QAction(self)
        activateTab5Action = QtGui.QAction(self)
        activateTab6Action = QtGui.QAction(self)
        activateTab7Action = QtGui.QAction(self)
        activateTab8Action = QtGui.QAction(self)
        activateTab9Action = QtGui.QAction(self)
        numActions = [activateTab1Action, activateTab2Action, activateTab3Action, activateTab4Action, activateTab5Action, activateTab6Action, activateTab7Action, activateTab8Action, activateTab9Action]
        for action in range(len(numActions)):
            numActions[action].setShortcuts(["Ctrl+" + str(action + 1), "Alt+" + str(action + 1)])
            exec("numActions[action].triggered.connect(self.activateTab" + str(action + 1) + ")")
            self.addAction(numActions[action])

        # Config button
        configAction2 = QtGui.QAction(QtGui.QIcon().fromTheme("preferences-system", QtGui.QIcon(ryouko_icon('settings.png'))), tr('options'), self)
        configAction2.setToolTip(tr('preferencesButtonTT'))
        configAction2.setShortcuts(['Ctrl+,'])
        configAction2.triggered.connect(self.showSettings)

        configAction = QtGui.QAction(QtGui.QIcon().fromTheme("preferences-system", QtGui.QIcon(ryouko_icon('settings.png'))), tr('preferencesButton'), self)
        configAction.setToolTip(tr('preferencesButtonTT'))
        configAction.setShortcuts(['Ctrl+Alt+P'])
        configAction.triggered.connect(self.showSettings)

        self.addAction(configAction)
        self.toolsMenu = QtGui.QMenu(tr("toolsHKey"))
        self.mainMenu.addMenu(self.toolsMenu)
        viewSourceAction = QtGui.QAction(tr("viewSource"), self)
        viewSourceAction.setShortcut("Ctrl+Alt+U")
        viewSourceAction.triggered.connect(self.viewSource)
        self.toolsMenu.addAction(viewSourceAction)

        inspectAction = QtGui.QAction(tr("webInspectorHKey"), self)
        inspectAction.setShortcut("F12")
        inspectAction.triggered.connect(self.inspect)
        self.toolsMenu.addAction(inspectAction)

        self.toolsMenu.addSeparator()
        self.toolsMenu.addAction(viewNotificationsAction)

        downloadsAction = QtGui.QAction(QtGui.QIcon().fromTheme("go-down", QtGui.QIcon(ryouko_icon("down.png"))), tr("downloadsHKey"), self)
        downloadsAction.setShortcuts(["Ctrl+Shift+Y", "Ctrl+J"])
        downloadsAction.triggered.connect(downloadManagerGUI.show)
        self.toolsMenu.addAction(downloadsAction)
        self.addAction(downloadsAction)

        self.toolsMenu.addAction(clearHistoryAction)
        self.toolsMenu.addAction(configAction2)
        self.mainMenu.addSeparator()
        
        aboutQtAction = QtGui.QAction(tr('aboutQtHKey'), self)
        if not sys.platform.startswith("win"):
            aboutQtAction.setIcon(QtGui.QIcon(ryouko_icon("qt.svg")))
        else:
            aboutQtAction.setIcon(QtGui.QIcon(ryouko_icon("qt-16.png")))
        aboutQtAction.triggered.connect(QtGui.QApplication.aboutQt)
        self.mainMenu.addAction(aboutQtAction)

        aboutAction = QtGui.QAction(tr('aboutRyoukoHKey'), self)
        if not sys.platform.startswith("win"):
            aboutAction.setIcon(QtGui.QIcon(ryouko_icon("logo.svg")))
        else:
            aboutAction.setIcon(QtGui.QIcon(ryouko_icon("logo.png")))
        aboutAction.triggered.connect(self.aboutRyoukoHKey)
        self.mainMenu.addAction(aboutAction)

        self.fileMenu = QtGui.QMenu(tr("fileHKey"))
        self.fileMenu.addAction(newTabAction)
        self.fileMenu.addAction(newWindowAction)
        self.fileMenu.addAction(newpbTabAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(savePageAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(printAction)
        self.fileMenu.addAction(printPreviewAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(closeTabAction)
        self.fileMenu.addAction(closeLeftTabsAction)
        self.fileMenu.addAction(closeRightTabsAction)
        self.fileMenu.addAction(closeTabForeverAction)
        self.fileMenu.addSeparator()

        self.editMenu = QtGui.QMenu(tr("editHKey"))
        self.editMenu.addAction(self.findAction)
        self.editMenu.addAction(self.findNextAction)
        self.editMenu.addAction(self.findPreviousAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(configAction)

        self.viewMenu = QtGui.QMenu(tr("viewHKey"))
        self.viewMenu.addAction(self.toggleMBAction)
        self.viewMenu.addAction(self.toggleBTAction)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.tabsOnTopAction)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(historyToggleAction)
        self.viewMenu.addSeparator()
        self.viewMenu.addAction(self.fullScreenAction)

        self.historyMenu = QtGui.QMenu(tr("historyHKey"))
        self.historyMenu.addAction(advHistoryAction)
        self.historyMenu.addSeparator()
        self.historyMenu.addAction(undoCloseTabAction)
        self.historyMenu.addAction(undoCloseWindowAction)

        self.bookmarksMenu = QtGui.QMenu(tr("bookmarks"))
        self.bookmarksMenu.addAction(manageBookmarksAction)

        self.helpMenu = QtGui.QMenu(tr("helpHKey"))
        self.helpMenu.addAction(aboutQtAction)
        self.helpMenu.addAction(aboutAction)

        self.menuBar.addMenu(self.fileMenu)
        self.menuBar.addMenu(self.editMenu)
        self.menuBar.addMenu(self.viewMenu)
        self.menuBar.addMenu(self.historyMenu)
        self.menuBar.addMenu(self.bookmarksMenu)
        self.menuBar.addMenu(self.toolsMenu)
        self.menuBar.addMenu(self.helpMenu)

        self.mainMenu.addSeparator()

        self.mainMenu.addAction(quitAction)

        self.setCentralWidget(self.tabs)

        self.tabs.currentChanged.connect(self.checkTabsOnTop)
        if len(sys.argv) == 1:
            try: h = settings_manager.settings['homePages'].split("\n")
            except: self.newTab()
            else:
                if len(h) == 0:
                    self.newTab()
                else:
                    if h[0] == "":
                        self.newTab()
                    else:
                        for u in h:
                            self.newTab(None, u)
        elif len(sys.argv) > 1:
            for arg in range(1, len(sys.argv)):
                if not "--pb" in sys.argv and not "-pb" in sys.argv:
                    try:
                        sys.argv[arg - 1]
                    except:
                        if not sys.argv[arg] == "-P":
                            a = sys.argv[arg]
                            if not "://" in a:
                                a = "http://" + a
                            self.newTab(None, a)
                    else:
                        if not (sys.argv[arg - 1] == "-P") and not sys.argv[arg] == "-P":
                            a = sys.argv[arg]
                            if not "://" in a:
                                a = "http://" + a
                            self.newTab(None, a)
                else:
                    try:
                        sys.argv[arg - 1]
                    except:
                        if not sys.argv[arg] == "-P" and not sys.argv[arg] == "--pb" and not sys.argv[arg] == "-pb":
                            a = sys.argv[arg]
                            if not "://" in a:
                                a = "http://" + a
                            self.newpbTab(None, a)
                    else:
                        if not (sys.argv[arg - 1] == "-P") and not sys.argv[arg] == "-P" and not sys.argv[arg] == "--pb" and not sys.argv[arg] == "-pb":
                            a = sys.argv[arg]
                            if not "://" in a:
                                a = "http://" + a
                            self.newpbTab(None, a)
            for arg in range(1, len(sys.argv)):
                del sys.argv[1]
            if self.tabs.count() == 0:
                self.newTab()
                self.tabs.widget(self.tabs.currentIndex()).webView.buildNewTabPage()

        m = os.path.join(app_profile, "maximized.conf")
        if os.path.exists(m):
            self.setWindowState(QtCore.Qt.WindowMaximized)

    def show(self):
        self.setVisible(True)
        m = os.path.join(app_profile, "maximized.conf")
        if os.path.exists(m):
            self.setWindowState(QtCore.Qt.WindowMaximized)
        
    def reverseToggleTabsOnTop(self):
        c = app_tabs_on_top_conf
        if os.path.exists(c):
            self.tabsOnTopAction.setChecked(True)
            global app_tabs_on_top
            app_tabs_on_top = True
            if sys.platform.startswith("win"):
                for win in app_windows:
                    try: win.tabs.widget(win.tabs.currentIndex()).addToolBar(win.mainToolBar)
                    except: do_nothing()
                    else: win.mainToolBar.setStyleSheet(tabsontopsheet); win.tabs.setStyleSheet(tabsontopsheet2)
            else:
                for win in app_windows:
                    try: win.tabs.widget(win.tabs.currentIndex()).addToolBar(win.mainToolBar)
                    except: do_nothing()
                    else: win.mainToolBar.setStyleSheet(""); win.tabs.setStyleSheet("")
        else:
            self.tabsOnTopAction.setChecked(False)
            global app_tabs_on_top
            app_tabs_on_top = False
            for win in app_windows:
                win.addToolBar(win.mainToolBar)
                win.mainToolBar.setStyleSheet(""); win.tabs.setStyleSheet("")

    def toggleTabsOnTop(self):
        c = app_tabs_on_top_conf
        if os.path.exists(app_tabs_on_top_conf):
            remove2(c)
            self.tabsOnTopAction.setChecked(False)
            global app_tabs_on_top
            app_tabs_on_top = False
            for win in app_windows:
                win.addToolBar(win.mainToolBar)
                win.mainToolBar.setStyleSheet(""); win.tabs.setStyleSheet("")
        else:
            f = open(c, "w")
            f.write("")
            f.close()
            global app_tabs_on_top
            app_tabs_on_top = True
            self.tabsOnTopAction.setChecked(True)
            if sys.platform.startswith("win"):
                for win in app_windows:
                    try: win.tabs.widget(win.tabs.currentIndex()).addToolBar(win.mainToolBar)
                    except: do_nothing()
                    else: win.mainToolBar.setStyleSheet(tabsontopsheet); win.tabs.setStyleSheet(tabsontopsheet2)
            else:
                for win in app_windows:
                    try: win.tabs.widget(win.tabs.currentIndex()).addToolBar(win.mainToolBar)
                    except: do_nothing()
                    else: win.mainToolBar.setStyleSheet(""); win.tabs.setStyleSheet("")

    def checkTabsOnTop(self):
        if app_tabs_on_top == True:
            try: self.tabs.widget(self.tabs.currentIndex()).addToolBar(self.mainToolBar)
            except: do_nothing()
            else:
                if sys.platform.startswith("win"):
                    self.mainToolBar.setStyleSheet(tabsontopsheet); self.tabs.setStyleSheet(tabsontopsheet2)
                else:
                    self.mainToolBar.setStyleSheet(""); self.tabs.setStyleSheet("")

    def reverseToggleMenuBar(self):
        c = app_menubar_conf
        if os.path.exists(c):
            self.toggleMBAction.setChecked(True)
            for win in app_windows:
                win.mainMenuButton.setVisible(False)
        else:
            self.toggleMBAction.setChecked(False)
            for win in app_windows:
                win.menuBar.hide()

    def toggleMenuBar(self):
        c = app_menubar_conf
        if os.path.exists(c):
            remove2(c)
            self.toggleMBAction.setChecked(False)
            for win in app_windows:
                win.mainMenuButton.setVisible(True)
            for win in app_windows:
                win.menuBar.hide()
        else:
            f = open(c, "w")
            f.write("")
            f.close()
            self.toggleMBAction.setChecked(True)
            for win in app_windows:
                win.mainMenuButton.setVisible(False)
            for win in app_windows:
                win.menuBar.show()

    def toggleBookmarksToolBar(self):
        cDialog.showBTBox.click(); cDialog.saveSettings()
        if settings_manager.settings['showBookmarksToolBar'] == True:
            self.toggleBTAction.setChecked(True)
        else:
            self.toggleBTAction.setChecked(False)

    def toggleFullScreen(self):
        if self.windowState() == QtCore.Qt.WindowFullScreen:
            self.setWindowState(QtCore.Qt.WindowNoState)
        else:
            self.setWindowState(QtCore.Qt.WindowFullScreen)

    def rMax(self):
        if self.windowState() == QtCore.Qt.WindowMaximized:
            self.setWindowState(QtCore.Qt.WindowNoState)
        else:
            self.setWindowState(QtCore.Qt.WindowMaximized)

    def viewSource(self):
        self.tabs.widget(self.tabs.currentIndex()).webView.viewSource()

    def inspect(self):
        self.tabs.widget(self.tabs.currentIndex()).webView.showInspector()

    def activateTab1(self):
        self.tabs.setCurrentIndex(0)

    def activateTab2(self):
        self.tabs.setCurrentIndex(1)

    def activateTab3(self):
        self.tabs.setCurrentIndex(2)

    def activateTab4(self):
        self.tabs.setCurrentIndex(3)

    def activateTab5(self):
        self.tabs.setCurrentIndex(4)

    def activateTab6(self):
        self.tabs.setCurrentIndex(5)

    def activateTab7(self):
        self.tabs.setCurrentIndex(6)

    def activateTab8(self):
        self.tabs.setCurrentIndex(7)

    def activateTab9(self):
        self.tabs.setCurrentIndex(self.tabs.count() - 1)

    def savePage(self):
        self.tabs.widget(self.tabs.currentIndex()).webView.savePage()

    def printPage(self):
        self.tabs.widget(self.tabs.currentIndex()).webView.printPage()

    def printPreview(self):
        self.tabs.widget(self.tabs.currentIndex()).webView.printPreview()

    def hideInspectors(self):
        for tab in range(self.tabs.count()):
            try:
                self.tabs.widget(tab).webInspectorDock.hide()
            except:
                doNothing()

    def showTabsContextMenu(self):
        x = QtCore.QPoint(QtGui.QCursor.pos()).x()
        if x + self.tabsContextMenu.width() > QtGui.QApplication.desktop().size().width():
            x = x - self.tabsContextMenu.width()
        y = QtCore.QPoint(QtGui.QCursor.pos()).y()
        if y + self.tabsContextMenu.height() > QtGui.QApplication.desktop().size().height():
            y = y - self.tabsContextMenu.height()
        self.tabsContextMenu.move(x, y)
        self.tabsContextMenu.show2()

    def showTabsContextMenuAtCornerWidgets(self, dummy=None):
        x = self.newTabButton.mapToGlobal(QtCore.QPoint(0,0)).x()
        y = self.newTabButton.mapToGlobal(QtCore.QPoint(0,0)).y()
        width = self.newTabButton.width()
        height = self.newTabButton.height()
        self.tabsContextMenu.show()
        if x - self.tabsContextMenu.width() + width < 0:
            x = 0
        else:
            x = x - self.tabsContextMenu.width() + width
        if y + height + self.tabsContextMenu.height() >= QtGui.QApplication.desktop().size().height():
            y = y - self.tabsContextMenu.height()
        else:
            y = y + height
        self.tabsContextMenu.move(x, y)

    def showCornerWidgetsMenu(self):
        self.mainToolBar.widgetForAction(self.mainMenuButton).showMenu()

    def showSettings(self):
        cDialog.show()
        centerWidget(cDialog)

    def updateSettings(self):
        for tab in range(self.tabs.count()):
            self.tabs.widget(tab).updateSettings()

    def nextTab(self):
        tabIndex = self.tabs.currentIndex() + 1
        if tabIndex < self.tabs.count():
            self.tabs.setCurrentIndex(tabIndex)
        else:
            self.tabs.setCurrentIndex(0)
    def previousTab(self):
        tabIndex = self.tabs.currentIndex() - 1
        if tabIndex >= 0:
            self.tabs.setCurrentIndex(tabIndex)
        else:
            self.tabs.setCurrentIndex(self.tabs.count() - 1)

    def correctURLText(self, url=False):
        if type(url) == QtCore.QUrl:
            if self.currentWebView().url() != url:
                return
        try: self.urlBar.setText(self.currentWebView().url().toString())
        except:
            do_nothing()

    def newWindowWithRWebView(self, webView):
        win = self.newWindow()
        win.closeTab(0, True, True)
        win.newTab(webView)

    def newpbWindowWithRWebView(self, webView):
        win = self.newWindow()
        win.closeTab(0, True, True)
        win.newpbTab(webView)

    def newTab(self, webView = None, url=False):
        if cDialog.settings['privateBrowsing']:
            self.newpbTab(webView, url)
        else:
            self.tabCount += 1
            s = str(self.tabCount)
            if url != False:
                try:
                    exec("tab" + s + " = Browser(self, \"" + metaunquote(url) + "\")")
                except:
                    exec("tab" + s + " = Browser(self, \"" + url + "\")")
            else:
                exec("tab%s = Browser(self)" % (s))
            if webView != None and webView:
                exec("tab%s.swapWebView(webView)" % (s))
            exec("tab%s.webView.newTabRequest.connect(self.newTab)" % (s))
            exec("tab%s.webView.newWindowRequest.connect(self.newWindowWithRWebView)" % (s))
            exec("tab%s.webView.titleChanged.connect(self.updateTitles)" % (s))
            exec("tab%s.webView.urlChanged.connect(self.reloadHistory)" % (s))
            exec("tab%s.webView.titleChanged.connect(self.reloadHistory)" % (s))
            exec("tab%s.webView.iconChanged.connect(self.updateIcons)" % (s))
            exec("tab%s.webView.urlChanged.connect(self.enableDisableBF)" % (s))
            exec("tab%s.webView.urlChanged.connect(self.updateText)" % (s))
            exec("tab%s.webView.urlChanged.connect(self.correctURLText)" % (s))
            exec("tab%s.webView.loadProgress.connect(self.toggleStopReload)" % (s))
            exec("tab%s.webView.loadFinished.connect(self.toggleStopReload)" % (s))
            if settings_manager.settings["relativeTabs"] == False:
                exec("self.tabs.addTab(tab" + s + ", tab" + s + ".webView.icon(), 'New Tab')")
                self.tabs.setCurrentIndex(self.tabs.count() - 1)
            else:
                exec("self.tabs.insertTab(self.tabs.currentIndex() + 1, tab" + s + ", tab" + s + ".webView.icon(), 'New Tab')")
                self.tabs.setCurrentIndex(self.tabs.currentIndex() + 1)
            if url != False:
                self.currentWebView().load(QtCore.QUrl(metaunquote(url)))
            self.currentWebView().loadLinks()

    def newpbTab(self, webView=None, url=False):
        self.tabCount += 1
        s = str(self.tabCount)
        if url != False:
            exec("tab" + s + " = Browser(self, '" + metaunquote(url) + "', True)")
        else:
            exec("tab" + s + " = Browser(self, 'about:blank', True)")
        if webView != None and webView:
            exec("tab%s.swapWebView(webView)" % (s))
        exec("tab%s.webView.newTabRequest.connect(self.newpbTab)" % (s))
        exec("tab%s.webView.newWindowRequest.connect(self.newpbWindowWithRWebView)" % (s))
        exec("tab" + s + ".webView.titleChanged.connect(self.updateTitles)")
        exec("tab" + s + ".webView.urlChanged.connect(self.reloadHistory)")
        exec("tab" + s + ".webView.titleChanged.connect(self.reloadHistory)")
        exec("tab" + s + ".webView.iconChanged.connect(self.updateIcons)")
        exec("tab%s.webView.urlChanged.connect(self.enableDisableBF)" % (s))
        exec("tab%s.webView.urlChanged.connect(self.updateText)" % (s))
        exec("tab%s.webView.urlChanged.connect(self.correctURLText)" % (s))
        exec("tab%s.webView.loadProgress.connect(self.toggleStopReload)" % (s))
        exec("tab%s.webView.loadFinished.connect(self.toggleStopReload)" % (s))
        exec("self.tabs.addTab(tab" + s + ", tab" + s + ".webView.icon(), 'New Tab')")
        self.tabs.setCurrentIndex(self.tabs.count() - 1)
        if url != False:
            self.currentWebView().load(QtCore.QUrl(metaunquote(url)))
        self.currentWebView().loadLinks()

    def newWindow(self):
        nwin = TabBrowser(self)
        nwin.show()
        return nwin

    def openHistoryItem(self, item):
        if self.searchOn == False:
            self.newTab(None, browserHistory.history[self.historyList.row(item)]['url'])
        else:
            self.newTab(None, self.tempHistory[self.historyList.row(item)]['url'])

    def reloadHistory(self):
        self.searchHistoryField.clear()    
        self.historyList.clear()
        browserHistory.reload()
        for item in browserHistory.history:
           self.historyList.addItem(qstring(unicode(item['name'])))
    def searchHistory(self, string=""):
        string = unicode(string)
        if string != "":
            self.searchOn = True
            self.historyList.clear()
            history = []
            string = unicode(string)
            for item in browserHistory.history:
                add = False
                for subitem in item:
                    if string.lower() in unicode(item[subitem]).lower():
                        add = True
                        break
                if add == True:
                    history.append(item)
                    self.historyList.addItem(item['name'])
            self.tempHistory = history
        else:
            self.searchOn = False
            self.reloadHistory()
    def deleteHistoryItem(self):
        if self.historyList.hasFocus():
            browserHistory.removeByName(unicode(self.historyList.currentItem().text()))

    def showClearHistoryDialog(self):
        clearHistoryDialog.display()

    def historyToggle(self):
        self.historyDock.setVisible(not self.historyDock.isVisible())
        if self.historyDock.isVisible():
            self.focusHistorySearch()
    def focusHistorySearch(self):
        self.searchHistoryField.setFocus()
        self.searchHistoryField.selectAll()

    def closeCurrentTab(self):
        self.closeTab(self.tabs.currentIndex())

    def closeTab(self, index=None, permanent=False, allowZeroTabs=False):
        if app_tabs_on_top == True:
            self.addToolBar(self.mainToolBar)
        self.addToolBar(self.findToolBar)
        self.findToolBar.hide()
        if index == None:
            index = self.tabs.currentIndex()
        if self.tabs.count() > 0:
            if (self.tabs.widget(index).webView.pb) or (unicode(self.tabs.widget(index).webView.url().toString()) == "" or unicode(self.tabs.widget(index).webView.url().toString()) == "about:blank") or permanent==True:
                self.tabs.widget(index).deleteLater()
            else:
                self.closedTabsList.append({'widget' : self.tabs.widget(index), 'title' : unicode(self.tabs.widget(index).webView.title()), 'url' : unicode(self.tabs.widget(index).webView.url().toString())})
                self.tabs.widget(index).webView.setHtml("<!DOCTYPE html><html><head><title></title></head><body></body></html>")
            self.tabs.removeTab(index)
            try: settings_manager.settings['maxUndoCloseTab']
            except:
                doNothing()
            else:
                if settings_manager.settings['maxUndoCloseTab'] >= 0:
                    if len(self.closedTabsList) >= int(settings_manager.settings['maxUndoCloseTab'] + 1):
                        self.closedTabsList[0]["widget"].deleteLater()
                        del self.closedTabsList[0]
            if self.tabs.count() == 0 and allowZeroTabs == False:
                self.newTab()
        self.reloadClosedTabsMenu()

    def reloadClosedTabsMenu(self):
        self.closedTabsMenu.clear()
        self.closedTabsMenu.setCurrentRow(0)
        for tab in self.closedTabsList:
            self.closedTabsMenu.addItem(tab["title"])

    def permanentCloseTab(self):
        self.closeTab(self.tabs.currentIndex(), True)

    def closeLeftTabs(self):
        t = self.tabs.currentIndex()
        self.tabs.setCurrentIndex(0)
        for i in range(t):
            self.closeTab(0)

    def closeRightTabs(self):
        while self.tabs.currentIndex() != self.tabs.count() - 1:
            self.closeTab(self.tabs.count() - 1)

    def undoCloseTabInThisTab(self, index=False):
        i = self.tabs.currentIndex()
        if index == False:
            index = len(self.closedTabsList) - 1
        elif type(index) != int:
            index = self.closedTabsMenu.row(index)
        self.closeTab(i, True, True)
        if len(self.closedTabsList) > 0:
            self.tabs.insertTab(i, self.closedTabsList[index]['widget'], self.closedTabsList[index]['widget'].webView.icon(), self.closedTabsList[index]['widget'].webView.title())
            self.updateTitles()
            self.tabs.setCurrentIndex(i)
            if self.tabs.widget(self.tabs.currentIndex()).webView.history().canGoForward():
                self.tabs.widget(self.tabs.currentIndex()).webView.forward()
                self.tabs.widget(self.tabs.currentIndex()).webView.back()
            elif self.tabs.widget(self.tabs.currentIndex()).webView.history().canGoBack():
                self.tabs.widget(self.tabs.currentIndex()).webView.back()
                self.tabs.widget(self.tabs.currentIndex()).webView.forward()
            else:
                self.tabs.widget(self.tabs.currentIndex()).webView.load(QtCore.QUrl(self.closedTabsList[index]["url"]))
            del self.closedTabsList[index]
        self.reloadClosedTabsMenu()

    def undoCloseTab(self, index=False):
        if index == False:
            index = len(self.closedTabsList) - 1
        elif type(index) != int:
            index = self.closedTabsMenu.row(index)
        if len(self.closedTabsList) > 0:
            self.tabs.addTab(self.closedTabsList[index]['widget'], self.closedTabsList[index]['widget'].webView.icon(), self.closedTabsList[index]['widget'].webView.title())
            self.updateTitles()
            self.tabs.setCurrentIndex(self.tabs.count() - 1)
            if self.tabs.widget(self.tabs.currentIndex()).webView.history().canGoForward():
                self.tabs.widget(self.tabs.currentIndex()).webView.forward()
                self.tabs.widget(self.tabs.currentIndex()).webView.back()
            elif self.tabs.widget(self.tabs.currentIndex()).webView.history().canGoBack():
                self.tabs.widget(self.tabs.currentIndex()).webView.back()
                self.tabs.widget(self.tabs.currentIndex()).webView.forward()
            else:
                self.tabs.widget(self.tabs.currentIndex()).webView.load(QtCore.QUrl(self.closedTabsList[index]["url"]))
            del self.closedTabsList[index]
        self.reloadClosedTabsMenu()

    def updateIcons(self):
        self.setIcon()
        for tab in range(self.tabs.count()):
            i = self.tabs.widget(tab).webView.icon()
            if i.actualSize(QtCore.QSize(16, 16)).width() > 0:
                self.tabs.setTabIcon(tab, self.tabs.widget(tab).webView.icon())
            else:
                self.tabs.setTabIcon(tab, app_webview_default_icon)

    def updateTitles(self):
        for tab in range(self.tabs.count()):
            if unicode(self.tabs.widget(tab).webView.title()) == "":
                if not self.tabs.widget(tab).pb:
                    self.tabs.setTabText(tab, tr('newTab'))
                else:
                    self.tabs.setTabText(tab, tr('newPBTab'))
                if tab == self.tabs.currentIndex():
                    self.setWindowTitle("Ryouko")
                self.tabs.setTabIcon(tab, app_webview_default_icon)                    
            else:
                u = unicode(self.tabs.widget(tab).webView.title())
                if len(u) > 20:
                    title = u[0:10] + "..." + u[len(u)-10:len(u)]
                    title = qstring(title)
                else:
                    title = u
                if self.tabs.widget(tab).pb:
                    title = unicode(title)
                    title = "%s (PB)" % (title)
                    title = qstring(title)
                self.tabs.setTabText(tab, title)
                if tab == self.tabs.currentIndex():
                    self.setWindowTitle("%s - Ryouko" % (unicode(self.tabs.widget(tab).webView.title())))

win = None

class Ryouko(QtGui.QWidget):
    def __init__(self):

        dA = QtWebKit.QWebPage()
        dA.mainFrame().setHtml("<html><body><span id='userAgent'></span></body></html>")
        dA.mainFrame().evaluateJavaScript("document.getElementById(\"userAgent\").innerHTML = navigator.userAgent;")
        global app_default_useragent
        app_default_useragent = unicode(dA.mainFrame().findFirstElement("#userAgent").toPlainText()).replace("Safari", "Ryouko/" + app_version + " Safari")
        dA.deleteLater()
        del dA
        q = QtWebKit.QWebView()
        q.load(QtCore.QUrl("about:blank"))
        global app_webview_default_icon
        app_webview_default_icon = QtGui.QIcon(q.icon())
        q.deleteLater()
        del q

        if os.path.exists(app_lock) and not sys.platform.startswith("win"):
            reply = QtGui.QMessageBox.question(None, tr("error"),
        tr("isRunning"), QtGui.QMessageBox.Yes | 
        QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
                f = open(app_instance2, "w")
                f.write("")
                f.close()
                f = open(app_instance2, "a")
                for arg in range(1, len(sys.argv)):
                    if not sys.argv[arg].lower() == "--pb" and not sys.argv[arg].lower() == "-pb" and not sys.argv[arg] == "-P":
                        f.write("%s\n" % (sys.argv[arg]))
                f.close()
            else:
                if os.path.exists(app_lock):
                    remove2(app_lock)
                args = ""
                for arg in sys.argv:
                    args = "%s%s " % (args, arg)
                os.system("%s && echo \"\"" % (args))
            QtCore.QCoreApplication.instance().quit()
            sys.exit()

        if not os.path.isdir(app_profile):
            os.makedirs(app_profile)
        if not os.path.isdir(os.path.join(app_profile, "adblock")):
            os.mkdir(os.path.join(app_profile, "adblock"))
        settings_manager.loadSettings()
        if not os.path.isdir(app_profile):
            os.makedirs(app_profile)
        if not os.path.isdir(os.path.join(app_profile, "temp")):
            os.mkdir(os.path.join(app_profile, "temp"))
        if not os.path.isdir(os.path.join(app_profile, "adblock")):
            os.mkdir(os.path.join(app_profile, "adblock"))
        sync_data()
        loadCookies()
        global library; global searchEditor; global cDialog; global win;
        global aboutDialog; global notificationManager;
        global clearHistoryDialog; global downloadManagerGUI;
        global app_extensions
        for folder in app_extensions_path:
            if os.path.isdir(folder):
                l = os.listdir(folder)
                for addon in l:
                    fname = os.path.join(folder, addon)
                    if os.path.exists(fname) and not os.path.isdir(fname):
                        f = open(fname, "r")
                        try: ext = json.load(f)
                        except: do_nothing()
                        else:
                            try: ext["path"] = fname
                            except: ext["path"] = None
                            try: ext["folder"] = folder
                            except: ext["folder"] = None
                            app_extensions.append(ext)
                            f.close()
        downloadManagerGUI = DownloadManagerGUI()
        downloadManagerGUI.networkAccessManager.setCookieJar(app_cookiejar)
        app_cookiejar.setParent(QtCore.QCoreApplication.instance())
        downloadManagerGUI.downloadFinished.connect(downloadFinished)
        aboutDialog = RAboutDialog()
        notificationManager = NotificationManager()
        clearHistoryDialog = ClearHistoryDialog()
        library = Library()
        searchEditor = SearchEditor()
        cDialog = CDialog(self)
        aboutDialog.updateUserAgent()
        win = TabBrowser(self)
    def primeBrowser(self):
        global win
        win.show()

def updateProgress(pr):
    global app_launcher
    if pr != 0.0:
        app_launcher.set_property("progress_visible", True)
        app_launcher.set_property("progress", pr)
    else:
        app_launcher.set_property("progress_visible", False)

def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(tr("help"))
    if "--icons" in sys.argv:
        print(app_icons)
    else:
        app = QtGui.QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)
        app.lastWindowClosed.connect(confirmQuit)
        app.aboutToQuit.connect(prepareQuit)
        ryouko = Ryouko()
        ryouko.primeBrowser()
        f = open(app_lock, "w")
        f.write("")
        f.close()
        if use_unity_launcher == True:
            loop = GObject.MainLoop()
            global app_launcher
            app_launcher = Unity.LauncherEntry.get_for_desktop_id("ryouko.desktop")
            downloadManagerGUI.downloadProgress.connect(updateProgress)
        app.exec_()

if __name__ == "__main__":
    main()