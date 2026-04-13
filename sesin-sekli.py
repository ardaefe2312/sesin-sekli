import streamlit as st
from groq import Groq
import base64

# Sayfa ayarları
st.set_page_config(page_title="Sesin Görünmeyen Gücü - AI", page_icon="🔊", layout="centered")

# --- ÜST BİLGİ VE LOGOLAR ---
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    # GitHub'daki dosya ismi: seal.jpg
    st.image("seal.jpg", width=100)

with col2:
    st.markdown("<h3 style='text-align: center; color: #2E4053;'>SALİHLİ BELEDİYE EVREN ANADOLU LİSESİ</h3>", unsafe_allow_html=True)
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
groq_api_key = st.sidebar.text_input("Groq API Key", type="password", help="Analiz yapabilmek için Groq API anahtarınızı girin.")

def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# Kullanıcının çektiği fotoğrafı yüklediği yer
uploaded_file = st.file_uploader("Kendi deneyinizden bir kare yükleyin...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Gerçek Zamanlı Deney Verisi", use_container_width=True)
    
    if st.button("AI Karşılaştırmalı Analizi Başlat"):
        if not groq_api_key:
            st.warning("Lütfen sol menüden Groq API anahtarınızı girin.")
        else:
            try:
                client = Groq(api_key=groq_api_key)
                
                with st.spinner('Yapay zeka verileri karşılaştırıyor ve felsefi analizini hazırlıyor...'):
                    base64_deney = encode_image(uploaded_file)
                    
                    # Llama 3.2 Vision modeli ile görsel analizi yapıyoruz
                    chat_completion = client.chat.completions.create(
                        messages=[
                            {
                                "role": "user",
                                "content": [
                                    {
                                        "type": "text", 
                                        "text": "Sana yüklediğim fotoğraf benim Chladni deneyime ait. Arayüzde sabit duran 'ideal grafik' ile benim bu fotoğrafımı kıyasla. Fotoğrafımdaki asimetriyi ve kum yığılmasını; dış dünyadaki eğimler, üretim kusurları ve zihinsel odak bozucular metaforuyla samimi ama bilimsel bir dille yorumla."
                                    },
                                    {
                                        "type": "image_url",
                                        "image_url": {"url": f"data:image/jpeg;base64,{base64_deney}"},
                                    },
                                ],
                            }
                        ],
                        model="llama-3.2-11b-vision-preview",
                    )
                    
                    st.success("Analiz Tamamlandı!")
                    st.markdown("### 🧠 AI Analiz Raporu")
                    st.write(chat_completion.choices[0].message.content)
            except Exception as e:
                st.error(f"Bir hata oluştu: {str(e)}")

st.markdown("---")
st.caption("Frekansın Görünmeyen Gücü - TÜBİTAK 4006 Proje AI Arayüzü")
