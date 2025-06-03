from user import user
from data import data_user
from data_category import data
from datetime import datetime
from collections import defaultdict
import csv

class showed_data(data, user):
    def __init__(self):
        super().__init__()
        self.tanggal_trans = None
        self.kategori = None

    def get_all_transactions(self):
        transaksi_all = []
        for kategori, tanggal_data in data_user[self.get__username()]["category"].items():
            for tanggal, transaksis in tanggal_data.items():
                for nama, nilai in transaksis.items():
                    transaksi_all.append((tanggal, nama, nilai))
        return transaksi_all

    def get_transactions_by_category(self, kategori):
        transaksi_kat = []
        if kategori in data_user[self.get__username()]["category"]:
            for tanggal, transaksis in data_user[self.get__username()]["category"][kategori].items():
                for nama, nilai in transaksis.items():
                    transaksi_kat.append((tanggal, nama, nilai))
        return transaksi_kat

    def group_by(self, transaksi_list, mode):
        grouped = defaultdict(lambda: {"total": 0.0, "transaksi": []})
        for tanggal, nama, nilai in transaksi_list:
            dt = datetime.strptime(tanggal, "%Y-%m-%d")
            if mode == 'day':
                key = dt.strftime("%Y-%m-%d")
            elif mode == 'week':
                key = f"{dt.strftime('%Y')}-W{dt.isocalendar()[1]}"
            elif mode == 'month':
                key = dt.strftime("%Y-%m")
            elif mode == 'year':
                key = dt.strftime("%Y")
            else:
                continue

            grouped[key]["total"] += float(nilai)
            grouped[key]["transaksi"].append((nama, float(nilai)))
        return grouped

    def export_to_csv(self, grouped_data, filename="output.csv"):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Periode", "Total", "Nama Transaksi", "Nilai"])
                for periode, data in grouped_data.items():
                    for nama, nilai in data["transaksi"]:
                        writer.writerow([periode, f"{data['total']:.2f}", nama, f"{nilai:.2f}"])
            print(f"✅ Data berhasil diekspor ke file '{filename}'")
        except Exception as e:
            print(f"❌ Gagal menulis file CSV: {e}")

    def tampilkan_data(self):
        print("=== Menu Data Transaksi ===")
        print("1. Semua Kategori")
        print("2. Kategori Tertentu")
        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == "1":
            transaksi = self.get_all_transactions()
        elif pilihan == "2":
            print("Daftar kategori:")
            for i, kat in enumerate(self.category, 1):
                print(f"{i}. {kat}")
            idx = int(input("Pilih kategori: ")) - 1
            self.kategori = self.category[idx]
            transaksi = self.get_transactions_by_category(self.kategori)
        else:
            print("Pilihan tidak valid.")
            return

        print("\nOpsi tampilan total:")
        print("1. Per Hari")
        print("2. Per Pekan")
        print("3. Per Bulan")
        print("4. Per Tahun")
        mode_map = {"1": "day", "2": "week", "3": "month", "4": "year"}
        mode_input = input("Pilih mode: ")
        mode = mode_map.get(mode_input)

        if not mode:
            print("Mode tidak valid.")
            return

        grouped = self.group_by(transaksi, mode)
        print(f"\n📊 Total transaksi berdasarkan {mode.capitalize()}:")
        for k, v in sorted(grouped.items()):
            print(f"\n🗓️ {k} - Total: {v['total']:.2f}")
            for nama, nilai in v["transaksi"]:
                print(f"  • {nama}: {nilai:.2f}")

        ekspor = input("\nApakah ingin ekspor ke CSV? (y/n): ").lower()
        if ekspor == "y":
            nama_file = input("Masukkan nama file CSV (misal: hasil.csv): ")
            self.export_to_csv(grouped, nama_file)

