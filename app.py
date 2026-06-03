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
    Aplikasi ini dikembangkan sebagai sistem pendukung keputusan (Decision Support System) untuk membantu optimasi penggunaan listrik di lingkungan rumah tangga. Dengan menggunakan logika fuzzy, sistem dapat memberikan rekomendasi tindakan yang lebih fleksibel dibandingkan logika benar/salah konvensional. Pendekatan ini memungkinkan penanganan variabel yang memiliki ketidakpastian tinggi seperti perilaku penggunaan daya dan skala prioritas perangkat secara lebih manusiawi.

    ### Arsitektur Sistem Fuzzy
    
    Sistem ini mengevaluasi variabel-variabel masukan melalui beberapa tahapan proses fuzzy yang diimplementasikan secara manual. Proses dimulai dari fuzzifikasi nilai crisp, diikuti dengan evaluasi aturan menggunakan inferensi Mamdani, agregasi output, dan diakhiri dengan defuzzifikasi menggunakan metode Centroid untuk mendapatkan nilai rekomendasi akhir.

    #### Variabel Masukan dan Luaran
    Untuk mencapai hasil yang akurat, sistem menggunakan variabel-variabel berikut:
    - **Daya Aktif**: Total konsumsi daya listrik real-time (0 - 2200 Watt).
    - **Jam Operasional**: Jam penggunaan dalam format 24 jam untuk mengidentifikasi beban puncak.
    - **Prioritas Perangkat**: Tingkat kepentingan operasional perangkat (Skala 1 - 10).
    - **Rekomendasi Penghematan**: Luaran sistem berupa persentase penghematan energi (0 - 100%).

    #### Basis Aturan (Rule Base)
    Berikut adalah daftar lengkap 27 aturan fuzzy yang menjadi fondasi pengambilan keputusan di dalam sistem ini:
    """)
    
    # Using a list to hold rules for cleaner code, then joining them into a table
    rules_data = [
        ["1", "Rendah", "Off-peak", "Rendah", "Kecil"],
        ["2", "Rendah", "Off-peak", "Sedang", "Kecil"],
        ["3", "Rendah", "Off-peak", "Tinggi", "Kecil"],
        ["4", "Rendah", "Normal", "Rendah", "Kecil"],
        ["5", "Rendah", "Normal", "Sedang", "Kecil"],
        ["6", "Rendah", "Normal", "Tinggi", "Kecil"],
        ["7", "Rendah", "Peak", "Rendah", "Sedang"],
        ["8", "Rendah", "Peak", "Sedang", "Kecil"],
        ["9", "Rendah", "Peak", "Tinggi", "Kecil"],
        ["10", "Sedang", "Off-peak", "Rendah", "Sedang"],
        ["11", "Sedang", "Off-peak", "Sedang", "Kecil"],
        ["12", "Sedang", "Off-peak", "Tinggi", "Kecil"],
        ["13", "Sedang", "Normal", "Rendah", "Sedang"],
        ["14", "Sedang", "Normal", "Sedang", "Sedang"],
        ["15", "Sedang", "Normal", "Tinggi", "Kecil"],
        ["16", "Sedang", "Peak", "Rendah", "Besar"],
        ["17", "Sedang", "Peak", "Sedang", "Sedang"],
        ["18", "Sedang", "Peak", "Tinggi", "Sedang"],
        ["19", "Tinggi", "Off-peak", "Rendah", "Sedang"],
        ["20", "Tinggi", "Off-peak", "Sedang", "Sedang"],
        ["21", "Tinggi", "Off-peak", "Tinggi", "Kecil"],
        ["22", "Tinggi", "Normal", "Rendah", "Besar"],
        ["23", "Tinggi", "Normal", "Sedang", "Sedang"],
        ["24", "Tinggi", "Normal", "Tinggi", "Sedang"],
        ["25", "Tinggi", "Peak", "Rendah", "Besar"],
        ["26", "Tinggi", "Peak", "Sedang", "Besar"],
        ["27", "Tinggi", "Peak", "Tinggi", "Sedang"],
    ]
    
    table_header = "| No | Daya Aktif | Waktu | Prioritas | Output |\n|----|------------|-------|-----------|--------|"
    table_rows = "\n".join([f"| {' | '.join(row)} |" for row in rules_data])
    st.markdown(f"{table_header}\n{table_rows}")

with col2:
    st.info("""
    **Petunjuk Navigasi**
    
    Gunakan menu di samping untuk mengakses fitur aplikasi:
    *   **Simulator**: Digunakan untuk melakukan simulasi perhitungan rekomendasi berdasarkan input user.
    *   **Visualisasi**: Digunakan untuk meninjau fungsi keanggotaan dan sebaran himpunan fuzzy.
    """)

st.markdown("---")
st.caption("Dokumentasi Tugas Akhir Mata Kuliah Logika Fuzzy")
