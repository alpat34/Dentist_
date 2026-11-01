#program kasir
pilihan = input("silahkan mau beli apa?\n1. nasi goreng Rp. 20000\n2. mie goreng Rp.25000 (1/2): ")
if pilihan == "1":
    jumlah = int(input("masukkan jumlah pesanan: "))
    total = jumlah * 20000
    print(f"total harga: Rp. {total}")
    uang = int(input(f"masukkan uang anda: "))
    if uang > total:
        kembalian = uang - total
        print(f"anda membeli {jumlah} porsi nasi goreng, total harga: Rp. {total}, uang anda: Rp. {uang}, kembalian: Rp. {kembalian}")
    elif uang == total:
        print(f"anda membeli {jumlah} porsi nasi goreng, total harga: Rp. {total}, uang anda: Rp. {uang}, kembalian: Rp. 0")
    elif uang < total:
        print(f"maaf uang anda kurang")
elif pilihan == "2":
    jumlah = int(input("masukkan jumlah pesanan: "))
    total = jumlah * 25000
    print(f"total harga: Rp. {total}")
    uang = int(input(f"masukkan uang anda: "))
    if uang > total:
        kembalian = uang - total
        print(f"anda membeli {jumlah} porsi mie goreng, total harga: Rp. {total}, uang anda: Rp. {uang}, kembalian: Rp. {kembalian}")
    elif uang == total:
        print(f"anda membeli {jumlah} porsi mie goreng, total harga: Rp. {total}, uang anda: Rp. {uang}, kembalian: Rp. 0")
    elif uang < total:
        print(f"maaf uang anda kurang")
else:   
    print("maaf pilihan tidak tersedia")