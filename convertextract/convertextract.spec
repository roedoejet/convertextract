"""
Example build.spec file
This hits most of the major notes required for
building a stand alone version of your Gooey application.
"""


import os
import platform
import gooey
import convertextract
gooey_root = os.path.dirname(gooey.__file__)
gooey_languages = Tree(os.path.join(gooey_root, 'languages'), prefix = 'gooey/languages')
gooey_images = Tree(os.path.join(gooey_root, 'images'), prefix = 'gooey/images')

from PyInstaller.building.api import EXE, PYZ, COLLECT
from PyInstaller.building.build_main import Analysis
from PyInstaller.building.datastruct import Tree
from PyInstaller.building.osx import BUNDLE
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None
hiddenimps = collect_submodules('convertextract')
PATH_PFX = os.getenv('GITHUB_WORKSPACE', os.getenv('HOME'))
if os.getenv('GITHUB_WORKSPACE'):
    PATH_EX = [os.path.join(PATH_PFX, 'convertextract/gui.py')]
else:
    PATH_EX = [os.path.join(PATH_PFX, 'convertextract/convertextract/gui.py')]
a = Analysis(['gui.py'],  # replace me with your path
             datas = [(os.path.join(PATH_PFX, 'g2p/g2p'), 'g2p')],
             pathex=PATH_EX,
             hiddenimports=hiddenimps,
             hookspath=None,
             runtime_hooks=None,
             )
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION'), ('v', None, 'OPTION'), ('w', None, 'OPTION')]


exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,
          gooey_languages,
          gooey_images,
          name='Convertextract',
          debug=False,
          strip=None,
          upx=True,
          console=False,
          icon=os.path.join(gooey_root, 'images', 'program_icon.ico'))

info_plist = {
    'addition_prop': 'additional_value', 
    'NSHighResolutionCapable': 'True'
    }
app = BUNDLE(exe,
             name='Convertextract.app',
             bundle_identifier=None,
             info_plist=info_plist
            )
