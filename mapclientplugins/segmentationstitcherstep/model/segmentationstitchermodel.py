"""
Segmentation stitcher with visualisation.
"""
import math
import os
import json

from cmlibs.maths.vectorops import add, axis_angle_to_rotation_matrix, euler_to_rotation_matrix, matrix_mult, \
    rotation_matrix_to_euler
from cmlibs.utils.zinc.finiteelement import evaluate_field_nodeset_range
from cmlibs.utils.zinc.general import ChangeManager
from cmlibs.zinc.field import Field
from cmlibs.zinc.glyph import Glyph
from cmlibs.zinc.graphics import Graphicslineattributes
from cmlibs.zinc.material import Material
from cmlibs.zinc.scenefilter import Scenefilter
from segmentationstitcher.annotation import AnnotationCategory
from segmentationstitcher.stitcher import Stitcher


class SegmentationStitcherModel(object):
    """
    Geometric fit model adding visualisations to github.com/ABI-Software/scaffoldfitter
    """

    def __init__(self, segmentation_file_locations, location, step_identifier,
                 network_group_1_keywords, network_group2_keywords):
        """
        :param location: Path to folder for mapclient step name.
        :param step_identifier: Workflow step name.
        :param network_group_1_keywords: List of keywords. Segmented networks annotated with any of these keywords are
        initially assigned to network group 1, allowing them to be stitched together.
        :param network_group2_keywords: List of keywords. Segmented networks annotated with any of these keywords are
        initially assigned to network group 2, allowing them to be stitched together.
        """
        self._stitcher = Stitcher(segmentation_file_locations, network_group_1_keywords, network_group2_keywords)
        self._location = os.path.join(location, step_identifier)
        self._step_identifier = step_identifier
        self._category_graphics_info = [
            (AnnotationCategory.GENERAL, "display_line_general", "green"),
            (AnnotationCategory.INDEPENDENT_NETWORK, "display_independent_networks", "yellow"),
            (AnnotationCategory.NETWORK_GROUP_1, "display_network_group_1", "mid blue"),
            (AnnotationCategory.NETWORK_GROUP_2, "display_network_group_2", "orange")
        ]
        self._end_point_material_name = "grey50"
        self._init_graphics_modules()
        self._display_settings = {
            "display_axes": True,
            "display_marker_points": True,
            "display_marker_names": False,
            "display_line_general": True,
            "display_line_general_radius": False,
            "display_line_general_trans": False,
            "display_network_group_1": True,
            "display_network_group_1_radius": False,
            "display_network_group_1_trans": False,
            "display_network_group_2": True,
            "display_network_group_2_radius": False,
            "display_network_group_2_trans": False,
            "display_independent_networks": True,
            "display_independent_networks_radius": False,
            "display_independent_networks_trans": False,
            "display_end_point_directions": True,
            "display_end_point_best_fit_lines": True,
            "display_end_point_radius": False,
            "display_end_point_trans": False,
            "display_radius_scale": 1.0
        }
        self._load_settings()
        self.create_graphics()
        segments = self._stitcher.get_segments()
        for segment in segments:
            self._set_segment_scene_transformation(segment)
        self._current_segment = segments[0] if segments else None
        connections = self._stitcher.get_connections()
        self._current_connection = connections[0] if connections else None
        self._current_annotation = None
        self._segmentDataChangeCallback = None

    def _init_graphics_modules(self):
        context = self._stitcher.get_context()
        self._materialmodule = context.getMaterialmodule()
        with ChangeManager(self._materialmodule):
            self._materialmodule.defineStandardMaterials()
            mid_blue = self._materialmodule.createMaterial()
            mid_blue.setName("mid blue")
            mid_blue.setManaged(True)
            mid_blue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.0, 0.2, 0.6])
            mid_blue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.0, 0.7, 1.0])
            mid_blue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
            mid_blue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
            mid_blue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.2)
            line_material_names = [graphics_info[-1] for graphics_info in self._category_graphics_info]
            for material_name in line_material_names + [self._end_point_material_name]:
                material = self._materialmodule.findMaterialByName(material_name)
                trans_material = self._materialmodule.createMaterial()
                trans_material.setName("trans " + material_name)
                trans_material.setManaged(True)
                for attribute in [Material.ATTRIBUTE_AMBIENT, Material.ATTRIBUTE_DIFFUSE,
                                  Material.ATTRIBUTE_EMISSION, Material.ATTRIBUTE_SPECULAR]:
                    value = material.getAttributeReal3(attribute)[1]
                    trans_material.setAttributeReal3(attribute, value)
                trans_material.setAttributeReal(Material.ATTRIBUTE_SHININESS,
                                                material.getAttributeReal(Material.ATTRIBUTE_SHININESS))
                trans_material.setAttributeReal(Material.ATTRIBUTE_ALPHA, 0.5)
        glyphmodule = context.getGlyphmodule()
        glyphmodule.defineStandardGlyphs()
        tessellationmodule = context.getTessellationmodule()
        default_tessellation = tessellationmodule.getDefaultTessellation()
        default_tessellation.setRefinementFactors([12])

    def _get_settings_file_name(self):
        return self._location + "-settings.json"

    def _get_display_settings_file_name(self):
        return self._location + "-display-settings.json"

    def _load_settings(self):
        settings_file_name = self._get_settings_file_name()
        if os.path.isfile(settings_file_name):
            with open(settings_file_name, "r") as f:
                settings = json.loads(f.read())
                self._stitcher.decode_settings(settings)
        display_settings_file_name = self._get_display_settings_file_name()
        if os.path.isfile(display_settings_file_name):
            with open(display_settings_file_name, "r") as f:
                display_settings = json.loads(f.read())
                self._display_settings.update(display_settings)

    def _save_settings(self):
        with open(self._get_settings_file_name(), "w") as f:
            settings = self._stitcher.encode_settings()
            f.write(json.dumps(settings, sort_keys=False, indent=4))
        with open(self._get_display_settings_file_name(), "w") as f:
            f.write(json.dumps(self._display_settings, sort_keys=False, indent=4))

    def get_output_file_name_stem(self):
        return self._location

    def get_output_segmentation_file_name(self):
        return self._location + ".exf"

    def done(self):
        self._save_settings()
        self._stitcher.write_output_segmentation_file(self.get_output_segmentation_file_name())

    def get_step_identifier(self):
        return self._step_identifier

    def get_context(self):
        return self._stitcher.get_context()

    def get_stitcher(self):
        return self._stitcher

    def get_root_region(self):
        return self._stitcher.get_root_region()

    def get_current_annotation(self):
        return self._current_annotation

    def set_current_annotation(self, annotation):
        """
        :param annotation: Stitcher Annotation object or None.
        """
        self._current_annotation = annotation

    def set_current_annotation_by_name(self, annotation_name):
        for annotation in self._stitcher.get_annotations():
            if annotation.get_name() == annotation_name:
                self.set_current_annotation(annotation)
                return
        else:
            self.set_current_annotation(None)

    def set_current_annotation_category_by_name(self, annotation_category_name):
        if self._current_annotation:
            self._current_annotation.set_category_by_name(annotation_category_name)

    def setSegmentDataChangeCallback(self, segmentDataChangeCallback):
        self._segmentDataChangeCallback = segmentDataChangeCallback

    def _segmentDataChanged(self, segment):
        if self._segmentDataChangeCallback:
            self._segmentDataChangeCallback(segment)

    def create_connection(self, segments):
        connection = self._stitcher.create_connection(segments)
        if connection:
            self.set_current_connection(connection)
            self._create_connection_graphics(only_connection=connection)
        return connection

    def delete_connection(self, connection):
        self._stitcher.delete_connection(connection)
        connections = self._stitcher.get_connections()
        connection = connections[0] if connections else None
        self.set_current_connection(connection)

    def connection_optimise_transformation(self, connection):
        connection.optimise_transformation()
        segment = connection.get_segments()[1]
        self._set_segment_scene_transformation(segment)
        self._segmentDataChanged(segment)

    def get_current_connection(self):
        """
        :return: Current connection or None if none.
        """
        return self._current_connection

    def set_current_connection(self, connection):
        self._current_connection = connection

    def get_current_segment(self):
        """
        :return: Current segment or None if none.
        """
        return self._current_segment

    def set_current_segment(self, segment):
        self._current_segment = segment

    def _set_segment_scene_transformation(self, segment):
        """
        Set the scene 4x4 matrix transformation to match the rotation and translation of segment.
        :param segment: Segment to transform.
        """
        rotation = [math.radians(angle_degrees) for angle_degrees in segment.get_rotation()]
        rotation_matrix_3x3 = euler_to_rotation_matrix(rotation)
        translation = segment.get_translation()
        transformation_matrix_4x4 = (
            rotation_matrix_3x3[0] + [translation[0]] +
            rotation_matrix_3x3[1] + [translation[1]] +
            rotation_matrix_3x3[2] + [translation[2]] +
            [0.0, 0.0, 0.0, 1.0])
        base_scene = segment.get_base_region().getScene()
        base_scene.setTransformationMatrix(transformation_matrix_4x4)

    def set_segment_rotation(self, segment, rotation):
        """
        Set the segment's transformation and update graphics transformation.
        :param segment: Segment to modify.
        :param rotation: 3 Euler angles in degrees.
        """
        segment.set_rotation(rotation)
        self._set_segment_scene_transformation(segment)
        self._segmentDataChanged(segment)

    def set_segment_translation(self, segment, translation):
        """
        Set the segment's transformation and update graphics transformation.
        :param segment: Segment to modify.
        """
        segment.set_translation(translation)
        self._set_segment_scene_transformation(segment)
        self._segmentDataChanged(segment)

    def _get_visibility(self, graphics_name):
        return self._display_settings[graphics_name]

    def _set_root_visibility(self, graphics_name, show):
        self._display_settings[graphics_name] = show
        region = self.get_root_region()
        scene = region.getScene()
        graphics = scene.findGraphicsByName(graphics_name)
        if graphics.isValid():
            graphics.setVisibilityFlag(show)

    def _set_raw_visibility(self, graphics_name, show):
        self._display_settings[graphics_name] = show
        segments = self._stitcher.get_segments()
        for segment in segments:
            region = segment.get_raw_region()
            scene = region.getScene()
            graphics = scene.findGraphicsByName(graphics_name)
            if graphics.isValid():
                graphics.setVisibilityFlag(show)

    def _set_line_visibility(self, graphics_name, show):
        self._set_raw_visibility(graphics_name, show)
        connections = self._stitcher.get_connections()
        for connection in connections:
            region = connection.get_region()
            scene = region.getScene()
            graphics = scene.findGraphicsByName(graphics_name)
            if graphics.isValid():
                graphics.setVisibilityFlag(show)

    def _set_working_visibility(self, graphics_name, show):
        self._display_settings[graphics_name] = show
        segments = self._stitcher.get_segments()
        for segment in segments:
            region = segment.get_working_region()
            scene = region.getScene()
            graphics = scene.findGraphicsByName(graphics_name)
            if graphics.isValid():
                graphics.setVisibilityFlag(show)

    def _get_line_radius(self, graphics_name):
        return self._display_settings[graphics_name + "_radius"]

    def _set_line_radius(self, graphics_name, show_radius):
        radius_name = graphics_name + "_radius"
        self._display_settings[radius_name] = show_radius
        segments = self._stitcher.get_segments()
        for segment in segments:
            region = segment.get_raw_region()
            scene = region.getScene()
            graphics = scene.findGraphicsByName(graphics_name)
            if graphics.isValid():
                line_attr = graphics.getGraphicslineattributes()
                line_attr.setShapeType(Graphicslineattributes.SHAPE_TYPE_CIRCLE_EXTRUSION
                                       if show_radius else Graphicslineattributes.SHAPE_TYPE_LINE)
        connections = self._stitcher.get_connections()
        for connection in connections:
            region = connection.get_region()
            scene = region.getScene()
            graphics = scene.findGraphicsByName(graphics_name)
            if graphics.isValid():
                line_attr = graphics.getGraphicslineattributes()
                line_attr.setShapeType(Graphicslineattributes.SHAPE_TYPE_CIRCLE_EXTRUSION
                                       if show_radius else Graphicslineattributes.SHAPE_TYPE_LINE)

    def _category_graphics_name_to_material_name(self, graphics_name):
        for graphics_info in self._category_graphics_info:
            if graphics_info[1] == graphics_name:
                return graphics_info[-1]
        return None

    def _get_line_trans(self, graphics_name):
        return self._display_settings[graphics_name + "_trans"]

    def _set_line_trans(self, graphics_name, trans):
        trans_name = graphics_name + "_trans"
        self._display_settings[trans_name] = trans
        material_name = self._category_graphics_name_to_material_name(graphics_name)
        if trans:
            material_name = "trans " + material_name
        material = self._materialmodule.findMaterialByName(material_name)
        segments = self._stitcher.get_segments()
        for segment in segments:
            region = segment.get_raw_region()
            scene = region.getScene()
            graphics = scene.findGraphicsByName(graphics_name)
            if graphics.isValid():
                graphics.setMaterial(material)
        connections = self._stitcher.get_connections()
        for connection in connections:
            region = connection.get_region()
            scene = region.getScene()
            graphics = scene.findGraphicsByName(graphics_name)
            if graphics.isValid():
                graphics.setMaterial(material)

    def is_display_axes(self):
        return self._get_visibility("display_axes")

    def set_display_axes(self, show):
        self._set_root_visibility("display_axes", show)

    def is_display_marker_points(self):
        return self._get_visibility("display_marker_points")

    def set_display_marker_points(self, show):
        self._set_raw_visibility("display_marker_points", show)

    def is_display_marker_names(self):
        return self._get_visibility("display_marker_names")

    def set_display_marker_names(self, show):
        self._set_raw_visibility("display_marker_names", show)

    def is_display_line_general(self):
        return self._get_visibility("display_line_general")

    def set_display_line_general(self, show):
        self._set_line_visibility("display_line_general", show)

    def is_display_line_general_radius(self):
        return self._get_line_radius("display_line_general")

    def set_display_line_general_radius(self, show_radius):
        self._set_line_radius("display_line_general", show_radius)

    def is_display_line_general_trans(self):
        return self._get_line_trans("display_line_general")

    def set_display_line_general_trans(self, trans):
        self._set_line_trans("display_line_general", trans)

    def is_display_independent_networks(self):
        return self._get_visibility("display_independent_networks")

    def set_display_independent_networks(self, show):
        self._set_line_visibility("display_independent_networks", show)

    def is_display_independent_networks_radius(self):
        return self._get_line_radius("display_independent_networks")

    def set_display_independent_networks_radius(self, show_radius):
        self._set_line_radius("display_independent_networks", show_radius)

    def is_display_independent_networks_trans(self):
        return self._get_line_trans("display_independent_networks")

    def set_display_independent_networks_trans(self, trans):
        self._set_line_trans("display_independent_networks", trans)

    def is_display_network_group_1(self):
        return self._get_visibility("display_network_group_1")

    def set_display_network_group_1(self, show):
        self._set_line_visibility("display_network_group_1", show)

    def is_display_network_group_1_radius(self):
        return self._get_line_radius("display_network_group_1")

    def set_display_network_group_1_radius(self, show_radius):
        self._set_line_radius("display_network_group_1", show_radius)

    def is_display_network_group_1_trans(self):
        return self._get_line_trans("display_network_group_1")

    def set_display_network_group_1_trans(self, trans):
        self._set_line_trans("display_network_group_1", trans)

    def is_display_network_group_2(self):
        return self._get_visibility("display_network_group_2")

    def set_display_network_group_2(self, show):
        self._set_line_visibility("display_network_group_2", show)

    def is_display_network_group_2_radius(self):
        return self._get_line_radius("display_network_group_2")

    def set_display_network_group_2_radius(self, show_radius):
        self._set_line_radius("display_network_group_2", show_radius)

    def is_display_network_group_2_trans(self):
        return self._get_line_trans("display_network_group_2")

    def set_display_network_group_2_trans(self, trans):
        self._set_line_trans("display_network_group_2", trans)

    def is_display_end_point_directions(self):
        return self._get_visibility("display_end_point_directions")

    def set_display_end_point_directions(self, show):
        self._set_working_visibility("display_end_point_directions", show)

    def is_display_end_point_best_fit_lines(self):
        return self._get_visibility("display_end_point_best_fit_lines")

    def set_display_end_point_best_fit_lines(self, show):
        self._set_working_visibility("display_end_point_best_fit_lines", show)

    def is_display_end_point_radius(self):
        return self._display_settings["display_end_point_radius"]

    def set_display_end_point_radius(self, show_radius):
        self._display_settings["display_end_point_radius"] = show_radius
        graphics_name = "display_end_point_best_fit_lines"
        segments = self._stitcher.get_segments()
        for segment in segments:
            working_region = segment.get_working_region()
            working_scene = working_region.getScene()
            graphics = working_scene.findGraphicsByName(graphics_name)
            if graphics.isValid():
                point_attr = graphics.getGraphicspointattributes()
                point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_CYLINDER if show_radius else Glyph.SHAPE_TYPE_LINE)

    def is_display_end_point_trans(self):
        return self._display_settings["display_end_point_trans"]

    def set_display_end_point_trans(self, trans):
        self._display_settings["display_end_point_trans"] = trans
        material_name = self._end_point_material_name
        if trans:
            material_name = "trans " + material_name
        material = self._materialmodule.findMaterialByName(material_name)
        graphics_names = ["display_end_point_best_fit_lines", "display_end_point_directions"]
        segments = self._stitcher.get_segments()
        for segment in segments:
            working_region = segment.get_working_region()
            working_scene = working_region.getScene()
            for graphics_name in graphics_names:
                graphics = working_scene.findGraphicsByName(graphics_name)
                if graphics.isValid():
                    graphics.setMaterial(material)

    def get_radius_scale(self):
        return self._display_settings["display_radius_scale"]

    def set_radius_scale(self, radius_scale):
        self._display_settings["display_radius_scale"] = radius_scale
        raw_line_graphics_names = [
            "display_line_general",
            "display_independent_networks",
            "display_network_group_1",
            "display_network_group_2"
        ]
        segments = self._stitcher.get_segments()
        for segment in segments:
            raw_region = segment.get_raw_region()
            raw_scene = raw_region.getScene()
            with ChangeManager(raw_scene):
                for graphics_name in raw_line_graphics_names:
                    graphics = raw_scene.findGraphicsByName(graphics_name)
                    if graphics.isValid():
                        line_attr = graphics.getGraphicslineattributes()
                        line_attr.setScaleFactors([2.0 * radius_scale])
            working_region = segment.get_working_region()
            working_scene = working_region.getScene()
            with ChangeManager(working_scene):
                end_point_directions = working_scene.findGraphicsByName("display_end_point_directions")
                point_attr = end_point_directions.getGraphicspointattributes()
                point_attr.setScaleFactors([2.0 * radius_scale, 2.0 * radius_scale, 2.0 * radius_scale])
                end_point_best_fit_lines = working_scene.findGraphicsByName("display_end_point_best_fit_lines")
                point_attr = end_point_best_fit_lines.getGraphicspointattributes()
                point_attr.setScaleFactors([1.0, 2.0 * radius_scale, 2.0 * radius_scale])
        connections = self._stitcher.get_connections()
        for connection in connections:
            region = connection.get_region()
            scene = region.getScene()
            with ChangeManager(scene):
                for graphics_name in raw_line_graphics_names:
                    graphics = scene.findGraphicsByName(graphics_name)
                    if graphics.isValid():
                        line_attr = graphics.getGraphicslineattributes()
                        line_attr.setScaleFactors([2.0 * radius_scale])

    def create_graphics(self):
        root_region = self.get_root_region()
        root_scene = root_region.getScene()
        # prepare fields and calculate axis and glyph scaling
        axes_scale = 1.0
        glyph_width_small = 0.01

        segments = self._stitcher.get_segments()
        minimums = maximums = None
        for segment in segments:
            region = segment.get_raw_region()
            fieldmodule = region.getFieldmodule()
            nodes = fieldmodule.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_NODES)
            coordinates = fieldmodule.findFieldByName("coordinates")
            segment_minimums, segment_maximums = evaluate_field_nodeset_range(coordinates, nodes)
            if segment_minimums:
                if not minimums:
                    minimums = segment_minimums
                    maximums = segment_maximums
                else:
                    for c in range(3):
                        if segment_minimums[c] < minimums[c]:
                            minimums[c] = segment_minimums[c]
                        elif segment_maximums[c] > maximums[c]:
                            maximums[c] = segment_maximums[c]
        if minimums:
            max_range = 0.0
            for c in range(3):
                max_range = max(max_range, maximums[c] - minimums[c])
            if max_range > 0.0:
                while axes_scale * 10.0 < max_range:
                    axes_scale *= 10.0
                while axes_scale * 0.1 > max_range:
                    axes_scale *= 0.1
                glyph_width_small = 0.01 * max_range

        with ChangeManager(root_scene):
            root_scene.removeAllGraphics()
            axes = root_scene.createGraphicsPoints()
            point_attr = axes.getGraphicspointattributes()
            point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_AXES_XYZ)
            point_attr.setBaseSize([axes_scale, axes_scale, axes_scale])
            point_attr.setLabelText(1, "  " + str(axes_scale))
            axes.setMaterial(self._materialmodule.findMaterialByName("grey50"))
            axes.setName("display_axes")
            axes.setVisibilityFlag(self._display_settings["display_axes"])

            radius_scale = self.get_radius_scale()
            for segment in segments:
                region = segment.get_raw_region()
                fieldmodule = region.getFieldmodule()
                coordinates = fieldmodule.findFieldByName("coordinates")
                marker_group = fieldmodule.findFieldByName("marker").castGroup()
                if marker_group.isValid():
                    marker_coordinates = fieldmodule.findFieldByName("marker coordinates")
                    if not marker_coordinates.isValid():
                        marker_coordinates = coordinates
                    marker_name = fieldmodule.findFieldByName("marker_name")
                    if not marker_name.isValid():
                        marker_name = None
                else:
                    marker_group = None
                    marker_coordinates = None
                    marker_name = None
                radius = fieldmodule.findFieldByName("radius")
                if not radius.isValid():
                    radius = None
                scene = region.getScene()
                with ChangeManager(scene):
                    scene.removeAllGraphics()

                    marker_points = scene.createGraphicsPoints()
                    marker_points.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
                    if marker_group:
                        marker_points.setSubgroupField(marker_group)
                    if marker_coordinates:
                        marker_points.setCoordinateField(marker_coordinates)
                    point_attr = marker_points.getGraphicspointattributes()
                    point_attr.setBaseSize([glyph_width_small, glyph_width_small, glyph_width_small])
                    point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_CROSS)
                    marker_points.setMaterial(self._materialmodule.findMaterialByName("white"))
                    marker_points.setName("display_marker_points")
                    marker_points.setVisibilityFlag(self.is_display_marker_points())

                    marker_names = scene.createGraphicsPoints()
                    marker_names.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
                    if marker_group:
                        marker_names.setSubgroupField(marker_group)
                    if marker_coordinates:
                        marker_names.setCoordinateField(marker_coordinates)
                    point_attr = marker_names.getGraphicspointattributes()
                    point_attr.setBaseSize([glyph_width_small, glyph_width_small, glyph_width_small])
                    point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_NONE)
                    if marker_name:
                        point_attr.setLabelField(marker_name)
                    marker_names.setMaterial(self._materialmodule.findMaterialByName("white"))
                    marker_names.setName("display_marker_names")
                    marker_names.setVisibilityFlag(self.is_display_marker_names())

                    self._create_category_graphics(segment, scene, coordinates, radius, radius_scale)

                working_region = segment.get_working_region()
                working_scene = working_region.getScene()
                end_point_coordinates, end_point_radius_direction, end_point_best_fit_line_orientation = (
                    segment.get_end_point_fields())
                show_radius = self.is_display_end_point_radius()
                with ChangeManager(working_scene):
                    working_scene.removeAllGraphics()

                    material_name = self._end_point_material_name
                    if self.is_display_end_point_trans():
                        material_name = "trans " + material_name
                    material = self._materialmodule.findMaterialByName(material_name)

                    end_point_directions = working_scene.createGraphicsPoints()
                    end_point_directions.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
                    end_point_directions.setCoordinateField(end_point_coordinates)
                    point_attr = end_point_directions.getGraphicspointattributes()
                    point_attr.setBaseSize([0.0, 0.0, 0.0])
                    point_attr.setOrientationScaleField(end_point_radius_direction)
                    point_attr.setScaleFactors([2.0 * radius_scale, 2.0 * radius_scale, 2.0 * radius_scale])
                    point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_CONE)
                    end_point_directions.setMaterial(material)
                    end_point_directions.setName("display_end_point_directions")
                    end_point_directions.setVisibilityFlag(self.is_display_end_point_directions())

                    end_point_best_fit_lines = working_scene.createGraphicsPoints()
                    end_point_best_fit_lines.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
                    end_point_best_fit_lines.setCoordinateField(end_point_coordinates)
                    point_attr = end_point_best_fit_lines.getGraphicspointattributes()
                    point_attr.setBaseSize([0.0, 0.0, 0.0])
                    point_attr.setOrientationScaleField(end_point_best_fit_line_orientation)
                    point_attr.setScaleFactors([1.0, 2.0 * radius_scale, 2.0 * radius_scale])
                    point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_CYLINDER if show_radius else Glyph.SHAPE_TYPE_LINE)
                    end_point_best_fit_lines.setMaterial(material)
                    end_point_best_fit_lines.setName("display_end_point_best_fit_lines")
                    end_point_best_fit_lines.setVisibilityFlag(self.is_display_end_point_best_fit_lines())

            self._create_connection_graphics()

    def _create_connection_graphics(self, only_connection=None):
        for connection in [only_connection] if only_connection else self._stitcher.get_connections():
            region = connection.get_region()
            fieldmodule = region.getFieldmodule()
            coordinates = fieldmodule.findFieldByName("coordinates")
            radius = fieldmodule.findFieldByName("radius")
            if not radius.isValid():
                radius = None
            radius_scale = self.get_radius_scale()
            scene = region.getScene()
            with ChangeManager(scene):
                scene.removeAllGraphics()
                self._create_category_graphics(connection, scene, coordinates, radius, radius_scale)

    def _create_category_graphics(self, object, scene, coordinates, radius, radius_scale):
        for category, settings_name, material_name in self._category_graphics_info:
            category_group = object.get_category_group(category)
            lines = scene.createGraphicsLines()
            lines.setSubgroupField(category_group)
            lines.setCoordinateField(coordinates)
            line_attr = lines.getGraphicslineattributes()
            if radius:
                line_attr.setOrientationScaleField(radius)
                line_attr.setScaleFactors([2.0 * radius_scale])
            line_attr.setShapeType(Graphicslineattributes.SHAPE_TYPE_CIRCLE_EXTRUSION
                                   if self._display_settings[settings_name + "_radius"] else
                                   Graphicslineattributes.SHAPE_TYPE_LINE)
            if self._display_settings[settings_name + "_trans"]:
                material_name = "trans " + material_name
            lines.setMaterial(self._materialmodule.findMaterialByName(material_name))
            lines.setName(settings_name)
            lines.setVisibilityFlag(self._display_settings[settings_name])

    def autorange_spectrum(self):
        scene = self.get_root_region().getScene()
        spectrummodule = scene.getSpectrummodule()
        spectrum = spectrummodule.getDefaultSpectrum()
        spectrum.autorange(scene, Scenefilter())

    # === Align Utilities ===

    def isStateAlign(self):
        return True

    def rotateModel(self, axis, angle):
        if self._current_segment:
            mat1 = axis_angle_to_rotation_matrix(axis, angle)
            rotation = self._current_segment.get_rotation()
            mat2 = euler_to_rotation_matrix([math.radians(deg) for deg in rotation])
            product_mat = matrix_mult(mat1, mat2)
            new_rotation = [math.degrees(rad) for rad in rotation_matrix_to_euler(product_mat)]
            self.set_segment_rotation(self._current_segment, new_rotation)

    def scaleModel(self, factor):
        pass

    def offsetModel(self, relative_offset):
        translation = self._current_segment.get_translation()
        new_translation = add(translation, relative_offset)
        self.set_segment_translation(self._current_segment, new_translation)

    def interactionStart(self):
        # print("interactionStart")
        pass

    def interactionEnd(self):
        # print("interactionEnd")
        pass
