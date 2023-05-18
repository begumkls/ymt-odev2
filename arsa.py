# arsa.py
# değişken global olacak şekilde atandı
denizKenari = 1.6
sehirMerkezi = 1.2
kirsal = 0.8
arsaBolge=0
def cember(r): # main.py modülünde kullanıcıdan alınan r değişkenine göre çember çevresini hesaplayan fonksiyon
    return 2*3.14*r

def dikdortgen(en,boy):  #  main.py modülünde kullanıcıdan alınan en ve boy değişkenlerine göre dikdörtgen çevresini hesaplayan fonksiyon
    return 2*(en+boy)

def arsaFiyat(bolge,cevre):  # main.py modülünde kullanıcıdan alınan bolge değişkenine göre bolge ve cevre parametreleri yardımıyla
    # arsa fiyatını yazdıran fonksiyon
    # kullanıcının seçimi if else blokları yardımıyla sınıflandıırlmıştır.
    global arsaBolge
    arsaBolge = bolge
    if arsaBolge == 1:
        return denizKenari*cevre*1000
    elif arsaBolge == 2:
        return sehirMerkezi*cevre*1000
    elif arsaBolge == 3:
        return kirsal*cevre*1000
    else:
        print("Hatalı tuşlama yaptınız...")
        return None # kullanıcı hatalı tuşlama yaparsa kod herhangi değer döndürmez.
        