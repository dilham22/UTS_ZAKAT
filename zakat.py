import mysql.connector
import pandas as pd


def create_connection():
    return mysql.connector.connect(
        host="localhost",      
        user="root",           
        password="",   
        database="zakat" 
    )