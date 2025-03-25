import pandas as pd
import os

# Data awal
harga_beras = 15000  # Harga default per kg
data_zakat = []
filename = "data_zakat.xlsx"

def tampilkan_harga_beras():
    print(f"\nHarga beras saat ini: Rp {harga_beras:,} per kg\n")

def input_harga_beras():
    global harga_beras
    try:
        baru = int(input("Masukkan harga beras baru per kg: "))
        if baru > 0:
            harga_beras = baru
            print("Harga beras berhasil diperbarui!")
            tampilkan_harga_beras()
        else:
            print("Harga harus lebih dari 0!")
    except ValueError:
        print("Input harus berupa angka!")

def hitung_zakat():
    nisab = 520 * harga_beras  # Nisab 520 kg beras
    print(f"\nNisab zakat saat ini: Rp {nisab:,}")
    
    try:
        nama = input("Nama Muzakki: ")
        harta = int(input("Jumlah harta (Rp): "))
        anggota = int(input("Jumlah anggota keluarga: "))
        
        if harta >= nisab:
            zakat = harta * 0.025  # 2.5%
            print(f"\nZakat yang harus dibayar: Rp {zakat:,}")
            
            # Tambahkan ke data
            data_zakat.append({
                "Nama": nama,
                "Harta (Rp)": harta,
                "Anggota Keluarga": anggota,
                "Zakat (Rp)": zakat,
                "Status": "Lunas"
            })
            print("Pembayaran zakat berhasil dicatat!")
        else:
            print("\nHarta Anda belum mencapai nisab, tidak wajib zakat.")
    except ValueError:
        print("Input harus berupa angka untuk harta dan anggota keluarga!")
