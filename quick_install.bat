@echo off
title TEDİL Uygulaması Hızlı Kurulum
echo TEDİL - Alıcı Dil + İfade Edici Uygulaması
echo ==========================================
echo.

REM Python'un yüklü olup olmadığını kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo HATA: Python bulunamadı!
    echo Lütfen Python 3.8+ yükleyin: https://python.org
    echo.
    pause
    exit /b 1
)

echo Python bulundu, kurulum başlatılıyor...
echo.

REM Kurulum scriptini çalıştır
python install.py

echo.
echo Kurulum tamamlandı!
echo TEDIL.exe dosyasını çalıştırmak için dist klasörüne bakın.
echo.
pause