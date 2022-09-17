import zipfile

target = "Luas_Bidang.7z"  # zip file

handle = zipfile.ZipFile(r"C:\Users\Alexander\Downloads\Luas_Bidang.7z")

handle.extractall("C:\\Users\Alexander\Downloads")

print("Success !!")
