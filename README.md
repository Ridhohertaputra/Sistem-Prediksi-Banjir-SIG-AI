# Sistem Prediksi Banjir dengan Deep Learning
Sistem prediksi banjir berbasis machine learning yang menggunakan data curah hujan untuk memprediksi kemungkinan terjadinya banjir di wilayah Sleman. Sistem ini mengintegrasikan data curah hujan, model CNN-LSTM, dan visualisasi peta untuk memberikan prediksi yang akurat dan mudah dipahami.
# Data yang digunakan
Proyek ini menggunakan beberapa jenis data utama, yaitu data elevasi berupa DEM (dem_sleman.tif) dan kemiringan lereng (slope_sleman.tif) dalam format GeoTIFF untuk analisis topografi dan potensi aliran air. Data penggunaan lahan dalam format shapefile (penggunaan_lahan.shp) memberikan informasi tipe lahan seperti sawah, pemukiman, dan lahan terbuka. Selain itu, data curah hujan bulanan selama 3 tahun terakhir (curah_hujan.csv) menjadi variabel utama input model, sedangkan data label banjir yang sudah diubah menjadi format bulanan (label_banjir.csv) digunakan sebagai ground truth untuk melatih model prediksi.
# Alur kerja sistem
* Pengumpulan Data
Sistem dimulai dengan mengumpulkan data input utama, yaitu data elevasi (DEM), data kemiringan lereng (slope), data penggunaan lahan, serta data curah hujan bulanan selama tiga tahun terakhir. Selain itu, tersedia data label banjir sebagai acuan pelatihan.
* Preprocessing Data
Data mentah tersebut diproses melalui script preprocessing untuk menyesuaikan format dan resolusi, menggabungkan data spasial dan non-spasial, serta menyiapkan dataset lengkap yang siap digunakan oleh model AI.
* Pelatihan Model
Data hasil preprocessing digunakan untuk melatih model deep learning dengan arsitektur hybrid CNN-LSTM yang dirancang untuk mengenali pola hubungan antara curah hujan, kondisi topografi, penggunaan lahan, dan kejadian banjir.
* Prediksi Banjir
Setelah model terlatih, dilakukan proses prediksi menggunakan data input terbaru. Hasil prediksi banjir disimpan dalam file CSV yang berisi estimasi risiko banjir per bulan di wilayah yang dianalisis.
* Visualisasi Hasil
Hasil prediksi diolah kembali untuk divisualisasikan dalam bentuk peta tematik menggunakan tools SIG dan plotting. Visualisasi ini memudahkan pemahaman dan pengambilan keputusan terkait daerah rawan banjir.
* Evaluasi dan Pembaruan Model
Model secara berkala dievaluasi menggunakan data banjir terbaru untuk menjaga akurasi prediksi dan melakukan pembaruan jika diperlukan.
# Fitur Utama
* Prediksi Banjir: Menggunakan model CNN-LSTM untuk prediksi berdasarkan data curah hujan
* Visualisasi Peta: Menampilkan hasil prediksi dalam bentuk peta interaktif
* Data Processing: Pengolahan dan penggabungan data curah hujan dengan label banjir
* Model Training: Pelatihan model deep learning dengan arsitektur CNN-LSTM
# Tools yang digunakan
* Python 3.8+
* TensorFlow/Keras - Deep Learning Framework
* GeoPandas - Geospatial Data Processing
* Pandas - Data Manipulation
* NumPy - Numerical Computing
* Matplotlib - Data Visualization
* Scikit-learn - Machine Learning Tools
* Rasterio - Geospatial Raster Data
# Hasil Output
Hasil dari proyek ini berupa model deep learning terlatih yang disimpan dalam file model_cnn_lstm.h5. Selain itu, hasil prediksi banjir disimpan dalam format CSV (prediksi_banjir.csv) yang memuat data prediksi bulanan secara tabular. Untuk visualisasi, terdapat juga file gambar peta (peta_visualisasi.png) yang menunjukkan area rawan banjir berdasarkan hasil prediksi tersebut.
# Saran pengembangan fitur lanjutan
* Integrasi Data Real-Time
Menambahkan sumber data curah hujan real-time dari sensor atau stasiun cuaca online agar prediksi banjir bisa dilakukan secara up-to-date dan responsif terhadap kondisi terkini.
* Prediksi Banjir Jangka Panjang dan Multi-Horizon
Mengembangkan model untuk prediksi banjir tidak hanya bulanan, tapi juga mingguan, harian, atau prediksi jangka panjang dengan horizon waktu yang fleksibel.
* Web Dashboard Interaktif
Membuat dashboard berbasis web yang menampilkan peta interaktif, grafik prediksi, dan notifikasi peringatan banjir sehingga pengguna akhir bisa memantau dan mengambil keputusan lebih mudah.

