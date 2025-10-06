@echo off
chcp 65001 > nul
echo ============================================================
echo TEDİL Uygulaması - EXE Oluşturma
echo ============================================================
echo.

REM Python'un kurulu olup olmadığını kontrol et
python --version >nul 2>&1
if errorlevel 1 (
    echo ✗ Python bulunamadı!
    echo Python'u https://www.python.org/downloads/ adresinden indirip kurun.
    echo Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin.
    pause
    exit /b 1
)

echo ✓ Python bulundu

REM PyInstaller'ı kur
echo.
echo PyInstaller kuruluyor...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

REM Eski build klasörlerini temizle
echo.
echo Eski build dosyaları temizleniyor...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist TEDiL.spec del /q TEDiL.spec

REM EXE'yi oluştur
echo.
echo EXE dosyası oluşturuluyor...
pyinstaller --onefile --windowed --name=TEDiL --hidden-import=tkinter --hidden-import=json ditest

REM Sonucu kontrol et
if exist "dist\TEDiL.exe" (
    echo.
    echo ============================================================
    echo ✓ EXE dosyası başarıyla oluşturuldu!
    echo ============================================================
    echo.
    echo Dosya konumu: dist\TEDiL.exe
    echo.
    echo Bu dosyayı başkalarıyla paylaşabilirsiniz.
    echo Python yüklü olmayan bilgisayarlarda da çalışacaktır.
    echo.
    
    REM dist klasörünü aç
    explorer dist
) else (
    echo.
    echo ✗ EXE dosyası oluşturulamadı!
    echo.
)

pause
