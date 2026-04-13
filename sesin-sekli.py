import streamlit as st
import google.generativeai as genai
from PIL import Image

# Sayfa ayarları
st.set_page_config(page_title="Sesin Görünmeyen Gücü - AI", page_icon="🔊", layout="centered")

# --- ÜST BİLGİ VE LOGOLAR ---
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    # GitHub'daki dosya ismi: seal.jpg
    st.image("seal.jpg", width=100)

with col2:
    st.markdown("<h3 style='text-align: center; color: #2E4053;'>SALİHLİ SEKİNE EVREN ANADOLU LİSESİ</h3>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #5D6D7E;'>TÜBİTAK 4006 - Bilim Fuarı</h4>", unsafe_allow_html=True)

with col3:
    # GitHub'daki dosya ismi: 4006_ana_1.jpg.webp
    st.image("4006_ana_1.jpg.webp", width=120)

st.markdown("---")

# --- İDEAL GRAFİK GÖSTERİMİ ---
st.subheader("🎯 Hedeflenen İdeal Form (Laboratuvar Koşulu)")
# GitHub'daki dosya ismi: kum grafik.png
st.image("kum grafik.png", caption="Kusursuz Simetri ve Geometrik Düzen", use_container_width=True)
st.info("Bu görsel, dış etkenlerden arındırılmış bir ortamda sesin madde üzerindeki etkisini temsil eder.")

st.markdown("---")

# --- ANALİZ BÖLÜMÜ ---
st.title("🔊 Akustik Veri Analiz Paneli")
st.sidebar.title("Ayarlar")
# Groq yerine Gemini API anahtarı girişi
gemini_api_key = st.sidebar.text_input("Gemini API Key", type="password", help="Analiz yapabilmek için Google AI Studio'dan aldığınız anahtarı girin.")

# Kullanıcının çektiği fotoğrafı yüklediği yer
uploaded_file = st.file_uploader("Kendi deneyinizden bir kare yükleyin...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Fotoğrafı Gemini'nin anlayacağı formata çeviriyoruz
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Gerçek Zamanlı Deney Verisi", use_container_width=True)
    
    if st.button("AI Karşılaştırmalı Analizi Başlat"):
        if not gemini_api_key:
            st.warning("Lütfen sol menüden Gemini API anahtarınızı girin.")
        else:
            try:
                # Gemini Yapılandırması
                genai.configure(api_key=gemini_api_key)
                model = genai.GenerativeModel('models/gemini-1.5-flash')
                
                with st.spinner('Gemini verileri analiz ediyor ve felsefi raporu hazırlıyor...'):
                    # AI'ya gönderilen talimat (Prompt)
                    prompt = """
                    Sana yüklediğim fotoğraf benim Chladni deneyime ait. 
                    Arayüzde sabit duran 'ideal grafik' (simetrik olan) ile benim bu fotoğrafımı kıyasla. 
                    Fotoğrafımdaki asimetriyi ve kum yığılmasını; dış dünyadaki eğimler, üretim kusurları ve zihinsel odak bozucular metaforuyla samimi ama bilimsel bir dille yorumla.
                    Salihli Sekine Evren Anadolu Lisesi TÜBİTAK fuarı için sunum yaptığımı unutma.
                    """
                    
                    # Analizi başlat
                    response = model.generate_content([prompt, input_image])
                    
                    st.success("Analiz Tamamlandı!")
                    st.markdown("### 🧠 AI Analiz Raporu")
                    st.write(response.text)
            except Exception as e:
                st.error(f"Bir hata oluştu: {str(e)}")

st.markdown("---")
st.caption("Frekansın Görünmeyen Gücü - TÜBİTAK 4006 Proje AI Arayüzü")
