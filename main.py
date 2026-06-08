"""
Aplikasi GUI Toko Mareno Fishing
Fitur: Search (Binary Search Tree) dan Sorting (Selection Sort)
"""

import tkinter as tk
from tkinter import ttk, messagebox
from bst import BinarySearchTree
from sorting import SelectionSort
from data_manager import DataManager


class TokoMarenoFishingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎣 Toko Mareno Fishing - Search & Sorting")
        self.root.geometry("1200x700")
        self.root.resizable(True, True)

        # Set style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Header.TLabel', font=('Arial', 16, 'bold'), foreground='#0066cc')
        style.configure('Title.TLabel', font=('Arial', 20, 'bold'), foreground='#003366')

        # Initialize data
        self.data_manager = DataManager()
        self.all_items = self.data_manager.get_fishing_equipment_data()
        self.bst = BinarySearchTree()
        self.sorter = SelectionSort()
        self.current_display = self.all_items.copy()

        # Load data ke BST
        for item in self.all_items:
            self.bst.insert(item['id'], item['nama'], item['jenis'], item['harga'])

        self.setup_ui()

    def setup_ui(self):
        """Setup tampilan aplikasi"""
        # ===== HEADER =====
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill=tk.X, padx=10, pady=10)

        title_label = ttk.Label(header_frame, text="🎣 TOKO MARENO FISHING", style='Title.TLabel')
        title_label.pack(side=tk.LEFT)

        info_label = ttk.Label(header_frame, text=f"Total Barang: {len(self.all_items)}", font=('Arial', 10))
        info_label.pack(side=tk.RIGHT, padx=20)

        # ===== SEARCH FRAME =====
        search_frame = ttk.LabelFrame(self.root, text="🔍 PENCARIAN", padding=10)
        search_frame.pack(fill=tk.X, padx=10, pady=5)

        # Search by ID
        ttk.Label(search_frame, text="Cari ID:").grid(row=0, column=0, padx=5, pady=5)
        self.search_id_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.search_id_var, width=15).grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(search_frame, text="Cari ID", command=self.search_by_id).grid(row=0, column=2, padx=5, pady=5)

        # Search by Name
        ttk.Label(search_frame, text="Cari Nama:").grid(row=0, column=3, padx=5, pady=5)
        self.search_name_var = tk.StringVar()
        ttk.Entry(search_frame, textvariable=self.search_name_var, width=20).grid(row=0, column=4, padx=5, pady=5)
        ttk.Button(search_frame, text="Cari Nama", command=self.search_by_name).grid(row=0, column=5, padx=5, pady=5)

        # Search by Jenis
        ttk.Label(search_frame, text="Pilih Jenis:").grid(row=1, column=0, padx=5, pady=5)
        self.jenis_var = tk.StringVar()
        jenis_list = ['Semua'] + self.data_manager.get_jenis_list()
        jenis_combo = ttk.Combobox(search_frame, textvariable=self.jenis_var, values=jenis_list, state='readonly', width=15)
        jenis_combo.grid(row=1, column=1, padx=5, pady=5)
        jenis_combo.set('Semua')
        ttk.Button(search_frame, text="Filter Jenis", command=self.filter_by_jenis).grid(row=1, column=2, padx=5, pady=5)

        # Reset Button
        ttk.Button(search_frame, text="Reset", command=self.reset_display).grid(row=1, column=3, padx=5, pady=5)

        # ===== SORTING FRAME =====
        sort_frame = ttk.LabelFrame(self.root, text="↕️ PENGURUTAN", padding=10)
        sort_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(sort_frame, text="Harga Termurah (ASC)", command=self.sort_ascending).pack(side=tk.LEFT, padx=5)
        ttk.Button(sort_frame, text="Harga Termahal (DESC)", command=self.sort_descending).pack(side=tk.LEFT, padx=5)
        ttk.Button(sort_frame, text="Sort Nama (A-Z)", command=self.sort_by_name).pack(side=tk.LEFT, padx=5)

        # ===== TABLE FRAME =====
        table_frame = ttk.LabelFrame(self.root, text="📊 DAFTAR BARANG", padding=5)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Treeview
        columns = ('ID', 'Nama', 'Jenis', 'Harga')
        self.tree = ttk.Treeview(table_frame, columns=columns, height=20, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)

        # Define columns
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.column('ID', anchor=tk.CENTER, width=50)
        self.tree.column('Nama', anchor=tk.W, width=400)
        self.tree.column('Jenis', anchor=tk.CENTER, width=120)
        self.tree.column('Harga', anchor=tk.E, width=150)

        # Create headings
        self.tree.heading('#0', text='', anchor=tk.W)
        self.tree.heading('ID', text='ID', anchor=tk.CENTER)
        self.tree.heading('Nama', text='Nama Barang', anchor=tk.W)
        self.tree.heading('Jenis', text='Jenis', anchor=tk.CENTER)
        self.tree.heading('Harga', text='Harga', anchor=tk.E)

        # Style
        self.tree.tag_configure('oddrow', background='#f0f0f0')
        self.tree.tag_configure('evenrow', background='#ffffff')
        self.tree.tag_configure('senar', background='#fff9e6')
        self.tree.tag_configure('kail', background='#fff0f5')
        self.tree.tag_configure('reel', background='#e6f2ff')
        self.tree.tag_configure('joran', background='#f0ffe6')

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Load initial data
        self.load_table(self.current_display)

        # ===== STATUS BAR =====
        status_frame = ttk.Frame(self.root)
        status_frame.pack(fill=tk.X, padx=10, pady=5)

        self.status_var = tk.StringVar()
        self.status_var.set(f"Total: {len(self.current_display)} item")
        ttk.Label(status_frame, textvariable=self.status_var).pack(side=tk.LEFT)

    def load_table(self, items):
        """Load data ke tabel"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert new items
        for idx, item in enumerate(items):
            tag = self.get_tag_for_jenis(item['jenis'])
            values = (
                item['id'],
                item['nama'],
                item['jenis'],
                self.data_manager.format_currency(item['harga'])
            )
            self.tree.insert('', 'end', values=values, tags=(tag,))

        # Update status
        self.status_var.set(f"Menampilkan: {len(items)} dari {len(self.all_items)} item")

    def get_tag_for_jenis(self, jenis):
        """Return tag color berdasarkan jenis"""
        jenis_lower = jenis.lower()
        if 'senar' in jenis_lower:
            return 'senar'
        elif 'kail' in jenis_lower:
            return 'kail'
        elif 'reel' in jenis_lower:
            return 'reel'
        elif 'joran' in jenis_lower:
            return 'joran'
        return 'oddrow'

    def search_by_id(self):
        """Search menggunakan Binary Search Tree berdasarkan ID"""
        try:
            search_id = int(self.search_id_var.get())
            result = self.bst.search_by_id(search_id)

            if result:
                self.current_display = [result]
                self.load_table(self.current_display)
                messagebox.showinfo("Hasil Pencarian", f"Ditemukan: {result['nama']}\nHarga: {self.data_manager.format_currency(result['harga'])}")
            else:
                messagebox.showwarning("Pencarian", "ID tidak ditemukan")
                self.reset_display()

        except ValueError:
            messagebox.showerror("Error", "Masukkan ID yang valid (angka)")

    def search_by_name(self):
        """Search berdasarkan nama"""
        search_name = self.search_name_var.get().strip()

        if not search_name:
            messagebox.showwarning("Pencarian", "Masukkan nama yang dicari")
            return

        results = self.bst.search_by_name(search_name)

        if results:
            self.current_display = results
            self.load_table(self.current_display)
            messagebox.showinfo("Hasil Pencarian", f"Ditemukan {len(results)} item dengan nama mengandung '{search_name}'")
        else:
            messagebox.showinfo("Hasil Pencarian", f"Tidak ditemukan item dengan nama '{search_name}'")
            self.reset_display()

    def filter_by_jenis(self):
        """Filter berdasarkan jenis"""
        jenis = self.jenis_var.get()

        if jenis == 'Semua':
            self.current_display = self.all_items.copy()
        else:
            results = self.bst.search_by_jenis(jenis)
            self.current_display = results

        self.load_table(self.current_display)

    def sort_ascending(self):
        """Sort harga dari termurah ke termahal"""
        if not self.current_display:
            messagebox.showwarning("Sorting", "Tidak ada data untuk di-sort")
            return

        sorted_items = self.sorter.sort_ascending(self.current_display)
        self.current_display = sorted_items
        self.load_table(self.current_display)
        messagebox.showinfo("Sorting", "Data diurutkan dari harga termurah ke termahal")

    def sort_descending(self):
        """Sort harga dari termahal ke termurah"""
        if not self.current_display:
            messagebox.showwarning("Sorting", "Tidak ada data untuk di-sort")
            return

        sorted_items = self.sorter.sort_descending(self.current_display)
        self.current_display = sorted_items
        self.load_table(self.current_display)
        messagebox.showinfo("Sorting", "Data diurutkan dari harga termahal ke termurah")

    def sort_by_name(self):
        """Sort berdasarkan nama"""
        if not self.current_display:
            messagebox.showwarning("Sorting", "Tidak ada data untuk di-sort")
            return

        sorted_items = self.sorter.sort_by_name(self.current_display)
        self.current_display = sorted_items
        self.load_table(self.current_display)
        messagebox.showinfo("Sorting", "Data diurutkan berdasarkan nama (A-Z)")

    def reset_display(self):
        """Reset tampilan ke data awal"""
        self.current_display = self.all_items.copy()
        self.load_table(self.current_display)
        self.search_id_var.set('')
        self.search_name_var.set('')
        self.jenis_var.set('Semua')
        messagebox.showinfo("Reset", "Tampilan di-reset ke data awal")


if __name__ == "__main__":
    root = tk.Tk()
    app = TokoMarenoFishingApp(root)
    root.mainloop()
