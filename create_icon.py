#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TEDİL uygulaması için basit icon oluşturucu
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

def create_simple_icon():
    """Basit bir icon oluştur"""
    if not PIL_AVAILABLE:
        print("PIL (Pillow) yüklü değil, basit icon oluşturulamıyor")
        return False
    
    # 64x64 boyutunda icon oluştur
    size = 64
    img = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Arka plan dairesi
    draw.ellipse([2, 2, size-2, size-2], fill=(70, 130, 180, 255), outline=(0, 0, 0, 255), width=2)
    
    # T harfi çiz
    # Dikey çizgi
    draw.rectangle([size//2-3, 8, size//2+3, size-8], fill=(255, 255, 255, 255))
    # Yatay çizgi
    draw.rectangle([8, 20, size-8, 26], fill=(255, 255, 255, 255))
    
    # Icon'u kaydet
    img.save('icon.png')
    print("icon.png oluşturuldu")
    return True

if __name__ == "__main__":
    create_simple_icon()