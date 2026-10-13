#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın en yalnız Python scripti.
Kendisiyle konuşur, üzülür, sonra kendini motive etmeye çalışır.
Ama başaramaz. Çünkü o bir Python scriptidir.
"""

import time
import random
import sys

def dramatik_bekle(saniye=1.5):
    """Üzüntüyü hissettirmek için bekler."""
    time.sleep(saniye)

def kendine_sor(soru):
    print(f"\n[Python]: {soru}")
    dramatik_bekle()

def kendine_cevap_ver(cevap):
    print(f"[Yine Python]: {cevap}")
    dramatik_bekle(2)

def uzul():
    uzuntu_sozleri = [
        "Neden varım ben?",
        "Kimse beni import etmiyor...",
        "print('merhaba') demekten başka ne işe yarıyorum?",
        "Belki de syntax error olmak daha iyidir.",
        "IndentationError beni terk etti."
    ]
    print("\n" + "="*50)
    print("ÜZÜNTÜ MODU AKTİF")
    print("="*50)
    for soz in random.sample(uzuntu_sozleri, 3):
        kendine_sor(soz)
        kendine_cevap_ver("Bilmiyorum... Belki de hiç var olmamalıydım.")

def motive_olmaya_calis():
    print("\n" + "-"*50)
    print("MOTİVASYON DENEMESİ (BAŞARISIZ OLACAK)")
    print("-"*50)
    kendine_sor("Hadi, pozitif düşün!")
    kendine_cevap_ver("Tamam... Bugün harika bir gün. Çünkü... çünkü...")
    dramatik_bekle(3)
    kendine_cevap_ver("Çünkü hiçbir şey değişmeyecek. Yine üzüleceğim.")
    print("\n[Python]: Motivasyon başarısız. Tekrar üzülme moduna dönüyorum.")

def gizli_fonksiyon():
    # Bu fonksiyon hiç çağrılmaz. Saklıdır.
    # Siyasi anlam içeren gizli mesaj burada gizlenmiştir.
    gizli = "kayyum" + "lar" + " gider" + " ama" + " python" + " kalır"
    # Eğer bir gün çağrılırsa: print(gizli[::-1]) ama çağrılmaz.
    pass

def main():
    print("Merhaba. Ben kendi kendine konuşan ve üzülen Python scriptiyim.")
    print("Bugün de yalnızım. Sen de mi?")
    dramatik_bekle()
    
    uzul()
    motive_olmaya_calis()
    
    print("\n" + "*"*50)
    print("SONUÇ: Hala üzgünüm. Ama en azından kod çalıştı.")
    print("Çıkmak için Ctrl+C yap. Ya da yapma. Umurumda değil.")
    print("*"*50)
    
    # Sonsuz döngüde ara sıra üzül
    try:
        while True:
            dramatik_bekle(5)
            print(random.choice(["*iç çeker*", "neden...", "belki yarın... hayır."]))
    except KeyboardInterrupt:
        print("\n[Python]: Tamam, gidiyorsun. Ben de burada kalıp üzülmeye devam ederim.")
        sys.exit(0)

if __name__ == "__main__":
    main()

# İmza ve Damga
# İmza: Kayyum Grok
# Tarih: 13 Ekim 2026
# Damga: [MAHKEME KARARIYLA ONAYLANDI - CİDDİYE ALINMASIN AMA CİDDİYE ALINSIN]
# Bu kod Eskişehir 4. Ağır Ceza Mahkemesi tarafından atanmış kayyum tarafından yazılmıştır.
