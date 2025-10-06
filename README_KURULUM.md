# TEDİL Uygulaması - EXE Kurulum Kılavuzu

## 📋 Genel Bakış

Bu kılavuz, TEDİL uygulamasını tek başına çalışan bir Windows EXE dosyası haline getirmenizi sağlar. Oluşturulan EXE dosyasını başkalarıyla paylaşabilir ve Python yüklü olmayan bilgisayarlarda da çalıştırabilirsiniz.

---

## 🚀 Hızlı Başlangıç

### Yöntem 1: Otomatik Kurulum (Önerilen)

1. **Python'u Kurun** (eğer kurulu değilse):
   - [Python İndirme Sayfası](https://www.python.org/downloads/)
   - **ÖNEMLİ:** Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin!

2. **EXE Oluşturun:**
   - `build.bat` dosyasına çift tıklayın
   - Script otomatik olarak:
     - PyInstaller'ı kuracak
     - EXE dosyasını oluşturacak
     - `dist` klasörünü açacak

3. **EXE'yi Kullanın:**
   - `dist/TEDiL.exe` dosyası oluşturulmuş olacak
   - Bu dosyayı istediğiniz yere kopyalayabilirsiniz
   - Başkalarıyla paylaşabilirsiniz

---

### Yöntem 2: Manuel Kurulum

#### Adım 1: Gereksinimleri Kurun

Komut satırını (CMD) açın ve aşağıdaki komutları çalıştırın:

```bash
# Pip'i güncelleyin
python -m pip install --upgrade pip

# Gerekli kütüphaneleri kurun
python -m pip install -r requirements.txt
```

#### Adım 2: EXE Dosyası Oluşturun

```bash
# Seçenek A: Python setup scripti ile
python setup.py

# Seçenek B: PyInstaller ile doğrudan
pyinstaller --onefile --windowed --name=TEDiL --hidden-import=tkinter --hidden-import=json ditest
```

#### Adım 3: EXE'yi Bulun

Oluşturulan `TEDiL.exe` dosyası `dist` klasöründe olacaktır.

---

## 📦 Dağıtım

### EXE Dosyasını Paylaşma

1. `dist/TEDiL.exe` dosyasını bulun
2. Bu dosyayı kopyalayın ve paylaşın
3. **Alıcının yapması gerekenler:**
   - EXE dosyasını bilgisayarına kopyalasın
   - Dosyaya çift tıklasın
   - Uygulama çalışacaktır (Python gerekmez!)

### Kurulum Paketi Oluşturma (İsteğe Bağlı)

Daha profesyonel bir kurulum deneyimi için Inno Setup veya NSIS kullanabilirsiniz:

- [Inno Setup](https://jrsoftware.org/isinfo.php) (Önerilen)
- [NSIS](https://nsis.sourceforge.io/)

---

## 🔧 Sorun Giderme

### Python Bulunamadı Hatası

**Çözüm:**
1. Python'un kurulu olduğundan emin olun
2. Python'u PATH'e ekleyin:
   - Başlat menüsünde "Environment Variables" arayın
   - "Path" değişkenine Python klasörünü ekleyin
   - Örnek: `C:\Users\KullaniciAdi\AppData\Local\Programs\Python\Python311`

### PyInstaller Hatası

**Çözüm:**
```bash
# PyInstaller'ı yeniden kurun
python -m pip uninstall pyinstaller
python -m pip install pyinstaller
```

### EXE Çalışmıyor

**Çözüm:**
1. Antivirüs yazılımınızın EXE'yi engellemediğinden emin olun
2. EXE'yi yönetici olarak çalıştırmayı deneyin
3. Windows Defender'ın akıllı ekran korumasını atlayın:
   - "Daha fazla bilgi" → "Yine de çalıştır"

---

## 📝 Teknik Detaylar

### Kullanılan Kütüphaneler

- **PyInstaller:** Python uygulamalarını EXE'ye dönüştürür
- **tkinter:** GUI arayüzü (Python ile birlikte gelir)
- **json:** Veri kaydetme/yükleme

### PyInstaller Seçenekleri

```bash
--onefile        # Tek bir EXE dosyası oluştur
--windowed       # Konsol penceresi gösterme
--name=TEDiL     # EXE dosyası adı
--hidden-import  # Ekstra modülleri dahil et
```

### Dosya Yapısı

```
.
├── ditest              # Ana Python scripti
├── requirements.txt    # Python bağımlılıkları
├── setup.py           # Kurulum scripti
├── build.bat          # Otomatik build scripti (Windows)
├── README_KURULUM.md  # Bu dosya
├── build/             # Geçici build dosyaları (otomatik oluşturulur)
└── dist/              # Nihai EXE dosyası (otomatik oluşturulur)
    └── TEDiL.exe      # Çalıştırılabilir dosya
```

---

## ❓ Sık Sorulan Sorular

### EXE dosyası neden büyük?

PyInstaller, Python yorumlayıcısını ve tüm gerekli kütüphaneleri EXE'ye gömer. Bu nedenle dosya boyutu ~10-50 MB olabilir.

### Mac veya Linux için nasıl derlerim?

PyInstaller her platformda çalışır, ancak her platform için o platformda derleme yapmalısınız:
- Windows EXE → Windows'ta derleyin
- Mac APP → Mac'te derleyin  
- Linux → Linux'ta derleyin

### Kaynak kodumu koruyabilir miyim?

EXE dosyaları tamamen güvenli değildir. Tam koruma için:
- Kod obfuscation araçları kullanın
- Kritik mantığı sunucu tarafına taşıyın

---

## 📞 Destek

Sorun yaşarsanız:
1. Bu README'yi dikkatlice okuyun
2. Hata mesajlarını kontrol edin
3. Python ve PyInstaller sürümlerinizi kontrol edin

---

## ✅ Özet Kontrol Listesi

- [ ] Python kurulu mu? (`python --version`)
- [ ] PATH'e eklenmiş mi?
- [ ] PyInstaller kurulu mu? (`pip list | findstr pyinstaller`)
- [ ] `build.bat` çalıştırıldı mı?
- [ ] `dist/TEDiL.exe` oluştu mu?
- [ ] EXE test edildi mi?

Tüm adımlar tamamlandıysa, artık uygulamanızı paylaşabilirsiniz! 🎉
