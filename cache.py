
        if nama_kat in self.category:
            tanggal = str(input("Masukkan tanggal: "))
            if tanggal in self.tanggal.values():
                for x in range(int(input("Berapa banyak transaksi yang mau di input?"))):
                    transaksi = str(input("Masukkan nama transaksi: "))
                    nilai = int(input("Masukkan nilai transaksi: "))
                    for x,y in data_user[self.get__username()]["category"][nama_kat][tanggal].items():
                        print(x,y)
                        if data_user[self.get__username()]["category"][nama_kat][tanggal][transaksi] == None:
                            data_user[self.get__username()]["category"][nama_kat][tanggal][transaksi] = nilai
                        else:
                                print(x)
                                data_user[self.get__username()]["category"][nama_kat][tanggal][x] = y