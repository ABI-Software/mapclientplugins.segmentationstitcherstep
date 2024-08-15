"""
Dialog/UI for interacting with SegmentationStitcherModel.
"""
"""
Segmentation stitcher user interface.
"""
import webbrowser

from PySide6 import QtCore, QtWidgets

from cmlibs.maths.vectorops import dot, magnitude, mult, normalize, sub
from mapclientplugins.segmentationstitcherstep.view.ui_segmentationstitcherwidget import Ui_SegmentationStitcherWidget
from segmentationstitcher.annotation import AnnotationCategory


def QLineEdit_parseInt(lineedit):
    """
    Return integer from line edit text, or None if invalid.
    """
    try:
        text = lineedit.text()
        return int(text)
    except ValueError:
        pass
    return None


def QLineEdit_parseVector(lineedit):
    """
    Return one or more component real vector as list from comma separated text in QLineEdit widget
    or None if invalid.
    """
    try:
        text = lineedit.text()
        values = [float(value) for value in text.split(",")]
        return values
    except ValueError:
        pass
    return None

class SegmentationStitcherWidget(QtWidgets.QWidget):

    def __init__(self, model, parent=None):
        super(SegmentationStitcherWidget, self).__init__(parent)
        self._ui = Ui_SegmentationStitcherWidget()
        self._ui.setupUi(self)
        self._model = model
        self._ui.alignmentsceneviewerwidget.setContext(model.get_context())
        self._ui.alignmentsceneviewerwidget.setModel(model)
        # self._model.registerTransformationChangeCallback(self._transformationChanged)
        self._done_callback = None
        self._build_segments_list()
        self._build_annotationName_comboBox()
        self._build_annotationCategory_comboBox()
        self._make_connections()
        self._refresh_options()

    def _graphics_initialized(self):
        """
        Callback for when SceneviewerWidget is initialised.
        Set custom scene from model.
        """
        sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            scene = self._model.get_root_region().getScene()
            self._ui.alignmentsceneviewerwidget.setScene(scene)
            # self._ui.alignmentsceneviewerwidget.setSelectModeAll()
            sceneviewer.setLookatParametersNonSkew([2.0, -2.0, 1.0], [0.0, 0.0, 0.0], [0.0, 0.0, 1.0])
            sceneviewer.setTransparencyMode(sceneviewer.TRANSPARENCY_MODE_SLOW)
            self._viewAll_buttonClicked()

    def _transformation_changed(self):
        # self._ui.segmentRotation_lineEdit.setText(self._model.getRotationText())
        # self._ui.segmentTranslation_lineEdit.setText(self._model.getTranslationText())
        pass

    def _make_connections(self):
        self._ui.alignmentsceneviewerwidget.graphicsInitialized.connect(self._graphics_initialized)
        self._ui.documentation_pushButton.clicked.connect(self._documentation_buttonClicked)
        self._ui.done_pushButton.clicked.connect(self._done_buttonClicked)
        self._ui.stdViews_pushButton.clicked.connect(self._stdViews_buttonClicked)
        self._ui.viewAll_pushButton.clicked.connect(self._viewAll_buttonClicked)
        self._ui.segmentRotation_lineEdit.editingFinished.connect(self._segmentRotation_lineEditChanged)
        self._ui.segmentTranslation_lineEdit.editingFinished.connect(self._segmentTranslation_lineEditChanged)
        self._ui.segmentTransformationCalculate_pushButton.clicked.connect(
            self._segmentTransformationCalculate_buttonPressed)

        self._ui.displayAxes_checkBox.clicked.connect(self._displayAxes_clicked)
        self._ui.displayMarkerPoints_checkBox.clicked.connect(self._displayMarkerPoints_clicked)
        self._ui.displayMarkerNames_checkBox.clicked.connect(self._displayMarkerNames_clicked)

        self._ui.displayLineGeneral_checkBox.clicked.connect(self._displayLineGeneral_clicked)
        self._ui.displayLineGeneralRadius_checkBox.clicked.connect(self._displayLineGeneralRadius_clicked)
        self._ui.displayIndepNetworks_checkBox.clicked.connect(self._displayIndepNetworks_clicked)
        self._ui.displayIndepNetworksRadius_checkBox.clicked.connect(self._displayIndepNetworksRadius_clicked)
        self._ui.displayNetworkGroup1_checkBox.clicked.connect(self._displayNetworkGroup1_clicked)
        self._ui.displayNetworkGroup1Radius_checkBox.clicked.connect(self._displayNetworkGroup1Radius_clicked)
        self._ui.displayNetworkGroup2_checkBox.clicked.connect(self._displayNetworkGroup2_clicked)
        self._ui.displayNetworkGroup2Radius_checkBox.clicked.connect(self._displayNetworkGroup2Radius_clicked)

        self._ui.annotationName_comboBox.currentIndexChanged.connect(self._annotationName_changed)
        self._ui.annotationCategory_comboBox.currentIndexChanged.connect(self._annotationCategory_changed)

    def _refresh_options(self):
        self._ui.identifier_label.setText('Identifier:  ' + self._model.get_step_identifier())
        self._ui.displayAxes_checkBox.setChecked(self._model.is_display_axes())
        self._ui.displayMarkerPoints_checkBox.setChecked(self._model.is_display_marker_points())
        self._ui.displayMarkerNames_checkBox.setChecked(self._model.is_display_marker_names())

        self._ui.displayLineGeneral_checkBox.setChecked(self._model.is_display_line_general())
        self._ui.displayLineGeneralRadius_checkBox.setChecked(self._model.is_display_line_general_radius())
        self._ui.displayIndepNetworks_checkBox.setChecked(self._model.is_display_independent_networks())
        self._ui.displayIndepNetworksRadius_checkBox.setChecked(self._model.is_display_independent_networks_radius())
        self._ui.displayNetworkGroup1_checkBox.setChecked(self._model.is_display_network_group_1())
        self._ui.displayNetworkGroup1Radius_checkBox.setChecked(self._model.is_display_network_group_1_radius())
        self._ui.displayNetworkGroup2_checkBox.setChecked(self._model.is_display_network_group_2())
        self._ui.displayNetworkGroup2Radius_checkBox.setChecked(self._model.is_display_network_group_2_radius())

        self._refresh_segment_data()
        self._refresh_current_annotation_settings()
        self._ui.done_pushButton.setEnabled(True)

    @staticmethod
    def _refresh_comboBox_names(comboBox, names, current_name):
        comboBox.blockSignals(True)
        comboBox.clear()
        current_index = 0
        index = 0
        for name in names:
            comboBox.addItem(name)
            if name == current_name:
                current_index = index
            index += 1
        comboBox.setCurrentIndex(current_index)
        comboBox.blockSignals(False)

    @staticmethod
    def _select_comboBox_item(comboBox, names, current_name):
        """
        Don't build combobox, just show the current annotation or None.
        :param comboBox:
        :param names: List of all valid names, optionally including '-' for None.
        :param current_name: Item name, including '-' for None if allowed.
        """
        current_index = names.index(current_name)
        comboBox.setCurrentIndex(current_index)

    def _build_annotationName_comboBox(self):
        annotations = self._model.get_stitcher().get_annotations()
        current_annotation = self._model.get_current_annotation()
        self._refresh_comboBox_names(
            self._ui.annotationName_comboBox,
            ['-'] + [annotation.get_name() for annotation in annotations],
            current_annotation.get_name() if current_annotation else '-')

    def _select_current_annotation(self):
        annotations = self._model.get_stitcher().get_annotations()
        names = ['-'] + [annotation.get_name() for annotation in annotations]
        current_annotation = self._model.get_current_annotation()
        self._select_comboBox_item(
            self._ui.annotationName_comboBox, names, current_annotation.get_name() if current_annotation else '-')

    def _build_annotationCategory_comboBox(self):
        self._refresh_comboBox_names(
            self._ui.annotationCategory_comboBox,
            [category.name for category in AnnotationCategory],
            AnnotationCategory.EXCLUDE.name)

    def _refresh_current_annotation_settings(self):
        """
        Display current annotation settings.
        """
        current_annotation = self._model.get_current_annotation()
        enabled = current_annotation is not None
        self._ui.annotationName_comboBox.setEnabled(True)
        self._ui.annotationTerm_lineEdit.setText(
            current_annotation.get_term() if current_annotation else '')
        self._ui.annotationTerm_lineEdit.setEnabled(enabled)
        self._ui.annotationDimension_lineEdit.setText(
            str(current_annotation.get_dimension()) if current_annotation else '')
        self._ui.annotationDimension_lineEdit.setEnabled(enabled)
        if current_annotation:
            names = [category.name for category in AnnotationCategory]
            self._select_comboBox_item(
                self._ui.annotationCategory_comboBox, names, current_annotation.get_category().name)
            index = 0
            current_category_name = current_annotation.get_category().name
            for category in AnnotationCategory:
                if category.name == current_category_name:
                    self._ui.annotationCategory_comboBox.setCurrentIndex(index)
                index += 1
        self._ui.annotationCategory_comboBox.setEnabled(enabled)

    def _annotationName_changed(self, index):
        annotation_name = self._ui.annotationName_comboBox.itemText(index)
        self._model.set_current_annotation_by_name(annotation_name)
        self._refresh_current_annotation_settings()

    def _annotationCategory_changed(self, index):
        annotation_category_name = self._ui.annotationCategory_comboBox.itemText(index)
        self._model.set_current_annotation_category_by_name(annotation_category_name)

    def get_model(self):
            return self._model

    def _documentation_buttonClicked(self):
        webbrowser.open("https://abi-mapping-tools.readthedocs.io/en/latest/mapclientplugins.segmentationstitcherstep/docs/index.html")

    def register_done_callback(self, done_callback):
        self._done_callback = done_callback

    def _done_buttonClicked(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self._ui.dockWidget.setFloating(False)
        self._model.done()
        self._model = None
        self._done_callback()
        QtWidgets.QApplication.restoreOverrideCursor()

    def _stdViews_buttonClicked(self):
        sceneviewer = self._ui.alignmentsceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            result, eyePosition, lookatPosition, upVector = sceneviewer.getLookatParameters()
            upVector = normalize(upVector)
            viewVector = sub(lookatPosition, eyePosition)
            viewDistance = magnitude(viewVector)
            viewVector = normalize(viewVector)
            # viewX = dot(viewVector, [1.0, 0.0, 0.0])
            viewY = dot(viewVector, [0.0, 1.0, 0.0])
            viewZ = dot(viewVector, [0.0, 0.0, 1.0])
            # upX = dot(upVector, [1.0, 0.0, 0.0])
            upY = dot(upVector, [0.0, 1.0, 0.0])
            upZ = dot(upVector, [0.0, 0.0, 1.0])
            if (viewZ < -0.999) and (upY > 0.999):
                # XY -> XZ
                viewVector = [0.0, 1.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            elif (viewY > 0.999) and (upZ > 0.999):
                # XZ -> YZ
                viewVector = [-1.0, 0.0, 0.0]
                upVector = [0.0, 0.0, 1.0]
            else:
                # XY
                viewVector = [0.0, 0.0, -1.0]
                upVector = [0.0, 1.0, 0.0]
            eyePosition = sub(lookatPosition, mult(viewVector, viewDistance))
            sceneviewer.setLookatParametersNonSkew(eyePosition, lookatPosition, upVector)

    def _viewAll_buttonClicked(self):
        if self._ui.alignmentsceneviewerwidget.getSceneviewer() is not None:
            self._ui.alignmentsceneviewerwidget.viewAll()

    def _segmentTransformationCalculate_buttonPressed(self):
        pass

    def _build_segments_list(self):
        """
        Fill the segments list including visibility check boxes.
        """
        if self._ui.segments_listWidget is not None:
            self._ui.segments_listWidget.clear()  # Must clear or holds on to graphics references
        stitcher = self._model.get_stitcher()
        segments = stitcher.get_segments()
        for segment in segments:
            name = segment.get_name()
            item = QtWidgets.QListWidgetItem(name)
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsUserCheckable)
            visible = segment.get_base_region().getScene().getVisibilityFlag()
            item.setCheckState(QtCore.Qt.CheckState.Checked if visible else QtCore.Qt.CheckState.Unchecked)
            self._ui.segments_listWidget.addItem(item)
            if segment == self._model.get_current_segment():
                self._ui.segments_listWidget.setCurrentItem(item)
        self._ui.segments_listWidget.itemClicked.connect(self._segments_list_itemClicked)
        self._ui.segments_listWidget.show()

    def _segments_list_itemClicked(self, item):
        """
        Either changes visibility flag or selects current segment.
        """
        clicked_index = self._ui.segments_listWidget.row(item)
        stitcher = self._model.get_stitcher()
        segments = stitcher.get_segments()
        segment = segments[clicked_index]
        visibility_flag = item.checkState() == QtCore.Qt.CheckState.Checked
        segment.get_base_region().getScene().setVisibilityFlag(visibility_flag)
        selected_modelIndex = self._ui.segments_listWidget.currentIndex()
        if clicked_index == selected_modelIndex.row():
            self._model.set_current_segment(segment)
            self._refresh_segment_data()

    def _refresh_segment_data(self):
        segment = self._model.get_current_segment()
        realFormat = "{:.7g}"
        rotation = segment.get_rotation()
        self._ui.segmentRotation_lineEdit.setText(", ".join(realFormat.format(value) for value in rotation))
        translation = segment.get_translation()
        self._ui.segmentTranslation_lineEdit.setText(", ".join(realFormat.format(value) for value in translation))

    def _segmentRotation_lineEditChanged(self):
        segment = self._model.get_current_segment()
        rotation = QLineEdit_parseVector(self._ui.segmentRotation_lineEdit)
        if rotation:
            while len(rotation) < 3:
                rotation.append(0.0)
            if len(rotation) > 3:
                rotation = rotation[:3]
            segment.set_rotation(rotation)
            self._model.set_segment_scene_transformation(segment)
        self._refresh_segment_data()

    def _segmentTranslation_lineEditChanged(self):
        segment = self._model.get_current_segment()
        translation = QLineEdit_parseVector(self._ui.segmentTranslation_lineEdit)
        if translation:
            while len(translation) < 3:
                translation.append(0.0)
            if len(translation) > 3:
                translation = translation[:3]
            segment.set_translation(translation)
            self._model.set_segment_scene_transformation(segment)
        self._refresh_segment_data()

    def _displayAxes_clicked(self):
        self._model.set_display_axes(self._ui.displayAxes_checkBox.isChecked())

    def _displayMarkerPoints_clicked(self):
        self._model.set_display_marker_points(self._ui.displayMarkerPoints_checkBox.isChecked())

    def _displayMarkerNames_clicked(self):
        self._model.set_display_marker_names(self._ui.displayMarkerNames_checkBox.isChecked())

    def _displayLineGeneral_clicked(self):
        self._model.set_display_line_general(self._ui.displayLineGeneral_checkBox.isChecked())

    def _displayLineGeneralRadius_clicked(self):
        self._model.set_display_line_general_radius(self._ui.displayLineGeneralRadius_checkBox.isChecked())

    def _displayIndepNetworks_clicked(self):
        self._model.set_display_independent_networks(self._ui.displayIndepNetworks_checkBox.isChecked())

    def _displayIndepNetworksRadius_clicked(self):
        self._model.set_display_independent_networks_radius(self._ui.displayIndepNetworksRadius_checkBox.isChecked())

    def _displayNetworkGroup1_clicked(self):
        self._model.set_display_network_group_1(self._ui.displayNetworkGroup1_checkBox.isChecked())

    def _displayNetworkGroup1Radius_clicked(self):
        self._model.set_display_network_group_1_radius(self._ui.displayNetworkGroup1Radius_checkBox.isChecked())

    def _displayNetworkGroup2_clicked(self):
        self._model.set_display_network_group_2(self._ui.displayNetworkGroup2_checkBox.isChecked())

    def _displayNetworkGroup2Radius_clicked(self):
        self._model.set_display_network_group_2_radius(self._ui.displayNetworkGroup2Radius_checkBox.isChecked())
