#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEDİL Uygulaması Otomatik Kurulum Scripti
Bu script gerekli tüm bağımlılıkları yükler ve uygulamayı hazırlar
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def check_python_version():
    """Python versiyonunu kontrol et"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"✗ HATA: Python 3.8+ gerekli! Mevcut versiyon: {version.major}.{version.minor}")
        print("Lütfen Python'u güncelleyin: https://python.org")
        return False
    print(f"✓ Python versiyonu uygun: {version.major}.{version.minor}.{version.micro}")
    return True

def install_requirements():
    """Gerekli paketleri yükle"""
    print("\nGerekli paketler yükleniyor...")
    print("-" * 40)
    
    try:
        # pip'i güncelle
        print("pip güncelleniyor...")
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"], 
                      check=True, capture_output=True)
        
        # requirements.txt'i yükle
        if os.path.exists("requirements.txt"):
            print("requirements.txt'den paketler yükleniyor...")
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                          check=True, capture_output=True)
        else:
            print("requirements.txt bulunamadı, temel paketler yükleniyor...")
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller", "auto-py-to-exe"], 
                          check=True, capture_output=True)
        
        print("✓ Tüm paketler başarıyla yüklendi!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Paket yükleme hatası: {e}")
        print("Manuel olarak yüklemeyi deneyin: pip install -r requirements.txt")
        return False

def create_desktop_shortcut():
    """Masaüstü kısayolu oluştur (Windows)"""
    if platform.system() != "Windows":
        return
    
    try:
        import winshell
        from win32com.client import Dispatch
        
        desktop = winshell.desktop()
        path = os.path.join(desktop, "TEDİL.lnk")
        target = os.path.join(os.getcwd(), "dist", "TEDIL.exe")
        
        if os.path.exists(target):
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = os.path.dirname(target)
            shortcut.IconLocation = target
            shortcut.save()
            print("✓ Masaüstü kısayolu oluşturuldu!")
    except ImportError:
        print("Masaüstü kısayolu oluşturulamadı (winshell gerekli)")

def create_start_menu_shortcut():
    """Başlat menüsü kısayolu oluştur (Windows)"""
    if platform.system() != "Windows":
        return
    
    try:
        import winshell
        from win32com.client import Dispatch
        
        start_menu = winshell.start_menu()
        programs_folder = os.path.join(start_menu, "Programs")
        os.makedirs(programs_folder, exist_ok=True)
        
        path = os.path.join(programs_folder, "TEDİL.lnk")
        target = os.path.join(os.getcwd(), "dist", "TEDIL.exe")
        
        if os.path.exists(target):
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = os.path.dirname(target)
            shortcut.IconLocation = target
            shortcut.save()
            print("✓ Başlat menüsü kısayolu oluşturuldu!")
    except ImportError:
        print("Başlat menüsü kısayolu oluşturulamadı (winshell gerekli)")

def test_application():
    """Uygulamayı test et"""
    print("\nUygulama test ediliyor...")
    print("-" * 30)
    
    try:
        # Python dosyasını test et
        result = subprocess.run([sys.executable, "-c", "import ditest; print('✓ Modül yüklendi')"], 
                              check=True, capture_output=True, text=True, timeout=10)
        print(result.stdout.strip())
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Test hatası: {e}")
        return False
    except subprocess.TimeoutExpired:
        print("✗ Test zaman aşımına uğradı")
        return False

def create_run_script():
    """Çalıştırma scripti oluştur"""
    if platform.system() == "Windows":
        script_content = '''@echo off
title TEDİL - Alıcı Dil + İfade Edici
echo TEDİL Uygulaması başlatılıyor...
python ditest
pause
'''
        with open("run_tedil.bat", "w", encoding="utf-8") as f:
            f.write(script_content)
        print("✓ Windows çalıştırma scripti oluşturuldu: run_tedil.bat")
    else:
        script_content = '''#!/bin/bash
echo "TEDİL Uygulaması başlatılıyor..."
python3 ditest
'''
        with open("run_tedil.sh", "w", encoding="utf-8") as f:
            f.write(script_content)
        os.chmod("run_tedil.sh", 0o755)
        print("✓ Linux çalıştırma scripti oluşturuldu: run_tedil.sh")

def main():
    """Ana kurulum fonksiyonu"""
    print("TEDİL Uygulaması Kurulum Scripti")
    print("=" * 50)
    print(f"İşletim Sistemi: {platform.system()} {platform.release()}")
    print(f"Python Versiyonu: {sys.version}")
    print()
    
    # Python versiyonunu kontrol et
    if not check_python_version():
        return False
    
    # Gerekli paketleri yükle
    if not install_requirements():
        return False
    
    # Uygulamayı test et
    if not test_application():
        print("⚠ Uyarı: Uygulama test edilemedi, ancak kurulum devam ediyor...")
    
    # Çalıştırma scripti oluştur
    create_run_script()
    
    # Kısayollar oluştur (Windows)
    if platform.system() == "Windows":
        try:
            create_desktop_shortcut()
            create_start_menu_shortcut()
        except Exception as e:
            print(f"Kısayol oluşturma hatası: {e}")
    
    print("\n" + "="*50)
    print("✓ KURULUM TAMAMLANDI!")
    print("="*50)
    print("Kullanım:")
    if platform.system() == "Windows":
        print("1. run_tedil.bat dosyasını çift tıklayın")
        print("2. Veya: python ditest")
    else:
        print("1. ./run_tedil.sh çalıştırın")
        print("2. Veya: python3 ditest")
    print()
    print("Executable oluşturmak için: python build_exe.py")
    print()
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        print("\n✗ Kurulum başarısız!")
        input("Çıkmak için Enter'a basın...")
        sys.exit(1)
    else:
        print("✓ Kurulum başarılı!")
        input("Çıkmak için Enter'a basın...")