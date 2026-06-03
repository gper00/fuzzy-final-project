import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import fuzzy.membership as fm

st.set_page_config(page_title="Visualisasi - Fuzzy Load Management", layout="wide")

st.title("Fungsi Keanggotaan")
st.markdown("Visualisasi variabel linguistik yang digunakan dalam sistem fuzzy Mamdani.")

st.markdown("---")

def plot_membership(x, sets, title, xlabel, ax):
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    for (label, func), color in zip(sets.items(), colors):
        y = [func(val) for val in x]
        ax.plot(x, y, label=label, linewidth=2, color=color)
    ax.set_title(title, fontsize=12, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel("Derajat Keanggotaan (\u03bc)")
    ax.set_ylim(0, 1.1)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()

# Grid Layout for plots
col1, col2 = st.columns(2)

with col1:
    # --- Daya Aktif ---
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    x_daya = np.linspace(0, 2200, 1000)
    sets_daya = {
        "Rendah": fm.m_daya_rendah,
        "Sedang": fm.m_daya_sedang,
        "Tinggi": fm.m_daya_tinggi
    }
    plot_membership(x_daya, sets_daya, "Variabel: Daya Aktif (Watt)", "Daya", ax1)
    st.pyplot(fig1)

    # --- Prioritas ---
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    x_prioritas = np.linspace(1, 10, 1000)
    sets_prioritas = {
        "Rendah": fm.m_prioritas_rendah,
        "Sedang": fm.m_prioritas_sedang,
        "Tinggi": fm.m_prioritas_tinggi
    }
    plot_membership(x_prioritas, sets_prioritas, "Variabel: Prioritas Perangkat", "Skor Prioritas", ax2)
    st.pyplot(fig2)

with col2:
    # --- Waktu ---
    fig3, ax3 = plt.subplots(figsize=(8, 4))
    x_waktu = np.linspace(0, 24, 1000)
    sets_waktu = {
        "Off-peak": fm.m_waktu_off_peak,
        "Normal": fm.m_waktu_normal,
        "Peak": fm.m_waktu_peak
    }
    plot_membership(x_waktu, sets_waktu, "Variabel: Waktu (Jam)", "Jam", ax3)
    st.pyplot(fig3)

    # --- Output ---
    fig4, ax4 = plt.subplots(figsize=(8, 4))
    x_hemat = np.linspace(0, 100, 1000)
    sets_hemat = {
        "Kecil": fm.m_hemat_kecil,
        "Sedang": fm.m_hemat_sedang,
        "Besar": fm.m_hemat_besar
    }
    plot_membership(x_hemat, sets_hemat, "Variabel: Rekomendasi Penghematan (%)", "Persentase (%)", ax4)
    st.pyplot(fig4)

st.markdown("---")
st.info("""
**Informasi Teknis:**
Fungsi keanggotaan menggunakan tipe **Trapesium** pada bagian tepi untuk menangani nilai ekstrim, 
dan tipe **Segitiga** pada bagian tengah untuk transisi yang linear.
""")
