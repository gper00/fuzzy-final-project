import streamlit as st

st.set_page_config(
    page_title="Fuzzy Load Management",
    page_icon="⚡",
    layout="wide"
)

# Custom CSS for better aesthetics
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Sistem Manajemen Beban Listrik Rumah Tangga")
st.subheader("Implementasi Logika Fuzzy Mamdani untuk Optimasi Konsumsi Energi")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Deskripsi Proyek
    Aplikasi ini dikembangkan sebagai sistem pendukung keputusan (Decision Support System) untuk membantu optimasi penggunaan listrik di lingkungan rumah tangga. Dengan menggunakan logika fuzzy, sistem dapat memberikan rekomendasi tindakan yang lebih fleksibel dibandingkan logika benar/salah (binary) konvensional.

    ### 📐 Arsitektur Sistem Fuzzy
    
    #### 1. Variabel Input & Output
    Sistem mengevaluasi tiga variabel utama untuk menghasilkan satu output rekomendasi:
    - **Input 1: Daya Aktif**: Total beban listrik (0 - 2200 Watt).
    - **Input 2: Waktu Penggunaan**: Jam penggunaan (0 - 24 Jam) untuk mendeteksi *Peak Hours*.
    - **Input 3: Prioritas Perangkat**: Tingkat kepentingan perangkat (Skala 1 - 10).
    - **Output: Rekomendasi Penghematan**: Persentase pengurangan konsumsi (0 - 100%).

    #### 2. Fungsi Keanggotaan
    Sistem menggunakan kombinasi fungsi:
    - **Trapesium**: Digunakan pada nilai batas (Rendah & Tinggi) untuk menangani nilai ekstrim secara stabil.
    - **Segitiga**: Digunakan pada nilai tengah (Sedang/Normal) untuk transisi linear yang presisi.

    #### 3. Rule Base (Basis Aturan)
    Terdapat **27 aturan fuzzy** yang dirancang dengan logika Mamdani. 
    *Prinsip Dasar:* Semakin tinggi daya dan semakin sibuk waktu penggunaan (Peak Hour), maka rekomendasi penghematan akan semakin besar, terutama jika prioritas perangkat rendah.

    #### 4. Proses Fuzzy
    Proyek ini mengimplementasikan siklus fuzzy lengkap secara manual:
    - **Fuzzifikasi**: Mengubah nilai crisp input menjadi derajat keanggotaan fuzzy.
    - **Inferensi (Mamdani)**: Mengevaluasi aturan menggunakan operator **MIN**.
    - **Agregasi**: Menggabungkan hasil evaluasi semua aturan menggunakan operator **MAX**.
    - **Defuzzifikasi (Centroid)**: Menghitung titik berat area hasil agregasi untuk mendapatkan nilai crisp output.
    """)

with col2:
    st.info("""
    **Petunjuk Navigasi**
    
    Gunakan menu di samping untuk mengakses:
    *   **Simulator**: Untuk melakukan pengujian perhitungan fuzzy.
    *   **Visualisasi**: Untuk melihat grafik fungsi keanggotaan.
    """)

st.markdown("---")
st.caption("Tugas Akhir Mata Kuliah Logika Fuzzy")
