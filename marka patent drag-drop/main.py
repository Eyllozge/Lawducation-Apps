from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from database import create_table, save_score, get_all_scores

handler=app
app = FastAPI()
create_table()


class ScoreData(BaseModel):
    ad_soyad: str
    skor: str
    tarih: str

@app.post("/skor-kaydet")
def skor_kaydet(data: ScoreData):
    save_score(data.ad_soyad, data.skor, data.tarih)
    return {"mesaj": "Kaydedildi"}

@app.get("/skorlar")
def skorlar():
    rows = get_all_scores()
    return [{"ad_soyad": r[0], "skor": r[1], "tarih": r[2]} for r in rows]