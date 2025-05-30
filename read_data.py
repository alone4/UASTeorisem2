from user import user
from data import data_user
from data_category import data

class showed_data(data,user):
    def __init__(self):
        super().__init__()
        self.isi_transaksi = {}
        self.kategori = []
        self.total = int
    def showed_transaction_by_category(self):
            print("Nama kategori:")
            no = 0
            no1 = 0
            for nama_kat in self.category:
                no +=1
                print(f"{no}. {nama_kat}")
            
            if nama_kat in self.category:
                if self.tanggal_trans == None:
                    self.get_tanggal_trans()
                else:
                    None    
                isi = data_user[self.get__username()]["category"][self.kategori][self.tanggal_trans]
                for transaksi,nilai in isi.items():
                        no1 +=1
                        self.isi_transaksi[no1] = {}
                        self.isi_transaksi[no1][transaksi] = nilai

    