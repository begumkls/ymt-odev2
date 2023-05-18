# daire.py
# kat değerleri değişkenlere atanır.
araKat = 3
ustKat = 1.6
zeminKat = 1

def daireMetrekare(en,boy): # main.py modülünde kullanıcının girdiği en boy bilgiisne göre alan hesaplayan fonksiyon
    daireMetrekareHesabi = en*boy
    return daireMetrekareHesabi

def daireFiyat(a,alan): # main.py modülünde kullanıcının seçimine göre if else blokları yardımıyla kat belirlenmiş ve fiyat hesaplanmıştır.
    if a == 1:
        return araKat*alan*5000
    elif a == 2:
        return ustKat*alan*5000
    elif a == 3:
        return zeminKat*alan*5000
    else:
        print("Hatalı tuşlama yaptınız...")
        return None # kullanıcı hatalı tuşlama yaparsa kod herhangi değer döndürmez.
