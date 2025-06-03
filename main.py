from user import user_login, user_register, forget_password
from create_data import create_transaction
from update_data import changed_transaction
from read_data import showed_data


def menu_login():
    while True:
        print("\n=== Menu Login ===")
        print("1. Login")
        print("2. Register")
        print("3. Lupa Password")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1-4): ")
        if pilihan == "1":
            login = user_login()
            login.login()
            return login.get__username()
        elif pilihan == "2":
            reg = user_register()
            reg.register()
        elif pilihan == "3":
            lupa = forget_password()
            lupa.forget()
        elif pilihan == "4":
            print("Keluar dari aplikasi.")
            exit()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


def menu_utama(username):
    while True:
        print(f"\n=== Menu Utama ({username}) ===")
        print("1. Tambah Transaksi")
        print("2. Ubah / Hapus Transaksi")
        print("3. Tampilkan Transaksi")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            try:
                transaksi = create_transaction()
                transaksi.add_transaction()
            except Exception as e:
                print(f"Terjadi kesalahan saat menambahkan transaksi: {e}")

        elif pilihan == "2":
            try:
                ubah = changed_transaction()
                ubah.showed_transaction()
            except Exception as e:
                print(f"Terjadi kesalahan saat mengubah transaksi: {e}")

        elif pilihan == "3":
            try:
                tampil = showed_data()
                tampil.tampilkan_data()
            except Exception as e:
                print(f"Terjadi kesalahan saat menampilkan data: {e}")

        elif pilihan == "4":
            print("Terima kasih telah menggunakan aplikasi.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    try:
        user_login = menu_login()
        menu_utama(user_login)
    except KeyboardInterrupt:
        print("\nAplikasi dihentikan oleh pengguna.")
    except Exception as e:
        print(f"Terjadi kesalahan tak terduga: {e}")
