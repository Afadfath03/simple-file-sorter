# File Sorter by First Letter

Skrip Python ini mengorganisir file dalam direktori saat ini dengan memindahkannya ke folder berdasarkan huruf pertama dari nama file.

## Cara Penggunaan

1.  Simpan skrip Python `simple-file-sorter.py` di direktori yang berisi file yang ingin Anda organisir.
2.  Buka terminal atau command prompt dan navigasikan ke direktori tersebut.
3.  Jalankan skrip menggunakan Python: `python simple-file-sorter.py` atau `py simple-file-sorter.py`

## Deskripsi

Skrip ini melakukan hal berikut:

* Mengiterasi semua item dalam direktori saat ini.
* Jika item adalah file, ia mengambil huruf pertama dari nama file (dalam huruf kapital).
* Jika huruf pertama adalah huruf alfabet (A-Z), file dipindahkan ke folder dengan nama huruf tersebut.
* Jika huruf pertama bukan huruf alfabet, file dipindahkan ke folder bernama "Unsupported".
* Jika folder yang sesuai belum ada, skrip akan membuatnya.
* Menampilkan pesan keberhasilan atau kegagalan setiap pemindahan file.

## Contoh

Misalkan direktori Anda berisi file-file berikut:
``` txt
Apple.txt
banana.jpg
Cat.pdf
123.doc
```

Setelah menjalankan skrip, direktori akan berisi folder-folder berikut:
``` txt
A/
  Apple.txt
B/
  banana.jpg
C/
  Cat.pdf
Unsupported/
  123.doc
```

## Dependensi

* Python 3.x
* Tidak ada dependensi eksternal.
