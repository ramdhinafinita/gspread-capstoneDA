import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
import pandas as pd
import numpy as np
import datetime
import re

# Bagian ini untuk menghubungkan dengan google spreadsheet

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'gs_credentials.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)
sh = gc.open_by_url("________________________________") # Link Spreadsheet
worksheet = sh.worksheet("________") # Nama sheet
list_of_lists = worksheet.get_all_values()

# Bagian ini untuk mengubah data dari spreadsheet menjadi dataframe yang nantinya dapat dianalisa
data = pd.DataFrame(_______) # ubah list_of_list menjadi dataframe
data.columns = ______ # ubah baris pertama menjadi nama kolom
data = data.iloc[1:]

data.reset_index(drop=True, inplace=True) # Mereset penomoran index

# Buatlah dataframe baru dengan informasi presentase ekspor GDP dari semua negara di Afrika.
upload_data = ____________________
upload_data.index = ___________________
upload_data.reset_index(inplace=True)
upload_data.fillna("", inplace=True)

# Bagian ini digunakan untuk upload dataframe baru ke spreadsheet
new_worksheet = sh.add_worksheet(title="_____________", rows=100, cols=20)
new_worksheet.update([___________.columns.values.tolist()] + __________.values.tolist())