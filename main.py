# data buku
from tabulate import tabulate
books = [
    {"ISBN":"9786237121144", "Judul":"ILMU FALSAFAT", "pengarang":"Bambang simajuntak", "jumlah":9, "terpinjam":7},
    {"ISBN":"9786231800718", "Judul":"LOGIKA FALLACY", "pengarang":"Muhammad Nurudin", "jumlah":15, "terpinjam":0},
    {"ISBN":"9786026163905", "Judul":"MADILOG", "pengarang":"Tan Malaka", "jumlah":2, "terpinjam":1},
    {"ISBN":"9786022912828", "Judul":"PSYCHOLOGY OF MONEY", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"ISBN":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"ISBN":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""}
]

def tampilkan_data():
    print("No\tISBN        \tJudul       \tpengarang      \tjumlah     \tterpinjam")
    for i in range(len(books)):
        print(i+1, "\t",end= "")
        print(books[i]["ISBN"],"\t",books[i]["Judul"], "\t", books[i]["pengarang"], "\t", books[i]["jumlah"],  "\t", books[i]["terpinjam"])
        

def tambah_data():
    print("menambahkan data")
    ISBN = int (input("masukkan ISBN buku:"))
    judul = input("masukkan judul buku:")
    pengarang = input("masukkan pengarang buku:")
    jumlah = int (input("masukkan jumlah buku:"))
    book = {"ISBN":ISBN, "JUDUL":judul, "PENGARANG":pengarang,"JUMLAH":jumlah}
    books.append(books)
    

def edit_data():
    print("\n}~~~~~~~~~~~ MENU UPDATE BUKU ~~~~~~~~~~~{")
    Nama = input("Masukkan Nama buku Yang Diupdate: ").upper()
    for book in books:
        if book["book"].upper() == book:
            print(f"Data saat ini: {book}")
            book["isbn"] = (input("Masukkan isbn baru: "))
            book["judul"] = (input("Masukkan judul buku: "))
            book["pengarang"] = (input("Masukkan nama pengarang: "))
            book["jumlah"] = int(input("Masukkan jumlah buku: "))
            print("Items berhasil diupdate!")
            menu()
            return

def hapus_data():
    hapus = input("Masukkan Judul buku  Yang mau Dihapus: ").upper()
    for i in range(len(books)):
        if books[i]["Judul"].upper() == hapus:
            del books[i]
            print("Buku berhasil dihapus!")
            tampilkan_data
            return
    print("Data buku tidak ditemukan!")

def tampilkan_peminjaman():
    print("}{")
    print("Menu Data Peminjaman Buku Perpustakaan ")
    print(tabulate(records, headers="keys", tablefmt="grid"))
    print("}{")


def tampilkan_belum():
    print("}{")
    print("Menu Data Peminjaman Buku Perpustakaan Kizu")
    print(tabulate([records for records in records if records['tanggal_kembali'] is None],  headers="keys", tablefmt="grid"))
    print("}{")


def peminjaman():
    print("}{")
    print("Menu Meminjam Buku Perpustakaan ")
    print("}{")
    isbn = input("Masukkan ISBN buku yang dipinjam: ")
    tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")

    for book in books:
        if book["isbn"] == isbn:
            if book["jumlah"] - book["terpinjam"] > 0:
                book["terpinjam"] += 1
                records.append({
                    "isbn": isbn,
                    "status": "Belum",
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": ""
                })
                print("Peminjaman berhasil dicatat.")
                return
            else:
                print("Stok buku habis!")
                return
    print("ISBN tidak ditemukan.")
    


def pengembalian():
    print("}{")
    print("Menu Meminjam Buku Perpustakaan")
    print("}{")
    isbn = input("Masukkan ISBN buku yang dipinjam: ")
    tanggal_pinjam = input("Masukkan tanggal pinjam (Y-M-D): ")

    for book in books:
        if book["isbn"] == isbn:
            if book["jumlah"] - book["terpinjam"] > 0:
                book["terpinjam"] += 1
                records.append({
                    "isbn": isbn,
                    "status": "Belum",
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": ""
                })
                print("Peminjaman berhasil dicatat.")
                return
            else:
                print("Stok buku habis!")
                return
    print("ISBN tidak ditemukan.")


    


while True:
    print("======> MENU <======")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    menu = input("Masukkan pilihan menu (1-8 atau x): ")
    
    
    match menu:
        case "1":
            tampilkan_data()
        case "2":
            tambah_data()
        case "3":
            edit_data()
        case "4":
            hapus_data()
        case "5":
            tampilkan_peminjaman()
        case "6":
            tampilkan_belum()
        case "7":
            peminjaman()
        case "8":
            pengembalian()
        case "X":
            print("Telah keluar dari sistem")
            break