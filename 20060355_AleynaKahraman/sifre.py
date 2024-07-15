ALFABE = 'abcçdefgğhıijklmnoöprsştuüvyz'

def sifrele(metin, a, b):
    sifreli_metin = ''
    for harf in metin:
        if harf.lower() in ALFABE:
            harf_sira = ALFABE.index(harf.lower())
            sifreli_harf_sira = (a * harf_sira + b) % len(ALFABE)
            sifreli_metin += ALFABE[sifreli_harf_sira].upper() if harf.isupper() else ALFABE[sifreli_harf_sira]
        else:
            sifreli_metin += harf
    return sifreli_metin

def desifre(sifreli_metin, a, b):
    orijinal_metin = ''
    for harf in sifreli_metin:
        if harf.lower() in ALFABE:
            sifreli_harf_sira = ALFABE.index(harf.lower())
            orijinal_harf_sira = ((sifreli_harf_sira - b) * mod_inverse(a, len(ALFABE))) % len(ALFABE)
            orijinal_metin += ALFABE[orijinal_harf_sira].upper() if harf.isupper() else ALFABE[orijinal_harf_sira]
        else:
            orijinal_metin += harf
    return orijinal_metin

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def ayarla_dogum_tarihi(tarih):
    try:
        gun, ay, yil = map(int, tarih.split('.'))
    except ValueError:
        print("Hatalı format! Lütfen doğru formatta (GG.AA.YYYY) girin.")
        return None, None
    # Basit bir örnek doğum tarihine dayalı ayarlama
    a = (gun + ay) % len(ALFABE) + 1  # 1-29 arası bir çarpma faktörü
    b = (ay + yil) % len(ALFABE) + 1  # 1-29 arası bir kaydırma miktarı
    return a, b

while True:
    islem_turu = input("Şifrelemek için 'şifrele', deşifrelemek için 'deşifrele' yazın, çıkmak için 'q' yazın: ").lower()

    if islem_turu == 'şifrele':
        metin = input("Şifrelemek istediğiniz metni girin: ")
        
        while True:
            dogum_tarihi = input("Doğum tarihinizi (GG.AA.YYYY formatında) girin: ")
            a, b = ayarla_dogum_tarihi(dogum_tarihi)
            if a is not None and b is not None:
                break

        # Şifreleme işlemi
        sifreli_metin = sifrele(metin, a, b)
        print("Şifrelenmiş Metin:", sifreli_metin)
    elif islem_turu == 'deşifrele':
        sifreli_metin = input("Deşifrelemek istediğiniz metni girin: ")
        
        while True:
            dogum_tarihi = input("Doğum tarihinizi (GG.AA.YYYY formatında) girin: ")
            a, b = ayarla_dogum_tarihi(dogum_tarihi)
            if a is not None and b is not None:
                break

        # Şifre çözme işlemi
        orijinal_metin = desifre(sifreli_metin, a, b)
        print("Orijinal Metin:", orijinal_metin)
    elif islem_turu == 'q':
        break
    else:
        print("Geçersiz işlem türü. Lütfen 'şifrele', 'deşifrele' veya 'q' (çıkış) olarak yazın.")
