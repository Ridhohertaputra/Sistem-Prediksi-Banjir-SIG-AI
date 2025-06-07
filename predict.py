import pandas as pd
import numpy as np
import joblib
import os
from tensorflow.keras.models import load_model

# Path absolut untuk load model dan scaler
model_path = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\models\model_cnn_lstm.h5"
scaler_path = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\models\scaler.save"

model = load_model(model_path)
scaler = joblib.load(scaler_path)

# Path absolut untuk file input
data_path = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\data\curah_hujan.csv"
df = pd.read_csv(data_path, sep=";")  # Tambahkan separator semicolon

# Debug: Cek kolom yang tersedia
print("Kolom yang tersedia:", df.columns.tolist())
print("Bentuk data:", df.shape)
print("Sample data:")
print(df.head())

# Strip whitespace dari nama kolom
df.columns = df.columns.str.strip()

# Cek nama kolom curah hujan yang benar
curah_hujan_cols = [col for col in df.columns if 'curah' in col.lower() or 'hujan' in col.lower()]
print("Kolom curah hujan yang ditemukan:", curah_hujan_cols)

# Gunakan kolom yang benar (sesuaikan dengan yang tersedia)
if 'curah_hujan_mm' in df.columns:
    kolom_curah_hujan = 'curah_hujan_mm'
elif 'curah_hujan_nm' in df.columns:
    kolom_curah_hujan = 'curah_hujan_nm'
elif curah_hujan_cols:
    kolom_curah_hujan = curah_hujan_cols[0]  # Gunakan kolom pertama yang ditemukan
else:
    raise ValueError("Kolom curah hujan tidak ditemukan!")

print(f"Menggunakan kolom: {kolom_curah_hujan}")
X = df[[kolom_curah_hujan]].values
X_scaled = scaler.transform(X)
X_scaled = X_scaled.reshape((X_scaled.shape[0], 1, 1))

predictions = model.predict(X_scaled)
df["prediksi_banjir"] = (predictions > 0.5).astype(int)

# Path absolut untuk output
output_dir = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "prediksi_banjir.csv")

df.to_csv(output_path, index=False)

print(f"Hasil prediksi disimpan di: {output_path}")