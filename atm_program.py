import random
import datetime
from customer import Customer

atm = Customer(id)

while True:

    id = int(input("Masukkan Pin Anda: "))
    trial = 0

    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin Anda Salah. Silahkan Masukkan lagi: "))
        trial += 1

        if trial == 3:
            print("Error. Silahkan ambil kartu dan coba lagi...")
            exit()

    while True:
        print("Selamat Datang di Atm Prograte...")
        print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar ")
    
        selectmenu = int(input("\nSilahkan Pilih Menu: "))

        if selectmenu == 1:
            print("\nSaldo Anda sekarang: Rp. " + str(atm.checkBalance()) + "\n" )

        elif selectmenu == 2:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_withdraw = input ("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y\n " + str(nominal) + " ")

            if verify_withdraw == "y":
                print("Saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
            else:
                break

            if nominal < atm.checkBalance() : 
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo sisa sekarang: Rp. " + str(atm.checkBalance()) + " ")
            else:
                print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                print("Silahkan lakukan penambahan nominal saldo")

        elif selectmenu == 3:
            nominal = float(input("Masukkan nominal saldo: "))
            verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n " + str(nominal) + " ")
    
            if verify_deposit == "y":
                atm.depositBalance(nominal)
                print("Saldo anda sekarang adalah: Rp." + str(atm.checkBalance()) + "\n")
            else: 
                break

        elif selectmenu == 4:
            verify_pin = int(input("Masukkan pin Anda: "))

            while verify_pin != int(atm.checkPin()):
                print("Pin Anda salah, silahkan masukkan pin: ")

            updated_pin = int(input("Silahkan masukkan pin baru: "))
            print("Pin Anda berhasil diganti")

            verify_newpin = int(input("Coba masukkan pin baru: "))

            if verify_newpin == updated_pin:
                print("Pin baru anda sukses")
            else:
                print("Maaf, pin anda salah")

        elif selectmenu == 5:
            print("Resi tercetak otomatis anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. Rekord: ", random.randint(100000, 1000000))
            print("Tanggal: ", datetime .datetime.now())
            print("Saldo akhir: ", atm.checkBalance())
            print("Terima aksih telah menggunakan ATM Prograte!")
            exit()
        else:
            print("Error. Maaf, menu tidak tersedia")