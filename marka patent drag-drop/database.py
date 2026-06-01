import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("HATA: DATABASE_URL bulunamadı! .env dosyanı kontrol et.")
    return psycopg2.connect(db_url)

def create_table():
    conn = get_connection()
    try:
        cur = conn.cursor()
        # skor INTEGER, tarih DATE (veya TIMESTAMP) olarak değiştirildi.
        cur.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id SERIAL PRIMARY KEY,
                ad_soyad TEXT,
                skor INTEGER,
                tarih DATE
            )
        """)
        conn.commit()
    finally:
        cur.close()  # Cursor kapatıldı
        conn.close() # Hata olsa bile bağlantı kesinlikle kapatılacak

def save_score(ad_soyad, skor, tarih):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO scores (ad_soyad, skor, tarih) VALUES (%s, %s, %s)",
            (ad_soyad, int(skor), tarih) # skor'u integer'a çeviriyoruz
        )
        conn.commit()
    finally:
        cur.close()
        conn.close()

def get_all_scores():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT ad_soyad, skor, tarih FROM scores")
        rows = cur.fetchall()
        return rows
    finally:
        cur.close()
        conn.close()