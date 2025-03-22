import os
import shutil
import string

exclude_extensions = input("Masukkan tipe file yang ingin di-exclude (pisahkan dengan koma, contoh: 'py,txt'): ")
EXCLUDE_EXTENSIONS = [ext.strip().lower() for ext in exclude_extensions.split(',')]

for item in os.listdir():
    if os.path.isfile(item):
        file_ext = os.path.splitext(item)[1].lower().lstrip('.')
        if file_ext in EXCLUDE_EXTENSIONS:
            print(f"File {item} di-exclude karena ekstensinya ({file_ext})")
            continue

        first_char = item[0]
        
        if first_char.isdigit():
            folder_name = '#'
        elif first_char in string.punctuation:
            folder_name = '-'
        elif first_char in string.ascii_letters:
            folder_name = first_char.upper()
        else:
            folder_name = 'Unsorted'
        
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        
        try:
            shutil.move(item, folder_name)
            print(f"File {item} dipindahkan ke folder {folder_name}")
        except Exception as e:
            print(f"Gagal memindahkan file {item}. Error: {str(e)}")

print("\nSelesai memindahkan file.")
