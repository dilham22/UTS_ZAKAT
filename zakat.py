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
