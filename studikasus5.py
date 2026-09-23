def menghitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Kamar Standard":
        harga = 200000
    elif jenis_kamar == "Kamar Deluxe":
        harga = 350000
    else:
        return 0

    total_biaya = harga * lama_menginap
    return total_biaya


print("=== PEMESANAN KAMAR HOTEL ===")
nama_pelanggan = input("Nama Pelanggan: ")
jenis_kamar = input("Jenis kamar (Kamar Standard/Kamar Deluxe): ")
check_in = input("Tanggal check-in: ")
check_out = input("Tanggal check-out: ")
lama_menginap = int(input("Lama menginap (malam): "))

total_biaya = menghitung_biaya(jenis_kamar, lama_menginap)

print("\n=== DETAIL PEMESANAN KAMAR HOTEL ===")
print("Nama Pelanggan :", nama_pelanggan)
print("Jenis :", jenis_kamar)
print("Check-in :", check_in)
print("Check-out :", check_out)
print("Lama menginap :", lama_menginap, "malam")
print("Total biaya : Rp.", total_biaya)

