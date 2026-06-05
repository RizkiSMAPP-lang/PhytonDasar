# Fungsi untuk menghitung rata-rata dari sejumlah angka
def hitung_rata_rata(angka):
    total = sum(angka)
    rata_rata = total / len(angka)
    return rata_rata

# fungsi untuk mendapatkan input angka dari pengguna 
def input_angka():
    angka = []
    while True:
        try:
            bilangan = float(input("masukkan angka (0 untuk mengak)"))
