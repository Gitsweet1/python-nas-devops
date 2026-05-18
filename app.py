import streamlit as st

st.title("האפליקציה שלי ב-NAS 🚀")
st.write("הגרסה המעודכנת ביותר שלי!")

if st.button("לחץ כאן להפתעה חדשה"):
    st.snow() # יציג אפקט של שלג/קונפטי במקום בלונים
    st.success("האוטומציה עובדת בהצלחה!")