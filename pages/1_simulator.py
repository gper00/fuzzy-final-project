import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from fuzzy.engine import hitung_penghematan

st.set_page_config(page_title="Simulator - Fuzzy Load Management", layout="wide")

st.title("Simulator Sistem Fuzzy")
st.markdown("Sesuaikan parameter input untuk melihat hasil rekomendasi penghematan energi secara real-time.")

st.markdown("---")

# Layout Input & Output
col_input, col_output = st.columns([1, 1.5], gap="large")

with col_input:
    st.subheader("Konfigurasi Input")
    
    with st.container(border=True):
        daya = st.slider("Daya Aktif Saat Ini (Watt)", 0, 2200, 1200, help="Total konsumsi daya listrik rumah tangga.")
        waktu = st.slider("Jam Operasional (Jam)", 0, 23, 19, help="Waktu saat ini dalam format 24 jam.")
        prioritas = st.slider("Prioritas Perangkat (1-10)", 1, 10, 5, help="1: Sangat Rendah (Lampu Hias), 10: Sangat Tinggi (Kulkas/Medis).")
        
        st.markdown(" ")
        btn_hitung = st.button("Proses Perhitungan", type="primary", use_container_width=True)

if btn_hitung:
    crisp_output, keputusan, aggregated_output, x_range = hitung_penghematan(daya, waktu, prioritas)
    
    with col_output:
        st.subheader("Hasil Analisis")
        
        # Dashboard Metric
        m1, m2 = st.columns(2)
        with m1:
            st.metric("Rekomendasi Penghematan", f"{crisp_output:.2f}%")
        with m2:
            # Color-coded status
            status_color = "green" if crisp_output <= 30 else "orange" if crisp_output <= 60 else "red"
            st.markdown(f"**Status:** <span style='color:{status_color}; font-weight:bold;'>{keputusan.split(' ')[0]}</span>", unsafe_allow_html=True)
            st.write(f"{' '.join(keputusan.split(' ')[1:])}")

        st.markdown("---")
        
        # Plot Result
        st.markdown("**Visualisasi Agregasi & Defuzzifikasi**")
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Plotting the shaded area
        ax.plot(x_range, aggregated_output, color='#1f77b4', linewidth=2, label='Area Agregasi')
        ax.fill_between(x_range, 0, aggregated_output, color='#1f77b4', alpha=0.3)
        
        # Vertical line for defuzzification result
        ax.axvline(x=crisp_output, color='#d62728', linestyle='--', linewidth=2, label=f'Hasil Crisp: {crisp_output:.2f}%')
        
        ax.set_ylim(0, 1.1)
        ax.set_xlabel("Rekomendasi Penghematan (%)")
        ax.set_ylabel("Derajat Keanggotaan (\u03bc)")
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend()
        
        st.pyplot(fig)
else:
    with col_output:
        st.info("Silakan tentukan nilai variabel pada panel kiri dan tekan tombol 'Proses Perhitungan' untuk melihat hasil.")
