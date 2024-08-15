# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuredialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_ConfigureDialog(object):
    def setupUi(self, ConfigureDialog):
        if not ConfigureDialog.objectName():
            ConfigureDialog.setObjectName(u"ConfigureDialog")
        ConfigureDialog.resize(418, 303)
        self.gridLayout = QGridLayout(ConfigureDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.configGroupBox = QGroupBox(ConfigureDialog)
        self.configGroupBox.setObjectName(u"configGroupBox")
        self.formLayout = QFormLayout(self.configGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label0 = QLabel(self.configGroupBox)
        self.label0.setObjectName(u"label0")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label0)

        self.lineEdit0 = QLineEdit(self.configGroupBox)
        self.lineEdit0.setObjectName(u"lineEdit0")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit0)

        self.networkGroup1Keywords_label = QLabel(self.configGroupBox)
        self.networkGroup1Keywords_label.setObjectName(u"networkGroup1Keywords_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.networkGroup1Keywords_label)

        self.networkGroup1Keywords_lineEdit = QLineEdit(self.configGroupBox)
        self.networkGroup1Keywords_lineEdit.setObjectName(u"networkGroup1Keywords_lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.networkGroup1Keywords_lineEdit)

        self.networkGroup2Keywords_label = QLabel(self.configGroupBox)
        self.networkGroup2Keywords_label.setObjectName(u"networkGroup2Keywords_label")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.networkGroup2Keywords_label)

        self.networkGroup2Keywords_lineEdit = QLineEdit(self.configGroupBox)
        self.networkGroup2Keywords_lineEdit.setObjectName(u"networkGroup2Keywords_lineEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.networkGroup2Keywords_lineEdit)


        self.gridLayout.addWidget(self.configGroupBox, 0, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(ConfigureDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)


        self.retranslateUi(ConfigureDialog)
        self.buttonBox.accepted.connect(ConfigureDialog.accept)
        self.buttonBox.rejected.connect(ConfigureDialog.reject)

        QMetaObject.connectSlotsByName(ConfigureDialog)
    # setupUi

    def retranslateUi(self, ConfigureDialog):
        ConfigureDialog.setWindowTitle(QCoreApplication.translate("ConfigureDialog", u"Configure Segmentation Stitcher", None))
        self.configGroupBox.setTitle("")
        self.label0.setText(QCoreApplication.translate("ConfigureDialog", u"identifier:  ", None))
        self.networkGroup1Keywords_label.setText(QCoreApplication.translate("ConfigureDialog", u"Network group 1 keywords:", None))
#if QT_CONFIG(tooltip)
        self.networkGroup1Keywords_lineEdit.setToolTip(QCoreApplication.translate("ConfigureDialog", u"<html><head/><body><p>Segmented networks annotated with any of these comma separated keywords are initially assigned to network group 1, allowing them to be stitched together.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.networkGroup2Keywords_label.setText(QCoreApplication.translate("ConfigureDialog", u"Network group 2 keywords:", None))
#if QT_CONFIG(tooltip)
        self.networkGroup2Keywords_lineEdit.setToolTip(QCoreApplication.translate("ConfigureDialog", u"<html><head/><body><p>Segmented networks annotated with any of these comma separated keywords are initially assigned to network group 2, allowing them to be stitched together.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

