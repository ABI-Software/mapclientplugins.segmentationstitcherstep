# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'segmentationstitcherwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDockWidget,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QScrollArea, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

from cmlibs.widgets.alignmentsceneviewerwidget import AlignmentSceneviewerWidget

class Ui_SegmentationStitcherWidget(object):
    def setupUi(self, SegmentationStitcherWidget):
        if not SegmentationStitcherWidget.objectName():
            SegmentationStitcherWidget.setObjectName(u"SegmentationStitcherWidget")
        SegmentationStitcherWidget.resize(1137, 878)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SegmentationStitcherWidget.sizePolicy().hasHeightForWidth())
        SegmentationStitcherWidget.setSizePolicy(sizePolicy)
        SegmentationStitcherWidget.setMinimumSize(QSize(0, 0))
        self.horizontalLayout = QHBoxLayout(SegmentationStitcherWidget)
        self.horizontalLayout.setSpacing(4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dockWidget = QDockWidget(SegmentationStitcherWidget)
        self.dockWidget.setObjectName(u"dockWidget")
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.identifier_label = QLabel(self.dockWidgetContents)
        self.identifier_label.setObjectName(u"identifier_label")
        sizePolicy.setHeightForWidth(self.identifier_label.sizePolicy().hasHeightForWidth())
        self.identifier_label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.identifier_label)

        self.segments_groupBox = QGroupBox(self.dockWidgetContents)
        self.segments_groupBox.setObjectName(u"segments_groupBox")
        sizePolicy.setHeightForWidth(self.segments_groupBox.sizePolicy().hasHeightForWidth())
        self.segments_groupBox.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.segments_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.segments_listWidget = QListWidget(self.segments_groupBox)
        self.segments_listWidget.setObjectName(u"segments_listWidget")

        self.verticalLayout_2.addWidget(self.segments_listWidget)

        self.stepedit_scrollArea = QScrollArea(self.segments_groupBox)
        self.stepedit_scrollArea.setObjectName(u"stepedit_scrollArea")
        sizePolicy.setHeightForWidth(self.stepedit_scrollArea.sizePolicy().hasHeightForWidth())
        self.stepedit_scrollArea.setSizePolicy(sizePolicy)
        self.stepedit_scrollArea.setFrameShape(QFrame.NoFrame)
        self.stepedit_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.stepedit_scrollArea.setWidgetResizable(True)
        self.stepedit_scrollAreaWidgetContents = QWidget()
        self.stepedit_scrollAreaWidgetContents.setObjectName(u"stepedit_scrollAreaWidgetContents")
        self.stepedit_scrollAreaWidgetContents.setGeometry(QRect(0, -23, 343, 92))
        self.verticalLayout_3 = QVBoxLayout(self.stepedit_scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.segment_frame = QFrame(self.stepedit_scrollAreaWidgetContents)
        self.segment_frame.setObjectName(u"segment_frame")
        self.segment_frame.setFrameShape(QFrame.StyledPanel)
        self.segment_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.segment_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.segmentTransformation_groupBox = QGroupBox(self.segment_frame)
        self.segmentTransformation_groupBox.setObjectName(u"segmentTransformation_groupBox")
        self.formLayout = QFormLayout(self.segmentTransformation_groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.segmentRotation_label = QLabel(self.segmentTransformation_groupBox)
        self.segmentRotation_label.setObjectName(u"segmentRotation_label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.segmentRotation_label)

        self.segmentRotation_lineEdit = QLineEdit(self.segmentTransformation_groupBox)
        self.segmentRotation_lineEdit.setObjectName(u"segmentRotation_lineEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.segmentRotation_lineEdit)

        self.segmentTranslation_label = QLabel(self.segmentTransformation_groupBox)
        self.segmentTranslation_label.setObjectName(u"segmentTranslation_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.segmentTranslation_label)

        self.segmentTranslation_lineEdit = QLineEdit(self.segmentTransformation_groupBox)
        self.segmentTranslation_lineEdit.setObjectName(u"segmentTranslation_lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.segmentTranslation_lineEdit)


        self.verticalLayout_5.addWidget(self.segmentTransformation_groupBox)


        self.verticalLayout_3.addWidget(self.segment_frame)

        self.stepedit_scrollArea.setWidget(self.stepedit_scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.stepedit_scrollArea)


        self.verticalLayout.addWidget(self.segments_groupBox)

        self.connections_groupBox = QGroupBox(self.dockWidgetContents)
        self.connections_groupBox.setObjectName(u"connections_groupBox")
        self.formLayout_3 = QFormLayout(self.connections_groupBox)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.connectionsControls_frame = QFrame(self.connections_groupBox)
        self.connectionsControls_frame.setObjectName(u"connectionsControls_frame")
        sizePolicy.setHeightForWidth(self.connectionsControls_frame.sizePolicy().hasHeightForWidth())
        self.connectionsControls_frame.setSizePolicy(sizePolicy)
        self.connectionsControls_frame.setFrameShape(QFrame.StyledPanel)
        self.connectionsControls_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.connectionsControls_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.conntectionsNew_pushButton = QPushButton(self.connectionsControls_frame)
        self.conntectionsNew_pushButton.setObjectName(u"conntectionsNew_pushButton")

        self.horizontalLayout_11.addWidget(self.conntectionsNew_pushButton)

        self.connectionsDelete_pushButton = QPushButton(self.connectionsControls_frame)
        self.connectionsDelete_pushButton.setObjectName(u"connectionsDelete_pushButton")

        self.horizontalLayout_11.addWidget(self.connectionsDelete_pushButton)


        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.connectionsControls_frame)

        self.connections_listWidget = QListWidget(self.connections_groupBox)
        self.connections_listWidget.setObjectName(u"connections_listWidget")

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.connections_listWidget)

        self.connectionsOptimizeAlignment_pushButton = QPushButton(self.connections_groupBox)
        self.connectionsOptimizeAlignment_pushButton.setObjectName(u"connectionsOptimizeAlignment_pushButton")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.connectionsOptimizeAlignment_pushButton)


        self.verticalLayout.addWidget(self.connections_groupBox)

        self.controls_tabWidget = QTabWidget(self.dockWidgetContents)
        self.controls_tabWidget.setObjectName(u"controls_tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.controls_tabWidget.sizePolicy().hasHeightForWidth())
        self.controls_tabWidget.setSizePolicy(sizePolicy2)
        self.display_tab = QWidget()
        self.display_tab.setObjectName(u"display_tab")
        self.verticalLayout_7 = QVBoxLayout(self.display_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.displayMisc_frame = QFrame(self.display_tab)
        self.displayMisc_frame.setObjectName(u"displayMisc_frame")
        self.displayMisc_frame.setFrameShape(QFrame.StyledPanel)
        self.displayMisc_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.displayMisc_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.displayMisc_frame)

        self.displayMarker_frame = QFrame(self.display_tab)
        self.displayMarker_frame.setObjectName(u"displayMarker_frame")
        self.displayMarker_frame.setFrameShape(QFrame.StyledPanel)
        self.displayMarker_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.displayMarker_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.displayMarkerNames_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerNames_checkBox.setObjectName(u"displayMarkerNames_checkBox")

        self.gridLayout.addWidget(self.displayMarkerNames_checkBox, 3, 2, 1, 1)

        self.displayMarkerPoints_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayMarkerPoints_checkBox.setObjectName(u"displayMarkerPoints_checkBox")

        self.gridLayout.addWidget(self.displayMarkerPoints_checkBox, 3, 1, 1, 1)

        self.displayAxes_checkBox = QCheckBox(self.displayMarker_frame)
        self.displayAxes_checkBox.setObjectName(u"displayAxes_checkBox")

        self.gridLayout.addWidget(self.displayAxes_checkBox, 3, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.displayMarker_frame)

        self.displayLineCategories_groupBox = QGroupBox(self.display_tab)
        self.displayLineCategories_groupBox.setObjectName(u"displayLineCategories_groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.displayLineCategories_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.displayLineGeneral_frame = QFrame(self.displayLineCategories_groupBox)
        self.displayLineGeneral_frame.setObjectName(u"displayLineGeneral_frame")
        self.displayLineGeneral_frame.setFrameShape(QFrame.StyledPanel)
        self.displayLineGeneral_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.displayLineGeneral_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.displayLineGeneral_checkBox = QCheckBox(self.displayLineGeneral_frame)
        self.displayLineGeneral_checkBox.setObjectName(u"displayLineGeneral_checkBox")

        self.horizontalLayout_9.addWidget(self.displayLineGeneral_checkBox)

        self.displayLineGeneralRadius_checkBox = QCheckBox(self.displayLineGeneral_frame)
        self.displayLineGeneralRadius_checkBox.setObjectName(u"displayLineGeneralRadius_checkBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.displayLineGeneralRadius_checkBox.sizePolicy().hasHeightForWidth())
        self.displayLineGeneralRadius_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_9.addWidget(self.displayLineGeneralRadius_checkBox)

        self.displayLineGeneralTrans_checkBox = QCheckBox(self.displayLineGeneral_frame)
        self.displayLineGeneralTrans_checkBox.setObjectName(u"displayLineGeneralTrans_checkBox")

        self.horizontalLayout_9.addWidget(self.displayLineGeneralTrans_checkBox)


        self.verticalLayout_4.addWidget(self.displayLineGeneral_frame)

        self.displayIndepNetworks_frame = QFrame(self.displayLineCategories_groupBox)
        self.displayIndepNetworks_frame.setObjectName(u"displayIndepNetworks_frame")
        self.displayIndepNetworks_frame.setFrameShape(QFrame.StyledPanel)
        self.displayIndepNetworks_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.displayIndepNetworks_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.displayIndepNetworks_checkBox = QCheckBox(self.displayIndepNetworks_frame)
        self.displayIndepNetworks_checkBox.setObjectName(u"displayIndepNetworks_checkBox")

        self.horizontalLayout_10.addWidget(self.displayIndepNetworks_checkBox)

        self.displayIndepNetworksRadius_checkBox = QCheckBox(self.displayIndepNetworks_frame)
        self.displayIndepNetworksRadius_checkBox.setObjectName(u"displayIndepNetworksRadius_checkBox")

        self.horizontalLayout_10.addWidget(self.displayIndepNetworksRadius_checkBox)

        self.displayIndepNetworksTrans_checkBox = QCheckBox(self.displayIndepNetworks_frame)
        self.displayIndepNetworksTrans_checkBox.setObjectName(u"displayIndepNetworksTrans_checkBox")

        self.horizontalLayout_10.addWidget(self.displayIndepNetworksTrans_checkBox)


        self.verticalLayout_4.addWidget(self.displayIndepNetworks_frame)

        self.displayNetworkGroup1_frame = QFrame(self.displayLineCategories_groupBox)
        self.displayNetworkGroup1_frame.setObjectName(u"displayNetworkGroup1_frame")
        self.displayNetworkGroup1_frame.setFrameShape(QFrame.StyledPanel)
        self.displayNetworkGroup1_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.displayNetworkGroup1_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.displayNetworkGroup1_checkBox = QCheckBox(self.displayNetworkGroup1_frame)
        self.displayNetworkGroup1_checkBox.setObjectName(u"displayNetworkGroup1_checkBox")

        self.horizontalLayout_6.addWidget(self.displayNetworkGroup1_checkBox)

        self.displayNetworkGroup1Radius_checkBox = QCheckBox(self.displayNetworkGroup1_frame)
        self.displayNetworkGroup1Radius_checkBox.setObjectName(u"displayNetworkGroup1Radius_checkBox")
        sizePolicy3.setHeightForWidth(self.displayNetworkGroup1Radius_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNetworkGroup1Radius_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.displayNetworkGroup1Radius_checkBox)

        self.displayNetworkGroup1Trans_checkBox = QCheckBox(self.displayNetworkGroup1_frame)
        self.displayNetworkGroup1Trans_checkBox.setObjectName(u"displayNetworkGroup1Trans_checkBox")

        self.horizontalLayout_6.addWidget(self.displayNetworkGroup1Trans_checkBox)


        self.verticalLayout_4.addWidget(self.displayNetworkGroup1_frame)

        self.displayNetworkGroup2_frame = QFrame(self.displayLineCategories_groupBox)
        self.displayNetworkGroup2_frame.setObjectName(u"displayNetworkGroup2_frame")
        self.displayNetworkGroup2_frame.setFrameShape(QFrame.StyledPanel)
        self.displayNetworkGroup2_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.displayNetworkGroup2_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.displayNetworkGroup2_checkBox = QCheckBox(self.displayNetworkGroup2_frame)
        self.displayNetworkGroup2_checkBox.setObjectName(u"displayNetworkGroup2_checkBox")

        self.horizontalLayout_4.addWidget(self.displayNetworkGroup2_checkBox)

        self.displayNetworkGroup2Radius_checkBox = QCheckBox(self.displayNetworkGroup2_frame)
        self.displayNetworkGroup2Radius_checkBox.setObjectName(u"displayNetworkGroup2Radius_checkBox")
        sizePolicy3.setHeightForWidth(self.displayNetworkGroup2Radius_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNetworkGroup2Radius_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.displayNetworkGroup2Radius_checkBox)

        self.displayNetworkGroup2Trans_checkBox = QCheckBox(self.displayNetworkGroup2_frame)
        self.displayNetworkGroup2Trans_checkBox.setObjectName(u"displayNetworkGroup2Trans_checkBox")

        self.horizontalLayout_4.addWidget(self.displayNetworkGroup2Trans_checkBox)


        self.verticalLayout_4.addWidget(self.displayNetworkGroup2_frame)


        self.verticalLayout_7.addWidget(self.displayLineCategories_groupBox)

        self.displayEndPoint_groupBox = QGroupBox(self.display_tab)
        self.displayEndPoint_groupBox.setObjectName(u"displayEndPoint_groupBox")
        self.horizontalLayout_7 = QHBoxLayout(self.displayEndPoint_groupBox)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.displayEndPointBestFitLines_checkBox = QCheckBox(self.displayEndPoint_groupBox)
        self.displayEndPointBestFitLines_checkBox.setObjectName(u"displayEndPointBestFitLines_checkBox")

        self.horizontalLayout_7.addWidget(self.displayEndPointBestFitLines_checkBox)

        self.displayEndPointDirections_checkBox = QCheckBox(self.displayEndPoint_groupBox)
        self.displayEndPointDirections_checkBox.setObjectName(u"displayEndPointDirections_checkBox")
        sizePolicy3.setHeightForWidth(self.displayEndPointDirections_checkBox.sizePolicy().hasHeightForWidth())
        self.displayEndPointDirections_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.displayEndPointDirections_checkBox)

        self.displayEndPointRadius_checkBox = QCheckBox(self.displayEndPoint_groupBox)
        self.displayEndPointRadius_checkBox.setObjectName(u"displayEndPointRadius_checkBox")

        self.horizontalLayout_7.addWidget(self.displayEndPointRadius_checkBox)

        self.displayEndPointTrans_checkBox = QCheckBox(self.displayEndPoint_groupBox)
        self.displayEndPointTrans_checkBox.setObjectName(u"displayEndPointTrans_checkBox")

        self.horizontalLayout_7.addWidget(self.displayEndPointTrans_checkBox)


        self.verticalLayout_7.addWidget(self.displayEndPoint_groupBox)

        self.displayEndPoints_frame = QFrame(self.display_tab)
        self.displayEndPoints_frame.setObjectName(u"displayEndPoints_frame")
        self.displayEndPoints_frame.setFrameShape(QFrame.StyledPanel)
        self.displayEndPoints_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.displayEndPoints_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_7.addWidget(self.displayEndPoints_frame)

        self.displayScale_frame = QFrame(self.display_tab)
        self.displayScale_frame.setObjectName(u"displayScale_frame")
        self.displayScale_frame.setFrameShape(QFrame.StyledPanel)
        self.displayScale_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.displayScale_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.displayRadiusScale_label = QLabel(self.displayScale_frame)
        self.displayRadiusScale_label.setObjectName(u"displayRadiusScale_label")

        self.horizontalLayout_3.addWidget(self.displayRadiusScale_label)

        self.displayRadiusScale_lineEdit = QLineEdit(self.displayScale_frame)
        self.displayRadiusScale_lineEdit.setObjectName(u"displayRadiusScale_lineEdit")

        self.horizontalLayout_3.addWidget(self.displayRadiusScale_lineEdit)


        self.verticalLayout_7.addWidget(self.displayScale_frame)

        self.controls_tabWidget.addTab(self.display_tab, "")
        self.annotations_tab = QWidget()
        self.annotations_tab.setObjectName(u"annotations_tab")
        self.verticalLayout_12 = QVBoxLayout(self.annotations_tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.annotations_group_frame = QFrame(self.annotations_tab)
        self.annotations_group_frame.setObjectName(u"annotations_group_frame")
        self.annotations_group_frame.setFrameShape(QFrame.StyledPanel)
        self.annotations_group_frame.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.annotations_group_frame)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.annotationName_label = QLabel(self.annotations_group_frame)
        self.annotationName_label.setObjectName(u"annotationName_label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.annotationName_label)

        self.annotationTerm_label = QLabel(self.annotations_group_frame)
        self.annotationTerm_label.setObjectName(u"annotationTerm_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.annotationTerm_label)

        self.annotationTerm_lineEdit = QLineEdit(self.annotations_group_frame)
        self.annotationTerm_lineEdit.setObjectName(u"annotationTerm_lineEdit")
        self.annotationTerm_lineEdit.setEnabled(False)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.annotationTerm_lineEdit)

        self.annotationDimension_label = QLabel(self.annotations_group_frame)
        self.annotationDimension_label.setObjectName(u"annotationDimension_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.annotationDimension_label)

        self.annotationDimension_lineEdit = QLineEdit(self.annotations_group_frame)
        self.annotationDimension_lineEdit.setObjectName(u"annotationDimension_lineEdit")
        self.annotationDimension_lineEdit.setEnabled(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.annotationDimension_lineEdit)

        self.annotationCategory_label = QLabel(self.annotations_group_frame)
        self.annotationCategory_label.setObjectName(u"annotationCategory_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.annotationCategory_label)

        self.annotationCategory_comboBox = QComboBox(self.annotations_group_frame)
        self.annotationCategory_comboBox.setObjectName(u"annotationCategory_comboBox")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.annotationCategory_comboBox)

        self.annotationName_comboBox = QComboBox(self.annotations_group_frame)
        self.annotationName_comboBox.setObjectName(u"annotationName_comboBox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.annotationName_comboBox)

        self.annotationAlignWeight_label = QLabel(self.annotations_group_frame)
        self.annotationAlignWeight_label.setObjectName(u"annotationAlignWeight_label")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.annotationAlignWeight_label)

        self.annotationAlignWeight_lineEdit = QLineEdit(self.annotations_group_frame)
        self.annotationAlignWeight_lineEdit.setObjectName(u"annotationAlignWeight_lineEdit")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.annotationAlignWeight_lineEdit)

        self.annotiationSetByCategory_checkBox = QCheckBox(self.annotations_group_frame)
        self.annotiationSetByCategory_checkBox.setObjectName(u"annotiationSetByCategory_checkBox")
        self.annotiationSetByCategory_checkBox.setChecked(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.annotiationSetByCategory_checkBox)


        self.verticalLayout_12.addWidget(self.annotations_group_frame)

        self.controls_tabWidget.addTab(self.annotations_tab, "")

        self.verticalLayout.addWidget(self.controls_tabWidget)

        self.bottom_frame = QFrame(self.dockWidgetContents)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.documentation_pushButton = QPushButton(self.bottom_frame)
        self.documentation_pushButton.setObjectName(u"documentation_pushButton")

        self.horizontalLayout_2.addWidget(self.documentation_pushButton)

        self.viewAll_pushButton = QPushButton(self.bottom_frame)
        self.viewAll_pushButton.setObjectName(u"viewAll_pushButton")

        self.horizontalLayout_2.addWidget(self.viewAll_pushButton)

        self.stdViews_pushButton = QPushButton(self.bottom_frame)
        self.stdViews_pushButton.setObjectName(u"stdViews_pushButton")

        self.horizontalLayout_2.addWidget(self.stdViews_pushButton)

        self.done_pushButton = QPushButton(self.bottom_frame)
        self.done_pushButton.setObjectName(u"done_pushButton")
        sizePolicy3.setHeightForWidth(self.done_pushButton.sizePolicy().hasHeightForWidth())
        self.done_pushButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.done_pushButton)


        self.verticalLayout.addWidget(self.bottom_frame)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.alignmentsceneviewerwidget = AlignmentSceneviewerWidget(SegmentationStitcherWidget)
        self.alignmentsceneviewerwidget.setObjectName(u"alignmentsceneviewerwidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(1)
        sizePolicy4.setHeightForWidth(self.alignmentsceneviewerwidget.sizePolicy().hasHeightForWidth())
        self.alignmentsceneviewerwidget.setSizePolicy(sizePolicy4)
        self.alignmentsceneviewerwidget.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.alignmentsceneviewerwidget)


        self.retranslateUi(SegmentationStitcherWidget)

        self.controls_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SegmentationStitcherWidget)
    # setupUi

    def retranslateUi(self, SegmentationStitcherWidget):
        SegmentationStitcherWidget.setWindowTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Segmentation Stitcher", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Control Panel", None))
        self.identifier_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Identifier", None))
        self.segments_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Segments:", None))
        self.segmentTransformation_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Transformation:", None))
        self.segmentRotation_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Rotation:", None))
        self.segmentTranslation_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Translation:", None))
        self.connections_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Connections:", None))
        self.conntectionsNew_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"New...", None))
        self.connectionsDelete_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Delete...", None))
