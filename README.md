# Implementasi Logika Fuzzy Mamdani untuk Optimasi Konsumsi Energi

Proyek ini merupakan implementasi sistem pendukung keputusan yang dirancang untuk mengelola dan mengoptimalkan konsumsi daya listrik pada skala rumah tangga. Dengan memanfaatkan logika fuzzy, sistem ini mampu memberikan rekomendasi tindakan penghematan yang lebih dinamis dan fleksibel dibandingkan dengan sistem kontrol berbasis logika biner konvensional. Pendekatan ini sangat relevan untuk diaplikasikan dalam skema manajemen beban listrik, di mana variabel yang terlibat seringkali memiliki ambiguitas dan ketidakpastian tinggi.

## Fitur Utama Sistem

Sistem ini dirancang dengan fokus pada transparansi algoritma dan kemudahan penggunaan, dengan fitur-fitur sebagai berikut:

*   **Fuzzifikasi Manual**: Seluruh perhitungan fungsi keanggotaan dibangun dari dasar menggunakan NumPy tanpa pustaka fuzzy pihak ketiga.
*   **Inferensi Mamdani**: Menggunakan metode MIN-MAX untuk mengevaluasi derajat keanggotaan terhadap aturan yang telah ditetapkan.
*   **Defuzzifikasi Centroid**: Menghasilkan nilai crisp yang akurat menggunakan perhitungan Center of Area (CoA).
*   **Dashboard Interaktif**: Antarmuka berbasis Streamlit untuk simulasi real-time dan analisis visual.

## Variabel Sistem

Untuk menghasilkan keputusan yang tepat, sistem mengevaluasi parameter masukan yang mewakili kondisi penggunaan listrik harian secara komprehensif:

### Variabel Masukan (Input)
*   **Daya Aktif**: Total beban listrik real-time dengan rentang 0 hingga 2200 Watt (Klasifikasi: Rendah, Sedang, Tinggi).
*   **Waktu Penggunaan**: Representasi waktu dalam format 24 jam untuk mendeteksi beban puncak (Klasifikasi: Off-peak, Normal, Peak Hour).
*   **Prioritas Perangkat**: Skala kepentingan operasional perangkat antara 1 hingga 10 (Klasifikasi: Rendah, Sedang, Tinggi).

### Variabel Luaran (Output)
*   **Rekomendasi Penghematan**: Persentase pengurangan konsumsi yang disarankan dalam rentang 0% hingga 100% (Klasifikasi: Kecil, Sedang, Besar).

## Basis Aturan (Rule Base)

Basis aturan terdiri dari 27 kombinasi logika yang mencakup seluruh ruang keadaan masukan. Tabel berikut mendefinisikan hubungan antara kondisi masukan dan rekomendasi luaran yang dihasilkan:

| No | Daya Aktif | Waktu Penggunaan | Prioritas Perangkat | Rekomendasi Penghematan |
|----|------------|------------------|---------------------|--------------------------|
| 1  | Rendah     | Off-peak         | Rendah              | Kecil                    |
| 2  | Rendah     | Off-peak         | Sedang              | Kecil                    |
| 3  | Rendah     | Off-peak         | Tinggi              | Kecil                    |
| 4  | Rendah     | Normal           | Rendah              | Kecil                    |
| 5  | Rendah     | Normal           | Sedang              | Kecil                    |
| 6  | Rendah     | Normal           | Tinggi              | Kecil                    |
| 7  | Rendah     | Peak             | Rendah              | Sedang                   |
| 8  | Rendah     | Peak             | Sedang              | Kecil                    |
| 9  | Rendah     | Peak             | Tinggi              | Kecil                    |
| 10 | Sedang     | Off-peak         | Rendah              | Sedang                   |
| 11 | Sedang     | Off-peak         | Sedang              | Kecil                    |
| 12 | Sedang     | Off-peak         | Tinggi              | Kecil                    |
| 13 | Sedang     | Normal           | Rendah              | Sedang                   |
| 14 | Sedang     | Normal           | Sedang              | Sedang                   |
| 15 | Sedang     | Normal           | Tinggi              | Kecil                    |
| 16 | Sedang     | Peak             | Rendah              | Besar                    |
| 17 | Sedang     | Peak             | Sedang              | Sedang                   |
| 18 | Sedang     | Peak             | Tinggi              | Sedang                   |
| 19 | Tinggi     | Off-peak         | Rendah              | Sedang                   |
| 20 | Tinggi     | Off-peak         | Sedang              | Sedang                   |
| 21 | Tinggi     | Off-peak         | Tinggi              | Kecil                    |
| 22 | Tinggi     | Normal           | Rendah              | Besar                    |
| 23 | Tinggi     | Normal           | Sedang              | Sedang                   |
| 24 | Tinggi     | Normal           | Tinggi              | Sedang                   |
| 25 | Tinggi     | Peak             | Rendah              | Besar                    |
| 26 | Tinggi     | Peak             | Sedang              | Besar                    |
| 27 | Tinggi     | Peak             | Tinggi              | Sedang                   |

## Struktur Folder

Proyek ini diatur secara modular untuk memudahkan pemeliharaan dan pengembangan lebih lanjut:
*   `app.py`: Berkas utama aplikasi Streamlit.
*   `fuzzy/`: Direktori inti algoritma (fuzzifikasi, inferensi, defuzzifikasi).
*   `pages/`: Kumpulan halaman tambahan untuk simulator dan visualisasi data.
*   `requirements.txt`: Daftar dependensi pustaka Python.

## Panduan Instalasi dan Penggunaan

Ikuti langkah-langkah di bawah ini untuk menjalankan sistem di lingkungan lokal:

1.  Lakukan klon terhadap repositori ini ke direktori lokal Anda.
2.  Pasang dependensi yang diperlukan melalui terminal dengan perintah:
    ```bash
    pip install -r requirements.txt
    ```
3.  Jalankan aplikasi utama menggunakan perintah:
    ```bash
    streamlit run app.py
    ```
