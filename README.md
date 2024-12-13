# Proyek Analisis Data: Bike Sharing Dashboard


# Dokumentasi Menjalankan dan Deploy Proyek Streamlit

## 1. Membuat Virtual Environment
Langkah pertama adalah membuat virtual environment untuk menjaga dependensi proyek tetap terisolasi.

bash
# Membuat virtual environment
python -m venv env

# Mengaktifkan virtual environment
# Windows
env\Scripts\activate

# MacOS/Linux
source env/bin/activate


## 2. Memperbarui pip
Pastikan pip di virtual environment telah diperbarui.

bash
pip install --upgrade pip


## 3. Menginstal Dependencies
Install semua library yang diperlukan berdasarkan file requirements.txt.

bash
pip install -r requirements.txt


Jika file requirements.txt belum dibuat, Anda dapat membuatnya dengan mengekspor dependensi proyek:

bash
pip freeze > requirements.txt


## 4. Menjalankan Aplikasi Streamlit Secara Lokal
Setelah virtual environment aktif dan semua dependensi terinstal, jalankan aplikasi Streamlit:

bash
streamlit run app.py


Pastikan mengganti app.py dengan nama file utama aplikasi Anda.

## 5. Deploy ke Streamlit Community Cloud
Untuk mendeply aplikasi Anda ke Streamlit Community Cloud, ikuti langkah-langkah berikut:

1. *Siapkan Repositori GitHub*
   - Push semua file proyek ke repositori GitHub, termasuk file requirements.txt dan file aplikasi utama (app.py).

2. *Login ke Streamlit Community Cloud*
   - Buka [Streamlit Community Cloud](https://share.streamlit.io/) dan login menggunakan akun GitHub Anda.

3. *Hubungkan Proyek Anda*
   - Klik tombol "New App" dan pilih repositori GitHub tempat proyek Anda berada.
   - Isi informasi seperti branch yang digunakan (misalnya main) dan file aplikasi utama (misalnya app.py).

4. *Deploy Aplikasi*
   - Klik "Deploy" untuk memulai proses deploy. Streamlit akan secara otomatis menginstal dependensi dari requirements.txt dan menjalankan aplikasi Anda.

5. *Testing dan Update*
   - Setelah deploy berhasil, Anda dapat mengakses aplikasi Anda melalui URL yang diberikan Streamlit.
   - Jika ada perubahan, lakukan commit dan push ke GitHub, lalu Streamlit akan otomatis memperbarui aplikasi Anda.
