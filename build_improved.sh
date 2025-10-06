#!/bin/bash
# TEDİL - Alıcı Dil + İfade Edici Uygulaması
# Geliştirilmiş Linux/macOS derleme scripti

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

# Tkinter'in yüklü olup olmadığını kontrol et
echo ""
echo "Tkinter kontrol ediliyor..."
python3 -c "import tkinter; print('Tkinter mevcut')" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "UYARI: Tkinter yüklü değil!"
    echo "Ubuntu/Debian için: sudo apt-get install python3-tk"
    echo "CentOS/RHEL için: sudo yum install tkinter"
    echo "macOS için: Python ile birlikte gelir"
    echo ""
    echo "Devam ediliyor, ancak uygulama çalışmayabilir..."
fi

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

# Executable'ı test et
echo ""
echo "Executable test ediliyor..."
if [ -f "dist/TEDİL" ]; then
    echo "✓ Executable başarıyla oluşturuldu: dist/TEDİL"
    chmod +x dist/TEDİL
else
    echo "✗ Executable oluşturulamadı!"
    exit 1
fi

# Kurulum paketi oluştur
echo ""
echo "Kurulum paketi oluşturuluyor..."
INSTALL_DIR="TEDİL_Install"
rm -rf "$INSTALL_DIR"
mkdir -p "$INSTALL_DIR"

# Executable'ı kopyala
cp dist/TEDİL "$INSTALL_DIR/"

# README ve diğer dosyaları kopyala
cp README.md "$INSTALL_DIR/"
cp requirements.txt "$INSTALL_DIR/"

# Çalıştırma scripti oluştur
cat > "$INSTALL_DIR/run_tedil.sh" << 'EOF'
#!/bin/bash
# TEDİL Uygulamasını Çalıştır

echo "TEDİL Uygulaması Başlatılıyor..."
echo "================================="

# Mevcut dizini kontrol et
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXECUTABLE="$SCRIPT_DIR/TEDİL"

if [ ! -f "$EXECUTABLE" ]; then
    echo "HATA: TEDİL executable dosyası bulunamadı!"
    echo "Dosya yolu: $EXECUTABLE"
    exit 1
fi

# Çalıştırma izni ver
chmod +x "$EXECUTABLE"

# Uygulamayı çalıştır
echo "Uygulama başlatılıyor..."
"$EXECUTABLE"
EOF

chmod +x "$INSTALL_DIR/run_tedil.sh"

# Windows için de bir script oluştur
cat > "$INSTALL_DIR/run_tedil.bat" << 'EOF'
@echo off
REM TEDİL Uygulamasını Çalıştır

echo TEDİL Uygulaması Başlatılıyor...
echo =================================

REM Mevcut dizini kontrol et
set SCRIPT_DIR=%~dp0
set EXECUTABLE=%SCRIPT_DIR%TEDİL.exe

if not exist "%EXECUTABLE%" (
    echo HATA: TEDİL.exe dosyası bulunamadı!
    echo Dosya yolu: %EXECUTABLE%
    pause
    exit /b 1
)

REM Uygulamayı çalıştır
echo Uygulama başlatılıyor...
"%EXECUTABLE%"
EOF

# Başarı mesajı
echo ""
echo "====================================="
echo "DERLEME TAMAMLANDI!"
echo "====================================="
echo ""
echo "Executable dosyası: dist/TEDİL"
echo "Kurulum paketi: $INSTALL_DIR/"
echo ""
echo "Kurulum paketini kullanmak için:"
echo "  1. $INSTALL_DIR klasörünü istediğiniz yere kopyalayın"
echo "  2. Linux/macOS için: ./run_tedil.sh"
echo "  3. Windows için: run_tedil.bat"
echo ""
echo "Tek dosya olarak kullanmak için:"
echo "  ./dist/TEDİL"
echo ""
echo "Bu dosyaları başka bilgisayarlara kopyalayabilirsiniz."
echo "Python yüklü olmasına gerek yoktur."
echo ""