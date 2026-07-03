import streamlit as st
import pandas as pd

st.title("متجر حوامل البهارات")

# رابط الملف الذي قمت بنشره (Publish to web) كـ CSV
# تأكد أن هذا الرابط هو الذي نسخته من Google Sheets (خيار النشر كـ CSV)
url = "https://docs.google.com/spreadsheets/d/1M-T1POUH1IvVOXDYX-rW9-Qw27OVGj069j2MiS3TlkA/export?format=csv&gid=0"

@st.cache_data(ttl=600)
def load_data():
    return pd.read_csv(url)

try:
    df = load_data()
    # تأكد من أسماء الأعمدة هنا تطابق تماماً ملف الإكسل الخاص بك
    selected_model = st.selectbox("اختر الموديل:", df['الموديل'].tolist())
    product = df[df['الموديل'] == selected_model].iloc[0]

    st.image(product['رابط_الصورة'], use_column_width=True)
    st.subheader(f"السعر: {product['السعر']} دج")

    if st.button("طلب المنتج"):
        st.success("تم تأكيد اختيارك!")
except Exception as e:
    st.error(f"خطأ في تحميل البيانات: {e}")
    
