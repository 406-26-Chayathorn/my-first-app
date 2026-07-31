import streamlit as st

st.markdown("# :red[แอปพลิเคชันคำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (kg):")
height_cm = st.number_input("กรอกส่วนสูงของคุณ (m):")
if st.button("คำนวณ BMI")
 height_m = height_cm / 100
 bmi = weight / (height_m ** 2)
 
 st.write("---")
 st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")
if bmi < 18.5:
  st.warning("ผอม")
elif 18.5 <= bmi < 23.0:
  st.success("สุขภาพดี")
elif 23.0 <= bmi < 25.0:
  st.error("อ้วน")

st.divider
st.write("นายชยธร ศุภการกิตติกุล เลขที่ 26 ม.4/6")
