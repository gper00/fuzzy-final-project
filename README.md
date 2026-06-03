# Sistem Manajemen Beban Listrik Rumah Tangga (Fuzzy Logic)

Proyek ini adalah implementasi **Logika Fuzzy Mamdani** untuk mengoptimalkan konsumsi energi listrik di rumah tangga. Sistem ini memberikan rekomendasi persentase penghematan energi berdasarkan kondisi penggunaan daya real-time, waktu penggunaan, dan prioritas perangkat.

## 📌 Fitur Utama
- **Fuzzifikasi Manual**: Implementasi fungsi keanggotaan (Triangular & Trapezoidal) menggunakan NumPy.
- **Inference Engine**: 27 aturan (Rule Base) Mamdani untuk evaluasi keputusan.
- **Defuzzifikasi Centroid**: Perhitungan nilai crisp menggunakan metode Center of Area (CoA).
- **Dashboard Interaktif**: Simulator berbasis Streamlit untuk pengujian skenario.
- **Visualisasi**: Grafik fungsi keanggotaan dan proses agregasi fuzzy.

## 🛠️ Variabel Sistem
1. **Input**:
   - Daya Aktif (0 - 2200 Watt)
   - Waktu Penggunaan (0 - 24 Jam)
   - Prioritas Perangkat (Skor 1 - 10)
2. **Output**:
   - Rekomendasi Penghematan (0 - 100 %)

## 🚀 Cara Menjalankan

1. **Clone repositori ini:**
   \`\`\`bash
   git clone <url-repository>
   cd fuzzy
   \`\`\`

2. **Install dependensi:**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. **Jalankan aplikasi Streamlit:**
   \`\`\`bash
   streamlit run app.py
   \`\`\`

## 📂 Struktur Proyek
- \`app.py\`: Halaman utama aplikasi.
- \`fuzzy/\`: Modul logika fuzzy (membership, inference, defuzzification, engine).
- \`pages/\`: Halaman simulator dan visualisasi.
- \`requirements.txt\`: Daftar library Python yang dibutuhkan.

---
**Tugas Akhir Mata Kuliah Logika Fuzzy**
