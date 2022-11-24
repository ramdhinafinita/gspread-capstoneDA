# Google Spreadsheets 
 [![GitHub version](https://badge.fury.io/gh/burnash%2Fgspread.svg)](https://badge.fury.io/gh/burnash%2Fgspread) ![pypi]( https://badge.fury.io/py/gspread.svg) ![downloads](https://img.shields.io/pypi/dm/gspread.svg) ![doc](https://readthedocs.org/projects/gspread/badge/?version=latest)
 
Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan dari projek ini adalah melakukan analisis data dengan menggunakan library `gspread` untuk mendapatkan informasi dan dikemas dengan rapih dalam notebook. Terdapat 5 task yang perlu dikerjakan dan diakhiri dengan uploading file hasil analisa.

## Data Summary
Data yang digunakan pada capstone project ini adalah dari data African Economic Outlook January 2019. Data ini terdiri dari beberapa variabe dengan rincian sebagai berikut:
- `country_and_regions` : ID Negara               
- `country_and_regions_name` : Nama Negara
- `country_and_regions_regionid` : Region ID
- `indicators` : 
- `indicators_name` : Topik klasifikasi indikator ekonomi           
- `scale` : Satuan yang digunakan   
- `units` : Tipe aplikasi (berbayar/gratis)       
- `1980 - 2020` : Tahun data      


Antarmuka sederhana untuk bekerja dengan Google Sheets.

Features:

* Buka spreadsheet berdasarkan **title**, **key** atau **url**.
* Read, write, and format cell ranges.
* Berbagi dan kontrol akses.
* Pembaruan batch.


## Dependencies
 
- gspread -> Requirements: Python 3.6+.
- oauthlib
- pandas

Atau Bapak/Ibu cukup menginstall requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
```
## Basic Usage

1. [Create credentials in Google API Console](http://gspread.readthedocs.org/en/latest/oauth2.html)
2. Start using gspread:

```python
import gspread

### Contoh
gc = gspread.service_account()

# Open a sheet from a spreadsheet in one go
wks = gc.open("Where is the money Lebowski?").sheet1

# Update a range of cells using the top left corner address
wks.update('A1', [[1, 2], [3, 4]])

# Or update a single cell
wks.update('B42', "it's down there somewhere, let me take another look.")

# Format the header
wks.format('A1:B1', {'textFormat': {'bold': True}})
```

## Rubrik
Pada capstone ini, Anda diharapkan untuk dapat membangun sebuah notebook sederhana dengan hasil analisis menggunakan library gspread yang fokus pada hasil analisis serta otomasi pembuatan file python yang dapat dilakukan secara lokal. Langkah pertama yang harus Anda lakukan adalah silahkan download atau clone repositori ini. File pada repositori ini merupakan sebuah skeleton untuk pembuatan capstone. Pada bagian app.py dan Notebook Guide.ipynb ada beberapa bagian yang rumpang dan harus Anda lengkapi. Beberapa bagian yang harus diperhatikan adalah sebagai berikut:

Maksimal skor yang akan didapatkan yakni 16 points:  

- **Data Preparation (3 points)**
    - [ ] **Import Library**
      - Melakukan importing library yang digunakan
    - [ ] **Read data from spreadsheet**
      - Mengambil kredensial pada akun google cloud masing-masing.
    - [ ] **Cek data dari hasil spreadsheet**
      - Important: Sebelum masuk kedalam tahap analisis, wajib melampirkan keterangan hasil buka file dengan kode berikut:
      ```
gc = gspread.authorize(credentials)
sh = gc.open_by_url("________________________________") # Link Spreadsheet
worksheet = sh.worksheet("________") # Nama sheet
list_of_lists = worksheet.get_all_values()
      ```

- **Analisis Data**
    - **Data cleansing (3 points)**
        - [ ] melakukan pengisian data NaN.
              Task 1: Hapus nama-nama selain nama negara pada kolom Country and Regions Name.
    - **Summary text report: `/summary` (5 points)**
        - [ ] Menampilkan hasil analisis:
              Task 2: Buat dataframe baru dengan menyeleksi kolom `Indicators Name` berdasarkan indikator `Gross domestic product`.
              Task 3: Carilah negara mana yang memiliki GDP terbersar dan terkecil pada tahun 2020.
              Task 4: Carilah progress ekspor dari negara dengan GDP terbesar dan terkecil kemudian buatlah visualisasinya (pembuatan plot).
    - **Visualization report: `/plot` (3 points)**
        - [ ] Perform necessary **data wrangling** steps to extract information
        - [ ] Perform the right **mathematical calculation**
        - [ ] Task 5: Buatlah dataframe baru dengan informasi presentase ekspor GDP dari semua negara di Afrika.
        - [ ] **Tidy** plot layout (title, label, color, size)
- **Application deployment (3 points)**
    - [ ] **`app.py`** untuk membuat notebook berjalan otomatis di local
    - [ ] **gspread** menggunakan library gspread 
    - [ ] **`app.py`** run berhasil tanpa error

## Project File Structure

```
gspred
├── 📁 assets
├── 📁 data_input
├── </> app.py
├── 📝 Notebook Guide.ipynb
└── 📝 requirements.txt
```

- Folders (**DO NOT CHANGE**):
    - `assets`: Images used in notebook
    - `data_input`: Dataset untuk analisis

- Application-related Files (**TO BE COMPLETED BY STUDENT**):
    - `app.py`: gspread untuk dijalankan secara lokal
    - `Notebook Guide.ipynb`: Panduan utama untuk alur kerja proyek

- Deployment-related Files (**DO NOT CHANGE**):
    - `.gitignore`: List of file extensions to be ignored when `git push` from local
    - `requirements.txt`: Daftar dependensi paket yang akan diinstall

## Expected Output

### Plot Analisis

Create a bot that can provide report on Facebook daily ads for different marketing campaign. Here is an example: https://t.me/algo_capstone_telebot

<p align="center" width="100%">
    <img src="assets/readme/telegram-bot.png" width="350px"> 
</p>

Here are the chatbot functionalities:

1. Command `/start` or `/help`: send welcome message containing list of available commands.

<p align="center" width="100%">
    <img src="assets/readme/start.png" width="350px"> 
</p>

2. Command `/about`: send information about the bot developer.

<p align="center" width="100%">
    <img src="assets/output.png""> 
</p>

3. Command `/summary`: generate text report for selected campaign ID.

<p align="center" width="100%">
    <img src="assets/readme/summary-1.png" width="350px">
</p>

Reply from bot after campaign ID is selected:

<p align="center" width="100%">
    <img src="assets/readme/summary-2.png" width="350px">
</p>

4. Command `/plot`: generate visualization and voice message report per age group for selected campaign ID.

<p align="center" width="100%">
    <img src="assets/readme/plot-1.png" width="350px">
</p>

Reply from bot after campaign ID is selected:

<p align="center" width="100%">
    <img src="assets/readme/plot-2.png" width="350px">
</p>

**Voice message:** 
<a href="https://drive.google.com/file/d/16hVORo-heUOjWje_g62aV6380-toBwWp/view?usp=sharing" target="_blank">Sample audio for Campaign ID 916</a>

> This is your requested plot for Campaign ID 916.
> Age group with the highest total spent is 30-34, while the lowest is 40-44. 
> Age group with the highest total approved conversion is 30-34, while the lowest is 45-49.
> Age group with the highest average CPC is 45-49, while the lowest is 40-44.

5. Default message: handle messages other than the previous commands.

<p align="center" width="100%">
    <img src="assets/readme/default-message.png" width="350px">
</p>

### Deployed Application

<p align="center" width="100%">
    <img src="assets/readme/deployed-app.png" width="350px"> 
</p>

This bot is expected to run **continuously** on a server. Therefore we create a `Flask` application which deployed to Heroku. Here is an example: https://algo-capstone-telebot.herokuapp.com/.
