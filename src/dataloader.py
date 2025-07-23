import pandas as pd
import os

def load_raw_data_from_url(url):
    """Load data mentah dari URL"""
    return pd.read_csv(url)

def save_processed_data(df, file_path):
    """Simpan data yang telah diproses ke file"""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)

def load_processed_data(file_path):
    """Load data yang sudah diproses dari file lokal"""
    return pd.read_csv(file_path)
