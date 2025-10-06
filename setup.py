"""
TEDİL Uygulama Kurulum Scripti
Bu script uygulamayı tek bir exe dosyası haline getirir.
"""
import os
import sys
import subprocess

def main():
    print("=" * 60)
    print("TEDİL Uygulaması - EXE Oluşturma Scripti")
    print("=" * 60)
    print()
    
    # PyInstaller'ın kurulu olup olmadığını kontrol et
    try:
        import PyInstaller
        print("✓ PyInstaller kurulu")
    except ImportError:
        print("✗ PyInstaller bulunamadı. Kuruluyor...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ PyInstaller kuruldu")
    
    print()
    print("EXE dosyası oluşturuluyor...")
    print()
    
    # PyInstaller komutunu çalıştır
    cmd = [
        "pyinstaller",
        "--onefile",  # Tek bir exe dosyası oluştur
        "--windowed",  # Konsol penceresi açma (GUI uygulaması)
        "--name=TEDiL",  # EXE dosyasının adı
        "--icon=NONE",  # İkon yoksa NONE kullan
        "--add-data=.;.",  # Tüm dosyaları dahil et
        "--hidden-import=tkinter",
        "--hidden-import=json",
        "ditest"
    ]
    
    try:
        subprocess.check_call(cmd)
        print()
        print("=" * 60)
        print("✓ EXE dosyası başarıyla oluşturuldu!")
        print("=" * 60)
        print()
        print("Oluşturulan dosya: dist/TEDiL.exe")
        print()
        print("Bu dosyayı başkalarıyla paylaşabilirsiniz.")
        print("Python yüklü olmayan bilgisayarlarda da çalışacaktır.")
        print()
    except subprocess.CalledProcessError as e:
        print()
        print("✗ Hata oluştu:", str(e))
        print()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
