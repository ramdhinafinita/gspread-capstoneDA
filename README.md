# Google Spreadsheets 
<p align="center" width="100%">
    <img src="assets/gspread.png"> 
</p>

## Background
Pembuatan notebook dan spreadsheet dengan menggunakan data `African Economic Outlook January 2019`. Notebook yang dibuat akan menghasilkan beberapa insight untuk menjawab permasalahan yang ada dan dapat dijadikan bahan pembelajaran mengenai ekonomi di Negara-negara di Benua Afrika. Latar belakang dari visualisasi data dengan Notebook beserta analisis dan narasi digunakan untuk membantu menganalisis perkembangan ekonomi di negara tersebut dimana seperti yang kita ketahui, negara-negara di Afrika selalu dinilai menjadi Benua Afrika merupakan benua yang kondisi ekonominya di bawah benua-benua lainnya. Namun, dengan dibuatnya sebuah dashboard interaktif dari data tersebut kita mengajak audience dalam melakukan analisa lebih jauh seperti mengurutkan negara-negara di Benua Afrika berdasarkan klasifikasi indikator penliai serta membandingkan dengan negara-negara lain di Benua Afrika tersebut.


Projek ini dikembangkan sebagai salah satu capstone project dari Algoritma Academy Data Analytics Specialization. Deliverables yang diharapkan dari projek ini adalah melakukan analisis data dengan menggunakan library `gspread` untuk mendapatkan informasi dan dikemas dengan rapih dalam notebook. Tahapan langkah untuk data preparation dapat dilihat pada [link berikut](https://scribehow.com/shared/Google_Workflow__q-35_aWiQnONzLsEHobAhQ). Terdapat 5 task yang perlu dikerjakan dan diakhiri dengan uploading file hasil analisa. 

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

![image](https://user-images.githubusercontent.com/64061969/203851497-6e544330-284a-4f7f-a68c-b8637f424574.png)
[Maps Africa](https://hub.arcgis.com/datasets/07610d73964e4d39ab62c4245d548625_0/explore?location=2.910951%2C-148.773003%2C2.85)<br>
Antarmuka sederhana untuk bekerja dengan Google Sheets.

## Dependencies

- gspread -> Requirements: Python 3.9+.
- oauthlib
- pandas

Atau Bapak/Ibu cukup menginstall requirements.txt dengan cara berikut

```python
pip install -r requirements.txt
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
      ``` python
      gc = gspread.authorize(credentials)
      sh = gc.open_by_url("________________________________") # Link Spreadsheet
      worksheet = sh.worksheet("________") # Nama sheet
      list_of_lists = worksheet.get_all_values()
      ```

- **Analisis Data**
    - **Data cleansing (3 points)**
        - [ ] melakukan pengisian data NaN.
              Task 1: Hapus nama-nama selain nama negara pada kolom Country and Regions Name.
    - **Summary text report: `/summary` (4 points)**
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
    - [ ] **`gspread`** menggunakan library gspread (Task 6)
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

## Ekspektasi Luaran

**Task 1:** Hapus nama-nama selain nama negara pada kolom Country and Regions Name<br>
**Task 2:** Buat dataframe baru dengan menyeleksi kolom Indicators Name berdasarkan indikator Gross domestic product<br>
**Task 3:** Carilah negara mana yang memiliki GDP terbersar dan terkecil pada tahun 2020<br>
**Task 4:** Carilah progress ekspor dari negara dengan GDP terbesar dan terkecil kemudian buatlah visualisasinya<br>

<p align="center" width="100%">
    <img src="assets/output.png""> 
</p>

**Task 5:** Buatlah dataframe baru dengan informasi presentase ekspor GDP dari semua negara di Afrika.<br>
**Task 6:** Upload data yang sudah bersih di spreadsheet<br>
**Extra** > Berhasil menjalankan `app.py` tanpa error<br>
