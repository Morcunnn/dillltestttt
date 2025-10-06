#!/bin/bash
# TEDİL - Alıcı Dil + İfade Edici Uygulaması
# Linux/macOS için derleme scripti

echo "TEDİL Uygulaması Derleniyor..."
echo "====================================="

# Python'un yüklü olup olmadığını kontrol et
if ! command -v python3 &> /dev/null; then
    echo "HATA: Python3 yüklü değil!"
    echo "Lütfen Python 3.8+ yükleyin."
    exit 1
fi

echo "Python bulundu, sürüm kontrol ediliyor..."
python3 --version

# Gerekli kütüphaneleri yükle
echo ""
echo "Gerekli kütüphaneler yükleniyor..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "HATA: Kütüphaneler yüklenirken hata oluştu!"
    exit 1
fi

# Eski derleme dosyalarını temizle
echo ""
echo "Eski derleme dosyaları temizleniyor..."
rm -rf build dist __pycache__

# PyInstaller ile derle
echo ""
echo "PyInstaller ile executable oluşturuluyor..."
pyinstaller tedil.spec

if [ $? -ne 0 ]; then
    echo "HATA: Derleme sırasında hata oluştu!"
    exit 1
fi

# Başarı mesajı
echo ""
echo "====================================="
echo "DERLEME TAMAMLANDI!"
echo "====================================="
echo ""
echo "Executable dosyası: dist/TEDİL"
echo ""
echo "Uygulamayı çalıştırmak için:"
echo "  cd dist"
echo "  ./TEDİL"
echo ""
echo "Bu dosyayı başka bilgisayarlara kopyalayabilirsiniz."
echo "Python yüklü olmasına gerek yoktur."
echo ""