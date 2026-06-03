# Sistem Manajemen Beban Listrik Rumah Tangga Berbasis Logika Fuzzy Mamdani

Proyek ini merupakan implementasi sistem pendukung keputusan yang dirancang untuk mengelola dan mengoptimalkan konsumsi daya listrik pada skala rumah tangga. Dengan memanfaatkan logika fuzzy, sistem ini mampu memberikan rekomendasi tindakan penghematan yang lebih dinamis dan fleksibel dibandingkan dengan sistem kontrol berbasis logika biner konvensional. Pendekatan ini sangat relevan untuk diaplikasikan dalam skema manajemen beban listrik, di mana variabel yang terlibat seringkali memiliki ambiguitas dan ketidakpastian tinggi.

## Deskripsi Sistem dan Arsitektur

Sistem ini mengevaluasi tiga parameter utama sebagai masukan untuk menentukan tingkat penghematan yang disarankan. Parameter pertama adalah Daya Aktif yang mencerminkan beban total secara real-time. Parameter kedua adalah Waktu Penggunaan, yang sangat krusial dalam mendeteksi periode beban puncak (peak hours) di mana tarif atau tekanan beban pada jaringan listrik cenderung lebih tinggi. Parameter ketiga adalah Prioritas Perangkat, yang memberikan konteks mengenai seberapa esensial suatu perangkat yang sedang beroperasi bagi pengguna.

Seluruh proses perhitungan dilakukan secara manual tanpa bergantung pada pustaka fuzzy eksternal untuk menjaga integritas logika dan kemudahan dalam audit algoritma. Proses dimulai dari tahap fuzzifikasi menggunakan fungsi keanggotaan triangular dan trapezoidal, dilanjutkan dengan tahap inferensi menggunakan operator minimum untuk evaluasi aturan, agregasi menggunakan operator maksimum, dan diakhiri dengan defuzzifikasi menggunakan metode Centroid (Center of Area).

## Basis Aturan (Rule Base)

Berikut adalah daftar lengkap 27 aturan fuzzy yang diimplementasikan ke dalam sistem. Aturan-aturan ini dirancang untuk mencakup seluruh kemungkinan kombinasi kondisi masukan untuk menjamin sistem tetap stabil dalam berbagai skenario penggunaan.

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

## Spesifikasi Variabel

Variabel input Daya Aktif memiliki rentang antara 0 hingga 2200 Watt, yang kemudian dibagi menjadi himpunan fuzzy Rendah, Sedang, dan Tinggi. Variabel Waktu Penggunaan direpresentasikan dalam format 24 jam dengan klasifikasi Off-peak, Normal, dan Peak Hour. Variabel Prioritas Perangkat diukur dalam skala 1 hingga 10 untuk menentukan urgensi operasional perangkat. Luaran sistem berupa persentase Rekomendasi Penghematan yang dikategorikan menjadi Kecil, Sedang, dan Besar.

## Prosedur Instalasi dan Operasional

Untuk menjalankan aplikasi ini, pengguna harus memiliki lingkungan Python yang telah terinstalasi. Langkah pertama adalah melakukan instalasi seluruh dependensi yang tercantum dalam berkas requirements.txt dengan menjalankan perintah instalasi paket melalui terminal. Setelah dependensi terpenuhi, aplikasi dashboard dapat diluncurkan menggunakan perintah streamlit run terhadap berkas utama app.py. Navigasi di dalam aplikasi memungkinkan pengguna untuk melakukan simulasi perhitungan secara interaktif dan memvisualisasikan seluruh fungsi keanggotaan yang aktif di dalam sistem.

---
**Dokumentasi Tugas Akhir Logika Fuzzy**
