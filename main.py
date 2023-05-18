# main.py
# main'de kullanılmak üzere arsa ve daire modülleri import edildi.
import daire
import arsa
# kullanıcıya kolaylık sağlamak adına bir seçim ekranı oluşturuldu.
def secimEkrani():
    print()
    print("1. Arsa")
    print("2. Daire")
    print("3. Havuz")
    print("4. Çıkış yapmak için h ya da H tuşlayınız..")
    print()
# işlemler main fonksiyonunda yapıldı.   
def main():

    cikis = "e"
    while cikis != "h" and cikis != "H": # kullanıcı "h" ya da "H" tuşlayana kadar döngünün devamı sağlandı.
        secimEkrani()
        secim = int(input("Lütfen fiyat hesaplaması yapmak için bir 1 ya da 2 olacak şeklinde tuşlama yapınız: "))
        # Kullanıcının seçimine göre if else blokları ile işleme devam edildi.
        if secim == 1:
            print()
            sekil = int(input("Arsa şeklini dikdörtgen istiyorsanız 1, çember istiyorsanız 2 tuşlayınız: "))
            print()
            
            if sekil == 1:
                x = int(input("Lütfen arsanın  en uzunluğunu giriniz: "))
                y = int(input("Lütfen arsanın  boy uzunluğunu giriniz: "))
                cevre = arsa.dikdortgen(x,y) # arsa.py modülündeki dikdortgen fonksiyonu yardımıyla arsanın çevresi hesaplandı.
            elif sekil == 2:
                z = int(input("Lütfen arsanın yarıçap uzunluğunu giriniz: "))
                cevre = arsa.cember(z) # arsa.py modülündeki cember fonksiyonu yardımıyla arsanın çevresi hesaplandı.
            else:
                print()
                print("Hatalı tuşlama yaptınız..")
                continue #secim atamasına geri yönlendirir.
            
            print()
            bolge = int(input("Deniz kenarı için 1, şehir merkezi için 2, kırsal için 3 tuşlayınız...: "))
            fiyat = arsa.arsaFiyat(bolge,cevre) # kullanıcının seçimine göre arsa.py modülünde if else blokları ile arsa fiyatı belirlendi.
            
            if fiyat is None:
                continue # kullanıcı hatalı giriş yaptığı için işlem en başa alındı.
            else:
                print()
                print(f"Arsa için fiyat: {fiyat:.2f}") 
            
        elif secim == 2:
            en=int(input("Dairenin enini giriniz: " ))
            boy=int(input("Dairenin boyunu giriniz: "))
            alan = daire.daireMetrekare(en,boy) # daire.py modülündeki daireMetrekare fonksiyonu yardımıyla daire alanı hesaplandı.
            a = int(input("ara kat için 1, üst kat için 2, zemin kat için 3'ü tuşlayınız: "))
            fiyat = daire.daireFiyat(a,alan) # kullanıcının kat girdisine göre daire fiyatı hesaplandı.
            
            if fiyat is None:
                continue # kullanıcı hatalı giriş yaptığı için işlem en başa alındı.
            else:
                print()
                print(f"Seçmiş olduğunuz daire fiyatı: {fiyat:.2f} türk lirası")
                
        elif secim == 3:
            havuzEn = int(input("Havuzun en uzunluğunu giriniz: "))
            havuzBoy = int(input("Havuzun boy uzunluğunu giriniz: "))
            havuzDerinlik = int(input("Havuzun derinlik uzunluğunu giriniz: "))
            adet = int(input("Lutfen kac adet havuz yaptırmak isteginizi giriniz.."))
            print("Lutfen nerede havuz yaptıracagınızı seciniz...")
            havuzMaliyet = havuzEn*havuzBoy*havuzDerinlik*adet*1000
            print(f"Havuzun maliyeti {havuzMaliyet:.2f} türk lirasıdır")
            
        elif secim == 4:
            cikis = input("Fiyat hesaplama işlemine devam etmek ister misiniz? (e/E/h/H) h/H tuşlanması durumunda program sonlandırılacak...: ")
            # while yardımıyla kullanıcının işleme devam edip etmeyeceği sorgulandı
            while cikis not in ["e", "E", "h", "H"]: # kullanıcı "e", "E", "h", "H" tuşlarından biri tuşlamazsa döngü tekrar eder.
                cikis = input("Lütfen geçerli tuşlama yapınız.. (e/E/h/H): ") # kullanıcı "e" ya da "E" tuşlarsa döngü başa alınır.
            # "h" ya da "H" tuşlaması durumunda döngüden çıkılır ve program sonlanır.    
        else:
            print()
            print("Hatalı tuşlama yaptınız... ")
            continue #secim atamasına geri yönlendirir.
                
main() # main fonksiyonu çalıştırılır.