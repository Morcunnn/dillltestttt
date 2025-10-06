#!/bin/bash
# TEDİL Uygulamasını Çalıştır

echo "TEDİL Uygulaması Başlatılıyor..."
echo "================================="

# Mevcut dizini kontrol et
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXECUTABLE="$SCRIPT_DIR/TEDİL"

if [ ! -f "$EXECUTABLE" ]; then
    echo "HATA: TEDİL executable dosyası bulunamadı!"
    echo "Dosya yolu: $EXECUTABLE"
    exit 1
fi

# Çalıştırma izni ver
chmod +x "$EXECUTABLE"

# Uygulamayı çalıştır
echo "Uygulama başlatılıyor..."
"$EXECUTABLE"
