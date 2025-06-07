import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Set environment variable untuk shapefile
os.environ['SHAPE_RESTORE_SHX'] = 'YES'

# Path absolut untuk load data
lahan_path = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\data\penggunaan_lahan.shp"
prediksi_path = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\output\prediksi_banjir.csv"

# Cek apakah file shapefile ada
if not os.path.exists(lahan_path):
    print(f"File shapefile tidak ditemukan: {lahan_path}")
    print("Mencari file shapefile lain di direktori data...")
    
    data_dir = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\data"
    shp_files = [f for f in os.listdir(data_dir) if f.endswith('.shp')]
    print(f"File .shp yang ditemukan: {shp_files}")
    
    if shp_files:
        lahan_path = os.path.join(data_dir, shp_files[0])
        print(f"Menggunakan file: {lahan_path}")
    else:
        print("Tidak ada file shapefile ditemukan!")
        # Buat visualisasi tanpa peta
        lahan = None
else:
    print(f"File shapefile ditemukan: {lahan_path}")

# Load data
try:
    if lahan_path and os.path.exists(lahan_path):
        lahan = gpd.read_file(lahan_path)
        print(f"Berhasil load shapefile dengan {len(lahan)} features")
    else:
        lahan = None
        print("Shapefile tidak tersedia, membuat visualisasi sederhana")
except Exception as e:
    print(f"Error saat membaca shapefile: {e}")
    lahan = None

prediksi = pd.read_csv(prediksi_path)

# Ambil prediksi terbaru
terbaru = prediksi.iloc[-1]["prediksi_banjir"]

fig, ax = plt.subplots(figsize=(10, 8))

if lahan is not None:
    # Plot peta dengan warna berdasarkan prediksi banjir
    if terbaru == 1:
        # Jika prediksi banjir, warnai merah
        lahan.plot(ax=ax, color='red', edgecolor='black', alpha=0.7)
        plt.title("Prediksi Banjir Bulan Terakhir: BANJIR", fontsize=16, color='red', fontweight='bold')
    else:
        # Jika aman, warnai hijau
        lahan.plot(ax=ax, color='green', edgecolor='black', alpha=0.7)
        plt.title("Prediksi Banjir Bulan Terakhir: AMAN", fontsize=16, color='green', fontweight='bold')
    
    # Tambahkan grid dan styling
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Longitude', fontsize=12)
    ax.set_ylabel('Latitude', fontsize=12)
    
    # Tambahkan legend
    status_text = "ZONA BANJIR" if terbaru == 1 else "ZONA AMAN"
    legend_color = 'red' if terbaru == 1 else 'green'
    ax.text(0.02, 0.98, status_text, transform=ax.transAxes, fontsize=12, 
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor=legend_color, alpha=0.7))
    
else:
    # Jika tidak ada shapefile, tampilkan pesan error yang jelas
    ax.text(0.5, 0.5, 'SHAPEFILE TIDAK DITEMUKAN\nTidak dapat menampilkan peta', 
            horizontalalignment='center', verticalalignment='center', 
            transform=ax.transAxes, fontsize=16, color='red', fontweight='bold')
    ax.set_title(f"Prediksi Banjir: {'BANJIR' if terbaru == 1 else 'AMAN'}", fontsize=16)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

# Path absolut untuk output
output_dir = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "peta_visualisasi.png")

plt.savefig(output_path, dpi=300, bbox_inches='tight')
plt.show()

print(f"Peta visualisasi disimpan di: {output_path}")