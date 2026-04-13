import streamlit as st
import google.generativeai as genai
from PIL import Image

# Sayfa ayarları
st.set_page_config(page_title="Sesin Görünmeyen Gücü - AI", page_icon="🔊", layout="centered")

# --- ÜST BİLGİ VE LOGOLAR ---
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.image("seal.jpg", width=100)
with col2:
    st.markdown("<h3 style='text-align: center; color: #2E4053;'>SALİHLİ SEKİNE EVREN ANADOLU LİSESİ</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #5D6D7E;'>TÜBİTAK 4006 - Bilim Fuarı</h4>", unsafe_allow_html=True)
with col3:
    st.image("4006_ana_1.jpg.webp", width=120)

st.markdown("---")
st.subheader("🎯 Hedeflenen İdeal Form")
st.image("kum grafik.png", caption="Kusursuz Simetri ve Geometrik Düzen", use_container_width=True)
st.markdown("---")

# --- ANALİZ BÖLÜMÜ ---
st.title("🔊 Akustik Veri Analiz Paneli")
gemini_api_key = st.sidebar.text_input("Gemini API Key", type="password")
uploaded_file = st.file_uploader("Deney fotoğrafınızı yükleyin...", type=["jpg", "jpeg", "png"])

if uploaded_file and gemini_api_key:
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Sizin Veriniz", use_container_width=True)
    
    if st.button("Analizi Başlat"):
        genai.configure(api_key=gemini_api_key)
        
        # DENENECEK MODELLER LİSTESİ (Hata almamak için)
        models_to_try = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro-vision']
        success = False
        
        with st.spinner('AI modelleri taranıyor ve analiz yapılıyor...'):
            for model_name in models_to_try:
                try:
                    model = genai.GenerativeModel(model_name)
                    prompt = "Bu bir Chladni deneyi fotoğrafıdır. Asimetriyi ve kum dağılımını felsefi ve bilimsel yorumla."
                    response = model.generate_content([prompt, input_image])
                    
                    st.success(f"Analiz Tamamlandı! (Model: {model_name})")
                    st.write(response.text)
                    success = True
                    break # Başarılı olursa döngüden çık
                except:
                    continue # Hata verirse bir sonraki modeli dene
            
            if not success:
                st.error("Üzgünüm, şu an hiçbir modele bağlanılamadı. Lütfen API anahtarınızın doğruluğunu veya internetinizi kontrol edin.")

st.markdown("---")
st.caption("Salihli Sekine Evren Anadolu Lisesi - TÜBİTAK 2026")
