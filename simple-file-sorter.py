import os
import shutil
import string

for item in os.listdir():
    if os.path.isfile(item):
        first_char = item[0].upper()
        
        if first_char in string.ascii_uppercase:
            folder_name = first_char
        else:
            folder_name = 'Unsupported'
        
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
        
        try:
            shutil.move(item, folder_name)
            print(f"File {item} dipindahkan ke folder {folder_name}")
        except Exception as e:
            print(f"Gagal memindahkan file {item}. Error: {str(e)}")

print("\nSelesai memindahkan file.")
