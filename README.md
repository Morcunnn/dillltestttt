# TEDİL - Alıcı Dil + İfade Edici Uygulaması

TEDİL (Test of Early Development of Language) uygulaması, 2-7 yaş arası çocukların alıcı ve ifade edici dil becerilerini değerlendirmek için geliştirilmiş kapsamlı bir değerlendirme aracıdır.

## Özellikler

- **Alıcı Dil Değerlendirmesi**: 38 madde ile kapsamlı alıcı dil becerisi değerlendirmesi
- **İfade Edici Dil Değerlendirmesi**: 39 madde ile ifade edici dil becerisi değerlendirmesi
- **Otomatik Puanlama**: Ham puan, standart puan, yüzdelik ve yaş eşdeğeri hesaplama
- **Bileşik Puan**: Alıcı ve ifade edici dil puanlarının birleşik değerlendirmesi
- **Veri Kaydetme**: Test sonuçlarını JSON formatında kaydetme ve yükleme
- **Kullanıcı Dostu Arayüz**: Modern ve sezgisel grafik arayüz

## Sistem Gereksinimleri

- **Python**: 3.8 veya üzeri
- **İşletim Sistemi**: Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **RAM**: En az 4GB
- **Disk Alanı**: 100MB boş alan

## Kurulum

### Otomatik Kurulum (Önerilen)

1. **Kurulum scriptini çalıştırın:**
   ```bash
   python install.py
   ```

2. **Uygulamayı başlatın:**
   - Windows: `run_tedil.bat` dosyasını çift tıklayın
   - Linux/macOS: `./run_tedil.sh` çalıştırın

### Manuel Kurulum

1. **Gerekli paketleri yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Uygulamayı çalıştırın:**
   ```bash
   python ditest
   ```

## Executable Oluşturma

Kurulabilir tek dosya executable oluşturmak için:

```bash
python build_exe.py
```

Bu komut şunları oluşturur:
- `dist/TEDIL.exe` (Windows)
- `dist/TEDIL` (Linux/macOS)
- Kurulum scriptleri

## Kullanım

### 1. Çocuk Bilgilerini Girme
- Uygulama açıldığında çocuğun adı, yaşı (yıl/ay/gün) bilgilerini girin
- Yaş bilgisi 2-7 yaş arasında olmalıdır

### 2. Test Uygulama
- **Alıcı Dil Testi**: Her madde için çocuğun performansını değerlendirin
- **Yanıt Seçenekleri**: 
  - 1: Yaptı/Başardı
  - 0: Yapamadı/Başaramadı
  - (boş): Değerlendirilmedi

### 3. Puanlama
- **Bireysel Puanlama**: Her alt test için ayrı ayrı puan hesaplama
- **Genel Rapor**: Bileşik puan, yüzdelik ve yaş eşdeğeri hesaplama

### 4. Veri Kaydetme
- **Oturum Kaydetme**: Test verilerini JSON formatında kaydetme
- **Norm Tablosu**: Özel norm tablolarını yükleme/kaydetme

## Klavye Kısayolları

- `←` / `→`: Önceki/Sonraki madde
- `0` / `1`: Hızlı yanıt girişi
- `Ctrl+S`: Oturumu kaydet

## Dosya Yapısı

```
tedil-app/
├── ditest                 # Ana uygulama dosyası
├── requirements.txt       # Python bağımlılıkları
├── setup.py              # Paket kurulum dosyası
├── build_exe.py          # Executable oluşturma scripti
├── install.py            # Otomatik kurulum scripti
├── run_tedil.bat         # Windows çalıştırma scripti
├── run_tedil.sh          # Linux/macOS çalıştırma scripti
└── README.md             # Bu dosya
```

## Norm Tabloları

Uygulama aşağıdaki norm tablolarını içerir:
- **Alıcı Dil Normları**: 2-7 yaş arası standart puanlar
- **İfade Edici Dil Normları**: 2-7 yaş arası standart puanlar
- **Bileşik Puan Normları**: Toplam standart puan dönüşümleri
- **Yüzdelik Normları**: Standart puan-yüzdelik eşleştirmeleri
- **Yaş Eşdeğeri Normları**: Ham puan-yaş eşdeğeri dönüşümleri

## Sorun Giderme

### Python Bulunamadı Hatası
- Python 3.8+ yüklü olduğundan emin olun
- PATH değişkeninde Python'un bulunduğunu kontrol edin

### Modül Bulunamadı Hatası
```bash
pip install -r requirements.txt
```

### GUI Açılmıyor
- Tkinter'ın yüklü olduğunu kontrol edin:
  ```bash
  python -c "import tkinter"
  ```

### Executable Çalışmıyor
- Antivirus yazılımının engellemediğini kontrol edin
- Windows Defender'da istisna ekleyin

## Geliştirici Notları

### Bağımlılıklar
- `tkinter`: GUI framework (Python ile birlikte gelir)
- `json`: Veri serileştirme (Python ile birlikte gelir)
- `datetime`: Tarih/saat işlemleri (Python ile birlikte gelir)
- `typing`: Tip kontrolü (Python 3.5+ ile birlikte gelir)
- `pyinstaller`: Executable oluşturma

### Kod Yapısı
- `ALICI_ITEMS`: Alıcı dil test maddeleri
- `IFADE_ITEMS`: İfade edici dil test maddeleri
- `NORM_TABLES`: Tüm norm tabloları
- `App`: Ana uygulama sınıfı
- `compute_score()`: Puanlama algoritması
- `lookup_*()`: Norm tablosu arama fonksiyonları

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## İletişim

Sorularınız için: info@tedil.com

## Sürüm Geçmişi

- **v1.0.0**: İlk sürüm
  - Alıcı ve ifade edici dil değerlendirmesi
  - Otomatik puanlama sistemi
  - Veri kaydetme/yükleme
  - Executable oluşturma desteği