"""
Data Manager - Mengelola data 150 alat pancing Toko Mareno Fishing
Jenis alat: Senar, Kail, Reel Pancing, Joran
"""

class DataManager:
    @staticmethod
    def get_fishing_equipment_data():
        """
        Mengembalikan list 150 alat pancing dengan struktur:
        {
            'id': int,
            'nama': str,
            'jenis': str (Senar, Kail, Reel Pancing, Joran),
            'harga': int
        }
        """
        data = []
        alat_id = 1

        # ===== SENAR (40 item) =====
        senar_data = [
            ("Senar Pancing Nylon 0.4mm", 15000),
            ("Senar Pancing Nylon 0.6mm", 18000),
            ("Senar Pancing Nylon 0.8mm", 20000),
            ("Senar Pancing Nylon 1.0mm", 25000),
            ("Senar Pancing PE Braided 8x", 45000),
            ("Senar Pancing PE Braided 12x", 55000),
            ("Senar Pancing Fluorocarbon 0.5mm", 35000),
            ("Senar Pancing Fluorocarbon 0.7mm", 42000),
            ("Senar Pancing Mono Japan 100m", 22000),
            ("Senar Pancing Mono Japan 150m", 28000),
            ("Senar Power Pro 125lb", 65000),
            ("Senar Power Pro 100lb", 60000),
            ("Senar Varivas Avani Eging", 52000),
            ("Senar Berkley Trilene", 19000),
            ("Senar Shimano Technium", 38000),
            ("Senar Daiwa J-Braid", 58000),
            ("Senar Penn Battle", 24000),
            ("Senar Abu Garcia", 30000),
            ("Senar Maxima", 26000),
            ("Senar Ativa", 23000),
            ("Senar Green", 21000),
            ("Senar Big Game", 68000),
            ("Senar Charter", 32000),
            ("Senar Intrepid", 36000),
            ("Senar Cortland", 29000),
            ("Senar Orvis", 40000),
            ("Senar Pflueger", 25000),
            ("Senar Rapala", 27000),
            ("Senar Spro", 33000),
            ("Senar Sufix", 31000),
            ("Senar YGK G-Soul", 50000),
            ("Senar Sunline", 44000),
            ("Senar Toray", 48000),
            ("Senar Ike Mata", 35000),
            ("Senar Clear Mono", 17000),
            ("Senar Brown Mono", 18500),
            ("Senar Orange Mono", 19500),
            ("Senar Smoke Mono", 20500),
            ("Senar White Mono", 16000),
            ("Senar Camo Green", 21500),
        ]

        for nama, harga in senar_data:
            data.append({
                'id': alat_id,
                'nama': nama,
                'jenis': 'Senar',
                'harga': harga
            })
            alat_id += 1

        # ===== KAIL (40 item) =====
        kail_data = [
            ("Kail Pancing Nomor 1", 5000),
            ("Kail Pancing Nomor 2", 5500),
            ("Kail Pancing Nomor 3", 6000),
            ("Kail Pancing Nomor 4", 6500),
            ("Kail Pancing Nomor 5", 7000),
            ("Kail Pancing Nomor 6", 7500),
            ("Kail Pancing Nomor 7", 8000),
            ("Kail Pancing Nomor 8", 8500),
            ("Kail Pancing Nomor 9", 9000),
            ("Kail Pancing Nomor 10", 9500),
            ("Kail Owner Saitou Worm", 12000),
            ("Kail Owner Offset", 11000),
            ("Kail Gamakatsu Worm", 13000),
            ("Kail Gamakatsu Finesse", 12500),
            ("Kail Mustad Viking", 10500),
            ("Kail Mustad Ultrapoint", 11500),
            ("Kail Berkley Fusion", 9500),
            ("Kail Shimano Beastmaster", 14000),
            ("Kail Daiwa Tournament", 13500),
            ("Kail Penn Battle", 11000),
            ("Kail Abu Garcia", 10000),
            ("Kail Rapala", 10500),
            ("Kail Spro", 11500),
            ("Kail Sufix", 10800),
            ("Kail YGK", 12000),
            ("Kail Sunline", 11200),
            ("Kail Toray", 10900),
            ("Kail Ike", 11800),
            ("Kail Umpan Master", 8500),
            ("Kail Premium Gold", 14500),
            ("Kail Silver Star", 13200),
            ("Kail Black Diamond", 15000),
            ("Kail Red Revolution", 12800),
            ("Kail Green Warrior", 13800),
            ("Kail Blue Thunder", 12500),
            ("Kail Purple King", 14200),
            ("Kail Orange Beast", 11800),
            ("Kail White Knight", 10500),
            ("Kail Brown Eagle", 11200),
            ("Kail Camo Snake", 13000),
        ]

        for nama, harga in kail_data:
            data.append({
                'id': alat_id,
                'nama': nama,
                'jenis': 'Kail',
                'harga': harga
            })
            alat_id += 1

        # ===== REEL PANCING (35 item) =====
        reel_data = [
            ("Reel Pancing Baitcasting Shimano", 250000),
            ("Reel Pancing Baitcasting Daiwa", 260000),
            ("Reel Pancing Baitcasting Abu Garcia", 270000),
            ("Reel Pancing Baitcasting Penn", 255000),
            ("Reel Pancing Spinning Shimano Sienna", 180000),
            ("Reel Pancing Spinning Shimano Sedona", 200000),
            ("Reel Pancing Spinning Shimano Nasci", 220000),
            ("Reel Pancing Spinning Daiwa Legalis", 190000),
            ("Reel Pancing Spinning Daiwa Freams", 210000),
            ("Reel Pancing Spinning Abu Garcia Orra", 205000),
            ("Reel Pancing Spinning Abu Garcia Black Max", 185000),
            ("Reel Pancing Spinning Penn Battle", 195000),
            ("Reel Pancing Spinning Penn Fierce III", 215000),
            ("Reel Pancing Spinning Berkley Cherrywood", 170000),
            ("Reel Pancing Spinning Pflueger President", 165000),
            ("Reel Pancing Spinning Rapala", 175000),
            ("Reel Pancing Spinning Spro", 198000),
            ("Reel Pancing Spinning Sufix", 192000),
            ("Reel Pancing Spinning YGK", 188000),
            ("Reel Pancing Spinning Sunline", 182000),
            ("Reel Pancing Spinning Toray", 196000),
            ("Reel Pancing Spinning Ike", 186000),
            ("Reel Pancing Baitrunner Shimano", 280000),
            ("Reel Pancing Baitrunner Daiwa", 290000),
            ("Reel Pancing Baitrunner Penn", 285000),
            ("Reel Pancing Multiplier Abu Garcia", 295000),
            ("Reel Pancing Multiplier Shimano", 300000),
            ("Reel Pancing Multiplier Daiwa", 310000),
            ("Reel Pancing Overhead Vintage", 320000),
            ("Reel Pancing Centrepin Classic", 330000),
            ("Reel Pancing Lever Drag", 350000),
            ("Reel Pancing Star Drag", 340000),
            ("Reel Pancing Electric Motor", 380000),
            ("Reel Pancing Jigging Premium", 360000),
            ("Reel Pancing Trolling Pro", 370000),
        ]

        for nama, harga in reel_data:
            data.append({
                'id': alat_id,
                'nama': nama,
                'jenis': 'Reel Pancing',
                'harga': harga
            })
            alat_id += 1

        # ===== JORAN (35 item) =====
        joran_data = [
            ("Joran Pancing Spinning 1.8m", 120000),
            ("Joran Pancing Spinning 2.0m", 130000),
            ("Joran Pancing Spinning 2.1m", 140000),
            ("Joran Pancing Spinning 2.4m", 155000),
            ("Joran Pancing Casting 1.5m", 135000),
            ("Joran Pancing Casting 1.8m", 150000),
            ("Joran Pancing Casting 2.0m", 165000),
            ("Joran Pancing Casting 2.1m", 175000),
            ("Joran Pancing Shimano Beastmaster", 280000),
            ("Joran Pancing Shimano Zodias", 320000),
            ("Joran Pancing Daiwa Crossfire", 260000),
            ("Joran Pancing Daiwa Exceler", 300000),
            ("Joran Pancing Abu Garcia Fantasista", 290000),
            ("Joran Pancing Abu Garcia Salty Stage", 310000),
            ("Joran Pancing Penn Carnage II", 240000),
            ("Joran Pancing Penn Prevail", 270000),
            ("Joran Pancing Berkley Lightning", 190000),
            ("Joran Pancing Berkley Powerstick", 210000),
            ("Joran Pancing Pflueger Champion", 185000),
            ("Joran Pancing Rapala", 205000),
            ("Joran Pancing Spro", 215000),
            ("Joran Pancing Sufix", 200000),
            ("Joran Pancing YGK Yamada", 250000),
            ("Joran Pancing Sunline", 195000),
            ("Joran Pancing Toray", 225000),
            ("Joran Pancing Ike Ishikawa", 235000),
            ("Joran Pancing Teleskopik 2.4m", 95000),
            ("Joran Pancing Teleskopik 3.0m", 110000),
            ("Joran Pancing Teleskopik 3.6m", 125000),
            ("Joran Pancing Fly 8ft", 280000),
            ("Joran Pancing Fly 9ft", 300000),
            ("Joran Pancing Fly 10ft", 320000),
            ("Joran Pancing Ultralight", 150000),
            ("Joran Pancing Medium Heavy", 220000),
            ("Joran Pancing Heavy", 245000),
        ]

        for nama, harga in joran_data:
            data.append({
                'id': alat_id,
                'nama': nama,
                'jenis': 'Joran',
                'harga': harga
            })
            alat_id += 1

        return data

    @staticmethod
    def get_jenis_list():
        """Mengembalikan list jenis-jenis alat pancing"""
        return ['Senar', 'Kail', 'Reel Pancing', 'Joran']

    @staticmethod
    def format_currency(amount):
        """Format harga ke format rupiah"""
        return f"Rp {amount:,.0f}".replace(',', '.')
