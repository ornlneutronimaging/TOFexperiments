try:
    from PyQt4.QtGui import QFileDialog
    from PyQt4 import QtCore, QtGui
except ImportError:
    from PyQt5.QtWidgets import QFileDialog
    from PyQt5 import QtCore, QtGui
import os
from decorators import format_directory


@format_directory
def gui_dname(dir=None):
    """Select files"""
    dirname = QFileDialog.getExistingDirectory(None, "Select Folder ...", 
                                            dir, 
                                            QFileDialog.ShowDirsOnly)
    return dirname


@format_directory
def gui_fname(dir=None):
    """Select one or more file via a dialog and returns the file name.
    """
    fname = QFileDialog.getOpenFileNames(None, "Select file(s)...", 
            directory = dir, filter="Fits files(*.fits);;TIFF files(*.tif)")
    return fname


@format_directory
def gui_single_file(dir=None):
    """Select one o file via a dialog and returns the file name.
    """
    if dir is None: 
        dir ='./'
    fname = QFileDialog.getOpenFileName(None, "Select file...", 
            dir, filter="Spectra File (*_Spectra.txt)")
    return fname


@format_directory
def gui_csv_fname(dir=None):
    """Select one or more file via a dialog and returns the file name.
    """
    if dir is None: 
        dir ='./'
    fname = QFileDialog.getOpenFileNames(None, "Select file(s)...", 
            dir, filter="Fits files(*.csv)")
    return fname
