# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'marker.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSlider, QSpinBox, QStatusBar,
    QToolBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 721)
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_save_as = QAction(MainWindow)
        self.action_save_as.setObjectName(u"action_save_as")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_pic = QGroupBox(self.centralwidget)
        self.groupBox_pic.setObjectName(u"groupBox_pic")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_pic)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_pic = QLabel(self.groupBox_pic)
        self.label_pic.setObjectName(u"label_pic")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pic.sizePolicy().hasHeightForWidth())
        self.label_pic.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_pic)


        self.verticalLayout_4.addWidget(self.groupBox_pic)

        self.groupBox_config = QGroupBox(self.centralwidget)
        self.groupBox_config.setObjectName(u"groupBox_config")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_config)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_text = QHBoxLayout()
        self.horizontalLayout_text.setObjectName(u"horizontalLayout_text")
        self.label_text = QLabel(self.groupBox_config)
        self.label_text.setObjectName(u"label_text")

        self.horizontalLayout_text.addWidget(self.label_text)

        self.lineEdit_text = QLineEdit(self.groupBox_config)
        self.lineEdit_text.setObjectName(u"lineEdit_text")

        self.horizontalLayout_text.addWidget(self.lineEdit_text)


        self.verticalLayout_3.addLayout(self.horizontalLayout_text)

        self.horizontalLayout_font = QHBoxLayout()
        self.horizontalLayout_font.setObjectName(u"horizontalLayout_font")
        self.label_size = QLabel(self.groupBox_config)
        self.label_size.setObjectName(u"label_size")

        self.horizontalLayout_font.addWidget(self.label_size)

        self.spinBox_size = QSpinBox(self.groupBox_config)
        self.spinBox_size.setObjectName(u"spinBox_size")
        self.spinBox_size.setMaximum(999)
        self.spinBox_size.setValue(50)

        self.horizontalLayout_font.addWidget(self.spinBox_size)


        self.verticalLayout_3.addLayout(self.horizontalLayout_font)

        self.horizontalLayout_space = QHBoxLayout()
        self.horizontalLayout_space.setObjectName(u"horizontalLayout_space")
        self.label_space = QLabel(self.groupBox_config)
        self.label_space.setObjectName(u"label_space")

        self.horizontalLayout_space.addWidget(self.label_space)

        self.spinBox_space = QSpinBox(self.groupBox_config)
        self.spinBox_space.setObjectName(u"spinBox_space")
        self.spinBox_space.setMaximum(999)
        self.spinBox_space.setValue(75)

        self.horizontalLayout_space.addWidget(self.spinBox_space)


        self.verticalLayout_3.addLayout(self.horizontalLayout_space)

        self.groupBox_color = QGroupBox(self.groupBox_config)
        self.groupBox_color.setObjectName(u"groupBox_color")
        self.verticalLayout = QVBoxLayout(self.groupBox_color)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_red = QHBoxLayout()
        self.horizontalLayout_red.setObjectName(u"horizontalLayout_red")
        self.label_red = QLabel(self.groupBox_color)
        self.label_red.setObjectName(u"label_red")

        self.horizontalLayout_red.addWidget(self.label_red)

        self.horizontalSlider_red = QSlider(self.groupBox_color)
        self.horizontalSlider_red.setObjectName(u"horizontalSlider_red")
        self.horizontalSlider_red.setMaximum(255)
        self.horizontalSlider_red.setOrientation(Qt.Horizontal)

        self.horizontalLayout_red.addWidget(self.horizontalSlider_red)


        self.verticalLayout.addLayout(self.horizontalLayout_red)

        self.horizontalLayout_green = QHBoxLayout()
        self.horizontalLayout_green.setObjectName(u"horizontalLayout_green")
        self.label_green = QLabel(self.groupBox_color)
        self.label_green.setObjectName(u"label_green")

        self.horizontalLayout_green.addWidget(self.label_green)

        self.horizontalSlider_green = QSlider(self.groupBox_color)
        self.horizontalSlider_green.setObjectName(u"horizontalSlider_green")
        self.horizontalSlider_green.setMaximum(255)
        self.horizontalSlider_green.setValue(178)
        self.horizontalSlider_green.setOrientation(Qt.Horizontal)

        self.horizontalLayout_green.addWidget(self.horizontalSlider_green)


        self.verticalLayout.addLayout(self.horizontalLayout_green)

        self.horizontalLayout_blue = QHBoxLayout()
        self.horizontalLayout_blue.setObjectName(u"horizontalLayout_blue")
        self.label_blue = QLabel(self.groupBox_color)
        self.label_blue.setObjectName(u"label_blue")

        self.horizontalLayout_blue.addWidget(self.label_blue)

        self.horizontalSlider_blue = QSlider(self.groupBox_color)
        self.horizontalSlider_blue.setObjectName(u"horizontalSlider_blue")
        self.horizontalSlider_blue.setMaximum(255)
        self.horizontalSlider_blue.setValue(148)
        self.horizontalSlider_blue.setOrientation(Qt.Horizontal)

        self.horizontalLayout_blue.addWidget(self.horizontalSlider_blue)


        self.verticalLayout.addLayout(self.horizontalLayout_blue)

        self.horizontalLayout_opacity = QHBoxLayout()
        self.horizontalLayout_opacity.setObjectName(u"horizontalLayout_opacity")
        self.label_opacity = QLabel(self.groupBox_color)
        self.label_opacity.setObjectName(u"label_opacity")

        self.horizontalLayout_opacity.addWidget(self.label_opacity)

        self.horizontalSlider_opacity = QSlider(self.groupBox_color)
        self.horizontalSlider_opacity.setObjectName(u"horizontalSlider_opacity")
        self.horizontalSlider_opacity.setMaximum(100)
        self.horizontalSlider_opacity.setValue(15)
        self.horizontalSlider_opacity.setOrientation(Qt.Horizontal)
        self.horizontalSlider_opacity.setInvertedAppearance(False)
        self.horizontalSlider_opacity.setInvertedControls(False)

        self.horizontalLayout_opacity.addWidget(self.horizontalSlider_opacity)


        self.verticalLayout.addLayout(self.horizontalLayout_opacity)


        self.verticalLayout_3.addWidget(self.groupBox_color)

        self.horizontalLayout_angle = QHBoxLayout()
        self.horizontalLayout_angle.setObjectName(u"horizontalLayout_angle")
        self.label_angle = QLabel(self.groupBox_config)
        self.label_angle.setObjectName(u"label_angle")

        self.horizontalLayout_angle.addWidget(self.label_angle)

        self.horizontalSlider_angle = QSlider(self.groupBox_config)
        self.horizontalSlider_angle.setObjectName(u"horizontalSlider_angle")
        self.horizontalSlider_angle.setMaximum(360)
        self.horizontalSlider_angle.setValue(30)
        self.horizontalSlider_angle.setOrientation(Qt.Horizontal)

        self.horizontalLayout_angle.addWidget(self.horizontalSlider_angle)


        self.verticalLayout_3.addLayout(self.horizontalLayout_angle)

        self.horizontalLayout_quality = QHBoxLayout()
        self.horizontalLayout_quality.setObjectName(u"horizontalLayout_quality")
        self.label_quality = QLabel(self.groupBox_config)
        self.label_quality.setObjectName(u"label_quality")

        self.horizontalLayout_quality.addWidget(self.label_quality)

        self.horizontalSlider_quality = QSlider(self.groupBox_config)
        self.horizontalSlider_quality.setObjectName(u"horizontalSlider_quality")
        self.horizontalSlider_quality.setMaximum(100)
        self.horizontalSlider_quality.setValue(100)
        self.horizontalSlider_quality.setOrientation(Qt.Horizontal)

        self.horizontalLayout_quality.addWidget(self.horizontalSlider_quality)


        self.verticalLayout_3.addLayout(self.horizontalLayout_quality)


        self.verticalLayout_4.addWidget(self.groupBox_config)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 522, 21))
        self.menu_F = QMenu(self.menubar)
        self.menu_F.setObjectName(u"menu_F")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_F.menuAction())
        self.menu_F.addAction(self.action_open)
        self.menu_F.addAction(self.action_save)
        self.menu_F.addAction(self.action_save_as)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_save)
        self.toolBar.addAction(self.action_save_as)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u6253\u6c34\u5370", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00(O)", None))
