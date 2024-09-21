nama1 = "Dian" 
nama2 = "Andi"

hasil = f"{nama1}: halo {nama2}, kamu sudah bayar biaya pendaftaran ukm itu belum?"
print(hasil)
hasil = f"{nama2}: belum nih, {nama1}. aku baru aja kepikiran mau bayar sekarang dikampus"
print(hasil)
hasil = f"{nama1}:kalo gitu mending bayar bareng bareng aja ayo?"
print(hasil)
hasil = f"{nama2}:boleh tuh, ayo berangkat!"
print(hasil)

harga_per_orang = int(input("Dian: oke, kalau begitu berapa total biaya pendaftaran nya untuk kita berdua?"))

jumlah_orang = 2
total_biaya = harga_per_orang * jumlah_orang

print(f"Andi: Kalau kita berdua totalnya jadi {total_biaya} rupiah")

uang_dian = int(input("Dian: Aku punya uang"))
uang_andi = int(input("Andi: Aku punya uang"))

total_uang = uang_dian + uang_andi

print(f"Jadi, total uang kita {total_uang} rupiah")

if total_uang >= total_biaya:
    print("Dian: Wah, uang kita cukup nih. ayo kita bayar!")
else:
    kekurangan = total_biaya - total_uang
    print(f"Andi: Sayang sekali, kita masih kurang {kekurangan} rupiah.")
    print("Dian: mungkin kita perlu menabung dulu, atau bayar pas uang kita cukup saja.")
    print("Andi: Ya, setuju. Ayo kita bayar lain kali saja.")