# TEDİL - Alıcı Dil + İfade Edici Uygulaması

TEDİL (Türkçe Erken Dil İzleme Listesi) - Alıcı Dil + İfade Edici Dil değerlendirme uygulaması. Bu uygulama, 2-7 yaş arası çocukların dil gelişimini değerlendirmek için kullanılır.

## Özellikler

- **Alıcı Dil Değerlendirmesi**: 38 madde ile alıcı dil becerilerini değerlendirme
- **İfade Edici Dil Değerlendirmesi**: 39 madde ile ifade edici dil becerilerini değerlendirme
- **Standart Puan Hesaplama**: Yaş gruplarına göre standart puan hesaplama
- **Bileşik Puan**: Alıcı ve ifade edici dil puanlarının toplamı
- **Yüzdelik Dilim**: Standart puanların yüzdelik karşılığı
- **Yaş Eşdeğeri**: Ham puanların yaş eşdeğeri karşılığı
- **Oturum Kaydetme/Yükleme**: JSON formatında oturum kaydetme
- **Norm Tablosu Yönetimi**: Özel norm tabloları yükleme/kaydetme

## Sistem Gereksinimleri

- **İşletim Sistemi**: Windows 10/11, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Python**: 3.8 veya üzeri (geliştirme için)
- **RAM**: En az 4GB
- **Disk Alanı**: En az 100MB

## Kurulum Seçenekleri

### Seçenek 1: Hazır Executable (Önerilen)

1. `dist` klasöründeki `TEDİL.exe` (Windows) veya `TEDİL` (Linux/macOS) dosyasını indirin
2. Dosyayı istediğiniz konuma kopyalayın
3. Çift tıklayarak çalıştırın
4. **Not**: Python yüklü olmasına gerek yoktur

### Seçenek 2: Kaynak Koddan Derleme

#### Windows için:

1. Python 3.8+ yükleyin
2. Bu klasörü açın
3. `build.bat` dosyasını çift tıklayın
4. Derleme tamamlandıktan sonra `dist\TEDİL.exe` dosyasını kullanın

#### Linux/macOS için:

```bash
# Gerekli kütüphaneleri yükle
pip3 install -r requirements.txt

# Derleme scriptini çalıştır
./build.sh

# Veya manuel olarak:
pyinstaller tedil.spec
```

### Seçenek 3: Python ile Çalıştırma

```bash
# Gerekli kütüphaneleri yükle
pip install -r requirements.txt

# Uygulamayı çalıştır
python ditest
```

## Kullanım

1. **Uygulamayı Başlatın**: TEDİL.exe dosyasını çift tıklayın
2. **Çocuk Bilgilerini Girin**: Yaş, ay, gün bilgilerini girin
3. **Alıcı Dil Testini Yapın**: Her madde için 0 (yapamadı) veya 1 (yaptı) puanlayın
4. **Puanları Hesaplayın**: "Alıcı Dil - PUANI HESAPLA" butonuna tıklayın
5. **İfade Edici Dil Testine Geçin**: "Testi Bitir ve İFADE EDİCİYE GEÇ" butonuna tıklayın
6. **İfade Edici Dil Testini Yapın**: Aynı şekilde puanlayın
7. **Genel Raporu Görüntüleyin**: "GENEL RAPOR" butonuna tıklayın

## Klavye Kısayolları

- `←` (Sol Ok): Önceki madde
- `→` (Sağ Ok): Sonraki madde
- `0`: Maddeyi 0 (yapamadı) olarak işaretle
- `1`: Maddeyi 1 (yaptı) olarak işaretle
- `Ctrl+S`: Oturumu kaydet

## Dosya Formatları

### Oturum Dosyası (.json)
```json
{
  "test": "TEDİL - Alıcı+İfade",
  "child_name": "Çocuk Adı",
  "age_year": 4,
  "age_month": 2,
  "age_day": 15,
  "timestamp": "20241201_143022",
  "current_subtest": "alici",
  "responses": {
    "alici": {"1": 1, "2": 0, ...},
    "ifade": {"1": 1, "2": 1, ...}
  }
}
```

### Norm Şablonu (.json)
```json
{
  "alici": {
    "columns": ["2-0_2-2", "2-3_2-5", ...],
    "rows": {
      "0": {"2-0_2-2": "74", "2-3_2-5": "72", ...},
      "1": {"2-0_2-2": "75", "2-3_2-5": "73", ...}
    }
  },
  "ifade": { ... },
  "composite": [ ... ],
  "percentiles": [ ... ],
  "age_equiv": { ... }
}
```

## Sorun Giderme

### Uygulama Açılmıyor
- Windows'ta: Antivirus yazılımı engelliyor olabilir, güvenlik ayarlarını kontrol edin
- Linux'ta: `chmod +x TEDİL` komutu ile çalıştırma izni verin
- macOS'ta: Güvenlik ayarlarından "Bilinmeyen geliştiricilerden gelen uygulamalara izin ver" seçeneğini etkinleştirin

### Puanlar Hesaplanmıyor
- Yaş bilgilerinin doğru girildiğinden emin olun (2-7 yaş arası)
- En az bir maddeyi puanladığınızdan emin olun
- Norm tablolarının yüklü olduğundan emin olun

### Performans Sorunları
- Uygulamayı yeniden başlatın
- Bilgisayarınızı yeniden başlatın
- Antivirus yazılımını geçici olarak devre dışı bırakın

## Geliştirici Bilgileri

- **Geliştirici**: TEDİL Development Team
- **Versiyon**: 1.0.0
- **Lisans**: MIT License
- **Python Versiyonu**: 3.8+
- **GUI Framework**: Tkinter

## Katkıda Bulunma

1. Bu projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeni-ozellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim

- **E-posta**: tedil@example.com
- **GitHub**: https://github.com/example/tedil
- **Web Sitesi**: https://example.com/tedil

## Sürüm Notları

### v1.0.0 (2024-12-01)
- İlk sürüm
- Alıcı dil değerlendirmesi
- İfade edici dil değerlendirmesi
- Standart puan hesaplama
- Bileşik puan hesaplama
- Yüzdelik dilim hesaplama
- Yaş eşdeğeri hesaplama
- Oturum kaydetme/yükleme
- Norm tablosu yönetimi
- Executable dosya desteği