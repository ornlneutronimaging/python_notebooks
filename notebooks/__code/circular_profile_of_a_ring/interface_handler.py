import os
from qtpy.QtWidgets import QMainWindow, QVBoxLayout, QProgressBar, QApplication
import pyqtgraph as pg
import numpy as np
from qtpy import QtGui, QtCore
import matplotlib

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from __code.panoramic_stitching.mplcanvas import MplCanvas

from __code import load_ui
from __code.decorators import wait_cursor
from __code.circular_profile_of_a_ring.calculate_profiles import CalculateProfiles
from __code.circular_profile_of_a_ring.configuration_handler import ConfigurationHandler

INNER_RING_MARKER_LENGTH = 30  # number of pixels
OUTER_RING_MARKER_LENGTH = 50  # number of pixels


class InterfaceHandler:

    def __init__(self, working_dir=None, o_norm=None):
        o_interface = Interface(data=o_norm.data['sample']['data'],
                                list_files=o_norm.data['sample']['file_name'],
                                working_dir=working_dir)
        o_interface.show()

        self.o_interface = o_interface


class Interface(QMainWindow):

    histogram_level = None
    current_live_image = None

    vLine = None
    hLine = None

    x_profile = None
    y_profile = None

    # {0: {'x_profile': None,
    #      'y_profile': None},
    #  1: {'x_profile': None,
    #      'y_profile':None},
    #  ...,
    #  }
    dict_profile = None

    guide_color_slider = {'red': 255,
                          'green': 0,
                          'blue': 255,
                          'alpha': 255}

    ring_markers_color = {'red': 0,
                          'green': 255,
                          'blue': 255,
                          'alpha': 255}

    ring_color = {'red': 255,
                  'green': 255,
                  'blue': 255,
                  'alpha': 255}

    line_view_binning = None
    ring_markers = None
    ring = None
    inner_ring_roi = None
    outer_ring_roi = None

    max_ring_thickness = 200
    ring_pen = None

    angle_bin = {'minimum': 1,
                 'maximum': 500,
                 'value': 100}
    angle_line = None

    def __init__(self, parent=None, data=None, list_files=None, working_dir=None):

        self.data = data
        self.list_files = list_files
        self.list_short_files = [os.path.basename(_file) for _file in list_files]
        [self.height, self.width] = np.shape(data[0])
        self.working_dir = working_dir if working_dir else "./"

        super(Interface, self).__init__(parent)

        ui_full_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                                    os.path.join('ui',
                                                 'ui_circular_profile_of_a_ring.ui'))
        self.ui = load_ui(ui_full_path, baseinstance=self)
        self.setWindowTitle("Circular Profile of a Ring")

        self.init_widgets()
        self.init_matplotlib()
        self.slider_image_changed(new_index=0)
        self.init_crosshair()
        self.display_grid()
        self.display_ring()
        self.init_statusbar()

    def init_statusbar(self):
        self.eventProgress = QProgressBar(self.ui.statusbar)
        self.eventProgress.setVisible(False)
        self.ui.statusbar.addPermanentWidget(self.eventProgress)

    def init_matplotlib(self):
        def _matplotlib(parent=None, widget=None):
            sc = MplCanvas(parent, width=5, height=4, dpi=100)
            # sc.axes.plot([0,1,2,3,4,5], [10, 1, 20 ,3, 40, 50])
            toolbar = NavigationToolbar(sc, parent)
            layout = QVBoxLayout()
            layout.addWidget(toolbar)
            layout.addWidget(sc)
            widget.setLayout(layout)
            return sc

        self.profile_plot = _matplotlib(parent=self,
                                        widget=self.ui.widget_profile)

        self.profile_plot.mpl_connect('button_press_event', self.click_on_profile_plot)

    def click_on_profile_plot(self, event):
        angle = event.xdata
        x0 = np.float(str(self.ui.circle_x.text()))
        y0 = np.float(str(self.ui.circle_y.text()))

        if self.angle_line:
            self.ui.image_view.removeItem(self.angle_line)

        _pen = QtGui.QPen()
        _pen.setColor(QtGui.QColor(255, 0, 0))
        _pen.setWidth(0.01)

        self.angle_line = pg.InfiniteLine([x0, y0],
                                          pen=_pen,
                                          label="{:.2f}".format(angle),
                                          angle=angle-90,
                                          span=(0, 1),
                                          labelOpts={'position': 0.9})
        # self.angle_line.addMarker('o', size=15)
        self.ui.image_view.addItem(self.angle_line)

    def clear_image_view(self):
        if self.angle_line:
            self.ui.image_view.removeItem(self.angle_line)

    def init_crosshair(self):
        x0 = float(str(self.ui.circle_x.text()))
        y0 = float(str(self.ui.circle_y.text()))

        if self.vLine:
            self.ui.image_view.removeItem(self.vLine)
            self.ui.image_view.removeItem(self.hLine)

        self.vLine = pg.InfiniteLine(pos=x0, angle=90, movable=True)
        self.hLine = pg.InfiniteLine(pos=y0, angle=0, movable=True)

        self.vLine.sigDragged.connect(self.manual_circle_center_changed)
        self.vLine.sigPositionChangeFinished.connect(self.manual_circle_center_changed_finished)
        self.hLine.sigDragged.connect(self.manual_circle_center_changed)
        self.hLine.sigPositionChangeFinished.connect(self.manual_circle_center_changed_finished)

        self.ui.image_view.addItem(self.vLine, ignoreBounds=False)
        self.ui.image_view.addItem(self.hLine, ignoreBounds=False)

    def init_widgets(self):

        list_ui = [self.ui.ring_inner_radius_doubleSpinBox,
                   self.ui.ring_inner_radius_slider,
                   self.ui.ring_thickness_doubleSpinBox,
                   self.ui.ring_thickness_slider]
        self.block_signals(list_ui=list_ui,
                           block_status=True)

        self.ui.image_view = pg.ImageView(view=pg.PlotItem())
        self.ui.image_view.ui.roiBtn.hide()
        self.ui.image_view.ui.menuBtn.hide()
        image_layout = QVBoxLayout()
        image_layout.addWidget(self.ui.image_view)
        self.ui.widget.setLayout(image_layout)

        self.ui.splitter.setSizes([500, 200])
        self.ui.profile_splitter.setSizes([500, 100])
        self.ui.top_splitter.setSizes([800, 0])

        nbr_files = len(self.data)
        self.ui.image_slider.setMaximum(nbr_files-1)

        self.ui.circle_y.setText(str("{:.2f}".format(self.width / 2)))
        self.ui.circle_x.setText(str("{:.2f}".format(self.height / 2)))

        self.ui.guide_red_slider.setValue(self.guide_color_slider['red'])
        self.ui.guide_green_slider.setValue(self.guide_color_slider['green'])
        self.ui.guide_blue_slider.setValue(self.guide_color_slider['blue'])
        self.ui.guide_alpha_slider.setValue(self.guide_color_slider['alpha'])

        # ring settings
        max_ring_value = self.width
        default_inner_ring_value = np.int(self.width/4)
        default_ring_thickness = 100
        self.ui.ring_inner_radius_slider.setMaximum(max_ring_value*100)  # *100 because slider is int
        self.ui.ring_inner_radius_slider.setValue(default_inner_ring_value*100)
        self.ui.ring_inner_radius_doubleSpinBox.setMaximum(max_ring_value)
        self.ui.ring_inner_radius_doubleSpinBox.setSingleStep(0.01)
        self.ui.ring_inner_radius_doubleSpinBox.setValue(default_inner_ring_value)
        self.ui.ring_thickness_slider.setMaximum(self.max_ring_thickness*100)
        self.ui.ring_thickness_slider.setValue(default_ring_thickness*100)
        self.ui.ring_thickness_doubleSpinBox.setMaximum(self.max_ring_thickness)
        self.ui.ring_thickness_doubleSpinBox.setValue(default_ring_thickness)

        _pen = QtGui.QPen()
        _pen.setColor(QtGui.QColor(255, 255, 255))
        _pen.setWidth(0.01)
        self.ring_pen = _pen

        self.block_signals(list_ui=list_ui,
                           block_status=False)

        self.ui.angle_bin_horizontalSlider.setMinimum(self.angle_bin['minimum'])
        self.ui.angle_bin_horizontalSlider.setMaximum(self.angle_bin['maximum'])
        self.ui.angle_bin_horizontalSlider.setValue(self.angle_bin['value'])

        self.ui.angle_bin_units.setText(u"\u2103")
        self.ui.angle_bin_value.setText("{:.2f}".format(self.angle_bin['value']/100))

        self.ui.profile_list_images.addItems(self.list_short_files)

    def display_grid(self):
        [width, height] = [self.width, self.height]
        # bin_size = float(str(self.ui.lineEdit.text()))
        bin_size = self.ui.grid_size_slider.value()
        x0 = 0
        y0 = 0

        nbr_height_bins = np.float(height) / np.float(bin_size)
        real_height = y0 + np.int(nbr_height_bins) * np.int(bin_size)

        nbr_width_bins = np.float(width) / np.float(bin_size)
        read_width = x0 + np.int(nbr_width_bins) * np.int(bin_size)

        # pos (each matrix is one side of the lines)
        pos = []
        adj = []

        # vertical lines
        x = x0
        index = 0
        while x <= x0 + width:
            one_edge = [x, y0]
            other_edge = [x, real_height]
            pos.append(one_edge)
            pos.append(other_edge)
            adj.append([index, index + 1])
            x += bin_size
            index += 2

        # horizontal lines
        y = y0
        while y <= y0 + height:
            one_edge = [x0, y]
            other_edge = [read_width, y]
            pos.append(one_edge)
            pos.append(other_edge)
            adj.append([index, index + 1])
            y += bin_size
            index += 2

        pos = np.array(pos)
        adj = np.array(adj)

        line_color = (self.guide_color_slider['red'],
                      self.guide_color_slider['green'],
                      self.guide_color_slider['blue'],
                      self.guide_color_slider['alpha'], 0.5)
        lines = np.array([line_color for n in np.arange(len(pos))],
                         dtype=[('red', np.ubyte), ('green', np.ubyte),
                                ('blue', np.ubyte), ('alpha', np.ubyte),
                                ('width', float)])

        line_view_binning = pg.GraphItem()
        self.ui.image_view.addItem(line_view_binning)
        line_view_binning.setData(pos=pos,
                                  adj=adj,
                                  pen=lines,
                                  symbol=None,
                                  pxMode=False)

        self.line_view_binning = line_view_binning

    def display_ring(self):

        if self.inner_ring_roi:
            self.ui.image_view.removeItem(self.inner_ring_roi)
            self.ui.image_view.removeItem(self.outer_ring_roi)

        x_central_pixel = np.float(str(self.ui.circle_x.text()))
        y_central_pixel = np.float(str(self.ui.circle_y.text()))

        ring_radius = self.ui.ring_inner_radius_doubleSpinBox.value()
        ring_thickness = self.ui.ring_thickness_doubleSpinBox.value()

        # image_width = self.width
        # image_height = self.height

        # x = np.arange(image_width) + 0.5
        # y = np.arange(image_height) + 0.5

        # xv, yv = np.meshgrid(y, x)
        # distances_power = np.sqrt((np.power(yv - y_central_pixel, 2) + np.power(xv - x_central_pixel, 2)))

        # used to test calculation
        #self.ui.image_view.setImage(np.transpose(distances_power))

        # mask_ring1 = np.where(distances_power > ring_radius)
        # mask_ring2 = np.where(distances_power < (ring_radius + ring_thickness))
        # mask_ring = np.where(mask_ring1 and mask_ring2)

        inner_ring_circle_width = 2 * ring_radius
        inner_x0 = x_central_pixel - ring_radius
        inner_y0 = y_central_pixel - ring_radius
        inner_width_and_height = inner_ring_circle_width
        outer_ring_circle_width = 2 * (ring_radius + ring_thickness)
        outer_x0 = x_central_pixel - ring_radius - ring_thickness
        outer_y0 = y_central_pixel - ring_radius - ring_thickness
        self.display_inner_and_outer_ring(inner_x0=inner_x0,
                                          inner_y0=inner_y0,
                                          inner_width_and_height=inner_width_and_height,
                                          outer_width_and_height=outer_ring_circle_width,
                                          outer_x0=outer_x0,
                                          outer_y0=outer_y0,
                                          )

    # def display_ring_marker(self):
    #
    #     if self.ring_markers:
    #         self.ui.image_view.removeItem(self.ring_markers)
    #
    #     x_central_pixel = np.float(str(self.ui.circle_x.text()))
    #     y_central_pixel = np.float(str(self.ui.circle_y.text()))
    #
    #     ring_radius = self.ui.ring_inner_radius_doubleSpinBox.value()
    #     ring_thickness = self.ui.ring_thickness_doubleSpinBox.value()
    #
    #     pos = []
    #     adj = []
    #
    #     x1_inner_left = x_central_pixel - ring_radius
    #     pos.append(np.flip([y_central_pixel - INNER_RING_MARKER_LENGTH, x1_inner_left]))
    #     pos.append(np.flip([y_central_pixel + INNER_RING_MARKER_LENGTH, x1_inner_left]))
    #     adj.append([0, 1])
    #
    #     x2_outer_left = x1_inner_left - ring_thickness
    #     pos.append(np.flip([y_central_pixel - OUTER_RING_MARKER_LENGTH, x2_outer_left]))
    #     pos.append(np.flip([y_central_pixel + OUTER_RING_MARKER_LENGTH, x2_outer_left]))
    #     adj.append([2, 3])
    #
    #     x1_inner_right = x_central_pixel + ring_radius
    #     pos.append(np.flip([y_central_pixel - INNER_RING_MARKER_LENGTH, x1_inner_right]))
    #     pos.append(np.flip([y_central_pixel + INNER_RING_MARKER_LENGTH, x1_inner_right]))
    #     adj.append([4, 5])
    #
    #     x2_outer_right = x1_inner_right + ring_thickness
    #     pos.append(np.flip([y_central_pixel - OUTER_RING_MARKER_LENGTH, x2_outer_right]))
    #     pos.append(np.flip([y_central_pixel + OUTER_RING_MARKER_LENGTH, x2_outer_right]))
    #     adj.append([6, 7])
    #
    #     y1_inner_top = y_central_pixel - ring_radius
    #     pos.append(np.flip([y1_inner_top, x_central_pixel - INNER_RING_MARKER_LENGTH]))
    #     pos.append(np.flip([y1_inner_top, x_central_pixel + INNER_RING_MARKER_LENGTH]))
    #     adj.append([8, 9])
    #
    #     y2_outer_top = y1_inner_top - ring_thickness
    #     pos.append(np.flip([y2_outer_top, x_central_pixel - OUTER_RING_MARKER_LENGTH]))
    #     pos.append(np.flip([y2_outer_top, x_central_pixel + OUTER_RING_MARKER_LENGTH]))
    #     adj.append([10, 11])
    #
    #     y1_inner_bottom = y_central_pixel + ring_radius
    #     pos.append(np.flip([y1_inner_bottom, x_central_pixel - INNER_RING_MARKER_LENGTH]))
    #     pos.append(np.flip([y1_inner_bottom, x_central_pixel + INNER_RING_MARKER_LENGTH]))
    #     adj.append([12, 13])
    #
    #     y2_outer_bottom = y1_inner_bottom + ring_thickness
    #     pos.append(np.flip([y2_outer_bottom, x_central_pixel - OUTER_RING_MARKER_LENGTH]))
    #     pos.append(np.flip([y2_outer_bottom, x_central_pixel + OUTER_RING_MARKER_LENGTH]))
    #     adj.append([14, 15])
    #
    #     pos = np.array(pos)
    #     adj = np.array(adj)
    #
    #     line_color = (self.ring_markers_color['red'],
    #                   self.ring_markers_color['green'],
    #                   self.ring_markers_color['blue'],
    #                   self.ring_markers_color['alpha'], 1)
    #     lines = np.array([line_color for n in np.arange(len(pos))],
    #                      dtype=[('red', np.ubyte), ('green', np.ubyte),
    #                             ('blue', np.ubyte), ('alpha', np.ubyte),
    #                             ('width', float)])
    #
    #     self.ring_markers = pg.GraphItem()
    #     self.ui.image_view.addItem(self.ring_markers)
    #     self.ring_markers.setData(pos=pos,
    #                               adj=adj,
    #                               pen=lines,
    #                               symbol=None,
    #                               pxMode=False)

    def display_inner_and_outer_ring(self, inner_x0=None, inner_y0=None,
                                     inner_width_and_height=None,
                                     outer_x0=None, outer_y0=None,
                                     outer_width_and_height=None):

        if self.inner_ring_roi:
            self.ui.image_view.removeItem(self.inner_ring_roi)
        self.inner_ring_roi = pg.CircleROI([inner_x0, inner_y0],
                                           [inner_width_and_height, inner_width_and_height],
                                           movable=True,
                                           pen=self.ring_pen)
        self.ui.image_view.addItem(self.inner_ring_roi)
        self.inner_ring_roi.sigRegionChanged.connect(self.manual_inner_ring_changed)
        self.inner_ring_roi.sigRegionChangeFinished.connect(self.manual_inner_ring_change_finished)

        if self.outer_ring_roi:
            self.ui.image_view.removeItem(self.outer_ring_roi)
        self.outer_ring_roi = pg.CircleROI([outer_x0, outer_y0],
                                           [outer_width_and_height, outer_width_and_height],
                                           movable=True,
                                           resizable=False,
                                           pen=self.ring_pen)
        self.remove_handles(ring_ui=self.outer_ring_roi)
        self.outer_ring_roi.sigRegionChanged.connect(self.manual_outer_ring_changed)
        self.outer_ring_roi.sigRegionChangeFinished.connect(self.manual_outer_ring_change_finished)

    def remove_handles(self, ring_ui=None):
        self.ui.image_view.addItem(ring_ui)
        handles = ring_ui.getHandles()
        for _handle in handles:
            ring_ui.removeHandle(_handle)

    # Event handler
    def grid_size_changed(self):
        self.ui.image_view.removeItem(self.line_view_binning)
        self.display_grid()

    def manual_inner_ring_change_finished(self):
        self.manual_inner_ring_changed()
        self.display_mode_changed()

    def manual_inner_ring_changed(self):

        self.ui.image_view.removeItem(self.outer_ring_roi)

        list_ui = [self.ui.ring_inner_radius_doubleSpinBox,
                   self.ui.ring_inner_radius_slider]
        self.block_signals(list_ui=list_ui,
                           block_status=True)

        region = self.inner_ring_roi.getArraySlice(self.current_live_image,
                                                   self.ui.image_view.imageItem)
        x0 = region[0][0].start
        x1 = region[0][0].stop
        y0 = region[0][1].start
        y1 = region[0][1].stop

        thickness = self.ui.ring_thickness_doubleSpinBox.value()

        if x0 - thickness <= 0:
            self.replot_inner_ring(x0=x0, y0=y0, x1=x1, y1=y1)
        if x1 + thickness >= self.width:
            self.replot_inner_ring(x0=x0, y0=y0, x1=x1, y1=y1)
        if y0 - thickness <= 0:
            self.replot_inner_ring(x0=x0, y0=y0, x1=x1, y1=y1)
        if y1 + thickness >= self.height:
            self.replot_inner_ring(x0=x0, y0=y0, x1=x1, y1=y1)

        region = self.inner_ring_roi.getArraySlice(self.current_live_image,
                                                   self.ui.image_view.imageItem)
        x0 = region[0][0].start
        x1 = region[0][0].stop
        y0 = region[0][1].start
        y1 = region[0][1].stop

        ring_radius = np.int(x1 - x0)/2

        self.ui.ring_inner_radius_doubleSpinBox.setValue(ring_radius)
        self.ui.ring_inner_radius_slider.setValue(100*ring_radius)

        x_central_pixel = np.mean([x1, x0])
        y_central_pixel = np.mean([y1, y0])

        self.ui.circle_x.setText(str(x_central_pixel))
        self.ui.circle_y.setText(str(y_central_pixel))

        ring_thickness = self.ui.ring_thickness_doubleSpinBox.value()
        outer_ring_circle_width = 2 * (ring_radius + ring_thickness)
        self.outer_ring_roi = pg.CircleROI([x_central_pixel - ring_radius - ring_thickness,
                                            y_central_pixel - ring_radius - ring_thickness],
                                           [outer_ring_circle_width, outer_ring_circle_width],
                                           movable=True,
                                           resizable=False,
                                           pen=self.ring_pen)
        self.ui.image_view.addItem(self.outer_ring_roi)
        self.remove_handles(ring_ui=self.outer_ring_roi)
        self.outer_ring_roi.sigRegionChanged.connect(self.manual_outer_ring_changed)
        self.outer_ring_roi.sigRegionChangeFinished.connect(self.manual_outer_ring_change_finished)

        self.vLine.setValue(x_central_pixel)
        self.hLine.setValue(y_central_pixel)

        self.block_signals(list_ui=list_ui,
                           block_status=False)

    def replot_outer_ring(self, x0=None, y0=None, x1=None, y1=None):
        ring_radius = self.ui.ring_inner_radius_doubleSpinBox.value()
        x_central_pixel = np.mean([x1, x0])
        y_central_pixel = np.mean([y1, y0])
        ring_thickness = self.ui.ring_thickness_doubleSpinBox.value()
        outer_ring_circle_width = 2 * (ring_radius + ring_thickness)
        self.ui.image_view.removeItem(self.outer_ring_roi)
        self.outer_ring_roi = pg.CircleROI([x_central_pixel - ring_radius - ring_thickness,
                                            y_central_pixel - ring_radius - ring_thickness],
                                           [outer_ring_circle_width, outer_ring_circle_width],
                                           movable=True,
                                           resizable=False,
                                           pen=self.ring_pen)
        self.ui.image_view.addItem(self.outer_ring_roi)
        self.remove_handles(ring_ui=self.outer_ring_roi)
        self.outer_ring_roi.sigRegionChanged.connect(self.manual_outer_ring_changed)

    def replot_inner_ring(self, x0=None, y0=None, x1=None, y1=None):
        ring_radius = self.ui.ring_inner_radius_doubleSpinBox.value()
        x_central_pixel = np.mean([x1, x0])
        y_central_pixel = np.mean([y1, y0])
        self.ui.image_view.removeItem(self.inner_ring_roi)
        inner_ring_radius = ring_radius
        inner_ring_circle_width = 2 * inner_ring_radius
        self.ui.image_view.removeItem(self.inner_ring_roi)
        self.inner_ring_roi = pg.CircleROI([x_central_pixel - inner_ring_radius,
                                            y_central_pixel - inner_ring_radius],
                                           [inner_ring_circle_width, inner_ring_circle_width],
                                           movable=True,
                                           pen=self.ring_pen)
        self.ui.image_view.addItem(self.inner_ring_roi)
        self.inner_ring_roi.sigRegionChanged.connect(self.manual_inner_ring_changed)

    def manual_outer_ring_change_finished(self):
        self.manual_outer_ring_changed()
        self.display_mode_changed()

    def manual_outer_ring_changed(self):
        list_ui = [self.ui.ring_inner_radius_doubleSpinBox,
                   self.ui.ring_inner_radius_slider,
                   self.ui.ring_thickness_doubleSpinBox,
                   self.ui.ring_thickness_slider]
        self.block_signals(list_ui=list_ui,
                           block_status=True)

        # outer ring
        region = self.outer_ring_roi.getArraySlice(self.current_live_image,
                                                   self.ui.image_view.imageItem)
        x0 = region[0][0].start
        x1 = region[0][0].stop
        y0 = region[0][1].start
        y1 = region[0][1].stop
        outer_radius = np.int(x1 - x0) / 2

        if x0 <= 0:
            self.replot_outer_ring(x0=x0, y0=y0, x1=x1, y1=y1)
        if x1 >= self.width:
            self.replot_outer_ring(x0=x0, y0=y0, x1=x1, y1=y1)
        if y0 <= 0:
            self.replot_outer_ring(x0=x0, y0=y0, x1=x1, y1=y1)
        if y1 >= self.height:
            self.replot_outer_ring(x0=x0, y0=y0, x1=x1, y1=y1)

        x_central_pixel = np.mean([x1, x0])
        y_central_pixel = np.mean([y1, y0])

        # inner ring
        # region = self.inner_ring_roi.getArraySlice(self.current_live_image,
        #                                            self.ui.image_view.imageItem)
        # x0 = region[0][0].start
        # x1 = region[0][0].stop
        # inner_radius = np.int(x1 - x0) / 2
        inner_radius = self.ui.ring_inner_radius_doubleSpinBox.value()

        # thickness = np.abs(inner_radius - outer_radius)
        self.ui.circle_x.setText(str(x_central_pixel))
        self.ui.circle_y.setText(str(y_central_pixel))

        self.ui.image_view.removeItem(self.inner_ring_roi)
        inner_ring_radius = inner_radius
        inner_ring_circle_width = 2 * inner_ring_radius
        self.inner_ring_roi = pg.CircleROI([x_central_pixel - inner_ring_radius,
                                            y_central_pixel - inner_ring_radius],
                                           [inner_ring_circle_width, inner_ring_circle_width],
                                           movable=True,
                                           pen=self.ring_pen)
        self.ui.image_view.addItem(self.inner_ring_roi)
        self.inner_ring_roi.sigRegionChanged.connect(self.manual_inner_ring_changed)

        # self.ui.ring_thickness_doubleSpinBox.setValue(thickness)
        # self.ui.ring_thickness_slider.setValue(thickness*100)

        # # outer ring
        # region = self.outer_ring_roi.getArraySlice(self.current_live_image,
        #                                            self.ui.image_view.imageItem)
        # x0 = region[0][0].start
        # x1 = region[0][0].stop
        # y0 = region[0][1].start
        # y1 = region[0][1].stop
        # outer_radius = np.int(x1 - x0) / 2
        #
        # #radius_inner = np.min([radius_1, radius_2])
        # #radius_outer = np.max([radius_1, radius_2])
        # thickness = np.abs(inner_radius - outer_radius)
        #
        # x_central_pixel = np.mean([x1, x0])
        # y_central_pixel = np.mean([y1, y0])
        #
        # self.ui.circle_x.setText(str(x_central_pixel))
        # self.ui.circle_y.setText(str(y_central_pixel))
        #
        # self.ui.ring_thickness_doubleSpinBox.setValue(thickness)
        # self.ui.ring_thickness_slider.setValue(thickness*100)
        #
        # inner_ring_radius = inner_radius
        # inner_ring_circle_width = 2 * inner_ring_radius
        # self.inner_ring_roi = pg.CircleROI([x_central_pixel - inner_ring_radius,
        #                                     y_central_pixel - inner_ring_radius],
        #                                    [inner_ring_circle_width, inner_ring_circle_width],
        #                                    movable=True,
        #                                    pen=self.ring_pen)
        # self.ui.image_view.addItem(self.inner_ring_roi)
        # self.inner_ring_roi.sigRegionChanged.connect(self.manual_inner_ring_changed)

        self.vLine.setValue(x_central_pixel)
        self.hLine.setValue(y_central_pixel)

        self.block_signals(list_ui=list_ui,
                           block_status=False)

    def manual_ring_changed(self):

        list_ui = [self.ui.ring_inner_radius_doubleSpinBox,
                   self.ui.ring_inner_radius_slider,
                   self.ui.ring_thickness_doubleSpinBox,
                   self.ui.ring_thickness_slider]
        self.block_signals(list_ui=list_ui,
                           block_status=True)

        # inner ring
        region = self.inner_ring_roi.getArraySlice(self.current_live_image,
                                                   self.ui.image_view.imageItem)
        x0 = region[0][0].start
        x1 = region[0][0].stop
        y0 = region[0][1].start
        y1 = region[0][1].end

        thickness = self.ui.ring_thickness_doubleSpinBox.value()

        if x0 - thickness <= 0:
            self.replot_inner_ring(x0=x0, y0=y0, x1=x1, y1=y1)
        if x1 + thickness >= self.width:
            self.replot_inner_ring(x0=x0, y0=y0, x1=x1, y1=y1)
        if y0 - thickness <= 0:
            self.replot_inner_ring(x0=x0, y0=y0, x1=x1, y1=y1)
        if y1 + thickness >= self.height:
            self.replot_inner_ring(x0=x0, y0=y0, x1=x1, y1=y1)

        region = self.inner_ring_roi.getArraySlice(self.current_live_image,
                                                   self.ui.image_view.imageItem)
        x0 = region[0][0].start
        x1 = region[0][0].stop
        # y0 = region[0][1].start
        # y1 = region[0][1].end
        radius_1 = np.int(x1 - x0)/2

        # outer ring
        region = self.outer_ring_roi.getArraySlice(self.current_live_image,
                                                   self.ui.image_view.imageItem)
        x0 = region[0][0].start
        x1 = region[0][0].stop
        radius_2 = np.int(x1 - x0)/2

        radius_inner = np.min([radius_1, radius_2])
        radius_outer = np.max([radius_1, radius_2])
        thickness = np.abs(radius_1 - radius_2)

        self.ui.ring_inner_radius_doubleSpinBox.setValue(radius_inner)
        self.ui.ring_inner_radius_slider.setValue(radius_inner*100)
        self.ui.ring_thickness_doubleSpinBox.setValue(thickness)
        self.ui.ring_thickness_slider.setValue(thickness*100)

        if radius_outer > self.max_ring_thickness:
            self.max_ring_thickness = radius_outer - radius_inner
            self.ui.ring_thickness_slider.setMaximum(self.max_ring_thickness*100)
            self.ui.ring_thickness_doubleSpinBox.setMaximum(self.max_ring_thickness)

        self.block_signals(list_ui=list_ui,
                           block_status=False)

    def block_signals(self, list_ui=None, block_status=True):
        for _ui in list_ui:
            _ui.blockSignals(block_status)

    def manual_circle_center_changed_finished(self):
        self.display_mode_changed()
        self.manual_circle_center_changed()

    def manual_circle_center_changed(self):
        new_x0 = np.float(self.vLine.value())
        self.ui.circle_x.setText("{:.2f}".format(new_x0))

        new_y0 = np.float(self.hLine.value())
        self.ui.circle_y.setText("{:.2f}".format(new_y0))
        self.display_ring()

    def help_button_clicked(self):
        pass

    @wait_cursor
    def guide_color_changed(self, index_position):
        red = self.ui.guide_red_slider.value()
        green = self.ui.guide_green_slider.value()
        blue = self.ui.guide_blue_slider.value()
        alpha = self.ui.guide_alpha_slider.value()
        self.guide_color_slider['red'] = red
        self.guide_color_slider['green'] = green
        self.guide_color_slider['blue'] = blue
        self.guide_color_slider['alpha'] = alpha
        # self.circle_center_changed()

        self.ui.image_view.removeItem(self.line_view_binning)
        self.display_grid()

    @wait_cursor
    def guide_color_clicked(self):
        self.guide_color_changed(-1)

    @wait_cursor
    def guide_color_released(self):
        self.guide_color_changed(-1)

    @wait_cursor
    def grid_slider_moved(self, index):
        self.grid_size_changed()

    @wait_cursor
    def grid_slider_pressed(self):
        self.grid_size_changed()

    def export_profiles_clicked(self):
        print("clicked")

    def cancel_clicked(self):
        pass

    def refresh_image(self):
        self.ui.image_view.clear()
        image_index = self.ui.image_slider.value()
        self.slider_image_changed(new_index=image_index)

    def slider_image_changed(self, new_index=0):
        # _view = self.ui.image_view.getView()
        # _view_box = _view.getViewBox()
        # _state = _view_box.getState()
        #
        # first_update = False
        # if self.histogram_level is None:
        #     first_update = True
        # _histo_widget = self.ui.image_view.getHistogramWidget()
        # self.histogram_level = _histo_widget.getLevels()

        data = self.data[new_index]
        _image = np.transpose(data)
        self.ui.image_view.setImage(_image)
        self.current_live_image = _image
        # _view_box.setState(_state)

        # if not first_update:
        #     _histo_widget.setLevels(self.histogram_level[0],
        #                             self.histogram_level[1])

    def ring_settings_thickness_slider_changed(self, slider_value):
        self.ui.ring_thickness_doubleSpinBox.setValue(slider_value/100)
        self.display_ring()

    def ring_settings_thickness_slider_released(self):
        self.display_mode_changed()

    def ring_settings_thickness_double_spin_box_changed(self, spin_box_value):
        self.ui.ring_thickness_slider.setValue(np.int(spin_box_value*100))
        self.display_ring()

    def ring_settings_thickness_double_spin_box_finished(self):
        self.display_mode_changed()

    def ring_settings_inner_radius_slider_changed(self, slider_value):
        self.ui.ring_inner_radius_doubleSpinBox.setValue(slider_value/100)
        self.display_ring()

    def ring_settings_inner_radius_slider_released(self):
        self.display_mode_changed()

    def ring_settings_inner_radius_double_spin_box_changed(self, spin_box_value):
        self.ui.ring_inner_radius_slider.setValue(np.int(spin_box_value*100))
        self.display_ring()

    def ring_settings_inner_radius_double_spin_box_finished(self):
        self.display_mode_changed()

    def clear_full_ring_clicked(self):
        if self.ring:
            self.ui.image_view.removeItem(self.ring)
        self.clear_full_ring_pushButton.setEnabled(False)

    def calculate_profiles_clicked(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        QtGui.QGuiApplication.processEvents()
        self.ui.setEnabled(False)
        self.ui.statusbar.showMessage("Calculating profiles ... IN PROGRESS")
        self.ui.statusbar.setStyleSheet("color: blue")
        o_cal = CalculateProfiles(parent=self)
        o_cal.run()
        o_cal.plot_profiles()
        self.ui.top_splitter.setSizes([400, 400])
        self.ui.setEnabled(True)
        self.ui.statusbar.showMessage("Calculating profiles ... Done!", 10000)
        self.ui.statusbar.setStyleSheet("color: green")
        QApplication.restoreOverrideCursor()
        QtGui.QGuiApplication.processEvents()

    def angle_bin_slider_moved(self, slider_value):
        real_bin_value = slider_value/100
        self.ui.angle_bin_value.setText("{:.2f}".format(real_bin_value))

    def display_mode_changed(self):
        if self.ui.display_radiographs_radioButton.isChecked():
            self.ui.image_view.clear()
            image_index = self.ui.image_slider.value()
            self.slider_image_changed(new_index=image_index)
        elif self.ui.display_angles_matrix_radioButton.isChecked():
            o_cal = CalculateProfiles(parent=self)
            o_cal.calculate_matrices(display=True)
        else:
            raise NotImplementedError("Display mode not implemented!")

    def profile_list_images_selection_changed(self):
        o_cal = CalculateProfiles(parent=self)
        o_cal.plot_profiles()

    def load_configuration(self):
        o_config = ConfigurationHandler(parent=self)
        o_config.load()

    def save_configuration(self):
        o_config = ConfigurationHandler(parent=self)
        o_config.save()

    def profile_plot_axis_type_changed(self):
        o_cal = CalculateProfiles(parent=self)
        o_cal.plot_profiles()
