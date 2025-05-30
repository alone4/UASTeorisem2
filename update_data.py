from data_category import data
from user import user
from data import data_user

class changed_transaction(data,user):
    def __init__(self):
        super().__init__()
        self.isi_transaksi = {}
        self.tanggal_trans = None
        self.kategori = None
    def get_kategori(self):
        self.kategori = str(input("Masukkan kategori anda: "))
    def get_tanggal_trans(self):
        self.tanggal_trans = str(input("masukkan tanggal: "))
    def showed_transaction(self):
        print("Nama kategori:")
        no = 0
        no1 = 0
        for nama_kat in self.category:
            no +=1
            print(f"{no}. {nama_kat}")
        if self.kategori == None:
            self.get_kategori()
        else:
            None
        
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
                    print(f"{no1}. {transaksi}: {nilai}")
            print(self.isi_transaksi[1]) 
            pilihan = int(input("Silahkan pilih data (menggunakan angka): "))
            pilihan2 = str(input("Data telah terpilih\n Data ingin di update atau delete?"))

            if pilihan2 == "update":
                self.update_transaction(isi,pilihan)
            if pilihan2 == "delete":
                 self.delete_transaction(isi,pilihan)

    def update_transaction(self,isi,pilihan):
        transaksi = str(input("Masukkan nama transaksi terbarunya: "))
        nilai = int(input("Masukkan nilai transaksi terbarunya:"))

        isi[transaksi] = nilai
        for x,y in self.isi_transaksi[pilihan].items():
                del isi[x] 
        print("data berhasil di update")
        self.lanjut_berhenti()

    def delete_transaction(self,isi,pilihan):
        for x,y in self.isi_transaksi[pilihan].items():
                del isi[x] 
        print("data berhasil di hapus")
        self.lanjut_berhenti()
        
    def lanjut_berhenti(self):
         print("1.Lanjut \n2.Berhenti")
         pilihan = str(input("Masukkan pilihan: "))
         if pilihan == "lanjut":
              self.showed_transaction()
         elif pilihan == "berhenti":
              None
         
changed_transaction().showed_transaction()