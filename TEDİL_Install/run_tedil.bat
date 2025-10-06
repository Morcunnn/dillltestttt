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
