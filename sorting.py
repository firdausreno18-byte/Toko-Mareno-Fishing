"""
Selection Sort untuk sorting alat pancing berdasarkan harga
"""

class SelectionSort:
    @staticmethod
    def sort_ascending(items):
        """
        Sorting harga dari termurah ke termahal (ascending)
        Menggunakan Selection Sort
        """
        items_copy = [item.copy() for item in items]
        n = len(items_copy)

        for i in range(n):
            # Cari index dengan harga minimum dari i sampai akhir
            min_idx = i
            for j in range(i + 1, n):
                if items_copy[j]['harga'] < items_copy[min_idx]['harga']:
                    min_idx = j

            # Tukar elemen
            items_copy[i], items_copy[min_idx] = items_copy[min_idx], items_copy[i]

        return items_copy

    @staticmethod
    def sort_descending(items):
        """
        Sorting harga dari termahal ke termurah (descending)
        Menggunakan Selection Sort
        """
        items_copy = [item.copy() for item in items]
        n = len(items_copy)

        for i in range(n):
            # Cari index dengan harga maksimum dari i sampai akhir
            max_idx = i
            for j in range(i + 1, n):
                if items_copy[j]['harga'] > items_copy[max_idx]['harga']:
                    max_idx = j

            # Tukar elemen
            items_copy[i], items_copy[max_idx] = items_copy[max_idx], items_copy[i]

        return items_copy

    @staticmethod
    def sort_by_name(items):
        """Sorting berdasarkan nama (alphabetical)"""
        items_copy = [item.copy() for item in items]
        n = len(items_copy)

        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if items_copy[j]['nama'] < items_copy[min_idx]['nama']:
                    min_idx = j

            items_copy[i], items_copy[min_idx] = items_copy[min_idx], items_copy[i]

        return items_copy
