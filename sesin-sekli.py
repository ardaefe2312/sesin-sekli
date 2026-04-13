import streamlit as st
from groq import Groq
import base64

# Sayfa ayarları
st.set_page_config(page_title="Sesin Görünmeyen Gücü - AI", page_icon="🔊", layout="centered")

# --- ÜST BİLGİ VE LOGOLAR ---
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.image("seal.jpg", width=100)
with col2:
    st.markdown("<h3 style='text-align: center;'>SALİHLİ SEKİNE EVREN ANADOLU LİSESİ</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>TÜBİTAK 4006 - Bilim Fuarı</h4>", unsafe_allow_html=True)
with col3:
    st.image("4006_ana_1.jpg.webp", width=120)

st.markdown("---")
st.subheader("🎯 Hedeflenen İdeal Form")
st.image("kum grafik.png", use_container_width=True)
st.markdown("---")

# --- ANALİZ BÖLÜMÜ ---
st.title("🔊 Akustik Veri Analiz Paneli")

# API key secrets'tan al
try:
    groq_api_key = st.secrets["GROQ_API_KEY"]
except:
    st.error("⚠️ API key bulunamadı. Streamlit Secrets'a GROQ_API_KEY ekleyin.")
    st.stop()

def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

uploaded_file = st.file_uploader("Deney fotoğrafınızı yükleyin...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Sizin Veriniz", use_container_width=True)

    if st.button("AI Karşılaştırmalı Analizi Başlat"):
        try:
            client = Groq(api_key=groq_api_key)
            base64_image = encode_image(uploaded_file)

            with st.spinner('Groq (Llama 4 Scout) analiz ediyor...'):
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "text",
                                    "text": ""text": """Sen bir bilim ve psikoloji yazarısın. Önündeki Chladni deneyi fotoğrafını dikkatlice incele.

Fotoğraftaki kum desenini TAM OLARAK tarif et: hangi bölgeler yoğun, hangi bölgeler seyrek, şekil simetrik mi değil mi, ortada mı kenarlarda mı toplanmış?

Sonra bu gözlemi şu üç başlıkta yorumla:

🔬 Fiziksel Yorum: Bu dağılım hangi frekans ve titreşim davranışına işaret ediyor?

🧠 Psikolojik Metafor: Bu kum deseni bir insan zihnini temsil etseydi ne anlatırdı? Odak noktaları, dağınıklık, boş alanlar — bunlar kişinin iç dünyası hakkında ne söyler?

✨ Fuara Özel Mesaj: Salihli Sekine Evren Anadolu Lisesi öğrencilerinin bu deneyde gözlemlediği gerçekliği, ziyaretçiye ilham verecek şiirsel ama bilimsel bir dille anlat.

Her fotoğraf için özgün ve o fotoğrafa özel bir yorum yaz, genel kalıplardan kaçın.""""
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                                },
                            ],
                        }
                    ],
                    model="meta-llama/llama-4-scout-17b-16e-instruct",
                    max_tokens=1024,
                )

            st.success("Analiz Tamamlandı!")
            st.markdown("### 🧠 AI Analiz Raporu")
            st.write(chat_completion.choices[0].message.content)

        except Exception as e:
            st.error(f"Hata oluştu: {str(e)}")

st.markdown("---")
st.caption("Frekansın Görünmeyen Gücü - TÜBİTAK 4006")
