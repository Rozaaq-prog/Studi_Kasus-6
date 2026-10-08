import json
import os

NAMA_FILE = r"C:\Users\Rozak\OneDrive\Documents\DDP\investaris.json"


# Membaca data dari file JSON
def baca_data():
    if not os.path.exists(NAMA_FILE):
        return []

    with open(NAMA_FILE, "r") as file:
        return json.load(file)


# Menampilkan seluruh data barang
def tampilkan_data():
    data = baca_data()

    if not data:
        print("\nData inventaris masih kosong.")
        return

    print("\n===== DATA INVENTARIS BARANG =====")
    for barang in data:
        print(f"ID     : {barang['id']}")
        print(f"Nama   : {barang['nama']}")
        print(f"Stok   : {barang['stok']}")
        print(f"Harga  : Rp{barang['harga']}")
        print("-" * 35)


# Menambahkan barang baru ke file
def tambah_barang():
    data = baca_data()

    id_barang = input("Masukkan ID barang  : ")
    nama = input("Masukkan nama barang: ")
    stok = int(input("Masukkan stok       : "))
    harga = int(input("Masukkan harga      : "))

    barang_baru = {
        "id": id_barang,
        "nama": nama,
        "stok": stok,
        "harga": harga
    }

    data.append(barang_baru)

    with open(NAMA_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("\nData barang berhasil ditambahkan!")


# Program utama
def main():
    while True:
        print("\n===== SISTEM MANAJEMEN INVENTARIS =====")
        print("1. Tampilkan Data Barang")
        print("2. Tambah Barang")
        print("3. Keluar")

        pilihan = input("Pilih menu (1-3): ")

        if pilihan == "1":
            tampilkan_data()

        elif pilihan == "2":
            tambah_barang()

        elif pilihan == "3":
            print("\nProgram selesai.")
            break

        else:
            print("\nPilihan tidak valid!")


main()