import mysql.connector
import pandas as pd


def create_connection():
    return mysql.connector.connect(
        host="localhost",     
        user="root",           
        password="",   
        database="zakat" 
    )

def add_zakat(nama, jenis_zakat, jumlah, tanggal):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO zakat_data (nama, jenis_zakat, jumlah, tanggal) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (nama, jenis_zakat, jumlah, tanggal))
    
    conn.commit()
    cursor.close()
    conn.close()

def update_zakat(id, nama, jenis_zakat, jumlah, tanggal):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = """UPDATE zakat_data 
               SET nama = %s, jenis_zakat = %s, jumlah = %s, tanggal = %s 
               WHERE id = %s"""
    cursor.execute(query, (nama, jenis_zakat, jumlah, tanggal, id))
    
    conn.commit()
    cursor.close()
    conn.close()

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

def add_transaksi_zakat(id_zakat, id_beras, jumlah_beras, tanggal):
    conn = create_connection()
    cursor = conn.cursor()
    
    # Menghitung total harga beras
    query_beras = "SELECT harga_per_kg FROM master_beras WHERE id = %s"
    cursor.execute(query_beras, (id_beras,))
    harga_per_kg = cursor.fetchone()[0]
    
    total_harga = harga_per_kg * jumlah_beras
    
    query = """INSERT INTO transaksi_zakat (id_zakat, id_beras, jumlah_beras, total_harga, tanggal) 
               VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (id_zakat, id_beras, jumlah_beras, total_harga, tanggal))
    
    conn.commit()
    cursor.close()
    conn.close()

def view_transaksi_zakat():
    conn = create_connection()
    cursor = conn.cursor()
    
    query = """SELECT tz.id, z.nama, z.jenis_zakat, m.nama_beras, tz.jumlah_beras, tz.total_harga, tz.tanggal
               FROM transaksi_zakat tz
               JOIN zakat_data z ON tz.id_zakat = z.id
               JOIN master_beras m ON tz.id_beras = m.id"""
    cursor.execute(query)
    result = cursor.fetchall()
    
    for row in result:
        print(f"ID Transaksi: {row[0]}, Nama Zakat: {row[1]}, Jenis Zakat: {row[2]}, Nama Beras: {row[3]}, "
              f"Jumlah Beras: {row[4]}, Total Harga: {row[5]}, Tanggal: {row[6]}")
    
    cursor.close()
    conn.close()