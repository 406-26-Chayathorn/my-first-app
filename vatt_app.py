import streamlit as st
st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")
vat = price * 0.07
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)
net_price = price - vat
st.write("นายชยธร ศุภการกิตติกุล เลขที่ 26  ม.4/6")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
