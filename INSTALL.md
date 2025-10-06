# TEDİL Kurulum Rehberi

Bu rehber, TEDİL uygulamasını farklı işletim sistemlerinde nasıl kuracağınızı ve çalıştıracağınızı gösterir.

## Hızlı Kurulum (Önerilen)

### Windows için:
1. `TEDİL_Install` klasörünü indirin
2. Klasörü istediğiniz konuma kopyalayın
3. `run_tedil.bat` dosyasını çift tıklayın

### Linux/macOS için:
1. `TEDİL_Install` klasörünü indirin
2. Klasörü istediğiniz konuma kopyalayın
3. Terminal açın ve şu komutu çalıştırın:
   ```bash
   cd TEDİL_Install
   ./run_tedil.sh
   ```

## Detaylı Kurulum

### Sistem Gereksinimleri

#### Minimum Gereksinimler:
- **İşletim Sistemi**: Windows 10, macOS 10.14, Ubuntu 18.04 veya üzeri
- **RAM**: 4GB
- **Disk Alanı**: 100MB
- **Python**: 3.8+ (sadece kaynak koddan derleme için)

#### Önerilen Gereksinimler:
- **İşletim Sistemi**: Windows 11, macOS 12+, Ubuntu 20.04+
- **RAM**: 8GB
- **Disk Alanı**: 500MB
- **Python**: 3.10+ (sadece kaynak koddan derleme için)

### Kurulum Seçenekleri

#### Seçenek 1: Hazır Executable (En Kolay)

**Windows:**
1. `dist/TEDİL.exe` dosyasını indirin
2. İstediğiniz klasöre kopyalayın
3. Çift tıklayarak çalıştırın

**Linux/macOS:**
1. `dist/TEDİL` dosyasını indirin
2. İstediğiniz klasöre kopyalayın
3. Terminal'de şu komutu çalıştırın:
   ```bash
   chmod +x TEDİL
   ./TEDİL
   ```

#### Seçenek 2: Kurulum Paketi

1. `TEDİL_Install` klasörünü indirin
2. Klasörü istediğiniz konuma kopyalayın
3. İşletim sisteminize göre çalıştırma scriptini kullanın

#### Seçenek 3: Kaynak Koddan Derleme

**Gereksinimler:**
- Python 3.8+
- pip (Python paket yöneticisi)
- Tkinter (GUI için)

**Windows:**
1. Python 3.8+ yükleyin (https://python.org)
2. Command Prompt'u yönetici olarak açın
3. Bu klasöre gidin
4. `build.bat` dosyasını çalıştırın

**Linux (Ubuntu/Debian):**
```bash
# Gerekli paketleri yükle
sudo apt-get update
sudo apt-get install python3 python3-pip python3-tk

# Derleme scriptini çalıştır
./build_improved.sh
```

**Linux (CentOS/RHEL):**
```bash
# Gerekli paketleri yükle
sudo yum install python3 python3-pip tkinter

# Derleme scriptini çalıştır
./build_improved.sh
```

**macOS:**
```bash
# Homebrew ile Python yükle (opsiyonel)
brew install python3

# Derleme scriptini çalıştır
./build_improved.sh
```

### Sorun Giderme

#### Uygulama Açılmıyor

**Windows:**
- Antivirus yazılımı engelliyor olabilir
- Windows Defender'da güvenlik ayarlarını kontrol edin
- "Bilinmeyen geliştiricilerden gelen uygulamalara izin ver" seçeneğini etkinleştirin

**Linux:**
- Çalıştırma izni verin: `chmod +x TEDİL`
- Tkinter yüklü değilse: `sudo apt-get install python3-tk`

**macOS:**
- Güvenlik ayarlarından "Bilinmeyen geliştiricilerden gelen uygulamalara izin ver" seçeneğini etkinleştirin
- Terminal'den çalıştırmayı deneyin

#### Tkinter Hatası

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**CentOS/RHEL:**
```bash
sudo yum install tkinter
```

**macOS:**
- Python ile birlikte gelir, ayrı yükleme gerekmez

#### PyInstaller Hatası

**Genel:**
```bash
pip3 install --upgrade pyinstaller
```

**Windows:**
```cmd
pip install --upgrade pyinstaller
```

### Performans Optimizasyonu

1. **Antivirus Yazılımı**: TEDİL klasörünü istisna listesine ekleyin
2. **Disk Alanı**: En az 1GB boş alan bırakın
3. **RAM**: Diğer uygulamaları kapatın
4. **Güncellemeler**: İşletim sisteminizi güncel tutun

### Güvenlik

- TEDİL uygulaması tamamen yerel çalışır
- İnternet bağlantısı gerektirmez
- Kişisel verileriniz bilgisayarınızda kalır
- Verileriniz hiçbir sunucuya gönderilmez

### Destek

Sorun yaşarsanız:
1. Bu rehberi tekrar okuyun
2. Hata mesajlarını not edin
3. Sistem bilgilerinizi toplayın
4. GitHub Issues'da sorun bildirin

### Lisans

Bu yazılım MIT lisansı altında dağıtılmaktadır. Ticari ve kişisel kullanım için ücretsizdir.