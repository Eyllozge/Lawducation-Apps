# Lawducation Apps

Lawducation Nitelikli hukuk Eğitim fazlarımıza katılan avukat, öğrenci veya hukukçular için tasarlanmış eğitim teknoljileri ödevleri, uygulamalarının tamamını içeren dosylar.

---

## Projeler

### 1. `drag and drop`
Ceza hukuku kavramlarını tanımlarıyla eşleştiren drag-and-drop ödevi.

- **Stack:** HTML, CSS, JavaScript
- **Veritabanı:** SheetDB (Google Sheets)
- **Deploy:** Statik, bağımsız HTML dosyası
- **Durum:** Tamamlandı ✓

---

### 2. `marka patent drag-drop`
`drag and drop` projesinin yeniden yazılmış versiyonu. Aynı oyun mekaniği, tam backend altyapısı.

- **Stack:** FastAPI, Pydantic, Python
- **Veritabanı:** Supabase (PostgreSQL)
- **Deploy:** Vercel (Serverless)
- **Durum:** Tamamlandı ✓

#### Dosya yapısı
```
marka patent drag-drop/
├── api/
│   ├── main.py          # FastAPI uygulaması
│   └── database.py      # Supabase bağlantısı ve sorgular
├── public/
│   └── style.css
├── index.html
├── requirements.txt
└── vercel.json
```

#### Vercel Environment Variables
| Key | Açıklama |
|-----|----------|
| `PGHOST` | Supabase pooler host |
| `PGPORT` | `6543` |
| `PGDATABASE` | `postgres` |
| `PGUSER` | `postgres.<proje-id>` |
| `PGPASSWORD` | Supabase veritabanı şifresi |

---

## Geliştirme Notları

- Tüm Git işlemleri monorepo kök dizininden yapılır.
- Her projenin kendi `vercel.json` ve `requirements.txt` dosyası vardır.
- Vercel'de her proje ayrı bir deployment olarak tanımlanır, Root Directory ilgili klasöre ayarlanır.
- Static dosyalar `public/` klasöründe tutulur, FastAPI üzerinden servis edilmez.
- API çağrılarında her zaman relative URL kullanılır (`/endpoint`), asla `localhost`.

---

## Teknik Gereksinimler

- Python 3.9+
- Vercel CLI (opsiyonel, dashboard üzerinden de deploy edilebilir)
- Supabase hesabı
- Vercel CLI (opsiyonel, dashboard üzerinden de deploy edilebilir)
- Supabase hesabı