#if QT_CONFIG(shortcut)
        self.action_open.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58(S)", None))
#if QT_CONFIG(shortcut)
        self.action_save.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.action_save_as.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a", None))
#if QT_CONFIG(shortcut)
        self.action_save_as.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Shift+S", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox_pic.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u6587\u4ef6\u540d", None))
        self.label_pic.setText("")
        self.groupBox_config.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u7f6e", None))
        self.label_text.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5370\u5185\u5bb9", None))
        self.lineEdit_text.setText(QCoreApplication.translate("MainWindow", u"H1DDENADM1N@GitHub", None))
        self.lineEdit_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"H1DDENADM1N@GitHub", None))
        self.label_size.setText(QCoreApplication.translate("MainWindow", u"\u5b57\u4f53\u5927\u5c0f", None))
        self.label_space.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5370\u95f4\u8ddd", None))
        self.groupBox_color.setTitle(QCoreApplication.translate("MainWindow", u"\u6c34\u5370\u989c\u8272", None))
        self.label_red.setText(QCoreApplication.translate("MainWindow", u"\u7ea2", None))
        self.label_green.setText(QCoreApplication.translate("MainWindow", u"\u7eff", None))
        self.label_blue.setText(QCoreApplication.translate("MainWindow", u"\u84dd", None))
        self.label_opacity.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u900f\u660e\u5ea6", None))
        self.label_angle.setText(QCoreApplication.translate("MainWindow", u"\u6c34\u5370\u65cb\u8f6c\u89d2\u5ea6", None))
        self.label_quality.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u56fe\u50cf\u8d28\u91cf", None))
        self.menu_F.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

