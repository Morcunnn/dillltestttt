## TEDİL Uygulamasını Windows İçin Kurulabilir EXE Yapma

Aşağıdaki adımlar, Windows üzerinde tek dosya `.exe` ve isteğe bağlı kurulumcı (NSIS) oluşturur.

### 1) Gerekli Dosyalar
- `ditest.py` (uygulama kodu; `run_tedil.py` bunu başlatır)
- `run_tedil.py` (giriş noktası)
- `requirements.txt` (3. parti bağımlılık yok; Tkinter Python ile birlikte gelir)
- `pyinstaller.spec` (PyInstaller yapı tarifi)
- `build_windows.bat` (Windows üzerinde derleme komutu)
- `installer.nsi` (NSIS kurulum betiği; opsiyonel)

### 2) Windows'ta Derleme
1. Python 3.10+ ve `pip` kurulu olmalı. (Tkinter Windows Python kurulumunda varsayılan gelir.)
2. `build_windows.bat` dosyasını çift tıklayın veya Komut İstemi'nden çalıştırın:
   ```bat
   build_windows.bat
   ```
3. Betik şunları yapar:
   - `.venv` sanal ortamını oluşturur
   - `pip` günceller, `requirements.txt` ve `pyinstaller` kurar
   - `pyinstaller.spec` ile uygulamayı derler
   - Çıktı: `dist/TEDIL.exe`
   - Eğer `makensis` (NSIS) kurulu ise kurulum dosyası üretir: `dist/TEDIL_Setup_1.0.0.exe`

### 3) Kurulum Dosyası (Opsiyonel)
- `NSIS` kurulu değilse `installer` kısmı atlanır. Kurulum oluşturmak için: `https://nsis.sourceforge.io/Download`
- Kurulu iken `build_windows.bat` otomatik çalıştırır.

### 4) Dağıtım
- Sadece tek dosya EXE istiyorsanız `dist/TEDIL.exe` dosyasını gönderin.
- Kurulum süreci tercih ediliyorsa `dist/TEDIL_Setup_1.0.0.exe` dosyasını gönderin.

### 5) Notlar
- Uygulama `tkinter` kullanır; ayrı bir bağımlılık gerektirmez.
- JSON içe/dışa aktarma diyalogları, dosya sistemi erişimi için standart izinler yeterlidir.
