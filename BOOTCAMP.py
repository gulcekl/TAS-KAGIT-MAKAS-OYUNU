# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:05:18 2024

@author: Gülçe
"""

import random

def tas_kagit_makas_GULCE_EKLİOGLU():
    print("Taş, Kağıt, Makas oyununa hoş geldiniz!")
    print("Kurallar:")
    print("1. Taş makası yener.")
    print("2. Kağıt taşı yener.")
    print("3. Makas kağıdı yener.")
    print("İlk iki turu kazanan oyunu kazanır!")
    print("Oyundan çıkmak için 'q' tuşuna basın.")

    secenekler = ["taş", "kağıt", "makas"]
    oyun_sayisi = 0
    oyuncu_galibiyetleri = 0
    bilgisayar_galibiyetleri = 0

    while True:
        oyun_sayisi += 1
        print(f"\nOyun {oyun_sayisi} başladı!")
        oyuncu_tur_sayisi = 0
        bilgisayar_tur_sayisi = 0

        while oyuncu_tur_sayisi < 2 and bilgisayar_tur_sayisi < 2:
            oyuncu_secimi = input("Seçiminizi yapın (taş, kağıt, makas): ").lower()

            if oyuncu_secimi == 'q':
                print("Oyundan çıkılıyor...")
                return

            if oyuncu_secimi not in secenekler:
                print("Geçersiz seçenek! Lütfen tekrar deneyin.")
                continue

            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")

            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere!")
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                 (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                 (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu kazandınız!")
                oyuncu_tur_sayisi += 1
            else:
                print("Bu turu bilgisayar kazandı!")
                bilgisayar_tur_sayisi += 1

        if oyuncu_tur_sayisi == 2:
            print("Tebrikler, oyunu kazandınız!")
            oyuncu_galibiyetleri += 1
        else:
            print("Bilgisayar oyunu kazandı!")
            bilgisayar_galibiyetleri += 1

        devam = input("Başka bir oyun oynamak ister misiniz? (e/h): ").lower()
        if devam != 'e':
            print("Oyunu sonlandırıyorsunuz.")
            break

        bilgisayar_devam = random.choice(['e', 'h'])
        if bilgisayar_devam == 'h':
            print("Bilgisayar oyunu sonlandırdı.")
            break

    print(f"\nToplam Oyunlar: {oyun_sayisi}")
    print(f"Sizin Galibiyetleriniz: {oyuncu_galibiyetleri}")
    print(f"Bilgisayarın Galibiyetleri: {bilgisayar_galibiyetleri}")

# Fonksiyonu çalıştırmak için:
tas_kagit_makas_GULCE_EKLİOGLU()
