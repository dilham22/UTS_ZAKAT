import mysql.connector
import pandas as pd


def create_connection():
    return mysql.connector.connect(
        host="localhost",      
        user="root",           
        password="",   
        database="zakat" 
    )

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

def delete_zakat(id):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "DELETE FROM zakat_data WHERE id = %s"
    cursor.execute(query, (id,))
    
    conn.commit()
    cursor.close()
    conn.close()

 def add_beras(nama_beras, harga_per_kg):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO master_beras (nama_beras, harga_per_kg) VALUES (%s, %s)"
    cursor.execute(query, (nama_beras, harga_per_kg))
    
    conn.commit()
    cursor.close()
    conn.close()

    def view_master_beras():
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM master_beras"
    cursor.execute(query)
    result = cursor.fetchall()
    
    for row in result:
        print(f"ID: {row[0]}, Nama Beras: {row[1]}, Harga per Kg: {row[2]}")
    
    cursor.close()
    conn.close()