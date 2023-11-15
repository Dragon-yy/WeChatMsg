# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 779)
        MainWindow.setStyleSheet("\n"
                                 "/*去掉item虚线边框*/\n"
                                 "QListWidget, QListView, QTreeWidget, QTreeView {\n"
                                 "    outline: 0px;\n"
                                 "}\n"
                                 "/*设置左侧选项的最小最大宽度,文字颜色和背景颜色*/\n"
                                 "QListWidget {\n"
                                 "    min-width: 120px;\n"
                                 "    max-width: 120px;\n"
                                 "    color: black;\n"
                                 "    background: white;\n"
                                 "    border:none;\n"
                                 "}\n"
                                 "QListWidget::item{\n"
                                 "    height:80;\n"
                                 "}\n"
                                 "/*被选中时的背景颜色和左边框颜色*/\n"
                                 "QListWidget::item:selected {\n"
                                 "    background: rgb(204, 204, 204);\n"
                                 "    border-left: 4px solid rgb(9, 187, 7);\n"
                                 "}\n"
                                 "/*鼠标悬停颜色*/\n"
                                 "HistoryPanel::item:hover {\n"
                                 "    background: rgb(52, 52, 52);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_info = QtWidgets.QFrame(self.centralwidget)
        self.frame_info.setMinimumSize(QtCore.QSize(80, 500))
        self.frame_info.setMaximumSize(QtCore.QSize(80, 16777215))
        self.frame_info.setStyleSheet("background-color:rgb(240,240,240)")
        self.frame_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_info.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_info.setObjectName("frame_info")
        self.myavatar = QtWidgets.QLabel(self.frame_info)
        self.myavatar.setGeometry(QtCore.QRect(10, 40, 60, 60))
        self.myavatar.setObjectName("myavatar")
        self.listWidget = QtWidgets.QListWidget(self.frame_info)
        self.listWidget.setGeometry(QtCore.QRect(0, 230, 120, 331))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.frame_info)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(False)
        font.setWeight(50)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 23))
        self.menubar.setObjectName("menubar")
        self.menu_F = QtWidgets.QMenu(self.menubar)
        self.menu_F.setObjectName("menu_F")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_about = QtWidgets.QMenu(self.menubar)
        self.menu_about.setObjectName("menu_about")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.action.setFont(font)
        self.action.setObjectName("action")
        self.action_desc = QtWidgets.QAction(MainWindow)
        self.action_desc.setObjectName("action_desc")
        self.menu_F.addSeparator()
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.action_3)
        self.menu_F.addAction(self.action_4)
        self.menu_2.addAction(self.action)
        self.menu_about.addAction(self.action_desc)
        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_about.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.myavatar.setText(_translate("MainWindow", "avatar"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "新建项目"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "新建项目"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "新建项目"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "新建项目"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "新建项目"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.menu_F.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu.setTitle(_translate("MainWindow", "编辑"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu_about.setTitle(_translate("MainWindow", "关于"))
        self.action_3.setText(_translate("MainWindow", "保存"))
        self.action_4.setText(_translate("MainWindow", "退出"))
        self.action.setText(_translate("MainWindow", "关于"))
        self.action_desc.setText(_translate("MainWindow", "说明"))
