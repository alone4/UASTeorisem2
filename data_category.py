from user import user
from data import data_user

class data(user):
    def __init__(self):
        super().__init__()
        self.category = []
        self.tanggal = {}
        self.get_category()
        self.get_tanggal()
    def add_category(self):
        for x in range(int(input("berapa banyak kategori yang ingin di tambahkan?"))):
            data_user[self.get__username()]["category"][input("Masukkan nama kategori: ")] = {}
            print("kategori baru berhasil di tambahkan")
    def get_category(self):
        for y in data_user[self.get__username()]["category"].keys():
            self.category.append(y)
    def get_tanggal(self):
        for kategori,isi in data_user[self.get__username()]["category"].items():
            self.tanggal[kategori] = []
            for tanggal in isi.keys():
                self.tanggal[kategori].append(tanggal)
        

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
            tanggal = str(input("masukkan tanggal?"))
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
