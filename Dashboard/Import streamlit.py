# Import library yang diperlukan
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv

# Membuat judul aplikasi
st.title("Gambar Grafik Proyek")
 
col1, col2, col3, col4 = st.columns(4)
 
with col1:
    st.header("Gambar A")
    st.image("D:\pindah\download.png")
    st.caption('Grafik 2D')
with col2:
    st.header("Gambar B")
    st.image("D:\pindah\cluster.png")
    st.caption('Grafik cluster')
with col3:
    st.header("Gambar C")
    st.image("D:\pindah\centroid.png")
    st.caption('Grafik centroid')
with col4:
    st.header("Gambar D")
    st.image("D:\pindah\plot.png")
    st.caption('Grafik plot')
