import geopandas as gpd
import rasterio
import numpy as np
import pandas as pd
from rasterio.plot import show
import matplotlib.pyplot as plt

def load_raster(path):
    with rasterio.open(path) as src:
        data = src.read(1)
        profile = src.profile
    return data, profile

def load_vector(path):
    return gpd.read_file(path)

def normalize(array):
    return (array - np.min(array)) / (np.max(array) - np.min(array))

def merge_features():
    # Ganti dengan path absolut sesuai lokasi file di komputer Anda
    dem_path = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\data\dem_sleman.tif"
    slope_path = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\data\slope_sleman.tif"
    curah_path = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\data\curah_hujan.csv"
    label_path = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\data\label_banjir.csv"

    # Load raster features
    dem, _ = load_raster(dem_path)
    slope, _ = load_raster(slope_path)

    # Load CSV data
    curah = pd.read_csv(curah_path, sep=";")
    label = pd.read_csv(label_path, sep=";")
    
    # Strip whitespace dari nama kolom
    curah.columns = curah.columns.str.strip()
    label.columns = label.columns.str.strip()
    
    # Gabung curah hujan dan label berdasarkan bulan dan tahun
    df = pd.merge(curah, label, on=["bulan", "tahun"])

    return df

if __name__ == "__main__":
    df = merge_features()
    print(df.head())