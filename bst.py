"""
Binary Search Tree (BST) untuk pencarian alat pancing
"""

class Node:
    def __init__(self, alat_id, nama, jenis, harga):
        self.alat_id = alat_id
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, alat_id, nama, jenis, harga):
        """Insert data ke dalam BST berdasarkan alat_id"""
        if self.root is None:
            self.root = Node(alat_id, nama, jenis, harga)
        else:
            self._insert_recursive(self.root, alat_id, nama, jenis, harga)

    def _insert_recursive(self, node, alat_id, nama, jenis, harga):
        if alat_id < node.alat_id:
            if node.left is None:
                node.left = Node(alat_id, nama, jenis, harga)
            else:
                self._insert_recursive(node.left, alat_id, nama, jenis, harga)
        else:
            if node.right is None:
                node.right = Node(alat_id, nama, jenis, harga)
            else:
                self._insert_recursive(node.right, alat_id, nama, jenis, harga)

    def search_by_id(self, alat_id):
        """Cari alat pancing berdasarkan ID"""
        return self._search_recursive(self.root, alat_id)

    def _search_recursive(self, node, alat_id):
        if node is None:
            return None

        if alat_id == node.alat_id:
            return {
                'id': node.alat_id,
                'nama': node.nama,
                'jenis': node.jenis,
                'harga': node.harga
            }
        elif alat_id < node.alat_id:
            return self._search_recursive(node.left, alat_id)
        else:
            return self._search_recursive(node.right, alat_id)

    def search_by_name(self, nama_cari):
        """Cari alat pancing berdasarkan nama (case-insensitive)"""
        hasil = []
        self._search_by_name_recursive(self.root, nama_cari.lower(), hasil)
        return hasil

    def _search_by_name_recursive(self, node, nama_cari, hasil):
        if node is None:
            return

        self._search_by_name_recursive(node.left, nama_cari, hasil)

        if nama_cari in node.nama.lower():
            hasil.append({
                'id': node.alat_id,
                'nama': node.nama,
                'jenis': node.jenis,
                'harga': node.harga
            })

        self._search_by_name_recursive(node.right, nama_cari, hasil)

    def search_by_jenis(self, jenis_cari):
        """Cari alat pancing berdasarkan jenis"""
        hasil = []
        self._search_by_jenis_recursive(self.root, jenis_cari.lower(), hasil)
        return hasil

    def _search_by_jenis_recursive(self, node, jenis_cari, hasil):
        if node is None:
            return

        self._search_by_jenis_recursive(node.left, jenis_cari, hasil)

        if jenis_cari in node.jenis.lower():
            hasil.append({
                'id': node.alat_id,
                'nama': node.nama,
                'jenis': node.jenis,
                'harga': node.harga
            })

        self._search_by_jenis_recursive(node.right, jenis_cari, hasil)

    def get_all_items(self):
        """Ambil semua item dari BST (in-order traversal)"""
        hasil = []
        self._inorder_traversal(self.root, hasil)
        return hasil

    def _inorder_traversal(self, node, hasil):
        if node is None:
            return

        self._inorder_traversal(node.left, hasil)
        hasil.append({
            'id': node.alat_id,
            'nama': node.nama,
            'jenis': node.jenis,
            'harga': node.harga
        })
        self._inorder_traversal(node.right, hasil)
