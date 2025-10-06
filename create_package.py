#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEDİL Uygulaması Dağıtım Paketi Oluşturma Scripti
Bu script tüm gerekli dosyaları bir paket halinde hazırlar
"""

import os
import shutil
import zipfile
from datetime import datetime
from pathlib import Path

def create_distribution_package():
    """Dağıtım paketi oluştur"""
    print("TEDİL Uygulaması Dağıtım Paketi Oluşturuluyor...")
    print("=" * 50)
    
    # Paket adı ve klasörü
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    package_name = f"TEDIL_v1.0.0_{timestamp}"
    package_dir = Path(package_name)
    
    # Paket klasörünü oluştur
    if package_dir.exists():
        shutil.rmtree(package_dir)
    package_dir.mkdir()
    
    # Dosyaları kopyala
    files_to_copy = [
        "ditest",                    # Ana uygulama
        "README.md",                 # Dokümantasyon
        "requirements.txt",          # Bağımlılıklar
        "setup.py",                  # Kurulum scripti
        "install.py",                # Otomatik kurulum
        "build_exe.py",              # Executable oluşturma
        "quick_install.bat",         # Windows hızlı kurulum
        "install.bat",               # Windows kurulum
        "install.sh",                # Linux kurulum
    ]
    
    print("Dosyalar kopyalanıyor...")
    for file_name in files_to_copy:
        if os.path.exists(file_name):
            shutil.copy2(file_name, package_dir)
            print(f"✓ {file_name}")
        else:
            print(f"⚠ {file_name} bulunamadı")
    
    # dist klasörünü kopyala (executable varsa)
    if os.path.exists("dist"):
        dist_dest = package_dir / "dist"
        shutil.copytree("dist", dist_dest)
        print("✓ dist/ klasörü (executable)")
    
    # Kurulum talimatları dosyası oluştur
    instructions = f"""# TEDİL Uygulaması Kurulum Talimatları

## Hızlı Kurulum

### Windows:
1. `quick_install.bat` dosyasını çift tıklayın
2. Veya `install.bat` dosyasını çalıştırın
3. `dist/TEDIL.exe` dosyasını çalıştırın

### Linux/macOS:
1. Terminal açın ve şu komutu çalıştırın:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```
2. `dist/TEDIL` dosyasını çalıştırın

## Manuel Kurulum

1. Python 3.8+ yüklü olduğundan emin olun
2. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
3. Uygulamayı çalıştırın:
   ```bash
   python ditest
   ```

## Executable Oluşturma

Kendi executable'ınızı oluşturmak için:
```bash
python build_exe.py
```

## Destek

Sorularınız için: info@tedil.com
Dokümantasyon: README.md dosyasına bakın

---
TEDİL v1.0.0 - {timestamp}
"""
    
    with open(package_dir / "KURULUM_TALIMATLARI.txt", "w", encoding="utf-8") as f:
        f.write(instructions)
    print("✓ KURULUM_TALIMATLARI.txt")
    
    # ZIP paketi oluştur
    zip_name = f"{package_name}.zip"
    print(f"\nZIP paketi oluşturuluyor: {zip_name}")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(package_dir):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(package_dir)
                zipf.write(file_path, arc_path)
    
    print(f"✓ ZIP paketi oluşturuldu: {zip_name}")
    
    # Paket boyutunu göster
    zip_size = os.path.getsize(zip_name) / (1024 * 1024)  # MB
    print(f"Paket boyutu: {zip_size:.1f} MB")
    
    return zip_name

def main():
    """Ana fonksiyon"""
    print("TEDİL Uygulaması Dağıtım Paketi Oluşturucu")
    print("=" * 50)
    
    try:
        zip_file = create_distribution_package()
        
        print("\n" + "="*50)
        print("✓ PAKET OLUŞTURMA TAMAMLANDI!")
        print("="*50)
        print(f"Oluşturulan paket: {zip_file}")
        print("\nBu paketi başkalarına gönderebilirsiniz.")
        print("Alıcılar paketi açıp kurulum talimatlarını takip edebilir.")
        
    except Exception as e:
        print(f"✗ Hata: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        exit(1)