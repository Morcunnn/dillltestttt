# -*- mode: python ; coding: utf-8 -*-

"""
TEDİL - Alıcı Dil + İfade Edici Uygulaması
PyInstaller spec dosyası
"""

import sys
import os
from PyInstaller.utils.hooks import collect_data_files

# Ana uygulama dosyası
main_script = 'ditest'

# Veri dosyalarını topla (eğer varsa)
datas = []

# Ek veri dosyaları ekle
if os.path.exists('data'):
    datas += collect_data_files('data')

# Icon dosyası (eğer varsa)
icon_path = None
if os.path.exists('icon.ico'):
    icon_path = 'icon.ico'
elif os.path.exists('icon.png'):
    icon_path = 'icon.png'

# Analiz ayarları
a = Analysis(
    [main_script],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'json',
        'datetime',
        'typing',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'PIL',
        'cv2',
        'tensorflow',
        'torch',
        'sklearn',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# PYZ ayarları
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# EXE ayarları
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='TEDİL',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # GUI uygulaması olduğu için console=False
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,
    version_file=None,
)

# Windows için tek dosya oluştur
if sys.platform == 'win32':
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name='TEDİL',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
        icon=icon_path,
        version_file=None,
    )