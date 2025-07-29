import random

def main():
    print("=== Kuis sederhana ===")
    nama_pengguna = input("Masukkan Nama Anda: ")
    print(f"Selamat datang, {nama_pengguna}! mari mulai kuis.\n")

    while True:
        skor1 = pertanyaan_satu()
        skor2 = pertanyaan_dua()
        skor3 = pertanyaan_tiga()
        
        skor_akhir = hitung_skor(skor1, skor2, skor3)
        print(f"\nSkor Akhir Anda: {skor_akhir}")

        if skor_akhir == 30:
            print("Luar biasa! Semua jawaban benar!")
        elif skor_akhir >= 20:
            print("Bagus! Tapi masih bisa lebih baik.")
        else:
            print("Coba lagi nanti!")

        ulang = input("\nApakah Anda ingin bermain lagi? (y/n): ").lower()
        if ulang != 'y':
            print(f"\nTerima kasih sudah bermain!{nama_pengguna}")
            break
        else:
            print("\n=== Mulai ulang kuis ===\n")

def pertanyaan_satu():
    jawaban = input("1. Apakah ibukota Indonesia? ")
    if jawaban.lower() == "jakarta":
        print("Benar! Anda mendapatkan 10 poin.")
        return 10
    else:
        print("Salah. Jawaban yang benar adalah Jakarta. Anda tidak mendapatkan poin.")
        return 0

def pertanyaan_dua():
    jawaban = input("2. Berapakah hasil dari 5 + 7? ")
    if jawaban.isdigit() and int(jawaban) == 12:
        print("Benar! Anda mendapatkan 10 poin.")
        return 10
    else:
        print("Salah. Jawaban yang benar adalah 12. Anda tidak mendapatkan poin.")
        return 0

def pertanyaan_tiga():
    print("3. Tebak angka yang saya pikirkan antara 1 hingga 10.")
    angka_pikiran = random.randint(1, 10)
    jawaban = input("Tebak angka: ")

    if jawaban.isdigit() and int(jawaban) == angka_pikiran:
        print(f"Benar! Angka yang saya pikirkan adalah {angka_pikiran}. Anda mendapatkan 10 poin.")
        return 10
    else:
        print(f"Salah. Angka yang saya pikirkan adalah {angka_pikiran}. Anda tidak mendapatkan poin.")
        return 0

def hitung_skor(s1, s2, s3):
    return s1 + s2 + s3

if __name__ == "__main__":
    main()
