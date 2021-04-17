import math
import random

def menu():
    print ("Pilih Aktivitas")
    print
    print ("1. Nilai Mutlak fungsi abs ")
    print ("2. Pembulatan ke bilangan diatasnya")
    print ("3. Nilai Absolut fungsi fabs")
    print ("4. Pembulatan ke bilangan di bawahnya")
    print ("5. Mencari nilai minimum")
    print ("6. Mencari nilai maksimum")
    print ("7. Menghitung nilai akar")
    print ("8. Memilih random angka dari list")
    print ("9. Keluar")


def mutlakabs():
    print("Nilai Mutlak fungsi abs")
    user = float(input("Masukkan angka : "))
    print("|",user,"|", "=", abs(user))
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def ceil():
    print("Pembulatan ke bilangan diatasnya")
    user = float(input("Masukkan angka : "))
    ceil = math.ceil(user)
    print(ceil)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def fabs():
    print("Nilai Absolut fungsi fabs")
    user = float(input("Masukkan angka : "))
    fabs = math.fabs(user)
    print("|", user, "|", fabs)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def floor():
    print("Pembulatan ke bilangan di bawahnya")
    user = float(input("Masukkan angka : "))
    floor = math.floor(user)
    print(floor)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def minimum():
    print("Mencari nilai minimum")
    list_angka = []
    inputan = ' '
    while inputan != 'done':
        inputan = input('Masukkan angka, ketik "done" jika done selesai \n>> ')

        if inputan != 'done':
            list_angka.append(float(inputan))
            print("List angka yang Anda masukkan adalah : ")

    print("Nilai minimum dari angka yang Anda masukkan : ", min(list_angka))
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def maximum():
    print("Mencari nilai maksimum")
    list_angka = []
    inputan = ' '
    while inputan != 'done':
        inputan = input('Masukkan angka, ketik "done" jika done selesai \n>> ')

        if inputan != 'done':
            list_angka.append(float(inputan))
            print("List angka yang Anda masukkan adalah : ")

    print("Nilai maksimum dari angka yang Anda masukkan : ", max(list_angka))
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def sqrt():
    print("Menghitung nilai akar")
    user = float(input("Masukkan angka yang ingin diakar pangkat dua : "))
    akar = math.sqrt(user)
    print(akar)
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()

def choice():
    print("Memilih random angka dari list")
    list_angka = []
    inputan = ' '
    while inputan != 'done':
        inputan = input('Masukkan angka, ketik "done" jika done selesai \n>> ')

        if inputan != 'done':
            list_angka.append(float(inputan))
            print("List angka yang Anda masukkan adalah : ")
    
    print("Komputer memilih random dan angka yang muncul adalah : ", random.choice(list_angka))
    print
    print("Coba lagi [Y/N]?")
    back = input().upper()
    if back == "Y":
        menu()
    else:
        exit()


# Program Fungsi String
print("Selamat Datang di Sulap Angka Valorous")
print("----------------------------------")
print
menu()

while 1:
    # Input
    pilih = int(input("Masukkan nomor yang ingin dilakukan Anda : "))

    if pilih == 1:
        mutlakabs()
    elif pilih == 2:
        ceil()
    elif pilih == 3:
        fabs()
    elif pilih == 4:
        floor()
    elif pilih == 5:
        minimum()
    elif pilih == 6:
        maximum()
    elif pilih == 7:
        sqrt()
    elif pilih == 8:
        choice()
    elif pilih == 9:
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
