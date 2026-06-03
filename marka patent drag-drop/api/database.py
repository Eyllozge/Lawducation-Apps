import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    
    return psycopg2.connect(
        host=os.getenv("PGHOST"),
        port=os.getenv("PGPORT"),
        dbname=os.getenv("PGDATABASE"),
        user=os.getenv("PGUSER"),
        password=os.getenv("PGPASSWORD")
    )

def create_table():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id SERIAL PRIMARY KEY,
                ad_soyad TEXT,
                skor INTEGER,
                toplam INTEGER,
                tarih TEXT
            )
        """)
        conn.commit()
    finally:
        cur.close()
        conn.close()

def save_score(ad_soyad, skor, toplam, tarih):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO scores (ad_soyad, skor, toplam, tarih) VALUES (%s, %s, %s, %s)",
            (ad_soyad, skor, toplam, tarih)
        )
        conn.commit()
    finally:
        cur.close()
        conn.close()

def get_all_scores():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT ad_soyad, skor, toplam, tarih FROM scores")
        rows = cur.fetchall()
        return rows
    finally:
        cur.close()
        conn.close()