#if QT_CONFIG(tooltip)
        self.connectionsOptimizeAlignment_pushButton.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>Optimize  transformation of the second segment in the selected connection to align its network end points with those of the first segment.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.connectionsOptimizeAlignment_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Optimize Alignment...", None))
        self.displayMarkerNames_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Marker names", None))
        self.displayMarkerPoints_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Marker points", None))
        self.displayAxes_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Axes", None))
        self.displayLineCategories_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"Line Segmentations:", None))
        self.displayLineGeneral_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"General               ", None))
        self.displayLineGeneralRadius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayLineGeneralTrans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans.", None))
        self.displayIndepNetworks_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Indep. networks  ", None))
        self.displayIndepNetworksRadius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayIndepNetworksTrans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans.", None))
        self.displayNetworkGroup1_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Network group 1", None))
        self.displayNetworkGroup1Radius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayNetworkGroup1Trans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans.", None))
        self.displayNetworkGroup2_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Network group 2", None))
        self.displayNetworkGroup2Radius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayNetworkGroup2Trans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans.", None))
        self.displayEndPoint_groupBox.setTitle(QCoreApplication.translate("SegmentationStitcherWidget", u"End Points", None))
        self.displayEndPointBestFitLines_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Lines", None))
        self.displayEndPointDirections_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Tips", None))
        self.displayEndPointRadius_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius", None))
        self.displayEndPointTrans_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Trans.", None))
        self.displayRadiusScale_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Radius scale:", None))
        self.controls_tabWidget.setTabText(self.controls_tabWidget.indexOf(self.display_tab), QCoreApplication.translate("SegmentationStitcherWidget", u"Display", None))
        self.annotationName_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Name:", None))
        self.annotationTerm_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Term:", None))
        self.annotationDimension_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Dimension:", None))
        self.annotationCategory_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Category:", None))
        self.annotationAlignWeight_label.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Align Weight:", None))
#if QT_CONFIG(tooltip)
        self.annotationAlignWeight_lineEdit.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p><br/>Weight applied to this annotation/category when optimizing alignment.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.annotiationSetByCategory_checkBox.setToolTip(QCoreApplication.translate("SegmentationStitcherWidget", u"<html><head/><body><p>If checked, the values entered in the following are set for all annotations in the current category.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.annotiationSetByCategory_checkBox.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Set by category:", None))
        self.controls_tabWidget.setTabText(self.controls_tabWidget.indexOf(self.annotations_tab), QCoreApplication.translate("SegmentationStitcherWidget", u"Annotations", None))
        self.documentation_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Online Documentation", None))
        self.viewAll_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"View All", None))
        self.stdViews_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Std. Views", None))
        self.done_pushButton.setText(QCoreApplication.translate("SegmentationStitcherWidget", u"Done", None))
    # retranslateUi

