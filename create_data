from data_category import data
from user import user
from data import data_user

class create_transaction(data,user):
    def __init__(self):
        super().__init__()
         
    def add_transaction(self):
        print("Nama kategori:")
        print(self.category)
        print(self.tanggal)
        no = 0
        for nama_kat in self.category:
            no +=1
            print(f"{no}. {nama_kat}")
        nama_kat = str(input("Masukkan kategori anda: "))
        if nama_kat in self.category:
            tanggal = '2025-05-01'
            if tanggal in self.tanggal[nama_kat]:
                for x in range(int(input("Berapa banyak transaksi yang mau di input?"))):
                    transaksi = str(input("Masukkan nama transaksi: "))
                    nilai = str(input("Masukkan nilai transaksi: "))
                    if transaksi not in data_user[self.get__username()]["category"][nama_kat][tanggal].items():
                            data_user[self.get__username()]["category"][nama_kat][tanggal][transaksi] = nilai
                print("Data berhasil di tambahkan")

                                
            else:
                data_user[self.get__username()]["category"][nama_kat][tanggal] = {}
                for x in range(int(input("Berapa banyak transaksi yang mau di input?"))):
                    transaksi = str(input("Masukkan nama transaksi: "))
                    nilai = str(input("Masukkan nilai transaksi: "))
                    
                    if transaksi not in data_user[self.get__username()]["category"][nama_kat][tanggal].items():
                            data_user[self.get__username()]["category"][nama_kat][tanggal][transaksi] = nilai
                print("Data berhasil di tambahkan")
