@echo off
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
