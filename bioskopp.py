class Bioskop:
    def __init__(self, film, studio, harga, kursi):
        self.film = film
        self.studio = studio
        self.harga = harga
        self.kursi = kursi
        
    def print_info(self):
        print("Kategori :", self.__class__.__name__)
        print("Judul Film :", self.film)
        print("Studio :", self.studio)
        print("Harga :", "Rp {:,.2f}".format(self.harga))
        print("Nomor kursi yang tersedia :")
        for section, seats in self.kursi.items():
            print(section, " ".join(str(seat) for seat in seats))
        
    def pesan(self, section, seat):
        if seat in self.kursi[section]:
            self.kursi[section].remove(seat)
            print("Selamat menikmati Film", self.film + "!")
            return self.harga
        else:
            print("Maaf, kursi yang anda pilih tidak tersedia")
            return 0
        
class Reguler(Bioskop):
    def __init__(self, film, studio):
        kursi = {"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]}
        super().__init__(film, studio, 30000, kursi)
        
class Ultra(Bioskop):
    def __init__(self, film, studio):
        kursi = {"A": [1, 2, 3, 4, 5], "B": [6, 7, 8, 9, 10]}
        super().__init__(film, studio, 50000, kursi)
        
class XDUltra(Bioskop):
    def __init__(self, film, studio):
        kursi = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9], "D": [10, 11, 12]}
        super().__init__(film, studio, 75000, kursi)
        
class Gold(Bioskop):
    def __init__(self, film, studio):
        kursi = {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9], "D": [10, 11, 12]}
        super().__init__(film, studio, 100000, kursi)

class MesinTiket:
    def __init__(self):
        self.tiket_reguler = Reguler("Bumi Manusia", 3)
        self.tiket_ultra = Ultra("Spider-Man: No Way Home", 1)
        self.tiket_xdultra = XDUltra("Avengers: Endgame", 2)
        self.tiket_gold = Gold("Dune", 4)
        self.pesanan = []
        
    def print_menu(self):
        print("Selamat Datang di Bioskop XYZ")
        print("Pilih tiket yang ingin Anda pesan:")
        print("1. Reguler")
        print("2. Ultra")
        print("3. XD Ultra")
        print("4. Gold")
        print("5. Keluar")

    def pesan_tiket(self):
        while True:
            self.print_menu()
            choice = input("Masukkan nomor pilihan Anda: ")
            
            if choice == "1":
                self.tiket_reguler.print_info()
                section = input("Pilih area (A/B): ")
                seat = int(input("Pilih nomor kursi yang tersedia: "))
                price = int(input("Masukkan nominal uang anda: "))
                harga = self.tiket_reguler.pesan(section, seat)
                if price > harga :
                    self.pesanan.append(("Reguler", harga))
                else:
                    print("Maaf uang anda tidak cukup")
            
            
            elif choice == "2":
                self.tiket_ultra.print_info()
                section = input("Pilih area (A/B): ")
                seat = int(input("Pilih nomor kursi yang tersedia: "))
                price = int(input("Masukkan nominal uang anda: "))
                harga = self.tiket_ultra.pesan(section, seat)
                if price > harga :
                    self.pesanan.append(("Ultra", harga))
                else:
                    print("Maaf uang anda tidak cukup")
            
            
            elif choice == "3":
                self.tiket_xdultra.print_info()
                section = input("Pilih area (A/B/C/D): ")
                seat = int(input("Pilih nomor kursi yang tersedia: "))
                price = int(input("Masukkan nominal uang anda: "))
                harga = self.tiket_xdultra.pesan(section, seat)
                if price > harga :
                    self.pesanan.append(("XD Ultra", harga))
                else:
                    print("Maaf uang anda tidak cukup")
            
            
            elif choice == "4":
                self.tiket_gold.print_info()
                section = input("Pilih area (A/B/C/D): ")
                seat = int(input("Pilih nomor kursi yang tersedia: "))
                price = int(input("Masukkan nominal uang anda: "))
                harga = self.tiket_gold.pesan(section, seat)
                if price > harga :
                    self.pesanan.append(("Gold", harga))
                else:
                    print("Maaf uang anda tidak cukup")
            
            elif choice == "5":
                break
            
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        
        self.print_invoice()
    
    def print_invoice(self):
        print("Terima kasih telah membeli tiket di Bioskop XYZ.")
        total_harga = 0
        for pesanan in self.pesanan:
            print(pesanan[0], " - Harga: Rp {:,.2f}".format(pesanan[1]))
            total_harga += pesanan[1]
        print("Total harga: Rp {:,.2f}".format(total_harga))


tiket = MesinTiket()
tiket.pesan_tiket()