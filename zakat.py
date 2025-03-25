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
