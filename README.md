
# 🔊 Frekansın Görünmeyen Gücü — AI Akustik Analiz Paneli

Aİ ANALİZ İÇİN 🏹 https://sesin-sekli.streamlit.app/ 

> **Salihli Sekine Evren Anadolu Lisesi | TÜBİTAK 4006 Bilim Fuarı**

## 🎯 Proje Hakkında

Ses sadece duyulan bir şey değildir — maddeyi elleriyle yoğuran bir heykeltıraş gibi şekillendirir.

Bu proje, **Chladni deneyi** aracılığıyla sesin madde üzerindeki fiziksel etkisini görselleştiriyor ve yapay zeka ile bu desenleri hem fiziksel hem de psikolojik bir metafor olarak yorumluyor.

Kullanıcı kendi deney fotoğrafını yüklediğinde, AI ideal Chladni deseniyle karşılaştırarak:
- Fiziksel farklılıkları açıklıyor
- Kum dağılımını zihinsel süreçlere benzeten bir metafor kuruyor
- "Kusur bir hata değil, gerçekliğin kanıtıdır" temasıyla ilham verici bir analiz sunuyor

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Kullanım Amacı |
|-----------|---------------|
| Python | Ana programlama dili |
| Streamlit | Web arayüzü |
| Groq API | Görüntü analizi (Llama 4 Scout) |
| meta-llama/llama-4-scout-17b-16e-instruct | Vision modeli |

---

## 🚀 Kurulum

### 1. Repoyu klonla
```bash
git clone https://github.com/ardaefe2312/sesin-sekli.git
cd sesin-sekli
```

### 2. Gereksinimleri yükle
```bash
pip install -r requirements.txt
```

### 3. API key ayarla

`.streamlit/secrets.toml` dosyası oluştur:
```toml
GROQ_API_KEY = "gsk_xxxxxxxxxxxx"
```

### 4. Uygulamayı başlat
```bash
streamlit run app.py
```

---

## 📁 Dosya Yapısı
sesin-sekli/
├── app.py                  # Ana uygulama
├── requirements.txt        # Bağımlılıklar
├── kum grafik.png          # Referans ideal Chladni deseni
├── seal.jpg                # Okul logosu
├── 4006_ana_1.jpg.webp     # TÜBİTAK logosu
└── .streamlit/
└── secrets.toml        # API key (git'e ekleme!)

---

## 🔬 Nasıl Çalışır?

1. Kullanıcı kendi Chladni deney fotoğrafını yükler
2. Uygulama, yüklenen fotoğrafı ideal referans deseniyle birlikte Groq API'ye gönderir
3. Llama 4 Scout modeli iki deseni karşılaştırarak Türkçe analiz üretir
4. Analiz; fiziksel yorum, psikolojik metafor ve ilham verici bir kapanıştan oluşur

---

## ⚠️ Önemli Not

`secrets.toml` dosyasını **kesinlikle GitHub'a push etme!**  
`.gitignore` dosyana şunu ekle:
.streamlit/secrets.toml

---

## 👥 Arda Efe Elgay / Selen Deniz Taş /  Melis Çakır /Bengisu KURUM 
/ Ersin Ömer Atagöz
/ Müge Dağ
      

**Salihli Sekine Evren Anadolu Lisesi**  
TÜBİTAK 4006 Bilim Fuarı Katılımcıları

---

Bu proje eğitim amaçlı geliştirilmiştir.
