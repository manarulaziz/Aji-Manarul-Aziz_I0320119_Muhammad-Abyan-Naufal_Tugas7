def menu():
    print ("Pilih Aktivitas")
    print
    print ("1. Mengkapitalisasi huruf awal kalimat")
    print ("2. Membuat string ada di center")
    print ("3. Menghitung huruf vokal dalam string")
    print ("4. Memeriksa substring akhir dari string")
    print ("5. Mencari indeks huruf vokal dalam string dengan fungsi find")
    print ("6. Mencari indeks huruf vokal dalam string dengan fungsi index")
    print ("7. Mengganti substring old menjadi new")
    print ("8. Membuat huruf pada kalimat menjadi kapital semua")
    print ("9. Membuat huruf pada kalimat menjadi kecil semua")
    print ("10. Keluar")

def capitalize():
    print("Mengkapitalisasi huruf awal kalimat")
    input_user = input("Masukkan kalimat yang ingin Anda kapitalisasi : ")
    p = input_user.capitalize()
    print(p)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def center():
    print("Membuat string ada di center")
    input_user = input("Masukkan kalimat yang ingin Anda tempatkan ke center : ")
    q = input_user.center(10, '=')
    print(q)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def count():
    print("Menghitung huruf vokal dalam string")
    input_user = input("Masukkan kalimat yang ingin Anda hitung huruf vokalnya : ")
    a = input_user.count("a")
    print("Jumlah huruf a = ", a)
    i = input_user.count("i")
    print("Jumlah huruf i = ", i)
    u = input_user.count("u")
    print("Jumlah huruf u = ", u)
    e = input_user.count("e")
    print("Jumlah huruf e = ", e)
    o = input_user.count("o")
    print("Jumlah huruf o = ", o)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def endswith():
    print("Memeriksa substring akhir dari string")
    input_user = input("Masukkan kalimat yang ingin Anda cek kata akhirnya : ")
    input_user2 = input("Masukkan kata terakhir yang Anda ingin cek pada kalimat di atas : ")
    print(input_user.endswith(input_user2))
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def find():
    print("Mencari indeks huruf vokal dalam string dengan fungsi find")
    input_user = input("Masukkan kalimat : ")
    a = input_user.find("a")
    print("indeks huruf a pada kalimat = ", a)
    i = input_user.find("i")
    print("indeks huruf i pada kalimat = ", i)
    u = input_user.find("u")
    print("indeks huruf u pada kalimat = ", u)
    e = input_user.find("e")
    print("indeks huruf e pada kalimat = ", e)
    o = input_user.find("o")
    print("indeks huruf o pada kalimat = ", o)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def index():
    print("Mencari indeks huruf vokal dalam string dengan fungsi index ")
    input_user = input("Masukkan kalimat : ")
    a = input_user.index("a")
    print("indeks huruf a pada kalimat = ", a)
    i = input_user.index("i")
    print("indeks huruf i pada kalimat = ", i)
    u = input_user.index("u")
    print("indeks huruf u pada kalimat = ", u)
    e = input_user.index("e")
    print("indeks huruf e pada kalimat = ", e)
    o = input_user.index("o")
    print("indeks huruf o pada kalimat = ", o)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def replace():
    print("Mengganti substring old menjadi new")
    input_user = input("Masukkan kalimat : ")
    print("Kalimat yang Anda masukkan adalah : ", input_user)
    diganti = input("Kata mana pada kalimat yang akan ganti : ")
    pengganti = input("Apa pengganti katanya : ")
    print("Baik sudah diganti")
    print("Kalimat Anda akan menjadi : ", input_user.replace(diganti, pengganti))
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def upper():
    print("Membuat huruf pada kalimat menjadi kapital semua")
    input_user = input("Masukkan kalimat : ")
    kapital = input_user.upper()
    print(kapital)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def lower():
    print("Membuat huruf pada kalimat menjadi kecil semua")
    input_user = input("Masukkan kalimat : ")
    kecil = input_user.lower()
    print(kecil)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

# Program Fungsi String
print("Selamat Datang di Sulap Kata Valorous")
print("----------------------------------")
print
menu()

while 1:
    # Input
    pilih = int(input("Masukkan nomor yang ingin dilakukan Anda : "))

    if pilih == 1:
        capitalize()
    elif pilih == 2:
        center()
    elif pilih == 3:
        count()
    elif pilih == 4:
        endswith()
    elif pilih == 5:
        find()
    elif pilih == 6:
        index()
    elif pilih == 7:
        replace()
    elif pilih == 8:
        upper()
    elif pilih == 9:
        lower()
    elif pilih == 10:
        print("\n"*100)
        break
    else:
        print("Maaf pilihan yang Anda masukkan tidak terdaftar :)")
        print("Coba lagi [Y/N] ?")
        coba = input().upper()
        if coba == "Y":
            menu()
        else:
            print("\n")*100
            break


