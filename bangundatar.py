def persegi():
    while True:
        try:
            s = int(input("Masukkan Sisi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas        = s * s
            keliling    = 4 * s
            hasil       = [luas, keliling]
        break
    return hasil

def persegiPanjang():
    while True:
        try:
            p = int(input("Masukkan Panjang : "))
            l = int(input("Masukkan Lebar : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas        = p * l
            keliling    = 2 * (p + l)
            hasil       = [luas, keliling]
        break
    return hasil

def segitiga():
    while True:
        try:
            a = int(input("Masukkan Alas : "))
            t = int(input("Masukkan Tinggi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas        = 0.5 * a * t
            keliling    = a + t + t
            hasil       = [luas, keliling]
        break
    return hasil

def lingkaran():
    while True:
        try:
            r = int(input("Masukkan Jari-Jari : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            if r % 7 == 0:
                luas        = 22 / 7 * r * r
                keliling    = 2 * (22 / 7 * r)
                hasil       = [luas, keliling]
            else:
                luas        = 3.14 * r * r
                keliling    = 2 * 3.14 * r
                hasil       = [luas, keliling]
        break
    return hasil

def jajargenjang():
    while True:
        try:
            a = int(input("Masukkan Alas : "))
            t = int(input("Masukkan Tinggi : "))
        except ValueError:
            print("Input Tidak Valid")
            continue
        else:
            luas        = a * t
            keliling    = 2 * (a + t)
            hasil       = [luas, keliling]
        break
    return hasil

confirm = "y"
while confirm == "y":
    print("Pilih Bangun Datar")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajargenjang")

    pilihan = input("Masukkan Pilihan (1/2/3/4/5) : ")

    if pilihan == "1":
        hasil = persegi()

        print("Luas Persegi : {}".format(hasil[0]))
        print("Keliling Persegi : {}".format(hasil[1]))
    elif pilihan == "2":
        hasil = persegiPanjang()

        print("Luas Persegi Panjang : {}".format(hasil[0]))
        print("Keliling Persegi Panjang : {}".format(hasil[1]))
    elif pilihan == "3":
        hasil = segitiga()

        print("Luas Segitiga : {}".format(hasil[0]))
        print("Keliling Segitiga : {}".format(hasil[1]))
    elif pilihan == "4":
        hasil = lingkaran()

        print("Luas Lingkaran : {}".format(hasil[0]))
        print("Keliling Lingkaran : {}".format(hasil[1]))
    elif pilihan == "5":
        hasil = jajargenjang()

        print("Luas Jajargenjang : {}".format(hasil[0]))
        print("Keliling Jajargenjang : {}".format(hasil[1]))
    else:
        print("Input Tidak Valid")

    confirm = input("Mau Coba Lagi Ndak? (y/t) : ")
    if confirm == "t":
        break
    elif confirm == "y":
        continue
    else:
        print("IKAN HIU MAKAN TOMAT, GAJELAS LU USER")

print("Terimakasih sudah mencoba :D")