# 🎣 Toko Mareno Fishing - Aplikasi Search & Sorting

Aplikasi desktop untuk mengelola inventori toko pancing dengan fitur pencarian menggunakan **Binary Search Tree (BST)** dan pengurutan menggunakan **Selection Sort**.

## 📋 Fitur Utama

### 1. **Pencarian (Search)**
- **Cari berdasarkan ID**: Menggunakan Binary Search Tree untuk pencarian cepat
- **Cari berdasarkan Nama**: Filter barang berdasarkan nama (case-insensitive)
- **Filter berdasarkan Jenis**: Tampilkan hanya barang jenis tertentu (Senar, Kail, Reel Pancing, Joran)

### 2. **Pengurutan (Sorting)**
- **Harga Termurah → Termahal (Ascending)**: Selection Sort dari harga terendah
- **Harga Termahal → Termurah (Descending)**: Selection Sort dari harga tertinggi
- **Nama A-Z**: Sort berdasarkan nama barang secara alfabetis

### 3. **Inventori**
- **Total 150 barang pancing** dengan struktur:
  - 40 item Senar
  - 40 item Kail
  - 35 item Reel Pancing
  - 35 item Joran

## 🛠️ Teknologi & Algoritma

### Struktur Data
- **Binary Search Tree (BST)**: Untuk pencarian efisien berdasarkan ID
  - Search time complexity: O(log n) rata-rata
  - Insert time complexity: O(log n) rata-rata

### Algoritma
- **Selection Sort**: Untuk pengurutan berdasarkan harga
  - Time complexity: O(n²)
  - Space complexity: O(1)

### GUI Framework
- **Tkinter**: Python's built-in GUI library
- **TTK (Themed Tkinter)**: Modern widget styling

## 📦 File Struktur

```
Toko-Mareno-Fishing/
├── main.py              # Aplikasi GUI utama
├── bst.py               # Implementasi Binary Search Tree
├── sorting.py           # Implementasi Selection Sort
├── data_manager.py      # Manager data 150 barang
├── requirements.txt     # Dependencies
└── README.md            # Dokumentasi
```

## 🚀 Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/firdausreno18-byte/Toko-Mareno-Fishing.git
cd Toko-Mareno-Fishing
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
python main.py
```

## 💡 Panduan Penggunaan

### Pencarian
1. **Cari ID**: Masukkan nomor ID barang (1-150) dan klik "Cari ID"
2. **Cari Nama**: Ketik kata kunci nama barang dan klik "Cari Nama"
3. **Filter Jenis**: Pilih jenis barang dari dropdown dan klik "Filter Jenis"

### Pengurutan
1. Klik tombol "Harga Termurah (ASC)" untuk urut dari harga rendah ke tinggi
2. Klik tombol "Harga Termahal (DESC)" untuk urut dari harga tinggi ke rendah
3. Klik tombol "Sort Nama (A-Z)" untuk urut berdasarkan nama

### Reset
- Klik tombol "Reset" untuk menampilkan semua barang lagi

## 📊 Data Barang

### Jenis-Jenis Barang

#### 1. **Senar** (40 item)
- Harga: Rp 15.000 - Rp 68.000
- Tipe: Nylon, PE Braided, Fluorocarbon, Mono
- Brand: Shimano, Daiwa, Abu Garcia, Penn, Berkley, dll

#### 2. **Kail** (40 item)
- Harga: Rp 5.000 - Rp 15.000
- Tipe: Various hooks dari berbagai brand
- Ukuran: Nomor 1-10

#### 3. **Reel Pancing** (35 item)
- Harga: Rp 165.000 - Rp 380.000
- Tipe: Spinning, Baitcasting, Multiplier, Electric
- Brand: Shimano, Daiwa, Abu Garcia, Penn, dll

#### 4. **Joran** (35 item)
- Harga: Rp 95.000 - Rp 320.000
- Tipe: Spinning, Casting, Teleskopik, Fly
- Brand: Shimano, Daiwa, Abu Garcia, Penn, Berkley, dll

## 🎨 Fitur Tampilan

- **Color-coded Table**: Setiap jenis barang memiliki warna berbeda untuk mudah diidentifikasi
  - 🟨 Senar (Kuning)
  - 🟩 Kail (Pink)
  - 🟦 Reel Pancing (Biru)
  - 🟩 Joran (Hijau)
- **Real-time Status**: Menampilkan jumlah barang yang sedang ditampilkan
- **Responsive Layout**: Tabel dapat di-scroll untuk data banyak
- **Professional UI**: Menggunakan tema TTK modern

## 💻 Requirements

- Python 3.6+
- Tkinter (biasanya sudah terinstall dengan Python)

## 📝 Contoh Penggunaan

### Contoh 1: Cari Reel Pancing Termurah
1. Filter jenis "Reel Pancing"
2. Klik "Harga Termurah (ASC)"
3. Lihat reel termurah di posisi teratas

### Contoh 2: Cari Senar Tertentu
1. Masukkan "Shimano" di field "Cari Nama"
2. Klik "Cari Nama"
3. Semua senar Shimano akan ditampilkan

### Contoh 3: Lihat Barang Paling Mahal
1. Klik "Reset"
2. Klik "Harga Termahal (DESC)"
3. Barang paling mahal akan di posisi paling atas

## 🔍 Analisis Kompleksitas

### Binary Search Tree (BST)
- **Best Case**: O(log n) - tree seimbang
- **Worst Case**: O(n) - tree miring
- **Average Case**: O(log n)

### Selection Sort
- **Best Case**: O(n²)
- **Worst Case**: O(n²)
- **Average Case**: O(n²)
- **Space Complexity**: O(1)

## 👨‍💻 Author
Firdaus Reno (firdausreno18-byte)

## 📄 License
MIT License

## 🤝 Kontribusi
Kontribusi terbuka untuk improvement dan penambahan fitur!

---

**Selamat menggunakan Aplikasi Toko Mareno Fishing! 🎣**
