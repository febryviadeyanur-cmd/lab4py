#Program Input Data mahasiswa ke list

def main():
    data_mhs = []
    no = 1

    while True:
        print(f"Data ke-{no}")
        nama = input("Nama : ")
        nim = input("NIM : ")

        try:
            tugas = float(input("Nilai Tugas : "))
            uts = float(input("Nilai UTS : "))
            uas = float(input("Nilai UAS : "))
        except ValueError:
            print("Nilai harus angka. Silakan input ulang data.")
            continue

        # Hitung nilai akhir dengan tugas 30%, UTS 35%, UAS 35%
        akhir = tugas * 0.3 + uts * 0.35 + uas * 0.35

        # Simpan data ke list
        data_mhs.append({
            'no': no,
            'nama': nama,
            'nim': nim,
            'tugas': tugas,
            'uts': uts,
            'uas': uas,
            'akhir': akhir
        })

        no += 1

        tambah = input("Tambah data(y/t)?").lower()
        if tambah == 't':
            break

    # Tampilan data ke layar
    print("=" * 65)
    print("| No |   Nama   |  NIM  | Tugas | UTS  | UAS  | Akhir  |")
    print("=" * 65)
    for mhs in data_mhs:
        print("| {no:<2} | {nama:<7} | {nim:<5} | {tugas:<5} | {uts:<4} | {uas:<4} | {akhir:<6.2f} |"
              .format(no=mhs['no'], nama=mhs['nama'], nim=mhs['nim'], tugas=int(mhs['tugas']), uts=int(mhs['uts']),
                      uas=int(mhs['uas']), akhir=mhs['akhir']))
    print("=" * 65)


if __name__ == "__main__":
    main()
