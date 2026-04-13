import streamlit as st
import google.generativeai as genai
from PIL import Image

# Sayfa ayarları
st.set_page_config(page_title="Sesin Görünmeyen Gücü - AI", page_icon="🔊", layout="centered")

# --- ÜST BİLGİ VE LOGOLAR ---
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    try:
        st.image("seal.jpg", width=100)
    except:
        st.error("seal.jpg bulunamadı")

with col2:
    st.markdown("<h3 style='text-align: center; color: #2E4053;'>SALİHLİ SEKİNE EVREN ANADOLU LİSESİ</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #5D6D7E;'>TÜBİTAK 4006 - Bilim Fuarı</h4>", unsafe_allow_html=True)

with col3:
    try:
        # GitHub'daki tam ismin bu olduğundan emin ol
        st.image("4006_ana_1.jpg.webp", width=120)
    except:
        st.error("TÜBİTAK logosu bulunamadı")

st.markdown("---")

# --- İDEAL GRAFİK GÖSTERİMİ ---
st.subheader("🎯 Hedeflenen İdeal Form (Laboratuvar Koşulu)")
try:
    st.image("kum grafik.png", caption="Kusursuz Simetri ve Geometrik Düzen", use_container_width=True)
except:
    st.error("kum grafik.png bulunamadı")
st.info("Bu görsel, dış etkenlerden arındırılmış bir ortamda sesin madde üzerindeki etkisini temsil eder.")

st.markdown("---")

# --- ANALİZ BÖLÜMÜ ---
st.title("🔊 Akustik Veri Analiz Paneli")
st.sidebar.title("Ayarlar")
gemini_api_key = st.sidebar.text_input("Gemini API Key", type="password")

uploaded_file = st.file_uploader("Kendi deneyinizden bir kare yükleyin...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Gerçek Zamanlı Deney Verisi", use_container_width=True)
    
    if st.button("AI Karşılaştırmalı Analizi Başlat"):
        if not gemini_api_key:
            st.warning("Lütfen sol menüden Gemini API anahtarınızı girin.")
        else:
            try:
                genai.configure(api_key=gemini_api_key)
                
                # EN GARANTİ MODEL ÇAĞIRMA YÖNTEMİ
                # Eğer models/gemini-1.5-flash hata verirse direkt ismini deniyoruz
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                with st.spinner('Analiz yapılıyor...'):
                    prompt = "Bu bir Chladni deneyi fotoğrafıdır. Gördüğün asimetriyi ve kum dağılımını, fiziksel engeller ve zihinsel gürültü metaforuyla bilimsel bir dille yorumla."
                    response = model.generate_content([prompt, input_image])
                    
                    st.success("Analiz Tamamlandı!")
                    st.markdown("### 🧠 AI Analiz Raporu")
                    st.write(response.text)
            except Exception as e:
                # Eğer hala hata verirse model ismini alternatif yolla dene
                try:
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    response = model.generate_content([prompt, input_image])
                    st.write(response.text)
                except:
                    st.error(f"Teknik bir hata oluştu: {str(e)}")

st.markdown("---")
st.caption("Frekansın Görünmeyen Gücü - TÜBİTAK 4006")
