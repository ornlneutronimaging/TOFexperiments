from PyQt4 import QtCore, QtGui

def gui_dname(dir=None):
    """Select files"""
    if dir is None: 
        dir ='./'
    if dir is "":
        dir = './'
        
    dirname = QtGui.QFileDialog.getExistingDirectory(None, "Select Folder ...", 
                                            dir, 
                                            QtGui.QFileDialog.ShowDirsOnly)
    return dirname

def gui_fname(dir=None):
    """Select one or more file via a dialog and returns the file name.
    """
    if dir is None: 
        dir ='./'
    fname = QtGui.QFileDialog.getOpenFileNames(None, "Select file(s)...", 
            dir, filter="Fits files(*.fits)")
    return fname

def gui_csv_fname(dir=None):
    """Select one or more file via a dialog and returns the file name.
    """
    if dir is None: 
        dir ='./'
    fname = QtGui.QFileDialog.getOpenFileNames(None, "Select file(s)...", 
            dir, filter="Fits files(*.csv)")
    return fname
