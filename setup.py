"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['ImageViewer/ImageViewer.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'ImageViewer/ImageViewer.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,  # type: ignore
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    version='1.0.0',
)
