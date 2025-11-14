Nama : Febryvia Deya Nur Havidtar Murti Aqsa

NIM : 312510194

Kelas : TI.25.A.2

Mata Kuliah : Pengantar Pemrograman

PRAKTIKUM 4


LATIHAN: Program Manipulasi List sesuai permintaan

1. Buat list sebanyak 5 elemen dengan nilai bebas

A = [12, 15, 20, 32, 45]

Print ("List A awal:" A) [] _#empty list_

#Akses list

Print ("Akses list:")

2. Tampilkan elemen ke-3

Print ("Elemen ke-3:", A = [2]) _#change the 2nd item_

3. Ambil nilai elemen ke-2 sampai ke-4

Print ("Nilai elemen ke-2 sampai elemen ke-4 A:", A = [1 : 4]) _#change 2nd to 4th items_

4. Ambil elemen terakhir

Print ("Elemen terakhir:," A = [-1]) _#print element index 2_

#Ubah elemen list:

5. Ubah elemen ke-4 dengan nilai lainnya

A[3] = 99 _#change the 2nd item_

Print ("Setelah ubah elemen ke 4:", A)

6. Ubah elemen ke-4 sampai dengan elemen terakhir

A ke-3 = [113, 222] _#change 2nd to 4th items_

Print setelah ubah elemen ke-4 sampai terakhir: A

#Tambah elemen list

Print ("Tambah elemen list:")

7. Ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B)

B = A [:2] _#print first elemen to index 2_

Print "List B (2 bagian dari A):", B

8. Tambah list B dengan nilai string A

B.append ("A") _#add one item to last element_

Print ("List B setelah tambah string 'A':", B)

9. Tambah list B dengan 3 nilai

B.extend ([60, 70, 80])_ #add sereval items to last element_
 
Print ("List B setelah tambah 3 nilai")

10. Gabungan list B dengan list A

C = B + A _#join list a and b into c_

a.extend(b) _#add several items b into a_

Print ("List A setelah digabungkan dengan B:", A)

Hasilnya :
<img width="1499" height="725" alt="Screenshot 2025-11-13 093610" src="https://github.com/user-attachments/assets/806ef85b-7b0c-43ad-85f4-0fe2aba108ea" />


PRAKTIKUM : Program Input Data mahasiswa ke list

1. Inisialisasi data_mahasiswa / data_msh [] _#empty list_

2. perulangan input data menggunakan while true

3. Hitung nilai akhir dengna tugas 30%, UTS 35%, UAS 35%

akhir = tugas * 0.3 + uts * 0.35 + uas * 0.35

Nilai akhir = (70 × 0.30) + (65 × 0.35) + (80 × 0.35)
= 21 + 22.75 + 28
= 71.75

4. Simpan data ke list

5. Kondisi berhenti

6. Menampilkan tabel hasil
   

Algoritma:

1. Mulai

2. Inisialisasi : data mahasiswa

3. Masukkan nomor urut = 1

4. Menggunakan perulangan untuk menerima input data

a. Input Nama Mahasiswa

b. Input NIM Mahasiswa

c. Input Nilai Tugas

d. Input Nilai UTS

e. Input Nilai UAS

5. Hitung nilai akhir 

Nilai akhir = tugas * 0.3 + uts * 0.35 + uas * 0.35

6. Simpan data mahasiswa

-Nomor

-Nama

-NIM

-Tugas

-UTS

-UAS

-Nilai Akhir

7. Tambahkan data

-Jika jawaban y, kembali ke langkah 4

-Jika jawaban t, lanjut ke langkah 8

8. Tampilkan semua data mahasiswa

Nomor, nama, NIM, uts, uas, nilai akhir

9. Selesai

Hasilnya :
<img width="1784" height="886" alt="Screenshot 2025-11-13 215815" src="https://github.com/user-attachments/assets/f718f775-f6d5-4f85-8f79-a0dbeb651658" />

Flowchart :
![Image 2025-11-14 at 23 29 22_05282253](https://github.com/user-attachments/assets/abc65998-bc6a-455d-b7a5-7ad83fb42dfb)
