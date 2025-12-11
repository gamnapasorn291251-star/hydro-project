import streamlit as st

st.set_page_config(page_title="โปรแกรมคำนวณปุ๋ยผัก", page_icon="🥬")

st.title("🥬 Hydroponics Calculator")
st.write("---")

col1, col2 = st.columns(2)
with col1:
    width = st.number_input("ความกว้าง (ซม.)", value=0.0)
    length = st.number_input("ความยาว (ซม.)", value=0.0)
    height = st.number_input("ระดับน้ำลึก (ซม.)", value=0.0)

with col2:
    veggie = st.selectbox("เลือกชนิดผัก", ["ผักสลัด", "ผักไทย"])
    price = st.number_input("ราคาปุ๋ย (บาท/ลิตร)", value=150.0)

if st.button("🚀 คำนวณ"):
    water = (width * length * height) / 1000
    dose = 3 if "สลัด" in veggie else 5
    total_fert = water * dose
    cost = (total_fert / 1000) * price
    
    st.success(f"💧 ปริมาณน้ำ: {water:,.2f} ลิตร")
    st.info(f"🧪 ปุ๋ยที่ต้องใช้: {total_fert:,.2f} cc")
    st.warning(f"💰 ต้นทุน: {cost:,.2f} บาท")
