import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Conv1D, MaxPooling1D, Flatten
import joblib
import os

# Path absolut untuk file data
df = pd.read_csv(r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\data\curah_hujan.csv", sep=";")
labels = pd.read_csv(r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\data\label_banjir.csv", sep=";")

# Strip whitespace dari nama kolom
df.columns = df.columns.str.strip()
labels.columns = labels.columns.str.strip()

data = pd.merge(df, labels, on=["bulan", "tahun"])

X = data[["curah_hujan_mm"]].values  # Sesuaikan nama kolom dengan yang ada di CSV
y = data["banjir"].values

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Bentuk data agar sesuai input LSTM-CNN
X_scaled = X_scaled.reshape((X_scaled.shape[0], 1, 1))

model = Sequential([
    Conv1D(32, kernel_size=1, activation='relu', input_shape=(1,1)),
    MaxPooling1D(pool_size=1),
    Flatten(),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_scaled, y, epochs=100, verbose=1)

# Path absolut untuk menyimpan model
models_dir = r"C:\Users\Hp\OneDrive\Documents\pyt\SIG\models"
os.makedirs(models_dir, exist_ok=True)
model.save(os.path.join(models_dir, "model_cnn_lstm.h5"))
joblib.dump(scaler, os.path.join(models_dir, "scaler.save"))