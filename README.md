# RetirePlan Dashboard

แอปวางแผนการลงทุนและเกษียณภาษาไทย บน Streamlit

ไฟล์ต้นฉบับชื่อ test101.py มีเนื้อหา HTML จึงแยกเป็น dashboard.html และเพิ่ม app.py เป็นไฟล์เริ่มต้นสำหรับ Streamlit โดยคงสูตรคำนวณเดิม

## รันในเครื่อง

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## GitHub

สร้าง repository ชื่อ retireplan-streamlitza แล้วอัปโหลดไฟล์ที่อยู่ในโฟลเดอร์นี้ไว้ที่รากของ repository รวม dashboard.html และ requirements.txt

## Streamlit Community Cloud

1. ลงชื่อเข้าใช้ https://share.streamlit.io/ และเชื่อมบัญชี GitHub
2. กด Create app แล้วเลือก repository retireplan-streamlitza
3. Branch: main
4. Main file path: app.py
5. ใน Advanced settings เลือก Python 3.12 แล้วกด Deploy
6. รอ build เสร็จและเปิด URL ของแอปเพื่อตรวจสอบ

แอปไม่ใช้ secrets หรือฐานข้อมูล หน้าตาและกราฟโหลด Tailwind CSS, Chart.js และ Google Fonts ผ่านอินเทอร์เน็ต

Streamlit 1.55.0 ถูกตรึงไว้เพื่อรองรับ HTML/JavaScript ใน iframe ของแอปนี้ เมื่อต้องการอัปเกรด ควรย้ายไป custom component ที่รองรับในเวอร์ชันใหม่

ตรวจสอบการแชร์ลิงก์อีกครั้งหลัง Deploy โดยเปลี่ยนค่า คัดลอกลิงก์ และเปิดลิงก์ในแท็บใหม่ หากเบราว์เซอร์ไม่อนุญาตให้คัดลอก จะมีช่องแสดงลิงก์ให้คัดลอกเอง

## ขอบเขตการคำนวณ

คงสูตรเดิม: ดอกเบี้ยรายเดือนเท่ากับอัตรารายปีหาร 12, เติมเงินก่อนคิดผลตอบแทน, ถอนก่อนคิดผลตอบแทน และเพิ่มเงินถอนตามเงินเฟ้อทุกปี ไม่มีค่าธรรมเนียม ภาษี หรือความผันผวนของผลตอบแทน
