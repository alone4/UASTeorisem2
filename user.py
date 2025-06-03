from data import data_user

class user:
    def __init__(self):
        self.__username = None
        self.__password = None
    
    def check_akun(self,usern):
        if usern in data_user:
            self.__username = usern
        else:
            return None
    def check_password(self):
        self.__password = data_user[self.__username]["Password"]
    def get__username(self):
         return self.__username
    def get__password(self):
         return self.__password
        
        

class user_login(user):
    def __init__(self):
        super().__init__()
    def login(self):
         usern = str(input("Masukkan username: "))
         password = str(input("Masukkan password: "))
         self.check_akun(usern)
         if usern == self.get__username():
            self.check_password()
            if password == self.get__password():
                print("selamat berhasil login")  
                status = "berhasil"
                return status    
            else:
                print("Maaf password salah")
         else:
            print("maaf username tidak ada")
    
    
class user_register(user):
    def __init__(self):
        super().__init__()
    
    def register(self):
        usern = str(input("masukkan username anda: "))
        self.check_akun(usern)
        if usern != self.get__username():
            print("Selamat username tersedia")
            pw = str(input("Masukkan Password anda: "))
            data_user[usern] = {
                    "Password": pw,
                    "category": {   }}
            
            print("Apakah anda ingin memasukkan data kategori sendiri atau dibuatkan sistem?")
            print("1.buat data kategori sendiri \n2.dibuatkan oleh sistem")
            pilihan = int(input("Masukkan pilihan anda menggunakan angka: "))
            if pilihan == 1:
                    self.add_category()
                    print("data baru telah berhasil di tambahkan!")
            elif pilihan == 2:
                    data_user[usern]["category"] =  {
                        "Password": pw,
                        "category": {
                            "Food": {},
                            "Transport": {},
                            "Bills": {},
                            "Groceries": {}
                                    }}
            
        else:
            print("maaf username telah digunakan")

class forget_password(user):
    def __init__(self):
        super().__init__()
    def forget(self):
        usern = str(input("masukkan username anda: "))
        self.check_akun(usern)
        if usern == self.get__username():
            print("masukkan salah satu nama transaksi dan tanggalnya")
            trans_i = str(input("Masukkan nama transaksi: "))
            nilai_i = int(input("Masukkan nilai transaksi: "))
            for kategori in data_user[self.get__username()]["category"].values():
                    for transaksi in kategori.values():
                        for nama,nilai in transaksi.items():
                            if trans_i == nama and nilai_i == nilai:
                                print("silahkan ganti password anda")
                                break
                            else:
                                print("maaf tidak ada transaksi")
                                break
