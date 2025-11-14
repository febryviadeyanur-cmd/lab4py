#Program manipulasi list sesuai permintaan

# Buat list sebanyak 5 elemen dengan nilai bebas
A = [12, 15, 20, 32, 45]
print("List A:", A)

# Akses list
print("Akses list:")
# 2. Tampilkan elemen ke-3 (index 2)
print("Elemen ke 3:", A[2])
# 3. Ambil nilai elemen ke-2 sampai ke-4 (index 1 sampai 3)
print("Nilai elemen ke 2 sampai elemen ke 4:", A[1:4])
# 4. Ambil elemen terakhir
print("Elemen terakhir:", A[-1])

# Ubah elemen list
print("Ubah elemen list:")
# 5. Ubah elemen 4 (index 3) dengan nilai lain
A[3] = 99  # Ubah elemen ke 4
print("Setelah ubah elemen ke 4:", A)

# 6. Ubah elemen ke 4 sampai dengan elemen terakhir
A[3:] = [113, 222]
print("Setelah ubah elemen ke 4 sampai terakhir:", A)

# Tambah elemen list
print("Tambah elemen list:")

# 7. Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)
B = A[:2]
print("List B (2 bagian dari A):", B)

# 8. Tambah list B dengan nilai string A (mungkin maksudnya tambah string representasi A)
B.append("A")
print("List B setelah tambah string A:", B)

# 9. Tambah list B dengan 3 nilai
B.extend([60, 70, 80])  # Tambah 3 nilai baru
print("List B setelah tambah 3 nilai:", B)

# 10. Gabungkan list B dengan list A
C = B + A
print("List A setelah digabungkan dengan B:", A)
