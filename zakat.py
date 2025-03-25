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
