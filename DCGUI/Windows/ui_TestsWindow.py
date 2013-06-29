
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TestsWindow(object):
    def setupUi(self, TestsWindow):
        TestsWindow.setObjectName(_fromUtf8("TestsWindow"))
        TestsWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        TestsWindow.resize(521, 359)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/multtests.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TestsWindow.setWindowIcon(icon)
        TestsWindow.setStyleSheet(_fromUtf8("QWidget, QMenuBar::item {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #c5d8ef, stop: 1 #89a5c3);\n"
"}\n"
"\n"
"QLabel, QSlider {\n"
"    background-color: transparent;\n"
"}"))
        self.centralwidget = QtGui.QWidget(TestsWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tests_tabs = QtGui.QTabWidget(self.centralwidget)
        self.tests_tabs.setEnabled(True)
        self.tests_tabs.setObjectName(_fromUtf8("tests_tabs"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.algorithm = QtGui.QComboBox(self.tab)
        self.algorithm.setMinimumSize(QtCore.QSize(100, 0))
        self.algorithm.setObjectName(_fromUtf8("algorithm"))
        self.algorithm.addItem(_fromUtf8(""))
        self.algorithm.addItem(_fromUtf8(""))
        self.algorithm.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.algorithm)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.projects = QtGui.QTreeWidget(self.tab)
        self.projects.setObjectName(_fromUtf8("projects"))
        self.verticalLayout_2.addWidget(self.projects)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.add = QtGui.QPushButton(self.tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add.setIcon(icon1)
        self.add.setObjectName(_fromUtf8("add"))
        self.verticalLayout.addWidget(self.add)
        self.remove = QtGui.QPushButton(self.tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove.setIcon(icon2)
        self.remove.setObjectName(_fromUtf8("remove"))
        self.verticalLayout.addWidget(self.remove)
        self.pushButton = QtGui.QPushButton(self.tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/dice.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.run = QtGui.QPushButton(self.tab)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.run.setIcon(icon4)
        self.run.setObjectName(_fromUtf8("run"))
        self.verticalLayout.addWidget(self.run)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.tests_tabs.addTab(self.tab, _fromUtf8(""))
        self.Graphs = QtGui.QWidget()
        self.Graphs.setObjectName(_fromUtf8("Graphs"))
        self.gridLayout_3 = QtGui.QGridLayout(self.Graphs)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.Graphs)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.label_3 = QtGui.QLabel(self.Graphs)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.vertical = QtGui.QComboBox(self.Graphs)
        self.vertical.setObjectName(_fromUtf8("vertical"))
        self.vertical.addItem(_fromUtf8(""))
        self.vertical.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.vertical)
        self.horizontal = QtGui.QComboBox(self.Graphs)
        self.horizontal.setObjectName(_fromUtf8("horizontal"))
        self.horizontal.addItem(_fromUtf8(""))
        self.horizontal.addItem(_fromUtf8(""))
        self.horizontal.addItem(_fromUtf8(""))
        self.horizontal.addItem(_fromUtf8(""))
        self.horizontal.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.horizontal)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.save = QtGui.QPushButton(self.Graphs)
        self.save.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/cd.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save.setIcon(icon5)
        self.save.setObjectName(_fromUtf8("save"))
        self.horizontalLayout_3.addWidget(self.save)
        self.scaledown = QtGui.QPushButton(self.Graphs)
        self.scaledown.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/scaledown.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scaledown.setIcon(icon6)
        self.scaledown.setObjectName(_fromUtf8("scaledown"))
        self.horizontalLayout_3.addWidget(self.scaledown)
        self.scaleup = QtGui.QPushButton(self.Graphs)
        self.scaleup.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/scaleup.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scaleup.setIcon(icon7)
        self.scaleup.setObjectName(_fromUtf8("scaleup"))
        self.horizontalLayout_3.addWidget(self.scaleup)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.graph = QtGui.QGraphicsView(self.Graphs)
        self.graph.setObjectName(_fromUtf8("graph"))
        self.verticalLayout_5.addWidget(self.graph)
        self.gridLayout_3.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.tests_tabs.addTab(self.Graphs, _fromUtf8(""))
        self.gridLayout.addWidget(self.tests_tabs, 0, 0, 1, 1)
        TestsWindow.setCentralWidget(self.centralwidget)
        self.actionSelect = QtGui.QAction(TestsWindow)
        self.actionSelect.setCheckable(True)
        self.actionSelect.setChecked(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/select.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect.setIcon(icon8)
        self.actionSelect.setObjectName(_fromUtf8("actionSelect"))
        self.actionVM = QtGui.QAction(TestsWindow)
        self.actionVM.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/computer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVM.setIcon(icon9)
        self.actionVM.setObjectName(_fromUtf8("actionVM"))
        self.actionEdge = QtGui.QAction(TestsWindow)
        self.actionEdge.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/edge.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdge.setIcon(icon10)
        self.actionEdge.setObjectName(_fromUtf8("actionEdge"))
        self.actionNew_System = QtGui.QAction(TestsWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/page.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_System.setIcon(icon11)
        self.actionNew_System.setObjectName(_fromUtf8("actionNew_System"))
        self.actionOpen_System = QtGui.QAction(TestsWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/folder.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_System.setIcon(icon12)
        self.actionOpen_System.setObjectName(_fromUtf8("actionOpen_System"))
        self.actionSave_System = QtGui.QAction(TestsWindow)
        self.actionSave_System.setIcon(icon5)
        self.actionSave_System.setObjectName(_fromUtf8("actionSave_System"))
        self.actionSave_System_As = QtGui.QAction(TestsWindow)
        self.actionSave_System_As.setObjectName(_fromUtf8("actionSave_System_As"))
        self.actionExit = QtGui.QAction(TestsWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionDemandStorage = QtGui.QAction(TestsWindow)
        self.actionDemandStorage.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/pics/pics/storage.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDemandStorage.setIcon(icon13)
        self.actionDemandStorage.setObjectName(_fromUtf8("actionDemandStorage"))

        self.retranslateUi(TestsWindow)
        self.tests_tabs.setCurrentIndex(0)
        QtCore.QObject.connect(self.add, QtCore.SIGNAL(_fromUtf8("clicked()")), TestsWindow.Add)
        QtCore.QObject.connect(self.remove, QtCore.SIGNAL(_fromUtf8("clicked()")), TestsWindow.Remove)
        QtCore.QObject.connect(self.run, QtCore.SIGNAL(_fromUtf8("clicked()")), TestsWindow.Run)
        QtCore.QObject.connect(self.vertical, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), TestsWindow.Replot)
        QtCore.QObject.connect(self.horizontal, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), TestsWindow.Replot)
        QtCore.QObject.connect(self.save, QtCore.SIGNAL(_fromUtf8("clicked()")), TestsWindow.Save)
        QtCore.QObject.connect(self.scaledown, QtCore.SIGNAL(_fromUtf8("clicked()")), TestsWindow.ScaleDown)
        QtCore.QObject.connect(self.scaleup, QtCore.SIGNAL(_fromUtf8("clicked()")), TestsWindow.ScaleUp)
        QtCore.QObject.connect(self.tests_tabs, QtCore.SIGNAL(_fromUtf8("currentChanged(int)")), TestsWindow.ChangeTab)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), TestsWindow.Generate)
        QtCore.QMetaObject.connectSlotsByName(TestsWindow)

    def retranslateUi(self, TestsWindow):
        TestsWindow.setWindowTitle(_translate("TestsWindow", "Run Multiple Tests", None))
        self.label_2.setText(_translate("TestsWindow", "Algorithm:", None))
        self.algorithm.setItemText(0, _translate("TestsWindow", "Ant Colony", None))
        self.algorithm.setItemText(1, _translate("TestsWindow", "Centralized", None))
        self.algorithm.setItemText(2, _translate("TestsWindow", "Decentralized", None))
        self.projects.headerItem().setText(0, _translate("TestsWindow", "Projects", None))
        self.add.setText(_translate("TestsWindow", "Add", None))
        self.remove.setText(_translate("TestsWindow", "Remove", None))
        self.pushButton.setText(_translate("TestsWindow", "Generate", None))
        self.run.setText(_translate("TestsWindow", "Run", None))
        self.tests_tabs.setTabText(self.tests_tabs.indexOf(self.tab), _translate("TestsWindow", "Tests", None))
        self.label.setText(_translate("TestsWindow", "Vertical axis:", None))
        self.label_3.setText(_translate("TestsWindow", "Horizontal axis:", None))
        self.vertical.setItemText(0, _translate("TestsWindow", "Number of assigned requests", None))
        self.vertical.setItemText(1, _translate("TestsWindow", "Number of replications", None))
        self.horizontal.setItemText(0, _translate("TestsWindow", "Computational nodes and data stores load", None))
        self.horizontal.setItemText(1, _translate("TestsWindow", "Computational nodes load (CPU and RAM)", None))
        self.horizontal.setItemText(2, _translate("TestsWindow", "CPU load", None))
        self.horizontal.setItemText(3, _translate("TestsWindow", "RAM load", None))
        self.horizontal.setItemText(4, _translate("TestsWindow", "Data stores load", None))
        self.tests_tabs.setTabText(self.tests_tabs.indexOf(self.Graphs), _translate("TestsWindow", "Graphs", None))
        self.actionSelect.setText(_translate("TestsWindow", "Select", None))
        self.actionSelect.setShortcut(_translate("TestsWindow", "Alt+1", None))
        self.actionVM.setText(_translate("TestsWindow", "Add VM", None))
        self.actionVM.setToolTip(_translate("TestsWindow", "Add VM", None))
        self.actionVM.setShortcut(_translate("TestsWindow", "Alt+2", None))
        self.actionEdge.setText(_translate("TestsWindow", "Add Virtual Channel", None))
        self.actionEdge.setToolTip(_translate("TestsWindow", "Add Virtual Channel", None))
        self.actionEdge.setShortcut(_translate("TestsWindow", "Alt+3", None))
        self.actionNew_System.setText(_translate("TestsWindow", "New Graph", None))
        self.actionNew_System.setShortcut(_translate("TestsWindow", "Ctrl+N", None))
        self.actionOpen_System.setText(_translate("TestsWindow", "Open Graph", None))
        self.actionOpen_System.setShortcut(_translate("TestsWindow", "Ctrl+O", None))
        self.actionSave_System.setText(_translate("TestsWindow", "Save Graph", None))
        self.actionSave_System.setShortcut(_translate("TestsWindow", "Ctrl+S", None))
        self.actionSave_System_As.setText(_translate("TestsWindow", "Save Graph As...", None))
        self.actionSave_System_As.setShortcut(_translate("TestsWindow", "Ctrl+Shift+S", None))
        self.actionExit.setText(_translate("TestsWindow", "Exit", None))
        self.actionExit.setShortcut(_translate("TestsWindow", "Ctrl+X", None))
        self.actionDemandStorage.setText(_translate("TestsWindow", "Add Storage", None))
        self.actionDemandStorage.setToolTip(_translate("TestsWindow", "Add Storage", None))
        self.actionDemandStorage.setShortcut(_translate("TestsWindow", "Alt+4", None))

from . import resources_rc
