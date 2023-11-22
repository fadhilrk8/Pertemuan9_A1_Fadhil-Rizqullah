angka = []
for i in range(0,5):
    angka_2 = float(input(f"Masukkan angka ke-{i+1}="))
    angka.append(angka_2)
rata_rata = sum(angka)/5
print("Hasil dari rata-rata ke-5 angka:", rata_rata)