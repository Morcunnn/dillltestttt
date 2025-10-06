#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEDİL Uygulaması için Executable Build Script
Bu script PyInstaller kullanarak tek dosya executable oluşturur
"""

import os
import sys
import subprocess
import shutil
import platform
from pathlib import Path

def check_pyinstaller():
    """PyInstaller'ın yüklü olup olmadığını kontrol et"""
    try:
        import PyInstaller
        print(f"✓ PyInstaller bulundu: {PyInstaller.__version__}")
        return True
    except ImportError:
        print("✗ PyInstaller bulunamadı!")
        print("Yüklemek için: pip install pyinstaller")
        return False

def clean_build_dirs():
    """Önceki build dosyalarını temizle"""
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            print(f"Temizleniyor: {dir_name}")
            shutil.rmtree(dir_name)
    
    # .spec dosyalarını da temizle
    for spec_file in Path('.').glob('*.spec'):
        print(f"Siliniyor: {spec_file}")
        spec_file.unlink()

def build_executable():
    """Executable oluştur"""
    print("\n" + "="*50)
    print("TEDİL Uygulaması Executable Oluşturuluyor...")
    print("="*50)
    
    # PyInstaller komutunu oluştur
    cmd = [
        'pyinstaller',
        '--onefile',                    # Tek dosya executable
        '--windowed',                   # Konsol penceresi gösterme (GUI uygulaması)
        '--name=TEDIL',                 # Executable adı
        '--hidden-import=tkinter',      # Tkinter'ı açıkça dahil et
        '--hidden-import=tkinter.ttk',  # TTK modülünü dahil et
        '--hidden-import=json',         # JSON modülünü dahil et
        '--hidden-import=datetime',     # Datetime modülünü dahil et
        '--hidden-import=typing',       # Typing modülünü dahil et
        '--clean',                      # Önceki build'i temizle
        'ditest'                        # Ana Python dosyası
    ]
    
    # İkon dosyası varsa ekle
    if os.path.exists('icon.ico'):
        cmd.insert(-1, '--icon=icon.ico')
    
    # README dosyasını dahil et (platform-specific syntax)
    if os.path.exists('README.md'):
        if platform.system() == "Windows":
            cmd.insert(-1, '--add-data=README.md;.')
        else:
            cmd.insert(-1, '--add-data=README.md:.')
    
    print(f"Çalıştırılan komut: {' '.join(cmd)}")
    print()
    
    try:
        # PyInstaller'ı çalıştır
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✓ Executable başarıyla oluşturuldu!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build hatası: {e}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print("✗ PyInstaller bulunamadı! Lütfen önce yükleyin: pip install pyinstaller")
        return False

def create_installer_script():
    """Kurulum scripti oluştur"""
    installer_content = '''@echo off
echo TEDİL Uygulaması Kurulumu
echo =========================
echo.

REM Python'un yüklü olup olmadığını kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo HATA: Python bulunamadı!
    echo Lütfen Python 3.8+ yükleyin: https://python.org
    pause
    exit /b 1
)

echo Python bulundu, gerekli kütüphaneler yükleniyor...
pip install -r requirements.txt

echo.
echo Kurulum tamamlandı!
echo TEDIL.exe dosyasını çalıştırabilirsiniz.
echo.
pause
'''
    
    with open('install.bat', 'w', encoding='utf-8') as f:
        f.write(installer_content)
    
    print("✓ Windows kurulum scripti oluşturuldu: install.bat")

def create_linux_installer():
    """Linux kurulum scripti oluştur"""
    installer_content = '''#!/bin/bash
echo "TEDİL Uygulaması Kurulumu"
echo "========================="
echo

# Python'un yüklü olup olmadığını kontrol et
if ! command -v python3 &> /dev/null; then
    echo "HATA: Python3 bulunamadı!"
    echo "Lütfen Python 3.8+ yükleyin"
    exit 1
fi

echo "Python bulundu, gerekli kütüphaneler yükleniyor..."
pip3 install -r requirements.txt

echo
echo "Kurulum tamamlandı!"
echo "TEDIL dosyasını çalıştırabilirsiniz: ./TEDIL"
echo
'''
    
    with open('install.sh', 'w', encoding='utf-8') as f:
        f.write(installer_content)
    
    # Çalıştırılabilir yap
    os.chmod('install.sh', 0o755)
    print("✓ Linux kurulum scripti oluşturuldu: install.sh")

def main():
    """Ana fonksiyon"""
    print("TEDİL Uygulaması Build Script")
    print("=" * 40)
    
    # PyInstaller kontrolü
    if not check_pyinstaller():
        return False
    
    # Önceki build'leri temizle
    clean_build_dirs()
    
    # Executable oluştur
    if not build_executable():
        return False
    
    # Kurulum scriptlerini oluştur
    create_installer_script()
    create_linux_installer()
    
    print("\n" + "="*50)
    print("✓ BUILD TAMAMLANDI!")
    print("="*50)
    print("Oluşturulan dosyalar:")
    print("- dist/TEDIL.exe (Windows executable)")
    print("- dist/TEDIL (Linux executable)")
    print("- install.bat (Windows kurulum scripti)")
    print("- install.sh (Linux kurulum scripti)")
    print()
    print("Kullanım:")
    print("1. install.bat (Windows) veya ./install.sh (Linux) çalıştırın")
    print("2. dist/ klasöründeki TEDIL dosyasını çalıştırın")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)