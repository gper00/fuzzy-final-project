import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import fuzzy.membership as fm

st.set_page_config(page_title="Visualisasi - Fuzzy Load Management", layout="wide")

st.title("Fungsi Keanggotaan")
st.markdown("Halaman ini menyajikan representasi visual dari variabel-variabel linguistik yang mendasari sistem inferensi fuzzy Mamdani.")

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

# Vertical layout with paragraphs
# --- Daya Aktif ---
st.header("Variabel: Daya Aktif")
st.markdown("""
Variabel daya aktif mengukur total beban listrik yang sedang dikonsumsi oleh rumah tangga dalam satuan Watt. 
Himpunan fuzzy untuk variabel ini dibagi menjadi tiga kategori utama: Rendah (untuk penggunaan minimal), 
Sedang (untuk penggunaan perangkat rumah tangga standar), dan Tinggi (yang mendekati batas kapasitas daya PLN).
Fungsi keanggotaan menggunakan model trapesium pada bagian tepi dan segitiga pada bagian tengah untuk 
memastikan transisi derajat keanggotaan yang halus.
""")
fig1, ax1 = plt.subplots(figsize=(10, 4))
x_daya = np.linspace(0, 2200, 1000)
sets_daya = {
    "Rendah": fm.m_daya_rendah,
    "Sedang": fm.m_daya_sedang,
    "Tinggi": fm.m_daya_tinggi
}
plot_membership(x_daya, sets_daya, "Himpunan Fuzzy Daya Aktif", "Watt", ax1)
st.pyplot(fig1)

st.markdown("---")

# --- Waktu ---
st.header("Variabel: Jam Operasional")
st.markdown("""
Variabel waktu membagi siklus 24 jam menjadi periode-periode penggunaan yang berbeda. Periode Off-peak 
mencerminkan waktu istirahat (malam hingga dini hari) di mana beban jaringan umumnya rendah. Periode Normal 
mencakup waktu aktivitas harian standar, sedangkan periode Peak mencerminkan waktu beban puncak (sore hingga malam hari). 
Identifikasi waktu ini sangat krusial karena manajemen beban seringkali diprioritaskan pada jam-jam sibuk.
""")
fig3, ax3 = plt.subplots(figsize=(10, 4))
x_waktu = np.linspace(0, 24, 1000)
sets_waktu = {
    "Off-peak": fm.m_waktu_off_peak,
    "Normal": fm.m_waktu_normal,
    "Peak": fm.m_waktu_peak
}
plot_membership(x_waktu, sets_waktu, "Himpunan Fuzzy Waktu", "Jam", ax3)
st.pyplot(fig3)

st.markdown("---")

# --- Prioritas ---
st.header("Variabel: Prioritas Perangkat")
st.markdown("""
Variabel prioritas memungkinkan pengguna untuk mengkategorikan tingkat kepentingan perangkat yang sedang aktif. 
Skala 1 hingga 10 digunakan untuk membedakan antara perangkat non-esensial (seperti lampu dekoratif) dan 
perangkat kritikal atau esensial (seperti lemari es atau peralatan medis). Tingkat prioritas ini akan 
mempengaruhi keputusan sistem dalam memberikan rekomendasi penghematan energi.
""")
fig2, ax2 = plt.subplots(figsize=(10, 4))
x_prioritas = np.linspace(1, 10, 1000)
sets_prioritas = {
    "Rendah": fm.m_prioritas_rendah,
    "Sedang": fm.m_prioritas_sedang,
    "Tinggi": fm.m_prioritas_tinggi
}
plot_membership(x_prioritas, sets_prioritas, "Himpunan Fuzzy Prioritas", "Skor (1-10)", ax2)
st.pyplot(fig2)

st.markdown("---")

# --- Output ---
st.header("Variabel: Rekomendasi Penghematan")
st.markdown("""
Variabel luaran (output) merupakan hasil akhir dari inferensi fuzzy yang menentukan persentase penghematan 
daya yang disarankan oleh sistem. Nilai ini dihitung melalui metode defuzzifikasi Centroid terhadap 
agregasi dari seluruh aturan yang aktif. Semakin tinggi nilai persentase, semakin mendesak tindakan 
penghematan atau pengurangan beban yang harus dilakukan oleh pengguna.
""")
fig4, ax4 = plt.subplots(figsize=(10, 4))
x_hemat = np.linspace(0, 100, 1000)
sets_hemat = {
    "Kecil": fm.m_hemat_kecil,
    "Sedang": fm.m_hemat_sedang,
    "Besar": fm.m_hemat_besar
}
plot_membership(x_hemat, sets_hemat, "Himpunan Fuzzy Output (Hemat)", "Persentase (%)", ax4)
st.pyplot(fig4)

st.markdown("---")
st.info("""
Seluruh fungsi keanggotaan di atas dirancang untuk memberikan cakupan yang menyeluruh terhadap domain 
permasalahan manajemen beban listrik, memastikan tidak ada nilai input yang berada di luar jangkauan evaluasi sistem.
""")
