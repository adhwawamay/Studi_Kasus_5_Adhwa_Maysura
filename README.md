# Studi_Kasus_5_Adhwa_Maysura

Nama  : Adhwa Maysura<br>
NIM   : 2609116103<br>
Kelas : C

## Membuat Function
<img width="1494" height="274" alt="1 5" src="https://github.com/user-attachments/assets/ba8138dc-a731-481d-87d7-38d04e93882b" />

1. Disini kita akan membuat **function** untuk menghitung biaya kamar dari 2 data **(parameter)** yaitu **jenis_kamar & lama_menginap**.

2. Kemudian ada **if** untuk mengecek kondisi,<br>
dimana **jenis_kamar == "Kamar Standard"** diharga 200.000 per malam sama seperti **jenis_kamar == "Kamar Deluxe"** diharga 350.000 per malam (lama_menginap) dengan menggunakan code **elif**.

3. Lalu **else:** **return 0** dijalankan apabila 2 kondisi tersebut tidak terpenuhi, yang artinya **function** mengembalikan nilai 0 sebagai total biaya.

4. Terakhir menghitung total biaya dengan **total_biaya = harga * lama_menginap** rumus dari code ini akan otomatis memasukan harga dari jenis kamar X lama menginap. Untuk code **return total_biaya** disebut return value adalah nilai hasil akhir yang dikirimkan kembali oleh sebuah fungsi setelah tugasnya selesai.

## Menginput Data
<img width="1573" height="228" alt="2 5" src="https://github.com/user-attachments/assets/52019117-c5cc-4d78-ac98-ba5f1cd2c123" />

1. **print** digunakan untuk menampilkan tulisan di sistem (bentuk ouput).

2. **input** digunakan agar pengguna dapat memasukkan data seperti :
  - nama pelanggan
  - jenis kamar
  - tanggal check-in
  - tanggal check-out
  - lama menginap

3. Memanggil function dengan **total_biaya = menghitung_biaya(jenis_kamar, lama_menginap)** untuk menghitung total biaya yang akan disimpan ke **total_biaya**.

## Menampilkan Output
<img width="1614" height="213" alt="3 5" src="https://github.com/user-attachments/assets/e485b77c-3eb0-41fa-947a-62352d1d5d93" />

1. **print("\n=== DETAIL PEMESANAN KAMAR HOTEL ===")** akan ditampilkan pada output sebagai bentuk detail pemesanan kamar hotel.

2. **print("Nama Pelanggan :", nama_pelanggan)** menampilkan "Nama Pelanggan" yang sebelumnya dimasukkan oleh pengguna

3. **print("Jenis :", jenis_kamar)** menampilkan output "Jenis" dari input jenis_kamar sebelumnya

4. **print("Check-in :", check_in),
     print("Check-out :", check_out)** sama seperti sebelumnya akan menampilkan keterangan tanggal yang dimasukkan pengguna

5. **print("Lama menginap :", lama_menginap, "malam")** menampilkan lama menginap dalam bentuk per malam ("malam")

6. **print("Total biaya : Rp.", total_biaya)** menampilkan total biaya dalam bentuk rupiah ("Rp.")


# Hasil Run
   <img width="1575" height="444" alt="run 5" src="https://github.com/user-attachments/assets/c861611f-8eb7-495c-88ee-95b270620887" />


