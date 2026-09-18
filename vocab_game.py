import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""
if "ans7_val" not in st.session_state:
    st.session_state.ans7_val = ""
if "ans8_val" not in st.session_state:
    st.session_state.ans8_val = ""
if "ans9_val" not in st.session_state:
    st.session_state.ans9_val = ""
if "ans10_val" not in st.session_state:
    st.session_state.ans10_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""  # เคลียร์ค่าช่องข้อ 3
    st.session_state.ans4_val = ""  # เคลียร์ค่าช่องข้อ 4
    st.session_state.ans5_val = ""  # เคลียร์ค่าช่องข้อ 5
    st.session_state.ans6_val = ""  # เคลียร์ค่าช่องข้อ 6
    st.session_state.ans7_val = ""  # เคลียร์ค่าช่องข้อ 7
    st.session_state.ans8_val = ""  # เคลียร์ค่าช่องข้อ 8
    st.session_state.ans9_val = ""  # เคลียร์ค่าช่องข้อ 9
    st.session_state.ans10_val = ""  # เคลียร์ค่าช่องข้อ 10
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans6 = ans6.strip().lower()
    u_ans7 = ans7.strip().lower()
    u_ans8 = ans8.strip().lower()
    u_ans9 = ans9.strip().lower()
    u_ans10 = ans10.strip().lower()


    if u_ans1 == "กรดอะมิโน":
        st.success("✅ ข้อ 1: ถูกต้อง")
    elif u_ans1 == "Amino acid":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    if u_ans2 == "ไทมีน":
        st.success("✅ ข้อ 2: ถูกต้อง")
    elif u_ans2 == "Thymine":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
 
    if u_ans3 == "ยูราซิล":
        st.success("✅ ข้อ 3: ถูกต้อง")
    elif u_ans3 == "Uracil":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    if u_ans4 == "เอนไซม์":
        st.success("✅ ข้อ 4: ถูกต้อง")
    elif u_ans4 == "Enzyme":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
  
    if u_ans5 == "กลูโคส":
        st.success("✅ ข้อ 5: ถูกต้อง")
    elif u_ans5 == "Glucose":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")


    if u_ans6 == "ไคติน":
        st.success("✅ ข้อ 6: ถูกต้อง")
    elif u_ans6 == "Chitin":
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")

    if u_ans7 == "ดีออกซีไรโบส":
        st.success("✅ ข้อ 7: ถูกต้อง")
    elif u_ans7 == "Deoxyribose":
        st.success("✅ ข้อ 7: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")
        
    if u_ans8 == "พันธะไกลโคซิดิก":
        st.success("✅ ข้อ 8: ถูกต้อง")
    elif u_ans8 == "Glycosidic bond":
        st.success("✅ ข้อ 8: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 8: ยังไม่ถูกต้อง (คุณตอบ '{u_ans8}')")

    if u_ans9 == "พันธะไฮโดรเจน":
        st.success("✅ ข้อ 9: ถูกต้อง")
    elif u_ans9 == "hydrogen bond":
        st.success("✅ ข้อ 9: ถูกต้อง")
    elif u_ans9 == "H bond":
        st.success("✅ ข้อ 9: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 9: ยังไม่ถูกต้อง (คุณตอบ '{u_ans9}')")

    if u_ans10 == "พันธะเอสเทอร์":
        st.success("✅ ข้อ 10: ถูกต้อง")
    elif u_ans10 == "Ester bond":
        st.success("✅ ข้อ 10: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 10: ยังไม่ถูกต้อง (คุณตอบ '{u_ans10}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 10:
        st.success("🎉 You win!")
    elif score >= 7:
        st.info("✨nice!")
    elif score >= 5:
        st.warning("⚠close")
    else:
        st.error("failed,do better")


TOTAL_MINUTES = 45  # Set your target duration in minutes
TOTAL_SECONDS = TOTAL_MINUTES * 60

st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

if "start" in st.session_state and not st.session_state.get("is_ended", False):
    elapsed_time = time.time() - st.session_state.start
    time_left = int(TOTAL_SECONDS - elapsed_time)

    if time_left > 0:
        minutes, seconds = divmod(time_left, 60)
        st.error(f"⏳ เหลือเวลา: {minutes} นาที {seconds:02d} วินาที")
        # Alternative digital format (e.g., 01:45):
        # st.error(f"⏳ เหลือเวลา: {minutes:02d}:{seconds:02d}")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "ข้อ 1:หน่วยย่อยที่สุดของโปรตีน เชื่อมต่อกันด้วยพันธะเพปไทด์",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "ข้อ 2: เบสที่พบเฉพาะใน DNA เท่านั้น ไม่พบใน RNA",
    value=st.session_state.ans2_val,
)
ans3 = st.text_input(
    "ข้อ 3:  เบสที่พบเฉพาะใน RNA โดยจะเข้าคู่กับอะดีนีน",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "ข้อ 4: โปรตีนที่ทำหน้าที่เป็นตัวเร่งเร่งปฏิกิริยาเคมีในร่างกาย",
    value=st.session_state.ans4_val,
)
ans5 = st.text_input(
    "ข้อ 5:น้ำตาลโมเลกุลเดี่ยว เป็นสารตั้งต้นหลักในการสร้างพลังงานของเซลล์",
    value=st.session_state.ans5_val,
)
ans6 = st.text_input(
    "ข้อ 6:พอลิแซ็กคาไรด์ที่เป็นโครงสร้างแข็งของเปลือกกุ้ง ปู และผนังเซลล์ของฟังไจ",
    value=st.session_state.ans6_val,
)
ans7 = st.text_input(
    "ข้อ 7:น้ำตาลคาร์บอน 5 ตัวที่เป็นส่วนประกอบของ DNA โดยมีออกซิเจนน้อยกว่า",
    value=st.session_state.ans7_val,
)
ans8 = st.text_input(
    "ข้อ 8:พันธะเคมีที่เชื่อมระหว่างโมเลกุลของน้ำตาไรโบส 1 อะตอม",
    value=st.session_state.ans8_val,
)
ans9 = st.text_input(
    "ข้อ 9:พันธะแรงยึดเหนี่ยวอย่างอ่อนที่ช่วยยึดเกลียวคู่ของ DNA และโครงสร้างโปรตีน",
    value=st.session_state.ans9_val,
)
ans10 = st.text_input(
    "ข้อ 10:พันธะเคมีที่เชื่อมระหว่างกลีเซอรอลกับกรดไขมันในลิพิด",
    value=st.session_state.ans10_val,
)
# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans1_val = ans3
st.session_state.ans2_val = ans4
st.session_state.ans1_val = ans5
st.session_state.ans2_val = ans6
st.session_state.ans1_val = ans7
st.session_state.ans2_val = ans8
st.session_state.ans1_val = ans9
st.session_state.ans2_val = ans10


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10)

st.divider()
st.write("กลุ่มที่8 ห้อง4/6")

st.divider()
st.write("นายชยธร ศุภการกิตติกุล เลขที่ 26 ม.4/6")
