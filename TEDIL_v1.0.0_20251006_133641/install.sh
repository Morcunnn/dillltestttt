#!/bin/bash
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
