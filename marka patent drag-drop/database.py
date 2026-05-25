import sqlite3

def get_connection():
    # scores.db adında bir veritabanı dosyası oluşturur
    # dosya yoksa otomatik yaratır
    conn = sqlite3.connect("scores.db")
    return conn

def create_table():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ad_soyad TEXT,
            skor TEXT,
            tarih TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_score(ad_soyad, skor, tarih):
    conn = get_connection()
    conn.execute(
        "INSERT INTO scores (ad_soyad, skor, tarih) VALUES (?, ?, ?)",
        (ad_soyad, skor, tarih)
    )
    conn.commit()
    conn.close()

def get_all_scores():
    conn = get_connection()
    cursor = conn.execute("SELECT ad_soyad, skor, tarih FROM scores")
    rows = cursor.fetchall()
    conn.close()
    return rows