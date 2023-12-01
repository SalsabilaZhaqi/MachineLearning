import streamlit as st
from st_pages import Page, show_pages, add_page_title

show_pages(
    [
        Page("Home.py"),
        Page("soalA1.py", "Soal Nomor 1"),
        Page("SoalA3.py", "Soal Nomor 2"),
        Page("SoalA4.py", "Soal Nomor 3"),
        Page("SoalA5.py", "Soal Nomor 4"),
        Page("SoalA6.py", "Soal Nomor 5"),
        Page("SoalA7.py", "Soal Nomor 6"),
        Page("SoalA8.py", "Soal Nomor 7"),
        Page("SoalA10.py", "Soal Nomor 8")
    ]
)

st.header('Selamat Datang di web Machine learning saya ')
st.image('./img.jpg')
st.header('Biodata')
st.subheader('Nama:  Haiqal Salsabila Zhaqi ')
st.subheader('NIM : 223307099')
st.subheader('Kelas : 3D')
st.subheader('Hobi saya adalah Bermain Game, dan mendesain UI')
