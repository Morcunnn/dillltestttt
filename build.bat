@echo off
REM TEDİL - Alıcı Dil + İfade Edici Uygulaması
REM Windows için derleme scripti

echo TEDİL Uygulaması Derleniyor...
echo =====================================

REM Python'un yüklü olup olmadığını kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo HATA: Python yüklü değil veya PATH'te bulunamıyor!
    echo Lütfen Python 3.8+ yükleyin ve PATH'e ekleyin.
    pause
    exit /b 1
)

echo Python bulundu, sürüm kontrol ediliyor...
python --version

REM Gerekli kütüphaneleri yükle
echo.
echo Gerekli kütüphaneler yükleniyor...
pip install -r requirements.txt

if errorlevel 1 (
    echo HATA: Kütüphaneler yüklenirken hata oluştu!
    pause
    exit /b 1
)

REM Eski derleme dosyalarını temizle
echo.
echo Eski derleme dosyaları temizleniyor...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "__pycache__" rmdir /s /q "__pycache__"

REM PyInstaller ile derle
echo.
echo PyInstaller ile executable oluşturuluyor...
pyinstaller tedil.spec

if errorlevel 1 (
    echo HATA: Derleme sırasında hata oluştu!
    pause
    exit /b 1
)

REM Başarı mesajı
echo.
echo =====================================
echo DERLEME TAMAMLANDI!
echo =====================================
echo.
echo Executable dosyası: dist\TEDİL.exe
echo.
echo Uygulamayı çalıştırmak için dist klasöründeki TEDİL.exe dosyasını çift tıklayın.
echo.
echo Bu dosyayı başka bilgisayarlara kopyalayabilirsiniz.
echo Python yüklü olmasına gerek yoktur.
echo.
pause