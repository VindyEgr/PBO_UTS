input("NIM  :   ")
input("nama :   ")

print("Silahkan Memilih Menu Yang Tersedia")
print("1. Kopi Capucino")
print("2. Teh Chamomile")
print("3. keluar")

a = int(input("silahkan pilih   :   "))
if a == 1:
    print("Memilih Kopi Capucino")
    print("harga: 5000")
    b = int(input("masukkan jumlah pesanan  :   "))
    c = 5000*b
    print("Total Harga  =   ", c + (c/10))
elif a == 2:
    print("Memilih Teh")
    print("harga: 3000")
    d = int(input("masukkan jumlah pesanan  :   "))
    e = 3000*d
    print("Total Harga  =   ", e + (e/10))
else:
    print("terimakasih sudah berkunjung")
